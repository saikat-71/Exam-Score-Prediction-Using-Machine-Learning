"""Student exam score prediction project. Run with: python main.py"""
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR.parent / "data" / "student_performance_messy.csv"
FEATURES = ["study_hours", "attendance_percent", "previous_score", "sleep_hours"]


def load_and_clean_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {path}\nKeep the dataset at ../data/student_performance_messy.csv relative to this script."
        )
    df = pd.read_csv(path)
    required = FEATURES + ["exam_score"]
    missing_columns = [col for col in required if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {', '.join(missing_columns)}")

    df = df.drop_duplicates().copy()
    # Handle the inconsistent text values found in the supplied dataset.
    df["study_hours"] = pd.to_numeric(
        df["study_hours"].astype(str).str.strip().str.replace(" hrs", "", regex=False), errors="coerce"
    )
    df["attendance_percent"] = pd.to_numeric(
        df["attendance_percent"].astype(str).str.strip().str.replace("eighty", "80", regex=False).str.replace("%", "", regex=False), errors="coerce"
    )
    df["previous_score"] = pd.to_numeric(
        df["previous_score"].astype(str).str.strip().str.replace(" / 100", "", regex=False), errors="coerce"
    )
    for col in ["sleep_hours", "exam_score"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df.loc[~df["study_hours"].between(0, 24), "study_hours"] = float("nan")
    df.loc[~df["attendance_percent"].between(0, 100), "attendance_percent"] = float("nan")
    df.loc[~df["previous_score"].between(0, 100), "previous_score"] = float("nan")
    df.loc[~df["sleep_hours"].between(0, 24), "sleep_hours"] = float("nan")
    df.loc[~df["exam_score"].between(0, 100), "exam_score"] = float("nan")
    # A target score is required for supervised training; missing feature values are imputed later.
    df = df.dropna(subset=["exam_score"])
    if len(df) < 5:
        raise ValueError("Not enough valid rows to train a model (need at least 5 rows).")
    return df


def main() -> None:
    print("=" * 54)
    print("       STUDENT EXAM SCORE PREDICTION")
    print("=" * 54)
    try:
        df = load_and_clean_data(DATA_FILE)
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as exc:
        print(f"\nError: {exc}")
        sys.exit(1)

    print(f"\nDataset loaded: {DATA_FILE.name}")
    print(f"Rows available for training: {len(df)}")
    print("\nCleaned data preview:")
    print(df[FEATURES + ["exam_score"]].head().to_string(index=False))
    print("\nMissing values after cleaning:")
    print(df[FEATURES + ["exam_score"]].isna().sum().to_string())

    X = df[FEATURES]
    y = df["exam_score"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    # Learn imputation values from training data only to avoid leakage.
    medians = X_train.median().fillna(0)
    X_train = X_train.fillna(medians)
    X_test = X_test.fillna(medians)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test).clip(0, 100)
    print("\nModel evaluation")
    print(f"Mean Absolute Error (MAE): {mean_absolute_error(y_test, predictions):.2f} points")
    print(f"R² score: {r2_score(y_test, predictions):.3f}")
    print("Note: metrics are estimates from this dataset/test split, not a guarantee of future accuracy.")

    print("\nEnter your own details to predict an exam score.")
    print("Allowed ranges: study hours 0-24, attendance 0-100%, previous score 0-100, sleep 0-24 hours.")

    def ask_number(prompt: str, minimum: float, maximum: float) -> float:
        while True:
            raw = input(prompt).strip()
            try:
                value = float(raw)
            except ValueError:
                print("Please enter a number (for example: 6 or 7.5).")
                continue
            if not minimum <= value <= maximum:
                print(f"Enter a value from {minimum:g} to {maximum:g}.")
                continue
            return value

    while True:
        new_student = pd.DataFrame({
            "study_hours": [ask_number("Study hours per day: ", 0, 24)],
            "attendance_percent": [ask_number("Attendance percentage (0-100): ", 0, 100)],
            "previous_score": [ask_number("Previous exam score (0-100): ", 0, 100)],
            "sleep_hours": [ask_number("Sleep hours per day: ", 0, 24)],
        }).fillna(medians)
        predicted_score = float(model.predict(new_student)[0])
        predicted_score = max(0.0, min(100.0, predicted_score))
        print("\n--- Prediction result ---")
        print(f"Study hours: {new_student.iloc[0]['study_hours']:g}")
        print(f"Attendance: {new_student.iloc[0]['attendance_percent']:g}%")
        print(f"Previous score: {new_student.iloc[0]['previous_score']:g}/100")
        print(f"Sleep: {new_student.iloc[0]['sleep_hours']:g} hours")
        print(f"Predicted exam score: {predicted_score:.1f}/100")
        print("Note: this is an estimate from the available dataset, not a guaranteed real exam result.")
        again = input("\nPredict for another student? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            break

    # Save the chart in the project folder as well as displaying it.
    plt.figure(figsize=(8, 5))
    plt.scatter(df["study_hours"], df["exam_score"], alpha=0.7)
    plt.xlabel("Study hours")
    plt.ylabel("Exam score")
    plt.title("Study Hours vs Exam Score")
    plt.grid(True, alpha=0.25)
    plt.tight_layout()
    chart_path = BASE_DIR / "study_hours_vs_exam_score.png"
    plt.savefig(chart_path, dpi=150)
    print(f"\nChart saved to: {chart_path.name}")
    try:
        plt.show()
    except Exception:
        print("Could not open chart window; the PNG chart has still been saved.")

    print("\nFinished successfully.")


if __name__ == "__main__":
    main()

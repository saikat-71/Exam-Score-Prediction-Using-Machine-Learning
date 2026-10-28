# ExamScore AI — Student Machine Learning Project

A student-friendly machine-learning project that explores how study habits and academic history relate to exam performance. It includes a browser-based prediction dashboard for GitHub Pages, a cleaned-up Python training script, a dataset, and a Jupyter Notebook for learning and experimentation.

> **Course-project style:** The project is organized so the website can be deployed from the repository root, while the dataset, notebook, and Python training files stay in clearly named folders.

## Live Demo with GitHub Pages

This project includes a static website edition. GitHub Pages hosts static files; it does not run Python or Flask. The browser dashboard uses the exported `model.json` file and the JavaScript in `app.js` to make predictions in the visitor's browser.

### Publish the website

1. Download and extract this ZIP.
2. Create a GitHub repository, for example `exam-score-prediction`.
3. Upload **the contents of this folder** to the repository root. Do not upload only the ZIP itself, and do not put all files inside an extra nested folder.
4. Confirm these files are visible at the repository's top level: `index.html`, `style.css`, `app.js`, `model.json`, and `.nojekyll`.
5. Open **Settings → Pages**.
6. Under **Build and deployment**, select **Deploy from a branch**.
7. Choose branch `main` and folder `/(root)`, then click **Save**.
8. Wait for the deployment to finish. GitHub will show the published URL in the Pages section, usually `https://YOUR-USERNAME.github.io/REPOSITORY-NAME/`.

## Run the Python training script locally

Requirements: Python 3.10+ recommended.

From the repository root:

```bash
python -m venv .venv
```

Activate the environment, then install dependencies and run the script:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -r python-project/requirements.txt
python python-project/main.py
```

The Python script reads `data/student_performance_messy.csv`. The notebook is in `notebooks/exam_score_prediction.ipynb`; open it with Jupyter and run the cells in order.

## Repository structure

```text
ExamScore_AI_Student_Project/
├── index.html                  # GitHub Pages entry point
├── style.css                   # Responsive website styling
├── app.js                      # Browser-side prediction and chart logic
├── model.json                  # Exported model and dashboard metrics/data
├── .nojekyll                   # Tells GitHub Pages not to apply Jekyll processing
├── README.md                   # Project overview and setup guide
├── assets/
│   └── study_hours_vs_exam_score.png
├── data/
│   └── student_performance_messy.csv
├── notebooks/
│   └── exam_score_prediction.ipynb
└── python-project/
    ├── main.py                 # Python model-training/evaluation script
    └── requirements.txt        # Python dependencies
```

## Project objectives

- Explore the relationship between study hours, attendance, previous scores, sleep, and exam scores.
- Practice data cleaning and basic supervised machine learning.
- Train/evaluate a Random Forest regression model using Python and scikit-learn.
- Present a simple interactive dashboard that estimates a score from user-provided inputs.
- Practice organizing and publishing a student project with GitHub Pages.

## Tools and technologies

- Python, pandas, scikit-learn, Matplotlib
- Jupyter Notebook
- HTML, CSS, JavaScript
- Chart.js (loaded from a CDN)
- Git and GitHub Pages

## Important limitations

- The output is an estimate, not a guaranteed exam result or a substitute for academic guidance.
- Model quality depends on the size, quality, and representativeness of the included dataset.
- The website uses Chart.js and Google Fonts from external CDNs, so those visual resources may need an internet connection.
- The live dashboard is a static browser application. The Python training script is for local learning and is not executed by GitHub Pages.
- This project is intended for educational use; review the dataset and model assumptions before drawing conclusions.

## Suggested next improvements

- Add a short report comparing model performance against a simple baseline.
- Use a reproducible train/test split and document evaluation results in the notebook.
- Add input validation tests and test the published website on mobile and desktop browsers.
- Replace the demo dataset with a larger, ethically collected dataset if permitted by the course.

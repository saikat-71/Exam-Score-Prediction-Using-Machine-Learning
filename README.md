# Exam Score Prediction Using Machine Learning

A machine learning project that explores the relationship between students' study habits and their exam performance. The project includes data analysis, model training, visualizations, and a simple web interface for predicting exam scores.

## About the Project

Students' exam results can be influenced by several factors, including study time, preparation, and learning habits. This project focuses on using available student performance data to understand these patterns and build a model that estimates exam scores.

The main goal was to get practical experience with the machine learning workflow, from preparing a dataset to training a model and presenting its predictions through a web interface.

This project was developed for educational purposes as part of learning Python, data analysis, and machine learning.

## Features

- Predict exam scores using input data.
- Explore the relationship between study hours and exam performance.
- Clean and prepare data for model training.
- Train and evaluate a machine learning model.
- Visualize the dataset and model-related results.
- Use an interactive web interface to try predictions.
- Access the project through GitHub Pages for the static website version.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and model development |
| Pandas | Data handling and preparation |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning and model evaluation |
| Jupyter Notebook | Experiments and data analysis |
| HTML | Web page structure |
| CSS | Styling and responsive layout |
| JavaScript | Browser-based interactions |
| GitHub Pages | Static website hosting |

## Project Structure

```text
ExamScore_AI_Student_Project/
│
├── index.html
├── style.css
├── app.js
├── model.json
├── README.md
├── PROJECT_REPORT.md
├── .gitignore
├── .nojekyll
│
├── data/
│   └── student_performance_messy.csv
│
├── notebooks/
│   └── exam_score_prediction.ipynb
│
├── python-project/
│   ├── app.py
│   ├── main.py
│   └── requirements.txt
│
└── assets/
    └── study_hours_vs_exam_score.png
```

*Note: The structure above describes the intended organization of the project. File names and locations should match the actual files in the repository.*

## How It Works

The project follows a basic machine learning workflow:

1. **Data collection:** Load the student performance dataset.
2. **Data preparation:** Inspect the data and handle issues that may affect analysis or training.
3. **Exploratory analysis:** Examine patterns in the data and visualize the relationship between study hours and exam scores.
4. **Model training:** Use a machine learning algorithm to learn from the available examples.
5. **Model evaluation:** Evaluate the model using suitable regression metrics.
6. **Prediction:** Use the trained model or exported model data to estimate an exam score from user inputs.
7. **Web interface:** Present the prediction process through a simple dashboard.

The accuracy of predictions depends on the quality of the dataset, the selected features, and how well the model generalizes to new data.

## Getting Started

### Option 1: Use the Website

If the project has been deployed through GitHub Pages, open the published website and enter the required values to try the prediction feature.

### Option 2: Run the Python Project

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/exam-score-prediction.git
```

Move into the project directory:

```bash
cd exam-score-prediction
```

Install the required packages:

```bash
pip install -r python-project/requirements.txt
```

Run the Python script or open the notebook in Jupyter, depending on which part of the project you want to explore.

If the Flask application is configured to run independently, start it using the appropriate entry point and follow the URL shown in the terminal.

## GitHub Pages Deployment

The static website can be hosted using GitHub Pages.

1. Push the project files to a GitHub repository.
2. Open **Settings** in the repository.
3. Select **Pages** from the sidebar.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select the `main` branch and the `/ (root)` folder.
6. Save the settings and wait for deployment to finish.

GitHub Pages supports static files such as HTML, CSS, and JavaScript. It does not run Python or Flask applications directly. The browser-based version must therefore contain the JavaScript and model data needed for its prediction feature.

## Limitations

- Predictions are estimates, not guaranteed exam results.
- Model performance depends on the available dataset and selected features.
- Patterns found in the dataset may not represent every student or educational setting.
- The static website and Python application have different runtime requirements.

## Future Improvements

- Include more relevant student performance features.
- Compare different regression algorithms.
- Improve data cleaning and model evaluation.
- Add more detailed charts and performance summaries.
- Improve input validation and the overall user experience.

## Learning Outcomes

Through this project, I explored data preprocessing, exploratory data analysis, regression-based prediction, model evaluation, and the process of presenting machine learning results through a web interface.

It also provided practical experience in organizing a project repository and deploying a static website with GitHub Pages.

## Author

**Md Sobahan Hasan Saikat**

GitHub: [@saikat-71](https://github.com/saikat-71)

## License

This project is intended for educational and learning purposes. Add a license file if you want to specify the terms under which others may use or modify the code.

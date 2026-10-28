# Project Report: ExamScore AI

## 1. Introduction

ExamScore AI is an educational project that demonstrates a simple machine-learning workflow for estimating a student's exam score from selected study and academic indicators.

## 2. Problem Statement

Students often want to understand how study routine and previous academic performance relate to exam outcomes. This project builds a small demonstration tool to explore those relationships. It should not be interpreted as a definitive prediction of an individual's real exam result.

## 3. Objectives

- Inspect and clean a tabular student-performance dataset.
- Explore relationships between input features and exam scores.
- Train and evaluate a Random Forest regression model.
- Build an accessible, responsive dashboard for entering values and viewing an estimate.
- Publish the static dashboard using GitHub Pages.

## 4. Input Features

- Daily study hours
- Class attendance percentage
- Previous exam score
- Daily sleep hours

The target variable is the recorded exam score.

## 5. Methodology

1. Load the CSV dataset and inspect its columns and inconsistent values.
2. Convert suitable fields to numeric values and handle invalid/missing records.
3. Train a Random Forest regression model with scikit-learn.
4. Evaluate the model using regression metrics such as Mean Absolute Error (MAE) and R-squared (R²).
5. Export the model representation and supporting data for the static browser dashboard.
6. Validate user inputs in the website and show an estimated score.

## 6. Technology Stack

Python, pandas, scikit-learn, Matplotlib, Jupyter Notebook, HTML, CSS, JavaScript, Chart.js, GitHub, and GitHub Pages.

## 7. Expected Outcome

The project provides practice in data preparation, regression, model evaluation, frontend development, and static-site deployment. The dashboard presents a convenient demonstration of how model inputs affect an estimated output.

## 8. Limitations

The dataset may be small or not representative of a wider student population. Relationships in the data do not prove causation. Estimates can be inaccurate and must not be used for high-stakes academic decisions. GitHub Pages cannot execute the included Python training script; the website runs its exported browser-side model.

## 9. Future Scope

Potential improvements include collecting a larger and more representative dataset with appropriate permission, comparing several regression algorithms, documenting cross-validation results, adding automated tests, and improving accessibility and model explanations.

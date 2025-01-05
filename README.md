# Linear Regression Implementation in Python

This repository provides a manually implemented Linear Regression model in Python. The implementation is complemented with a Jupyter Notebook that demonstrates the usage of the Linear Regression class using a real-world dataset.

## Features
- **Custom Linear Regression Class**:
  - `fit` method: Computes the slope (coefficient) and intercept based on the training data.
  - `predict` method: Predicts target values for new inputs using the fitted model.
- Practical demonstration with data preprocessing, training, and evaluation.

## Repository Contents

1. **`LinearR.py`**:
   - This file contains the implementation of the `LinearRegression` class, which includes methods for fitting a model and making predictions.

2. **`Usage_Linear_regression_class.ipynb`**:
   - A Jupyter Notebook that demonstrates how to use the `LinearRegression` class with the Seaborn `tips` dataset.
   - Covers data preprocessing, model training, and prediction steps.

## Usage

### 1. Clone the Repository
```bash
git clone https://github.com/Dawood006/LinearRegression.git
cd LinearRegression
```

### 2. Install Dependencies
Ensure you have Python 3.6+ and the following libraries installed:

```bash
pip install numpy pandas seaborn scikit-learn
```

### 3. Run the Jupyter Notebook
To see the demonstration:

```bash
jupyter notebook Usage_Linear_regression_class.ipynb
```


## Demonstration
The included Jupyter Notebook (`Usage_Linear_regression_class.ipynb`) illustrates:

1. Loading and exploring the `tips` dataset.
2. Splitting data into training and testing sets.
3. Using the `LinearRegression` class for training and prediction.
4. Generating predictions for unseen data.




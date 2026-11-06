# Titanic Survival Prediction

A simple machine-learning web application that predicts whether a Titanic passenger is likely to survive. The application uses a pre-trained Logistic Regression model and a Streamlit interface.

## Project Overview

Users enter passenger details in the sidebar and click **Predict Survival**. The app displays the predicted outcome, estimated survival probability, and a progress indicator.

## Project Files

| File | Description |
|---|---|
| `app.py` | Streamlit application and prediction interface |
| `titanic_logistic_model.pkl` | Saved, pre-trained Logistic Regression model |
| `Titanic_train.csv` | Training dataset (891 rows; includes the `Survived` target column) |
| `Titanic_test.csv` | Test dataset (418 rows; does not include the target column) |
| `requirements.txt` | Python package dependencies |

## Input Features

The app collects these passenger details:

- **Passenger Class (`Pclass`)**: 1, 2, or 3
- **Gender (`Sex`)**: male or female
- **Age (`Age`)**
- **Siblings / Spouses (`SibSp`)**
- **Parents / Children (`Parch`)**
- **Ticket Fare (`Fare`)**
- **Port of Embarkation (`Embarked`)**: S, C, or Q

## Requirements

- Python 3.10 or a compatible Python version
- pip
- Packages listed in `requirements.txt`

## Setup and Run

1. Download or clone this project and extract the ZIP file.
2. Open a terminal in the project folder (the folder containing `app.py`).
3. Create and activate a virtual environment (recommended):

   **Windows**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **macOS / Linux**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

6. Streamlit will open the application in your browser. If it does not, open the local URL shown in the terminal.

## How to Use

1. Select the passenger class and gender.
2. Enter age, family counts, and fare.
3. Select the embarkation port.
4. Click **Predict Survival**.
5. Review the predicted result and survival probability.

## Notes

- Keep `titanic_logistic_model.pkl` in the same folder as `app.py`; the app loads it using a relative file path.
- The saved model must be compatible with the installed versions of its Python dependencies.
- `Titanic_train.csv` and `Titanic_test.csv` are included as project datasets. The current `app.py` loads the saved model directly and does not train it when the app starts.
- Predictions are estimates from a machine-learning model, not guarantees of actual outcomes.

## Technologies Used

- Python
- Pandas
- Scikit-learn (model)
- Joblib (saved model loading)
- Streamlit

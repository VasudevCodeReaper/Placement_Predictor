from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
model_xgb = joblib.load("model_xgb.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    probability = None
    confidence = None

    if request.method == "POST":

        gender_map = {
            "F": 0,
            "M": 1
        }

        board_map = {
            "Central": 0,
            "Others": 1
        }

        subject_map = {
            "Arts": 0,
            "Commerce": 1,
            "Science": 2
        }

        degree_map = {
            "Comm&Mgmt": 0,
            "Others": 1,
            "Sci&Tech": 2
        }

        work_map = {
            "No": 0,
            "Yes": 1
        }

        specialisation_map = {
            "Mkt&Fin": 0,
            "Mkt&HR": 1
        }

        data = [[
            gender_map[request.form["gender"]],
            float(request.form["ssc_percentage"]),
            board_map[request.form["ssc_board"]],
            float(request.form["hsc_percentage"]),
            board_map[request.form["hsc_board"]],
            subject_map[request.form["hsc_subject"]],
            float(request.form["degree_percentage"]),
            degree_map[request.form["undergrad_degree"]],
            work_map[request.form["work_experience"]],
            float(request.form["emp_test_percentage"]),
            specialisation_map[request.form["specialisation"]],
            float(request.form["mba_percent"])
        ]]

        columns = [
            "gender",
            "ssc_percentage",
            "ssc_board",
            "hsc_percentage",
            "hsc_board",
            "hsc_subject",
            "degree_percentage",
            "undergrad_degree",
            "work_experience",
            "emp_test_percentage",
            "specialisation",
            "mba_percent"
        ]

        df = pd.DataFrame(data, columns=columns)
        df = pd.get_dummies(df)
        df = df.reindex(columns=model_xgb.feature_names_in_, fill_value=0)
        pred = model_xgb.predict(df)[0]
        probability = model_xgb.predict_proba(df)[0][1] * 100

        prediction = "Placed ✅" if pred == 1 else "Not Placed ❌"

        if probability >= 80:
            confidence = "High"
        elif probability >= 60:
            confidence = "Medium"
        else:
            confidence = "Low"

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, jsonify, request
from database import load_profile_questions_from_db, add_survey_to_db

app = Flask(__name__)


@app.route("/")
def hello_mind():
  profile_questions = load_profile_questions_from_db()
  return render_template("survey.html", profile_questions=profile_questions)


@app.route("/survey/submit", methods=['post'])
def submit_survey():
  data = request.form
  profile_questions=load_profile_questions_from_db()
  add_survey_to_db(data)

  return render_template("survey_submitted.html",
                    profile_answers=data,
                    profile_questions=profile_questions)
 


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

from flask import Flask, render_template, jsonify, request
from database import load_profile_questions_from_db, load_survey_questions_from_db, add_profile_to_db, add_survey_to_db

from generate_radom_survey import generate_random_survey

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template("home.html")


  
@app.route("/survey")
def hello_mind():
  profile_questions = load_profile_questions_from_db()
  survey_questions=generate_random_survey()
  return render_template("survey.html", profile_questions=profile_questions,
                        survey_questions=survey_questions)


@app.route("/survey/submit", methods=['post'])
def submit_survey():
  data = request.form
  profile_questions=load_profile_questions_from_db()
  add_profile_to_db(data)

  survey_questions=generate_random_survey()
  add_survey_to_db(data)

  return render_template("survey_submitted.html",
                    profile_answers=data,
                    profile_questions=profile_questions,
                    survey_questions=survey_questions)



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

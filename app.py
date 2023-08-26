from flask import Flask, render_template, jsonify, request

app=Flask(__name__)

@app.route("/")
def hello_mind():
  survey=load_survey_from_db()
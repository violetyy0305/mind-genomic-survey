from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_profile_questions_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from profile_questions"))
    profile_questions = []
    keys = list(result.keys())
    for question in result.all():
      d = {}
      for i in range(len(question)):
        d[keys[i]] = question[i]
      profile_questions.append(d)

  return profile_questions


def add_profile_to_db(data):
  with engine.connect() as conn:
    query = text(
      "insert into profile_answers(gender,age_group,employment) values(:gender,:age_group, :employment)"
    )
    conn.execute(
      query, {
        "gender": data['gender'],
        "employment": data['employment'],
        "age_group": data['age_group']
      })


def load_survey_questions_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from survey_questions"))
    survey_questions = []
    keys = list(result.keys())
    for question in result.all():
      d = {}
      for i in range(len(question)):
        d[keys[i]] = question[i]
      survey_questions.append(d)

  return survey_questions


def add_survey_to_db(data,r_time):
  with engine.connect() as conn:
    query = text(
      "insert into survey_answers(question_1,question_2,question_3,question_4,question_5,question_6,question_7,question_8,question_9,question_10,r_time) values(:question_1,:question_2,:question_3,:question_4,:question_5,:question_6,:question_7,:question_8,:question_9,:question_10,:r_time)"
    )
    conn.execute(
      query, {
        "question_1": data['question_1'],
        "question_2": data['question_2'],
        "question_3": data['question_3'],
        "question_4": data['question_4'],
        "question_5": data['question_5'],
        "question_6": data['question_6'],
        "question_7": data['question_7'],
        "question_8": data['question_8'],
        "question_9": data['question_9'],
        "question_10": data['question_10'],
        "r_time":r_time
      })

'''
def add_time_to_db(r_time):
  with engine.connect() as conn:
    query = text(
      "insert into time(q1_r_time, q2_r_time, q3_r_time ,q4_r_time ,q5_r_time ,q6_r_time ,q7_r_time ,q8_r_time ,q9_r_time ,q10_r_time) values(:q1_r_time,:q2_r_time,:q3_r_time,:q4_r_time,:q5_r_time,:q6_r_time,:q7_r_time,:q8_r_time,:q9_r_time,:q10_r_time)"
    )
    conn.execute(
      query, {
       "q1_r_time":r_time['question_1'], 
       "q2_r_time":r_time['question_2'], 
       "q3_r_time":r_time['question_3'], 
       "q4_r_time":r_time['question_4'], 
       "q5_r_time":r_time['question_5'], 
       "q6_r_time":r_time['question_6'], 
       "q7_r_time":r_time['question_7'], 
       "q8_r_time":r_time['question_8'], 
       "q9_r_time":r_time['question_9'], 
       "q10_r_time":r_time['question_10']
      })

'''


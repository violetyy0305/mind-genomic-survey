from sqlalchemy import create_engine, text
import os

db_connection_string=os.environ['DB_CONNECTION_STRING']

engine=create_engine(db_connection_string,
                    connect_args=
                     {
                      "ssl":{
                        "ssl_ca": "/etc/ssl/cert.pem"
                      }
                    })

def load_profile_questions_from_db():
  with engine.connect() as conn:
    result=conn.execute(text("select * from profile_questions"))
    profile_questions=[]
    keys=list(result.keys())
    for question in result.all():
      d={}
      for i in range(len(question)):
        d[keys[i]]=question[i]
      profile_questions.append(d)

  return profile_questions


def add_survey_to_db(data):
  with engine.connect() as conn:
    query=text("insert into profile_answers(gender,age_group,employment) values(:gender,:age_group, :employment)")
    conn.execute(query,
                {
                 "gender":data['gender'],
                  "employment":data['employment'],
                  "age_group":data['age_group']})









def load_profile_question_from_db(id):
  with engine.connect() as conn:
    result=conn.execute(text("select * from profile_questions where id=:val"),{"val":id})
    row=result.all()
    if len(row)==0:
      return None
    else:
      key=list(result.keys())
      d={}
      for i in range(len(row[0])):
        d[key[i]]=row[0][i]
      return d



from database import load_survey_questions_from_db

import random

survey_questions = load_survey_questions_from_db()
'''
def get_category(): 
  category=[]
  for i in range(len(survey_questions[0].keys())-1):
    keys=list(survey_questions[0].keys())
    category_tmp=[]
    for j in range(len(survey_questions)):
        category_tmp.append(survey_questions[j][keys[i+1]])
    category.append(category_tmp)

  return category



'''


def get_category():
  category = {}
  keys = list(survey_questions[0].keys())

  for i in range(len(survey_questions[0].keys()) - 1):

    categl = []

    for j in range(len(survey_questions)):

      category[keys[i + 1]] = categl
      categl.append(survey_questions[j][keys[i + 1]])

  return category


category_dict = get_category()

num_category = len(category_dict)
# every category has same number of elements
num_element = len(category_dict[list(category_dict.keys())[0]])
num_element_per_vignette = 3
num_vignette = 10
num_per_element = int(
  round((num_element_per_vignette * num_vignette) / (num_category * num_element)))


def generate_random():
  category = []
  for key in category_dict.keys():
    catel = []
    for i in range(len(category_dict[key])):
      for j in range(num_per_element):
        catel.append(category_dict[key][i])
    category.append(catel)
  
  for i in range(len(category)):
    random.shuffle(category[i])
 
  return category

def generate_random_survey():
  survey=[]
  ele=generate_random()
  for i in range(len(ele[0])):
    surl=["question_"+str(i+1)]
    for j in range(num_element_per_vignette):
      surl.append(ele[j][i])
    survey.append(surl)

  return survey


  
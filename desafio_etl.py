import pandas as pd
import requests
import json
import openai

# EXTRACT
sdw2023_api = 'https://sdw-2023-prd.up.railway.app'

data = pd.read_csv('list_users.csv')
user_ids = data['UserID'].tolist()
print(user_ids)

def get_user(id):
  response = requests.get(f'{sdw2023_api}/users/{id}')
  return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

# TRANSFORM
for user in users:
  news = "Leve sua saúde financeira à sério. Conheça nossos cursos e mentorias sobre Educação Financeira. Participe!"
  print(news)
  user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
  })

#LOAD
def update_user(user):
  response = requests.put(f"{sdw2023_api}/users/{user['id']}", json=user)
  return True if response.status_code == 200 else False

for user in users:
  success = update_user(user)
  print(f"User {user['name']} updated? {success}!")
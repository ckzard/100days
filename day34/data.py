import requests

api_questions = requests.get("https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean")
api_questions.raise_for_status()

question_data = api_questions.json()["results"]
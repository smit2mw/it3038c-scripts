#https://gist.github.com/iampawan/f7c084f8ba8889a87b3e8d148fc78341
#https://www.youtube.com/watch?v=EolFGrohtzw&ab_channel=mtechviral




import requests
from bs4 import BeautifulSoup
import json

res = requests.get("https://stackoverflow.com/questions")

soup = BeautifulSoup(res.text, "html.parser")

questions_data = {
    "questions": []
}

questions = soup.select(".question-summary")

for que in questions:
    q = que.select_one('.question-hyperlink').getText()
    vote_count = que.select_one('.vote-count-post').getText()
    views = que.select_one('.views').attrs['title']
    questions_data['questions'].append({
        "question": q,
        "views": views,
        "vote_count": vote_count
    })

json_data = json.dumps(questions_data)

print(json_data)
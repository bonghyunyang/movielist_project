import requests
import json
import pandas as pd
from pandas.io.json import json_normalize

api_url = 'https://yts.mx/api/v2/list_movies.json?limit=50&page=5'
data = requests.get(api_url)
json_data = json.loads(data.text)  # requests로 데이터 받아 dict 형태로 구현

body = [json_data['data']['movies']]
result = json_normalize(json_data['data']['movies'])  # pandas normalize 이용
result.to_csv('result.csv')  # csv 파일로 저장

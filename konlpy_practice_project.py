# 라이브러리
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import string
import re
from konlpy.downloader import default_download_dir
from konlpy.tag import Okt
import os
import pandas as pd
import torch
from wordcloud import WordCloud


# 텍스트 수집
url = "https://www.yna.co.kr/view/AKR20260624044200002?input=1195m"

    # 웹사이트 차단을 방지하기 및 정상적인 html을 받기위해
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

    # 제목
title = soup.select_one("header h1").get_text(strip=True)

    # 본문
article = soup.select_one("#articleWrap > div.story-news.article")
paragraphs = article.find_all("p")

content = "\n".join(
    p.get_text(strip=True)
    for p in paragraphs)

text = title + content

# print(title)
# print(content)
# print(text)


# 텍스트 정제
clean_text = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣\s]',' ', text)
clean_text = re.sub(r'\s+', ' ', clean_text).strip()
# print("정제된 텍스트:")
# print(clean_text)


# 형태소 분석
okt = Okt()


# 불용어 제거
stopwords = pd.read_csv('data/stopword.csv', header=None, encoding='utf-8')
stopwords = stopwords[0].tolist()
tokens = okt.nouns(text)
tokens = [word for word in tokens if word not in stopwords and len(word) > 1]
# print(tokens)


# 단어 빈도 계산
word_dic = {}

for word in tokens:
    print(word, end=" ")
    if word not in word_dic:
        word_dic[word] = 0
    word_dic[word] += 1

keys = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)
# print(keys[:20])


# PyTorch Tensor 변환
    # 숫자로 변환 후 tensor 변환
vocab = list(word_dic.keys())
word_to_id = {keys:idx for idx, keys in enumerate(vocab)}
word_ids = [word_to_id[word] for word in tokens]
word_tensor = torch.tensor(word_ids, dtype=torch.long)


# 워드클라우드 생성
wordcloud = WordCloud(
    font_path = "C:/Windows/Fonts/malgun.ttf",
    width=1200, height=800,
    background_color="white",
    min_font_size=10,
    max_font_size=500,
).generate_from_frequencies(word_dic)


# 상위 20개 단어 시각화
plt.figure(figsize=(12, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.title = "Konlpy Practice Project"
plt.show()


# 결과 분석 보고서 작성

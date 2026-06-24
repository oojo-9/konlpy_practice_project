# KoNLPy Practice Project

KoNLPy를 활용한 뉴스 기사 텍스트 분석 프로젝트입니다.

연합뉴스의 IT 관련 기사를 수집한 후 형태소 분석을 수행하고, 단어 빈도를 계산하여 WordCloud를 통해 핵심 키워드를 시각화하였습니다.

---

## 프로젝트 개요

최근 IT 뉴스 중 빅테크 관련 기사를 선정하여 텍스트 데이터를 분석하였습니다.

본 프로젝트에서는 뉴스 기사로부터 제목과 본문을 추출한 후, KoNLPy를 이용하여 형태소 분석 및 불용어 제거를 수행하였습니다.

이후 단어 빈도를 계산하고 WordCloud를 생성하여 기사에서 중요하게 언급되는 핵심 단어를 직관적으로 확인할 수 있도록 하였습니다.

---

## 사용 라이브러리

* requests
* BeautifulSoup4
* re
* KoNLPy
* pandas
* PyTorch
* WordCloud

---

## 프로젝트 구조

```text
konlpy_practice_project
│
├── data
│   └── stopword.csv
│   └── img.png
│
├── fonts
│   └──  malgun.ttf
│
├── .gitignore
├── konlpy_practice_project.py
├── README.md
├── requirements.txt
└── 결과분석보고서.md

```
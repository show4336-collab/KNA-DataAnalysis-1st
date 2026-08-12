# 1. 현재 경로에 가상환경 생성(터미널에서)
# python -m venv .venv


# 2. 가상환경 활성화
# source .venv/Scripts/activate
# (이후에는 가상환경 안에서 터미널 명령 실행 가능
# python -m pip install pandas

# 3. (작업/실행 끝나고) 가상환경 종료
# deactivate
# 다시 실행할땐 source .venv/Scripts/activate
# python 파일이름.py
# 작업끝 deactivate

# import pandas as pd
# import os

# cwd = os.getcwd()
# cwd = os.path.join()
# cwd_path = os.path.join(cwd, '.venv', '12_metro_small.csv')
# cwd_path = os.path.join('.venv', '12_metro_small.csv')

# 실습 1. csv 불러오기 워밍업
# df = pd.read_csv('.venv/12_metro_small.csv')
# print(df.shape) # (30, 7) -> 열 제목 제외하고 (행, 열)
# print(df.head(2)) # 0, 1, 2번 인덱스 총 3줄 보여줌

# head로 보고, shape로 재고, describe로 뽑고

# try:
    # df = pd.read_csv('.venv/12_metro_small.csv', encoding='utf-8', sep=',', index_col=(0))
    # 위, 아래는 동일함.
    # df = pd.read_csv('.venv/12_metro_small.csv', encoding='utf-8', sep=',', index_col='측정시각')
    # df = pd.read_csv('.venv/12_metro_small.csv', encoding='utf-8', sep=',', index_col='측정시각', nrows=5)
    # nrows는 위에서 5줄만 가져와봐
    # print(df.shape) # (5, 6)
    # df = pd.read_csv('.venv/12_metro_small.csv', encoding='utf-8', sep=',', index_col='측정시각', nrows=5, usecols=["측정시각", "가동상태"])
    # index_col='측정시각'을 했기 때문에 usecols을 사용할 때 반드시 포함 시켜야함.
    # usecols=["측정시각", "가동상태"]
    # print(df)
    # print(df.shape)

# except FileNotFoundError:
    # print('파일이 없습니다.')

# 실습 2. 설비 센서 csv 불러오기
# import pandas as pd

# 12_metro_compressor.csv
# 200행 7열 인덱스 3번 행 오일온도가 NaN

# df = pd.read_csv('.venv/12_metro_compressor.csv', encoding='utf-8')
# print(df.head(10))
# print(df.shape) # (200, 7)

# 실습 3. 한글•구분자 깨짐 옵션 다루기
# 세미콜론 구분 파일
# sep 없이 읽으면 200행 1열, sep=';'이면 200행 7열

# import pandas as pd

# df = pd.read_csv('.venv/12_metro_compressor_semicolon.csv', encoding='utf-8')
# print(df.head(4))
# print(df.shape) # (200, 1)
# df = pd.read_csv('.venv/12_metro_compressor_semicolon.csv', encoding='utf-8', sep=';')
# print(df.head(4))
# print(df.shape) # (200, 7)

# 실습 4. 필요한 열만 골라 불러오기
# usecols와 nrows로 열 많은 데이터에서 필요한 부분만

# import pandas as pd

# df = pd.read_csv('.venv/12_metro_compressor.csv')
# print(df.shape) # (200, 7)

# df = pd.read_csv('.venv/12_metro_compressor.csv', 
#                  usecols=['측정시각', '압축압력', '배출압력', '가동상태'])
# print(df.shape) # (200, 4)
# print(df.head(3))

# 실습 5. 경로옵션 오류 고치기
# import pandas as pd

# df = pd.read_csv('없는파일.csv') # FileNotFoundError
# print(df.shape)

# 실습 6. read_csv 옵션 종합 연습
# 실습과제 세미콜론+한글 파일에서 필요한 열만
# sep을 잘 사용해서 여러 컬럼이 읽히도록 해주세요.
# encoding도 지정해주세요.
# 모든 컬럼을 다 읽지는 마시고, '측정시각', '오일온도', '모터전류' 컬럼만 읽어주세요.

# import pandas as pd

# df = pd.read_csv('.venv/12_metro_compressor_semicolon.csv', encoding='utf-8', sep=';', usecols=['측정시각', '오일온도', '모터전류'])
# print(df.shape) # (200, 3)
# print(df)

# import pandas as pd

# print("실습 1. head, tail로 디지털 신호 살펴보기")
# df = pd.read_csv('.venv/12_metro_digital.csv', encoding='utf-8')
# print(df.shape) # (120, 4)
# print(df.head())
# print(df.head(50))
# print(df.tail(60))



# print("실습 2. head, tail 행 개수 조절")
# df = pd.read_csv('.venv/12_metro_compressor.csv', encoding='utf-8')
# print(df.shape) # (200, 7)
# print(df.head(1))
# print(df.head(10))
# print(df.tail(7))
# print(df.head(500))

# =================================
# print(df.columns) # Index(['측정시각', '압축압력', '배출압력', '저장압력', '오일온도', '모터전류', '가동상태'], dtype='str')
# columns로 열 제목을 확인해서 usecols=['열 제목 1', '열 제목 2'] 처럼 원하는 열만 출력 가능!!




# print("실습 3. 구조 파악 3종 도구")
# shape · columns · dtypes로 데이터 뼈대 읽기

# 12_metro_digital.csv 읽어와서 DataFrame에 담기
# .shape 출력
# .columns 출력 df.columns.tolist() 도 출력
# .dtypes 출력

import pandas as pd
# df = pd.read_csv('.venv/12_metro_digital.csv', encoding='utf-8')
# print(df.shape) # (120, 4)
# print(df.columns) # Index(['측정시각', '압축기', '타워', '저압스위치'], dtype='str')
# print(df.dtypes)


# print("실습 4. 열 이름 자료형 점검")
# 12_metro_compressor.csv 읽어와서 DF에 담기 
# .columns 출력 df.columns.tolist() 도 출력
# DF의 dtypes 출력
# df = pd.read_csv('.venv/12_metro_compressor.csv', encoding='utf-8')
# print(df.columns) # Index(['측정시각', '압축압력', '배출압력', '저장압력', '오일온도', '모터전류', '가동상태'], dtype='str')
# print(df.columns.tolist()) # ['측정시각', '압축압력', '배출압력', '저장압력', '오일온도', '모터전류', '가동상태']
# print(df.dtypes)

# =============================================
# df.info()은 non null count가 핵심
# info() 하나면 데이터 구조를 거의 다 파악 - 종합 검진 같은 도구
# RangeIndex: 200 entries, 0 to 199
# Data columns (total 7 columns):
# #   Column  Non-Null Count  Dtype  
#  0   측정시각    200 non-null    str    
#  1   압축압력    200 non-null    float64
#  2   배출압력    200 non-null    float64
#  3   저장압력    200 non-null    float64
#  4   오일온도    199 non-null    float64
#  5   모터전류    200 non-null    float64
#  6   가동상태    200 non-null    str    
# dtypes: float64(5), str(2)

# print("실습 5. info로 데이터 건강검진")

# 12_metro_digital.csv 파일을 읽어서 df 생성
# df의 info() 호출 출력
# 
# df = pd.read_csv('.venv/12_metro_digital.csv', encoding='utf-8')
# print(df.info())
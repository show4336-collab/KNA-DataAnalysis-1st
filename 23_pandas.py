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

# import pandas as pd

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

# print("실습 6. describe로 이상 신호 찾기")

# import pandas as pd

# df = pd.read_csv(
# ".venv/12_metro_compressor.csv", encoding="utf-8", usecols=["오일온도", "모터전류"]
# )
# print(df.shape)
# print(df.head(1))
# print(df.tail(5))
# df.info()

# print(df.describe())
# describe는 데이터가 잘 읽혔나 미리보는 느낌임. 저기서 가져올 순 없음.
# 온도 평균 63.181910 최댓값 75.0
# 온도 75% 68.1 최댓값 75.0


# 1 온도의 평균과 최댓값 차이를 숫자로 적었는가
# 평균 75 대 max 75.0 — 차이를 기록
#  75.000000 - 63.181910 = 11.81809

# 2 75%와 max 차이가 큰 열을 두 개 이상 찾았는가
# 온도와 진동— max가 멀리 튄 열 찾기
# 오일온도 : 75% = 68.1, max = 75.0
# CSV 확인 : 109번 행(2020-03-03 12:36:57), 오일온도 75.0
#            162번 행(2020-03-05 08:35:57), 오일온도 75.0

# 모터전류 : 75% = 3.8125, max = 6.19
# CSV 확인 : 103번 행(2020-03-03 06:31:23), 모터전류 6.19


# 3 모터전류처럼 고른 열과 비교해 차이를 설명
# 모터전류는 75%와 max가 가까움— 온도와의 차이 설명
# 모터전류 75% 3.8125 최댓값 6.19

# 가깝다는 기준이 모호함.
# 퍼센트로 보면 온도 75%와 최댓값과의 퍼센트 차이는 약 10프로
# 모터전류는 약 150% 차이가 나서 비교 불가임.

# print("실습 7. 통계량 문장으로 묘사")
# describe() 통계를 자기 말로 풀어 설명
# 설비 센서 데이터의 "한 열(1 column)을 묘사"

# import pandas as pd

# df = pd.read_csv(".venv/12_metro_compressor.csv", encoding="utf-8")
# df.info()

# print(df["오일온도"])
# df["오일온도"].info()

# 오일온도 컬럼만 떼서 describe 통계 보기
# print(df["오일온도"].describe())

# count    199.000000
# mean      63.181910 (평균)
# std        6.249822 (표준편차)
# min       50.100000 (최솟값)
# 25%       58.100000
# 50%       62.900000 (중앙값)
# 75%       68.100000
# max       75.000000 (최댓값)
# Name: 오일온도, dtype: float64

# 1. 오일온도의 평균은 약 63.18이며, 최저 50.1, 최고 75.0이고 중앙값은 62.9이다.

# 2. 표준편차는 약 6.25로, 오일온도가 크게 들쭉날쭉하기보다는
#    평균을 중심으로 일정 범위 안에서 변동하는 것으로 보인다.

# 3. 전체 데이터의 절반 정도가 58.1~68.1 사이에 분포하고 있어,
#    오일온도는 대부분 평균인 63도 부근에서 형성되는 것으로 보인다.

# print("실습 8. 압축기와 디지털 신호 구조 비교")
# .venv/12_metro_compressor.csv
# .venv/12_metro_digital.csv
# shape, info, describe

# import pandas as pd

# df_compressor = pd.read_csv(".venv/12_metro_compressor.csv")
# print(df_compressor.shape) # (200, 7)
# df_compressor.info()
# print(df_compressor.describe())
# print(df_compressor.head(5))

# df_digital = pd.read_csv(".venv/12_metro_digital.csv")
# print(df_digital.shape)  # (120, 4)
# df_digital.info()
# print(df_digital.describe())

# 1. 변수를 구분했는가 : df_compressor, df_digital

# 2. info로압축기는결측없고디지털신호은있다는차이확인
# 디지털 신호는 결측 없음.
# 압축기는 3번 인덱스값에 오일온도 NaN으로 결측있음.

# 3. 어느쪽이바로분석가능하고어느쪽이정리필요한가
# 압축기 데이터는 오일온도에 결측치가 있어 정리가 필요하고
# 디지털신호는 결측치가 없어 바로 분석이 가능하다.

# import pandas as pd

# print("실습 9. 첫 탐색 종합")

# df_digital_sample = pd.read_csv(".venv/12_metro_small.csv")

# print(df_digital_sample.head(5))
# print(df_digital_sample.shape)  # (30, 7)
# print(
#     df_digital_sample.columns
# )  # Index(['측정시각', '압축압력', '배출압력', '저장압력', '오일온도', '모터전류', '가동상태'],dtype='str')
# print(df_digital_sample.dtypes) # object
# df_digital_sample.info() # 오일온도 NaN 결측 발견!


# print("종합 실습 2 - 통계 미리보기")
# import pandas as pd

# df_digital_sample = pd.read_csv(".venv/12_metro_small.csv")
# print(df_digital_sample.describe())
#     압축압력       배출압력    저장압력   오일온도    모터전류
# count  30.000000  30.000000  30.000000  29.000000  30.000000
# mean    8.895333  -0.019667   8.896000  54.675862   1.383000
# std     0.571083   0.001826   0.570629   2.864893   2.167832
# min     8.130000  -0.020000   8.130000  50.100000   0.030000
# 25%     8.432500  -0.020000   8.432500  51.800000   0.040000
# 50%     8.655000  -0.020000   8.660000  55.400000   0.040000
# 75%     9.315000  -0.020000   9.315000  57.100000   3.745000
# max     9.960000  -0.010000   9.960000  59.600000   6.070000

# 오일온도 NaN값 모터전류 평균값 1.38인데 max가 6.07


# print("종합 실습 3 - 첫 탐색 리포트")

# 1. 개요
# 압축기 데이터는 총 200행 7열로 구성되어 있다.

# 2. 열 구성
# 측정시각, 압축압력, 배출압력, 저장압력,
# 오일온도, 모터전류, 가동상태로 구성되어 있다.
# 측정시각과 가동상태는 문자형이고,
# 압력, 오일온도, 모터전류는 숫자형 데이터이다.

# 3. 결측
# 오일온도의 count가 199로 확인되어 결측값이 1개 존재한다.
# 따라서 오일온도를 분석하기 전에 결측값 확인이 필요하다.

# 4. 통계
# 오일온도는 평균 약 63.18, 중앙값 62.9,
# 최솟값 50.1, 최댓값 75.0이다.
# 표준편차는 약 6.25로 평균을 중심으로 어느 정도 변동하고 있다.
# 전체 데이터의 가운데 50%는 58.1~68.1 사이에 분포한다.

# 5. 이상 신호
# 오일온도의 75% 값은 68.1이고 최댓값은 75.0으로 차이가 있다.
# 최댓값처럼 평소 범위에서 벗어난 값은 이상 신호 후보로 볼 수 있다.
# 다만 이 값만으로 실제 설비 이상이라고 단정할 수는 없다.

# 6. 종합 의견
# 데이터의 전체적인 구조와 통계 분포는 확인할 수 있었지만,
# 오일온도에 결측값이 있어 분석 전에 확인 및 처리가 필요하다.
# 또한 최댓값 등 평소 범위에서 벗어난 값은 실제 이상인지
# 추가로 확인할 필요가 있다.

# print("종합 실습 - 결과 공유와 교차 점검")

# 1. 결측
# 오일온도에 결측값 1개가 있는 것을 확인했다.

# 2. 이상 신호
# 오일온도의 75%는 68.1, 최댓값은 75.0으로 차이가 있어
# 최댓값이 이상 신호 후보가 될 수 있다고 판단했다.

# 3. 종합 의견
# 다른 사람의 분석과 비교할 때 결측값을 동일하게 발견했는지,
# 어떤 값을 이상 신호로 판단했는지 비교할 필요가 있다.
# 특히 같은 통계값을 보고도 이상 신호에 대한 판단은
# 서로 다를 수 있으므로 그 판단 근거를 함께 확인해야 한다.


# ===============================

# 단일 컬럼(col) 선택

# import pandas as pd

# df = pd.read_csv(".venv/13_diecasting_small.csv")
# df.info()  # <class 'pandas.DataFrame'>

# 데이터 프레임(2차원)에서 컬럼 한개를 도려내보면 시리즈(1차원)이 된다.

# 단일 열 선택 df['형체력']
# s = df["형체력"]
# s.info() # <class 'pandas.Series'>
# print(s)
# print(s)
# print(s[0])  # 258.0

# series랑 DataFrame차이는 info()로 확인해도 되고 type(df['형체력])으로 확인해도 됨

# df["형체력"].info()  # Series

# 복수 열 선택 df[['형체력', '실린더압력']]
# df[["형체력", "실린더압력"]].info()  # DataFrame


# 한 겹과 두 겹 결과 비교
# 한 겹 df['형체력'] -> Series
# 두 겹 df[['형체력']] -> DataFrame
# 두 겹 여러 열 df[['형체력', '실린더압력']] -> DataFrame
# .info() 하면 Series인지 DataFrame인지 바로 알 수 있음.

# print(df.columns)

# print("실습 1. 데이터 불러오기와 구조 확인하기")

# df = pd.read_csv(".venv/13_diecasting_small.csv")
# print(df.shape)  # (30, 7)
# print(df.columns) # Index(['샷', '실린더압력', '주조압력', '사이클타임', '비스킷두께', '형체력', '품질등급'], dtype='str')


# line()
# print("실습 2. 열 선택하기")

# df = pd.read_csv(".venv/13_diecasting_small.csv")
# print(df["형체력"])
# df["형체력"].info() # Series

# df[["형체력", "실린더압력"]].info()  # DataFrame
# print(round(df["형체력"].mean(), 1))  # 267.8
# print(round(df["실린더압력"].mean(), 1))  # 219.7
# 밑에는 응용해봤습니다. 데이터프레임도 이렇게 쓸 수 있는군요.
# print(round(df[["실린더압력", "형체력"]].mean(), 1))  # 실린더 압력 219.7  형체력 267.8
# print(df[["실린더압력", "형체력"]].max())
# print(df[["실린더압력", "형체력"]].min())
# print(df[["실린더압력", "형체력"]].std())
# print(df[["실린더압력", "형체력"]].describe())

# line()
# print("실습 3. 공정 센서 열 골라내기")

# df = pd.read_csv(".venv/13_diecasting_shot.csv")

# print(df.columns)

# s = df["형체력"]
# s.info()  # series

# print(df[["형체력", "실린더압력", "주조압력"]].shape) # (200, 3)


# line()

# df = pd.read_csv(".venv/13_diecasting_shot.csv")

# df.loc[0].info()
# print(df.loc[0])  # series
# print(df.loc[:2])  # DataFrame


# df_part = df.loc[0:2, ["품질등급", "형체력"]]
# print(df_part)
# df_total = df.loc[:, ["형체력", "실린더압력"]]
# print(df_total)
# print(df.iloc[:5])  # 정렬 후 맨 위 인덱스를 몰라도 상위5개를 정확히 추출

# print('실습 4. loc와 iloc로 행 선택하기')

# import pandas as pd

# df = pd.read_csv(".venv/13_diecasting_shot.csv")
# print(df.loc[0])
# print(df.iloc[0])
# 위는 동일

# print(df.loc[0, "품질등급"])  # 양품
# print(df.iloc[0]["품질등급"])  # 양품
# print(df.loc[0])
# print(df.iloc[0])
# print(len(df.loc))
# print(len(df.iloc[3, 2]))
# print(len(df.loc[0:2])) # 3 loc은 0, 1, 2
# print(len(df.iloc[0:2])) # 2 iloc은 0, 1


# print("실습 5 loc iloc로 행 열 동시 선택하기")

# print(df.loc[:4, ["형체력", "주조압력"]].shape)  # (5, 2)
# print(df.loc[6:10, ["형체력", "주조압력", "사이클타임"]].shape)  # (5, 3)
# print(df.iloc[-3:])
# 샷  실린더압력   주조압력   사이클타임  비스킷두께    형체력 품질등급
# 197  198  113.0  255.0    36.6   27.0  354.0   불량
# 198  199  264.0  595.0    36.1   19.0  372.0   불량
# 199  200  108.0  525.0  6170.0   15.0  237.0   불량


# # print("실습 6. 특정 구간 추출 종합")
# df_shot = pd.read_csv(".venv/13_diecasting_shot.csv")

# cols = ["실린더압력", "주조압력", "사이클타임", "비스킷두께", "형체력"]
# # print(df_shot[cols].iloc[0:10].shape)  # 결과는? (10, 5)
# print(df_shot.loc[:10, ["주조압력", "사이클타임"]].shape)  # 결과는 ? (11, 2)
# print(df_shot.iloc[:10, :6].shape)  # (10, 6)


# def line():
#     print("=" * 40)


# line()
# print('실습 1. 단일 조건으로 행 추출하기')
# import pandas as pd

# df = pd.read_csv(".venv/13_diecasting_small.csv")
# df.info()
# df_pressure = df["실린더압력"] >= 230

# print(len(df_pressure))  # 30
# print(df_pressure.sum())  # 5

# line()
# print('실습 2. 임계값 넘는 설비 골라내기')
# df = pd.read_csv(".venv/13_diecasting_small.csv")

# 만든 조건을 데이터프레임 대괄호에 넣어 임계값 초과 설비만 추출
# 전체 df를 대상으로 앞서 특정 컬럼에 대한 불리언 시리즈를
# 컬럼 요구하는 [] 사이에 넣어주면,
# 각 줄마다 비교를 해서 True인 경우만 추려 새로운 df를 만든다.
# s_limit = df["비스킷두께"] >= 16  # series
# print(df[s_limit])
# 위, 아래는 동일한 코드임.
# print(df[df["비스킷두께"] >= 16])
# print(len(df[df["비스킷두께"] >= 16]))  # 5

# df_sub = df[df["비스킷두께"] >= 16]
# print(df_sub[["샷", "비스킷두께"]])
# 위, 아래는 동일한 코드임
# print(df[df["비스킷두께"] >= 16][["샷", "비스킷두께"]])


# line()

# df = pd.read_csv(".venv/13_diecasting_small.csv")
# df_sub_1 = df[df["비스킷두께"] >= 13]
# df_sub_1.info()  # 6 entries

# df_sub_2 = df[df["사이클타임"] >= 25]
# df_sub_2.info() # 6 entries
# df_both = df[(df["비스킷두께"] >= 13) & (df["사이클타임"] >= 25)]
# print(df_both)
# print(len(df_both))  # 5


# df_both = df[(df["비스킷두께"] >= 13) | (df["사이클타임"] >= 25)]
# print(df_both)
# print(len(df_both))  # 7

# df = pd.read_csv(".venv/13_diecasting_small.csv")


# 범위 검사 between
# print(
# df[(df["비스킷두께"].between(13, 20))]
# )  # 비스킷두께 13이상 20이하인 값의 행들을 보여줌.
# print((df["비스킷두께"].between(13, 20)))  # True, False로 반환.


# 부정 뒤집기 ~(조건).isin(목록)

# .str.contains('문자')
# print(df["품질등급"].str.contains("양품"))  # True, False로 반환.
# print(df[df["품질등급"].str.contains("양품")])  # 품질등급이 양품인 행들만 출력 / 문자열만 가능!


# print()

# line()
# print("실습 3. 두 조건 묶기")
# df = pd.read_csv(".venv/13_diecasting_shot.csv")

# df_both = df[(df["비스킷두께"] >= 13) & (df["사이클타임"] >= 25)]
# print(len(df_both))  # 83

# df_either = df[(df["비스킷두께"] >= 13) | (df["사이클타임"] >= 25)]
# print(len(df_either))  # 104


# line()
# print("실습 4. 부정 목록 범위 조건")

# df = pd.read_csv(".venv/13_diecasting_shot.csv")
# print(df["품질등급"] == "불량")  # True, False 반환
# print(df[df["품질등급"] == "불량"].head())  # 추려본 내용에 불량만 5개
# print(len(df[df["품질등급"] == "불량"]))  # 20

# 불량이 아닌 것들은?
# print(df[~(df["품질등급"] == "불량")].head())  # 불량 아닌 것들 5개
# print(len(df[~(df["품질등급"] == "불량")]))  # 180
# print(len(df[(df["품질등급"] == "양품") | (df["품질등급"] == "주의")]))  # 180

# print(len(df["품질등급"].isin(["양품", "주의"])))  # True, False로 반환되서 200
# print(len(df[df["품질등급"].isin(["양품", "주의"])]))  # 180

# between으로 실린더압력값 지정 범위에 든 행 추출 : 210 ~ 230
# print(df[df["실린더압력"].between(210, 230)].head())
# print(len(df[df["실린더압력"].between(210, 230)]))  # 89

# 그 외의 것들로

# print(len(df[~df["실린더압력"].between(210, 230)]))  # 111

# 조건에 ~ 를 해야함. / True, False로 반환되는 값 앞에 해야함.


# ==========================================================
# line()
# print("실습 5. 위험 순으로 정렬하기")

# df = pd.read_csv(".venv/13_diecasting_shot.csv")

# print(df.sort_values("비스킷두께", ascending=False).head(5))

# 직접 해당 값들만 뽑아서 list로 출력해보려면? 일단 series 추출하고 .tolist() 호출
# print(df.sort_values("비스킷두께", ascending=False)["비스킷두께"].head(5).tolist())

# 여러 열을 리스트로 묶어 우선순위 다중 정렬
# 형체력을 우선 오름차순으로 정렬하고
# 비스킷두께를 그 다음 순서로 내림차순 정렬하기
# print(df.sort_values(["형체력", "비스킷두께"], ascending=[True, False]).head(5))


# line()
# print("실습 6. 필터링과 정렬 연결")
# 조건으로 거른 결과에 정렬을 이어 붙이기

# 고장 여부 조건으로 고장 설비만 먼저 거르기
# df_filtered = df[df["품질등급"] == "불량"]
# print(df_filtered.head(5))

# 거른 결과에 sort_values를 점으로 이어 비스킷두께 내림차순 정렬
# df_filtered_after = (
#     df[df["품질등급"] == "불량"].sort_values("비스킷두께", ascending=False).head(5)
# )

# print(df_filtered_after)

# import pandas as pd

# df = pd.read_csv(".venv/13_diecasting_shot.csv")

# df.info()

# print(len(df[~(df["품질등급"] == "불량")]))
# print(sum(df["품질등급"].isin(["양품", "주의"])))  # 180
# print(sum(df["품질등급"].isin(["양품"])))  # 162
# print(sum(df["품질등급"].isin(["주의"])))  # 18
# print(sum(df["품질등급"].isin(["불량"])))  # 20
# isin.([])은 (안에 리스트로 넣어야함 [])


# print(df[df["비스킷두께"].between(10, 15)])

# pandas에서 원본에 변경을 주려면 꼭 .copy()를 해야함.
# 안그러면 SettingWithCopyWarning 경고 발생

# import pandas as pd

# df = pd.read_csv(".venv/13_diecasting_shot.csv")
# df.info()

# df_bad = df[df["품질등급"] == "불량"].copy()


# df_bad["품질등급"] = "점검"
# print(df_bad.head(5))

# line()
# print("실습 7. 이상 의심 설비 리포트")


# 워크플로우 5단계 맞춰가기

# 1. 불러오기
# df = pd.read_csv(".venv/13_diecasting_shot.csv", encoding="utf-8")


# 2. 확인하기
# df.info()

# 3. 필터링
# df_warning = df[(df["비스킷두께"] >= 16) | (df["사이클타임"] >= 100)]
# print(len(df_warning))  # 76

# 4. 정렬(내림차순)

# df_report = df_warning.sort_values("형체력", ascending=False)[
#     ["샷", "품질등급", "형체력", "사이클타임"]
# ]

# print(len(df_report))

# 5. 선택

# very_danger = df_report.head(1)
# sid = int((very_danger["샷"]).tolist()[0])
# force = very_danger["형체력"].tolist()[0]
# print(f"가장 시급한 샷 : {sid}, 형체력 {force}, 우선 점검")
# # 가장 시급한 샷 : 172, 형체력 384.0, 우선 점검

# 불량 = df[df["품질등급"] == "불량"].sort_values("형체력", ascending=False)
# print(불량[["샷", "형체력"]].head)


# =============================================
import pandas as pd

# df = pd.read_csv(".venv/14_hydraulic.csv", encoding="utf-8")


# df_old = df[df["냉각기상태"] == "고장"]
# print(len(df_old))  # 40
# 하지만 이 방식으로 모든 상태를 일일이 찾아서 통계내는 것은 비효율적

# 냉각기상태별 사이클 건수 세기
# print(df["냉각기상태"].value_counts())
# 냉각기상태 고장 40 저하 40 정상 40

# result 열의 정상 고장 건수 세기
# print(df["result"].value_counts())
# result 정상 67 고장 53

# normalize로 비율 구하기
# value_count.(normalize=True)

# print(df["result"].value_counts(normalize=True).round(3))
# .round(자릿수) 판다스 메써드

# print(df["result"].value_counts(normalize=True).round(3) * 100)

# sort=False
# dropna=False
# print(df["result"].value_counts(dropna=False))
# NaN 같은 결측값도 세줌

# print(df["온도"].value_counts())
# 위와 같이 범위 없이 개별 경우의 수를 따지면 ~개가 된다.
# 그래서 범위를 설정해 경우의 수를 줄여보기 -> 범주화

# band = pd.cut(df["온도"])
# print(band.value_counts()) # Type Error bin을 넣어야함
# pd.cut으로 수치형을 구간으로 묶어 세기
# 형식 : pd.cut(df['수치열'], bins=[경계...], labels=[이름..]) # 구간 라벨 series
# 엣지 : 경계(bins)는 이름표 labels보다 반드시 하나 많아야 함(경계 4개 -> 구간 3개)
# band = pd.cut(df["온도"], bins=[0, 40, 50, 200], labels=["낮음", "보통", "높음"])
# print(band.value_counts())
# 온도 낮음 41, 보통 40, 높음 39

# line()
# print("실습 1. value_counts로 빈도 세기")

# 설비 데이터를 불러와 앞부분과 구조 확인
# 설비 열(컬럼)에 value_counts를 붙여 값별 개수 세기
# print(df["밸브상태"].value_counts())
# 정상 61, 지연 20, 경미 20, 심각 19

# print(df["운전부하"].value_counts())
# 고부하 60, 저부하 60

# line()
# print("실습 2. 비율과 불균형 데이터")

# df_qc = pd.read_csv(".venv/14_hydraulic_qc.csv", encoding="utf-8")

# df_qc.info()
# print(df_qc.head(3))
# print(df_qc["검사결과"].value_counts())
# 합격 188 불합격 12

# print(df_qc["검사결과"].value_counts(normalize=True).round(3))
# 합격 0.94 불합격 0.06

# line()
# print("실습 3. 구간으로 묶어 세기")
# pd.cut으로 수치형 값을 구간으로 묶어 빈도 세기
# 수치형 센서 값을 구간으로 나눠 분포 확인

# 진동 열(컬럼)의 최솟값과 최댓값으로 값의 범위 확인

# df = pd.read_csv(".venv/14_hydraulic.csv", encoding="utf-8")
# print(df.head(3))  # 0.577 ~ 0.640 ??
# print(df["진동"].max())  # 0.779
# print(df["진동"].min())  # 0.53

# pd.cut()올 경계와 이름표를 정해 세 구간으로 묶기
# band = pd.cut(
#     df["진동"], bins=[0, 0.6, 0.7, 10], labels=["약함", "보통", "강함"]
# ).value_counts()
# print(band)  # 보통 55 약함 48 강함 17


# band = (
#     pd.cut(df["진동"], bins=[0, 0.6, 0.7, 10], labels=["약함", "보통", "강함"])
#     .value_counts(normalize=True)
#     .round(3)
# )
# print(band)  # 보통 0.458 약함 0.400 강함 0.142

# groupby()
# df = pd.read_csv(".venv/14_hydraulic.csv", encoding="utf-8")

# print(df.head(3))

# '냉각기상태' 컬럼의 내용별로 그룹핑을 하자 -> 분할
# 분할된 df마다 '온도' 컬럼이 있으니까, '온도'의 평균을 구해보자.
# print(df.groupby("냉각기상태")["온도"].mean().round(2))
# 고장 54.67 저하 45.46 정상 35.89

# 온도 말고 냉각기상태별 진동 평균도 알고 싶다면? Series

# print(df.groupby("냉각기상태")["진동"].mean().round(2))
# 고장 0.69 저하 0.61 정상 0.55

# 냉각기상태에 따른 온도와 진동의 평균값을 동시에 DataFrame
# print(df.groupby("냉각기상태")[["온도", "진동"]].mean().round(2))

# print(df.groupby(["냉각기상태", "운전부하"])["온도"].mean().round(2))

# 고장 고부하 55.51
#      저하부 54.05
# 저하 고부하 44.07
#      저부하 44.07
# 정상 고부하 35.89

# def line():
#     print("=" * 40)


# import pandas as pd

# df = pd.read_csv(".venv/students_groupby_practice.csv", encoding="utf-8")

# line()
# print("[문제 1] 이 학교의 전체 학생 수를 구하세요.")

# print(len(df))  # 60


# line()
# print("[문제 2] 학년별 학생 수를 구하세요.")
# print(df.groupby("학년").size())
# print(df["학년"].value_counts())  # 1 20 2 20 3 20

# line()
# print("[문제 3] 학년 내 각 반별 학생 수를 구하세요.")
# print((df.groupby(["학년", "반"]).size()))
# print(df[["학년", "반"]].value_counts())

# line()
# print("[문제 4] 각 반(학년, 반 조합)의 국어 점수 평균을 소수점 둘째 자리까지 구하세요.")
# print(df.groupby(["학년", "반"])["국어"].mean().round(2))

# line()
# print("[문제 5] 각 학년의 영어 점수 평균을 소수점 둘째 자리까지 구하세요.")
# print(df.groupby("학년")["영어"].mean().round(2))

# line()
# print("[문제 6] 학교 전체의 수학 점수 평균을 소수점 둘째 자리까지 구하세요.")
# print(df["수학"].mean().round(2))

# line()

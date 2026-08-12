def line():
    print("=" * 50)

import pandas as pd

line()

print("실습 1. csv 불러오기 워밍업")
df = pd.read_csv('.venv/12_metro_small.csv')
print(df.shape) # (30, 7)
print(df.head(2)) 

line()
print("실습 2. 설비 센서 csv 불러오기")

# 12_metro_compressor.csv
# 200행 7열 인덱스 3번 행 오일온도가 NaN

df = pd.read_csv('.venv/12_metro_compressor.csv', encoding='utf-8')
print(df.head(10))
print(df.shape) # (200, 7)


line()
print("실습 3. 한글 구분자 깨짐 옵션 다루기")

# import pandas as pd

df = pd.read_csv('.venv/12_metro_compressor_semicolon.csv', encoding='utf-8')
print(df.head(4))
print(df.shape) # (200, 1)
df = pd.read_csv('.venv/12_metro_compressor_semicolon.csv', encoding='utf-8', sep=';')
print(df.head(4))
print(df.shape) # (200, 7)

line()
print("실습 4. 필요한 열만 골라 불러오기")

# import pandas as pd

df = pd.read_csv('.venv/12_metro_compressor.csv')
print(df.shape) # (200, 7)

df = pd.read_csv('.venv/12_metro_compressor.csv', 
                 usecols=['측정시각', '압축압력', '배출압력', '가동상태'])
print(df.shape) # (200, 4)
print(df.head(3))

line()
print("실습 5. 경로옵션 오류 고치기")
# import pandas as pd

# df = pd.read_csv('없는파일.csv') # FileNotFoundError
# print(df.shape)

line()
print("실습 6. read_csv 옵션 종합 연습")

import pandas as pd

df = pd.read_csv('.venv/12_metro_compressor_semicolon.csv', encoding='utf-8', sep=';', usecols=['측정시각', '오일온도', '모터전류'])
print(df.shape) # (200, 3)
print(df)
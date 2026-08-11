# import numpy as np

# 0부터 4까지 생성
# under_five = np.arange(5)
# print(under_five)  # [0 1 2 3 4]
# print(under_five * 2)

# 0부터 8까지 2 간격
# gap_two = np.arange(0, 10, 2) # [0 2 4 6 8]
# gap_two = np.arange(0, 9, 2) # [0 2 4 6 8]

# linspace
# 개수 중심 균등 분할
# 시작과 끝 구간을 지정한 개수만큼 정확히 나눕니다.
# div_five = np.linspace(0, 1, 5)
# print(div_five)  # [0.   0.25 0.5  0.75 1.  ]

# 0으로 채우기
# block_zeros = np.zeros(5)
# print(block_zeros)  # [0. 0. 0. 0. 0.]

# # 7로 채우기
# block_seven = np.full(5, 7)
# print(block_seven)  # [7 7 7 7 7]
# block_senves = np.full(5, 7.0)
# print(block_senves) # [7. 7. 7. 7. 7.]

# 0부터 30까지 13등분 나누어 배열 내용 채우기
# div_thirty = np.linspace(0, 30, 13)
# print(div_thirty)
# # [ 0.   2.5  5.   7.5 10.  12.5 15.  17.5 20.  22.5 25.27.5 30. ]

# 실습 2. 균등 간격 배열 만들기
# lists = np.linspace(0, 100, 5)
# print(lists) # [  0.  25.  50.  75. 100.]

# 실습 3. 측정 시간축 배열 만들기
# lists_arange = np.arange(0, 11, 2)
# print(lists_arange) # [ 0  2  4  6  8 10]

# 특정 시작 시각과 끝 시각을 정해서
# 특정 간격 시간들이 지난다면
# 언제 언제 체크포인트가 만들어지나를
# numpy의 배열로 알아보기
# checks = np.arange(0, 60, 5) # [ 0  5 10 15 20 25 30 35 40 45 50 55]
# print(checks)


# 배열의 차원(ndim)
# 괄호없는 속성
# a = np.array([1, 2, 3])
# b = np.array([[1, 2], [3, 4]])
# print(a.ndim) # 1
# print(b.ndim) # 2

# 기존 파이썬 리스트로 2차원을 표현
# dim_2_list = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [2,4,6,8,10],
#     [3,6,9,3,6],
# ]

# print(dim_2_list[0]) # [1, 2, 3, 4, 5]
# print(dim_2_list[1][1]) # 7

# numpy에서 배열

# dim_2_array = np.array(dim_2_list)
# print(dim_2_array)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
# [ 2  4  6  8 10]
# [ 3  6  9  3  6]]

# print(dim_2_array[0]) # [1 2 3 4 5]
# print(dim_2_array[1][1]) # 7

# 이 배열의 형태 알아보기 (몇 행, 몇 컬럼)
# print(dim_2_array.shape) # (4, 5)

# 배열의 크기 알아보기 (보통 행 x 컬럼)
# print(dim_2_array.size) # 20

# # dtype에 대해 알아보자
# a = np.array([1, 2, 3])
# b = np.array([1.5, 2, 3])
# print(a.dtype) # int64
# print(b.dtype) # float64
# 64는 저장 공간 크기 64비트

# 형 변환 (astype)
# astype으로 자료형 바꾸기 실수 -> 정수는 소수점 버림

# a = np.array([1.7, 2.3, 3.9])
# print(a.astype(int))  # [1 2 3]

# 실습 4. 배열 구조 확인하기
# import numpy as np

# 2차원 배열을 만들어주세요.
# values = np.array([[1, 2, 3], [3,6,9]])
# print(values.ndim) # 2
# print(np.shape(values)) # (2, 3)
# print(np.size(values)) # 6

# 실습 5. 자료형 확인과 변환하기
# numbers = np.array([1.2, 3, 3.6])
# print(numbers.dtype) # float64
# print(numbers.astype(int)) # [1 3 3]
# astype은 변수에 담지 않으면 반환되지 않아서 바로 출력하거나 변수에 담아서 해야함

# reshape로 형태 바꾸기
# 값은 그대로, 모양만 바꾸기 -> 값 개수는 같아야 함
# size로 확인되는 값 개수는 같아야 한다!!

# under_ten = np.arange(10)
# print(f'{under_ten}')
# print(f'ndim : {under_ten.ndim}') # 1
# print(f'shape : {under_ten.shape}') # (10,)
# print(f'size : {under_ten.size}') # 10

# reshape_ten = under_ten.reshape(2,5)
# 2행, 5열로 바꾸기
# print(reshape_ten)
# print(f'ndim : {reshape_ten.ndim}') # 2
# print(f'shape : {reshape_ten.shape}') # (2, 5)
# print(f'size : {reshape_ten.size}') # 10 -> size만 안바뀜

# 데이터가 많아 개수를 세기 어려울 때, 열만 정하고 행은 -1로 두면 Numpy가 맞춤.
# 단, -1은 행과 열 중 한 곳에만 쓸 수 있습니다.

# flatten으로 1차원 만들기
# flatten_ten = np.array(reshape_ten)
# print(flatten_ten.flatten()) # [0 1 2 3 4 5 6 7 8 9]

# 실습 6. 배열 모양 바꾸기

# 연속 정수 배열을 arange로 생성
# 값 개수에 맞는 행·열을 정해 reshape로 형태 변환
# 바뀐 배열 출력

# num_int = np.arange(8)
# print(num_int)
# converted_numbers = num_int.reshape(2, 4)
# print(converted_numbers)


# 실습 7. 센서 데이터 표로 정리하기
# 시점과 센서 수를 곱한 개수만큼 연속값을 arange로 생성
# 만약 시점이 오전 6시, 오후 6시라면 시점은 2개
# 센서는 5개 있다고 가정
# 시점 x 센서 = 10개
# data = np.arange(10)

# 행을 시점, 열을 센서 수로 정해 reshape로 표 형태 변환
# converted_data = data.reshape(2, 5)

# 정리된 표 배열 출력

# print(converted_data)
# [[0 1 2 3 4]
# [5 6 7 8 9]]

# 실습 8. 배열 생성부터 정리까지

# 센서 측정값을 np.array로 배열 생성
# 최종 결과가 3행 2열 표로 정리된 배열 출력
# 최종형태 shape(3, 2)
# 최종형태 size = 6
# data_list = np.array([4.5, 3.2, 1.7, 6.2, 1.1, 3.1])

# shape와 dtype으로 구조 확인

# print(f'shape : {data_list.shape}') # (6,)
# print(f'dtype : {data_list.dtype}') # float64

# reshape로 분석용 표 형태로 정리한 뒤 출력

# converted = data_list.reshape(3, 2)
# print(converted)
# [[4.5 3.2]
# [1.7 6.2]
# [1.1 3.1]]

# reshape으로 분석용 표 형태로 정리한 뒤 출력


# temp = np.array([[70, 72.1], [72, 72.3]])
# print(temp[0]) # 행 전체 [70. 72.1]
# print(temp[:, 0]) # 열 전체 [70. 72.]
# print(temp.dtype) # float64

# 0행 0열부터 시작
# print(temp[0, 1]) # 0행의 1열 72.1

# 2차원 슬라이싱 - 행/열 선택
# 행 전체, 열 전체, 일부 구간 잘라내기 - 콜론이 전부를 의미

# import numpy as np

# data = np.array([
#     [70, 2.2],
#     [80, 3.3]
# ])

# print(data)

# print(data[0]) # [70. 2.2]
# print(data[:, 0]) [70. 80.]


# 실습 1. 특정 센서·구간 추출하기

# import numpy as np

# 예시 : 회전수 배열
# rpm = np.array([1551, 1408, 1498, 1443, 1425, 1558, 2861, 1410])
# print(rpm[0], rpm[-1])
# print(rpm[:3])
# print(rpm[::2])


# 실습 2. 행·열 단위로 추출하기
# import numpy as np

# 예시: 회전수와 토크 배열
# data = np.array([[1151, 42.8], [1408, 46.3], [2861, 4.6], [1410, 65.7]])

# print(data[2])
# print(data[:, 0])
# print(data[:, 1])

# import numpy as np

# 배열의 산술 연산
# 두 배열을 같은 위치끼리 한 번에 계산
# x = np.array([1, 2, 3])
# y = np.array([10, 20, 30])
# print(x + y)  # [11 22 33]
# print(x * 2)  # [2 4 6]
# print(x * y)  # [10 40 90]

# 브로드캐스팅

# table = np.array([[72, 2.3], [95, 6.8]])
# base = np.array([70, 2.0])
# print(table - base)
# [[2. 0.3]
#  [25. 4.8]]

# 실습 3. 센서값 정규화하기

# min-max 정규화 공식
# 데이터를 0과 1 사이 범위로 변환
# 정규화된 x = (비교대상 - 최소값) / (최대값 - 최소값)
# x_norm = x - x_min / x_max - x_min


# rpm = np.array([1551, 1408, 1498, 1433, 1425, 1558, 2861, 1410])

# rpm_max = rpm.max()
# rpm_min = rpm.min()

# normalized = (rpm - rpm_min) / (rpm_max - rpm_min)

# print(normalized)
# [0.09841707 0.         0.06194081 0.01720578 0.01169993 0.10323469
# 1.         0.00137646]

# 소수점 이하값이 너무 길어진다면 numpy 배열에서 제공하는 round 기능 활용

# print(np.round(normalized, 2))
# [0.1  0.   0.06 0.02 0.01 0.1  1.   0.  ]

# import numpy as np

# 비교 연산과 불리언 배열
# v = np.array([70, 95, 71, 88, 73])
# print(v > 85)  # [False  True False  True False]

# Boolean indexing
# 불리언 배열로 조건에 맞는 값만 골라내기
# print(v[v > 85])  # [95 88]

# np.where
# 조건에 따라 값을 둘중 하나로 바꾸기
# - 조건/참/거짓 세 가지 인자
# 조건이 참이면 1(위험)
# 거짓이면 0(정상)

# print(np.where(v > 85, 1, 0))  # [0 1 0 1 0]

# 다중 조건 결합
# vals = np.array([70, 95, 71, 88, 73])
# print((vals > 70) & (vals < 90))
# print(vals[[False, False, True, True, True]])  # [71 88 73]
# 반환값이 배열이라 [False False True True True]를 따로 넣으면 오류나서
# ((vals > 70) & (vals < 90))처럼 반환값으로 써야함.
# [False, False, True, True, True] 는 따로 , 를 넣어줘서 출력된거라
# 위에 것은 잘 안쓰임
# print(vals[(vals > 70) & (vals < 90)])  # [71 88 73]

# 실습 4. 이상 센서값 필터링하기
import numpy as np

# rpms = np.array([3421, 1698, 2000, 3330, 1995, 2001])

# 비교 연산으로 회전수가 기준을 넘는 조건 생성 -> 2000 이상
# print(rpms[rpms > 2000])


# 다중 조건으로 회전수 과다 또는 토크 과소 위험 시점 필터링
# rpm[0] 데이터와 torque[0] 데이터는 같은 시기의 상황을 다룸
# torques = np.array([600, 200, 700, 300, 400, 501])
# print((rpms > 2000) | (torques < 500))

# 예상 결과
# [ True  True False  True  True  True]
# 기준 초과 회전수 값과, 위험 조건을 만족하는 위치가 출력

# 실습 5. 조건별 개수와 비율 세기


# 토크 배열 준비
# torque_list = np.array([10.2, 30.1, 20.1, 15.0, 34, 11, 10, 9, 39, 40, 50])
# high_torque = torque_list > 11
# 비교 조건으로 참·거짓 불리언 배열 생성
# print(high_torque)  # [False  True  True  True  True False False False  TrueTrue  True]
# print(torque_list[torque_list > 11])  # [30.1 20.1 15.  34.  39.  40.  50. ]
# 불리언 배열의 합으로 개수, 평균으로 비율 계산
# 불리언 배열의 합(sum)으로 개수, 평균(mean)으로 비율 계산
# print(high_torque.sum())  # 7 (True = 1, False =0 으로 합산)
# print(high_torque.mean())  # 0.63636363
# print(round(high_torque.mean(), 2))  # 0.64

# # 합계와 평균(mean), 중앙값(median)

# s = np.array([70, 72, 71, 95, 73])
# print(s.sum())  # 381
# print(s.mean())  # 76.2
# print(np.median(s))  # 72.0

# 분산(Variance) (각 값 - 평균)을 제곱해서 다 더한 후 평균 낸 값
# 표준편차(Standard Deviation) 분산에 제곱근(루트)을 씌워 원래 단위로 되돌린 값

# 분산
# stable = np.array([70, 71, 70, 72, 71])
# unstable = np.array([60, 85, 65, 95, 70])


# print(stable.var())  # 0.5599999999
# print(round(stable.var(), 2))  # 0.56

# print(unstable.var())  # 170.0
# print(round(unstable.var(), 2))  # 170.0


# axis 개념 (행열 방향)
# 통계를 어느 방향으로 낼지 정하기 - axis 생략 시 전체 평균
# mat = np.array([[70, 2.1], [72, 2.3]])
# print(mat.mean()) # 전체 값 평균 36.6
# print(mat.mean(axis=0))  # 열별(센서별) 평균 [71. 2.2]
# print(mat.mean(axis=1))  # 행별(시점별) 평균 [36.05 37.15]

# 실습 6. 센서별 기초 통계 구하기

# data6 = np.array([[1600, 42.8], [1400, 46.3], [1465, 49.2], [2600, 6.9]])
# print(data6.mean(axis=0))  # [1766.25   36.3 ]
# print(np.round(data6.std(axis=0), 2))  # [486.74  17.12]

# 실습 7. 파일 데이터로 기초 통계 구하기

# [실습 7 코드 라인 설명 주석]
# - np.loadtxt: CSV 파일 데이터를 직접 NumPy 배열로 로드하는 함수입니다.
#   * delimiter=',': 쉼표 구분자
#   * skiprows=1: 맨 윗줄 열 이름(헤더) 1줄 건너뜀
#   * usecols=4: 4번 인덱스 열(회전수) 데이터만 선택 로드
# - 로드된 실데이터의 평균(4212.6), 표준편차(1144.9), 최솟값(58.0), 최댓값(4987.0)을 한 줄로 정량 산출합니다.

# 파일로 저장된 공정 데이터를 불러와 기초 통계 계산
import numpy as np

# np.loadtxt로 회전수 열을 파일에서 불러오기
rpm7 = np.loadtxt(
    "10_mct_tool.csv", delimiter=",", skiprows=1, usecols=4, encoding="utf-8"
)

# 불러온 배열의 평균과 표준편차 계산
print(round(rpm7.mean(), 1))  # 4212.6
print(round(rpm7.std(), 1))  # 1144.9

# 최솟값과 최댓값으로 값의 범위 확인
print(rpm7.min() - rpm7.max())  # -4929.0
print(rpm7.max() - rpm7.min())  # 4929.0
print(f"최댓값은 {rpm7.max()} 최솟값은 {rpm7.min()}")

# 실습 8. 필터링과 통계 결합하기

# - [필터링 + 통계 결합]: 데이터 분석의 궁극적 핵심 패턴입니다.
# - 1단계: 'torque8 > 50' 조건으로 토크 50 초과인 고토크 위험 시점만 'high8' 변수로 불리언 추출 [65.7, 60.7]
# - 2단계: 선별된 위험 수치들에 대해서만 평균(63.2)과 위험 발생 횟수(high8.size = 2회)를 정량 계산해냅니다.

# 토크 배열 준비
torque8 = np.array([4.6, 40.2, 60.7, 41.9, 65.7, 42.8, 46.3, 49.4])

# 불리언 인덱싱으로 기준을 넘는 값만 추출
high8 = torque8[torque8 > 45]
print(high8)  # [60.7 65.7 46.3 49.4]

# 추출한 값들의 평균과 개수 계산
print(round(high8.mean(), 1))  # 55.5
print(high8.size)  # 4

# 실습 9. Numpy 기초 종합 분석

# - 캡스톤 종합 분석 워크플로우:
#   1) 불러오기: usecols=(4, 5) 지정하여 회전수, 토크 2개 열 2차원 로드
#   2) 구조확인: data9.shape (40행 2열), float64 타입 검수
#   3) 추출 & 필터링: 0번 열(rpm9) 분리 후 1000 RPM 미만으로 스핀들 회전수가 떨어진 공구 고장 이상 시점 선별
#   4) 통계요약: 이상 발생 횟수(1회) 및 이상 시점 평균 회전수(58.0 RPM) 종합 리포팅

data9 = np.loadtxt(
    "10_mct_tool.csv", delimiter=",", skiprows=1, usecols=(4, 5), encoding="utf-8"
)

print(data9)
print(data9.shape, data9.dtype)

# 회전수가 기준 아래로 떨어진 이상 시점을 필터링해 개수와 평균 계산
rpm9 = data9[:, 0]
print(rpm9)
anomaly = rpm9[rpm9 < 1000]
print(anomaly)  # [58.]
print(anomaly.size, round(anomaly.mean(), 1))  # 1 58.0

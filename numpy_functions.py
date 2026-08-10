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
# data = np.array([
#     [1151, 42.8],
#     [1408, 46.3],
#     [2861, 4.6],
#     [1410, 65.7]
# ])

# print(data[2])
# print(data[:, 0])
# print(data[:, 1])
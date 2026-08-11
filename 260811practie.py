def line():
    print("=" * 50)


import numpy as np

line()

# 실습 1. 특정 센서·구간 추출하기
rpm = np.array([1551, 1408, 1498, 1443, 1425, 1558, 2861, 1410])
print(rpm[0], rpm[-1])  # 1551 1410
print(rpm[:3])  # [1551 1408 1498]
print(rpm[::2])  # [1551 1498 1425 2861]


line()

# 실습 2. 행·열 단위로 추출하기

data = np.array([[1151, 42.8], [1408, 46.3], [2861, 4.6], [1410, 65.7]])

print(data[2])  # [2861. 4.6]
print(data[:, 0])  # [1151. 1408. 2861. 1410.]
print(data[:, 1])  # [42.8 46.3 4.6 65.7]


line()

# 실습 3. 센서값 정규화하기
rpm = np.array([1551, 1408, 1498, 1433, 1425, 1558, 2861, 1410])

rpm_max = rpm.max()
rpm_min = rpm.min()

normalized = (rpm - rpm_min) / (rpm_max - rpm_min)

print(normalized)
print(np.round(normalized, 2))  # [0.1  0.   0.06 0.02 0.01 0.1  1.   0.  ]

line()

# 실습 4. 이상 센서값 필터링하기

rpms = np.array([3421, 1698, 2000, 3330, 1995, 2001])

print(rpms[rpms > 2000])  # [3421 3330 2001]


torques = np.array([600, 200, 700, 300, 400, 501])
print((rpms > 2000) | (torques < 500))

# [ True  True False  True  True  True]


line()

# 실습 5. 조건별 개수와 비율 세기

torque_list = np.array([10.2, 30.1, 20.1, 15.0, 34, 11, 10, 9, 39, 40, 50])
high_torque = torque_list > 11
print(high_torque)  # [False  True  True  True  True False False False  TrueTrue  True]
print(torque_list[torque_list > 11])  # [30.1 20.1 15.  34.  39.  40.  50. ]
print(high_torque.sum())  # 7 
print(high_torque.mean())  # 0.63636363
print(round(high_torque.mean(), 2))  # 0.64

line()

# 실습 6. 센서별 기초 통계 구하기

data6 = np.array([[1600, 42.8], [1400, 46.3], [1465, 49.2], [2600, 6.9]])
print(data6.mean(axis=0))  # [1766.25   36.3 ]
print(np.round(data6.std(axis=0), 2))  # [486.74  17.12]


line()

# 실습 7. 파일 데이터로 기초 통계 구하기


rpm7 = np.loadtxt(
    "10_mct_tool.csv", delimiter=",", skiprows=1, usecols=4, encoding="utf-8"
)

print(round(rpm7.mean(), 1))  # 4212.6
print(round(rpm7.std(), 1))  # 1144.9

print(rpm7.min() - rpm7.max())  # -4929.0
print(rpm7.max() - rpm7.min())  # 4929.0
print(f"최댓값은 {rpm7.max()} 최솟값은 {rpm7.min()}")


line()

# 실습 8. 필터링과 통계 결합하기

torque8 = np.array([4.6, 40.2, 60.7, 41.9, 65.7, 42.8, 46.3, 49.4])

high8 = torque8[torque8 > 45]
print(high8)  # [60.7 65.7 46.3 49.4]

print(round(high8.mean(), 1))  # 55.5
print(high8.size)  # 4


line()

# 실습 9. Numpy 기초 종합 분석

import numpy as np

np.set_printoptions(suppress=True)


data9 = np.loadtxt(
    "10_mct_tool.csv", delimiter=",", skiprows=1, usecols=(4, 5), encoding="utf-8"
)

print(data9)
print(data9.shape, data9.dtype)

rpm9 = data9[:, 0]
print(rpm9)
anomaly = rpm9[rpm9 < 1000]
print(anomaly)  # [58.]
print(anomaly.size, round(anomaly.mean(), 1))  # 1 58.0

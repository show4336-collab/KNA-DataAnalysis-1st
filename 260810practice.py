def line():
    print("=" * 50)

import numpy as np

line()

# 실습 1. 센서값 배열 만들기

temp_list = np.array([34.1, 35, 36])
print((temp_list * 1.8) + 32)

line()

# 실습 2. 균등 간격 배열 만들기

linspace_value = np.linspace(0, 100, 5)
print(linspace_value)

line()
# 실습 3. 측정 시간축 배열 만들기
arange_value = np.arange(0, 100, 10)
print(arange_value)

line()
# 실습 4. 배열 구조 확인하기
sensors_value = np.array([[10,20,30,], [40, 50, 60]])
print(sensors_value.ndim)
print(sensors_value.shape)
print(sensors_value.size)

line()

# 실습 5. 자료형 확인과 변환하기

float_list = np.array([10.2, 30.4, 50.5])
print(float_list.dtype)
print(float_list.astype(int))

line()
# 실습 6. 배열 모양 바꾸기
numbers = np.arange(8)
reshape_numbers = numbers.reshape(2, 4)
print(reshape_numbers)


line()
# 실습 7. 센서 데이터 표로 정리하기
sensors_value = np.arange(6)
reshape_value = sensors_value.reshape(3, 2)
print(reshape_value)



line()
# 실습 8. 배열 생성부터 정리까지
sensor_values = np.array([15, 30, 45, 60, 75, 90])
print(sensor_values.shape)
print(sensor_values.dtype)
sensor_values_reshape = sensor_values.reshape(3, 2)
print(sensor_values_reshape)

line()
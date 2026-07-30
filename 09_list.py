# list는 python의 자료형 중 하나
# 여러 개의 값을 [대괄호]에 감싸서 순서대로 저장
# 나열된 값들은 자동으로 각자의 인덱스 번호를 순서대로 가지게 됨

# temps = [35, 26, 37, 38]  # int 리스트
# float_temps = [36.4, 36.5, 36.6, 36, 7]  # float 리스트
# machines = ["펌프", "압축기", "모터"]  # string 리스트

# 리스트는 자료형이 달라도 한 리스트에 담을 수 있음
# mixed = ["펌프", 78, True]

# 리스트에 자동으로 순서 인덱스가 붙는다면?
# print(temps[2])  # 37 -> 인덱스로 해당 순서에 위치한 요소 뽑아내기 가능

# 리스트 안에 몇 개의 값이 담겼는지 모르지만 마지막 요소를 뽑고 싶다면?
# print(temps[-1])  # 38 (가장 마지막 요소 출력)

# print(len(temps))  # 4 (담긴 값의 개수)
# results = []  # 빈 리스트
# print(len(results))  # 0
# 리스트에 담긴 값의 갯수 세기
# len() 내장함수 사용

# 리스트의 담긴 값의 갯수 변수에 저장
# temps_length = len(temps) # 변수에 4라는 값이 할당
# print(temps_length) # 4

# temps = [34, 35, 36, 37, 38]
# print(temps[-4:-1]) # [35, 36, 37]
# print(len(temps))
# vibration = []
# print(len(vibration))

# 리스트의 인덱스
# print(temps[0], temps[-1]) # 가장 첫 번째 요소, 가장 마지막 요소
# -1을 사용하는 이유는 최신 값은 대체로 뒤에 추가가 됨
# 가장 최신 값은 결국 마지막 인덱스의 요소
# len 함수를 사용해서 리스트 길이-1로 계산이 가능하지만
# 이 작업이 번거로워 -1을 가장 많이 사용

# 없는 인덱스 호출
# temps 리스트는 길이가 5
# print(temps[5]) # IndexError : list index out of range
# 인덱스 범위를 벗어나지 않도록 유의

# temps = [10, 11, 12, 13, 14, 15]
# print(temps[0])
# print(temps[2])
# print(temps[-1])

# outputs = [10, 20, 30, 40, 50, 60]
# line1 = outputs[0]
# line2 = outputs[-1]
# print(line1 + line2)
# print((line1 + line2) / 2)

# 리스트의 자료형
# print(f"temps : {temps}")
# print(f"type(temps) : {type(temps)}")  # <class 'list'>

# print(f"temps[0] : {temps[0]}")
# print(f"type(temps[0]) : {type(temps[0])}")  # <class 'int'>

# float_temps = [36.4, 36.5, 36.6, 36, 7]  # float 리스트
# machines = ["펌프", "압축기", "모터"]  # string 리스트
# 다른 자료형의 값이 들어있는 리스트의 요소 타입
# float 값이 들어있는 float_temps 리스트의 0번째 요소

# print(type(float_temps[0]))  # <class 'float'>
# print(type(machines[0]))  # <class 'str'>

# 리스트 슬라이싱
# 리스트명[시작:끝:간격]
# 시작, 끝, 간격 인덱스는 모두 생략 가능 (문자열과 동일)
# temps = [1, 2, 3, 4, 5, 6]
# print(temps[2])  # 3
# print(temps[2:3])  # [3]
# print(temps[:2], temps[3:])  # [1, 2], [4, 5]
# print(temps[::1])  # [1, 2, 3, 4, 5, 6]
# print(temps[::3])  # [1, 4]
# print(temps[100:999]) # [] > 슬라이싱은 없는 인덱스를 넣으면 빈 값 출력

# 인덱싱 vs 슬라이싱
# 인덱싱 temps[0]은 값 인트 1
# temps[999]와 같이 없는 인덱스 사용 시 : 에러

# 슬라이싱 temps[0:2]은 리스트 [1, 2]
# 슬라이싱은 영역을 잘라내는 역할이기 때문에 리스트를 반환하는 것
# 슬라이싱은 '있는 만큼만' 자름 : 에러 발생하지 않음 ex) temps[100:999]

# 실습 4. 슬라이싱으로 구간 자르기
# temps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(temps[:3])
# print(temps[:3])
# print(len(temps[-3:]))
# print(len(temps[-3:]))

# 실습 5. 데이터를 두 구간으로 나누기
# total = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# first = total[:6]
# print(first)
# second = total[6:]
# print(second)
# print(len(first), len(second))

# 인덱스로 특정 값 바꾸기
# temps = [35, 36, 37, 38]

# print("원본 :", temps)
# temps[2] = 999
# print("2번 인덱스 값 변경 결과 :", temps)

# print(35 in temps)  # True
# print("35" in temps)  # False
# print(35 not in temps)  # False
# print("35" not in temps)  # True

# machines = ["펌프", "압축기", "모터"]
# i = machines.index("압축기")
# print(i)  # 1
# .index() 메서드는 리스트에서 가장 처음 등장하는 인덱스만 반환
# machines2 = ["펌프", "압축기", "모터", "압축기"]


# 실습 6. 값 찾아 바꾸기
# temps = [10, 240, 30, 40, 50]
# print(240 in temps) # True
# temps[temps.index(240)] = 24
# print(temps) # [10, 24, 30, 40, 50]
# print(240 in temps) # False

# append 끝에 값 추가
# insert 원하는 위치에 삽입 (원래 있던 값은 뒤로 밀림)

# 리스트 값 추가
# .append(추가할 값)
# 리스트의 가장 마지막에 값을 추가
# 리스트 원본이 수정 (재할당 필요 x)
# nums = [1, 2, 3, 4, 5]
# nums.append(6)
# 만약 원본 리스트와 특정 값을 추가한 리스트 둘 다 필요하다면
# 원본 리스트를 복사해서 리스트 수정 진행

# nums = [1, 2, 3, 4, 5] -> 기존 리스트는 원본으로 둠
# new_nums = nums # 스스로의 메모리를 할당받지 않고, 메모리 주소만 복사
# print(new_nums)  # [1, 2, 3, 4, 5, 6]

# new_nums.append(111)
# print("원본 nums 리스트 :", nums)
# 기대 결과 : [1, 2, 3, 4, 5, 6]
# 실제 결과 : [1, 2, 3, 4, 5, 6, 111]
# 복사한 메모리 주소에 append를 했기 때문에 원본까지!!!
# 영향을 받는다!!!!!!!!!!!!!!!!!

# 이를 해결하기 위해서 .copy()라는 메서드를 사용
# new_nums2는 새로운 메모리에 nums 배열을 새로 저장
# print("복사본 new_nums에 111 append 결과 :", new_nums)

# new_nums2 = nums.copy()
# new_nums2.append(222) # nums 배열에 영향을 미치지 않고 사용
# print("원본 nums 리스트 :", nums)
# print("복사본 new_nums2에 222 append 결과 :", new_nums2)

# .insert(위치, 값)
# 내가 리스트에서 원하는 위치에 값을 삽입
# 원본 배열에 바로 삽입
# 기존 배열에서 삭제는 되지 않고,
# 해당하는 인덱스 값이 삽입 (뒤에 요소 )
# nums = [1, 2, 3, 4, 5]
# nums.insert(3, 333)  #
# print(nums) # [1, 2, 3, 333, 4, 5]

# morning = [20, 21, 22]
# afternoon = [23, 24, 25]
# morning.extend(afternoon) # morning에 afternoon을 이어붙여라

# abc = [1, 2, 3]
# abc.extend([4, 5])
# print(abc) # [1, 2, 3, 3, 4]

# extend 리스트 이어붙이기
# 다른 리스트의 값들을 "풀어서" 이어붙임
# data = [1, 2, 3]
# new_data = [7, 8, 9]
# data.extend(new_data)
# print(data) # [1, 2, 3, 7, 8, 9]

# print(data.extend(new_data))
# 기대 결과 : [1, 2, 3, 7, 8, 9]
# 실제 결과 : None
# extend() 메서드는 data라는 리스트를 "수정". 이를 반환하지는 않음
# 반환값이 없어서 print를 할 값이 없는 것
# print(data) # [1, 2, 3, 7, 8, 9]

# 리스트를 수정하는 메서드는 모두 반환값이 없는가?
# print(data.append(123))
# print(data.insert(0, 123))
# print(data.extend(new_data))
# 일단 현재 배운 메서드는 반환값이 없음

# 정리
# 오늘 "꼭" 알아야 하는 리스트 수정 메서드와 개념
# .append(추가할 값) : 리스트의 가장 마지막에 값을 추가
# .insert(위치, 값) : 첫 번째 인자인 위치 인덱스에 값을 삽입
# .extend(합칠 리스트) : 두 리스트를 하나의 리스트로 합체
# 위 세가지 메서드들은 원본 리스트 자체를 수정

# abc = []
# abc.append(30)
# print(abc)
# abc.insert(0, 28)
# print(abc)
# abc.extend([31, 32])
# print(abc)

# 리스트에서 요소 삭제
# .remove(값) : 위치는 모르고 삭제할 "값"만 알 때 사용하는 요소 삭제 메서드
# list1 = ["가", "나", "다", "라", "마", "바"]
# list1.remove("마")
# print(list1)  # ['가', '나', '다', '라', '바']

# print("===")
# list1.remove("카") # ValueError : list.remove(x) : not in list

# .pop(인덱스) : 인덱스로 특정 요소를 삭제할 때 사용
# 삭제할 인덱스의 값을 반환
# list1.pop(0)
# print(list1)  # ['나', '다', '라', '바']
# pop 메서드는 삭제한 인덱스 값을 반환해준다는 것을 설명하는 용도
# print(list1.pop(2))  # 삭제도 하고, 삭제한 인덱스 2번의 값인 라 출력
# print(list1)

# pop으로 없는 인덱스로 값 삭제 시도
# list1.pop(999) # 불가함. Index Error : pop index ouf of range
# print(list1)

# del : 인덱스로 리스트의 요소 삭제 (슬라이싱으로 영역 삭제 가능)
# del list1[0]
# print(list1)

# del 건너뛰기
# list2 = ["빨강", "노랑", "초록", "파랑", "남색", "보라"]
# del list2[::2] # "빨강", "초록", "남색"
# print(list2) # ['노랑', '파랑', '보라']
# 없는 인덱스로 삭제
# del list2[999] # IndexError : list assignment index out of range

# del list2[100:999] # 슬라이싱 할 값이 없기 때문에 그대로 유지 > Error 안남
# print(list2)

# list1 = [25, 26, 24, 28, 26, 999]
# list1.remove(999)
# print(list1)
# print(list1.pop(1))
# del list1[0]
# print(list1)

# 리스트 정렬하기
# 리스트.sort()
# 데이터를 정렬하는 친구
# 기본적으로 오름차순(작은 숫자부터 큰 숫자까지)
# 내림차순으로 정렬하고 싶은 경우에는 .sort(reverse=True)

# n = [37, 2, 8, 109, 1004, -2, 22]
# print("n 리스트 원본 :", n)  # [37, 2, 8, 109, 1004, -2, 22]

# 오름차순 정렬
# n.sort()  # 원본 리스트 수정
# print("n 리스트 오름차순 정렬 결과 :", n)  # [-2, 2, 8, 22, 37, 109, 1004]

# 내림차순 정렬
# n.sort(reverse=True)
# print("n 리스트 내림차순 정렬 결과 :", n)

# 리스트 순서 뒤집기
# .reverse()
# 값의 크기대로 정렬은 하진 않음
# 뒤로 계속 쌓인 결과(최신)을 앞에서부터 보고 싶을 때

# n = [37, 1, 2, 3, 5]
# print("n 리스트 원본 :", n)

# n.reverse()
# print("n 리스트 순서 뒤집기 결과 :", n)

# 리스트 안 값의 갯수 구하기
# .count(찾을 값)

# f = ["텀블러", "일회용컵", "일회용컵", "텀블러", "텀블러", "일회용컵"]
# print(f.count("일회용컵"))  # 3
# print(f)  # 원본 배열 그대로

# 특정 값의 위치 찾기
# .index(위치를 찾을 값)
# 리스트에서 가장 첫 위치만 찾아줌
# print(f.index("일회용컵"))  # 1
# print(f)  # 원본 배열에 변화 없음

# 실습 9. 정렬하고 탐색하기
# temps = [28, 22, 24, 24, 26, 27, 30]
# temps.sort()
# print(temps)
# temps.reverse()
# print(temps)
# print(temps.count(24))
# print(temps.index(24))

# print(not True) # False
# print(not 5 == 5) # False

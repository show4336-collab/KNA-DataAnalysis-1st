# while은 특정 조건(횟수 x)이 False가 될 때까지
# 반복해야 하는 경우 사용

# 무한반복 중지 : ctrl + c
# 무한루프 유의
# count = 1
# while count <= 3:
# print(count)
# while문은 조건이 거짓이 되는 플래그를 꼭 세워야 함

# while문 사용 체크리스트
# 1. 반복 전 변수(시작값) 존재 여부
# 2. 반복을 하다가 언젠가 False가 될 수 있는 종료 조건 포함 여부
# 3. 변수가 거짓 방향으로 값이 변경되는지

# count = 1  # 1번
# while count >= 1:  # 2번
# count = 0 # 반복문 안에 count 변수를 계속 0으로 재할당해서 무한 0
# print(count)
# count += 1  # 3번

# answer = 7
# guess = 0
# while guess != answer:  # 종료 조건 : 멈출 상태의 반대를 조건식으로
# guess = int(input("정답을 맞춰보세요."))  # 종료를 향해 값 바꾸기
# print("정답입니다!")

# break로 반복 중단하기
# for i in range(1, 11):
# if i == 5:
# break
# print(i)

# continue로 회차 건너뛰기
# for i in range(1, 7):
# if i % 2 == 0:
# continue
# print(i) # 출력 1, 3, 5

# 사용자 입력으로 반복 제어
# while True:
# x = input("입력 (q:종료) : ")
# if x == "q":
# break
# print("입력 :", x)

# break
# 반복을 그만 돌고 싶을 때
# 예시 1) [1, 1, 3, 3, 2, 1, 1, 1]
# 위 리스트를 돌면서 10 이상이 되면 중단하고 싶을 때
# 예시 2) 사용자 입력값을 누적하다가 누적값이 총 15를 넘으면
# 종료하고 싶을 때
# break 사용 시 즉시 for문을 나감

# input_sum = 0
# while True:  # 조건만 보면 무한반복하는 코드
#     user_input = int(input("값을 입력하세요. 값의 누적이 15를 넘으면 종료합니다 : "))
#     input_sum += user_input  # 누적값 업데이트
#     if input_sum > 15:  # 종료 트리거
#         print("누적 합계 :", input_sum, "입력을 종료합니다.")
#         break  # 누적 합계가 15를 넘으면 반복 종료
# print("break를 통해 while문을 나가면 이후 코드가 실행됨")

# 사용자 입력값을 확인만 하고 저장할 필요가 없는 경우
# while True:
#     # 변수 x는 반복을 돌 때마다 재할당되기 때문에 휘발되지만
#     x = input("입력 (종료는 q를 입력하세요) : ")
#     # 현재 입력값이 뭔지는 확인할 수 있음
#     if x == "q":
#         break
#     print(f"입력받은 값 : {x}")

#  =======================
# n = int(input("횟수 : "))
# for i in range(n):
#     v = int(input("측정값 : "))
#     if v > 80:
#         print("이상 발생")
#         print("가동 횟수 :", n)
#         break
#     else:
#         print("정상 상태")

# 실습 up down 게임
# 1~50 중 하나의 숫자를 정답으로 저장
# 사용자의 입력값 기준으로 정답이 up인지 down인지 출력
# 정답이 나오면 정답이고, 게임이 종료되었다고 출력

# answer = 25
# while True:
#     guess = int(input("정답은 ? : "))
#     if guess > answer:
#         print("down")
#     elif guess < answer:
#         print("up")
#     elif guess == answer:
#         print("정답입니다.")
#         print("게임이 종료되었습니다.")
#         break

# 최대값 찾기
# first = int(input("1번째 입력값 : "))
# max_value = first
# for i in range(4):
#     v = int(input(f"{i + 2}번째 입력값 : "))
#     # 위에서 1번째 입력을 받고, i는 0부터 시작하기 때문에 2를 더해서 출력
#     # max_value에는 현 시점 최대값
#     # v에는 방금 사용자가 입력한 값
#     # max_value와 v의 값을 비교해 더 큰 값을 max_value에 재할당
#     if v > max_value:
#         max_value = v
# print("최대값 : ", max_value)

# 플래그 변수 활용
found = False
# for v in [70, 92, 65]:
#     if v > 80:
#         found = True
# if found:
#     print("이상값 있음")
# else:
#     print("모두 정상")

# # 조건 반복 결합 흐름 읽기
# sum = 0
# for i in [4, 7, 6]:
#     if i > 5:
#         sum += i
# print(f"합계 : {sum}")

# found = False
# n = int(input("반복 횟수 : "))
# for i in range(n):
#     v = int(input("측정값 : "))
#     if v > 80:
#         found = True
#         break
# if found:
#     print("발견")
# else:
#     print("없음")

# temps = [25, 32, 28, 35, 19]
# temps.sort()
# for t in temps:
#     if t > 30:
#         print(f"{t} : 고온주의")
#     else:
#         print(f"{t} : 저온")

# temps = [32, 35, 31, 20, 21, 28]
# for t in temps:
#     if t >= 30:
#         print(f"고온 : {t}")

# time = [1, 2, 3, 4, 8, 6, 10, 9]
# for t in time:
#     if t >= 5 and t <= 10:
#         print(t)

# temps = [25, 32, 28, 35, 27]
# biggest = temps[0]
# for t in temps:
#     if t > biggest:
#         biggest = t
# print(biggest) # 35

# temps = [20, 21, 22, 36, 32, 31]
# total = 0
# counts = 0
# for t in temps:
#     if t > 30:
#         total += t
#         counts += 1
# print(f"고온 평균 : {total / counts:.1f}")

# temps = [25, 26, 24, 28]
# doubled = []
# for t in temps:
#     doubled.append(t * 2)
# print(doubled)  # [50, 52, 48, 56]

# temps = [25, 32, 28, 35, 27]
# high = []
# for t in temps:
#     if t > 30:
#         high.append(t)
# print(high)

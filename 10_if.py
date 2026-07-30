# 조건문 - IF=f
# 항상 실행되지 않고 조건에 따라서
# 실행되는 코드가 달랐으면 할 때 사용
# 코드의 분기라고도 표현
# 조건문의 조건은 True와 False로 결과가 나와야 함

# if 조건식:
#   실행할 코드 (한 칸 들여쓰기(탭기준))

# if문의 :은 다음 올 코드가 if문 조건식 결과가 True일 때만 실행하라는 의미
# 들여쓰기 한 코드는 if문의 조건식 결과가 True일 때 실행
# 즉, 여기서부터 이 조건에 속한다 라는 신호
# 조건에 속하는 코드는 모두 들여쓰기가 적용되어야 함

# temp = 85
# if temp > 80: # 만약 temp라는 변수가 80보다 크면?
# print("temp 변수의 값이 80보다 크다!!!")
# print("호호") # 이건 항상 실행되는 코드

# temp = 85
# if temp > 80:
#     print("경고")
# else:
#     print("정상")


# age = int(input("나이를 입력하세요 : "))
# if age >= 19:
# print("성인입니다")
# else:
# print("미성년자입니다")

# 실습 1. 조건 하나로 나이 판정하기 정답
# age = int(input("나이를 입력하세요 :"))
# if age >= 20:
#     print("성인입니다")
# else:
#     print("미성년자 입니다.")

# 실습 2. 숫자맞추기 게임
# 정답을 맞추면 맞았습니다. 틀리면 틀렸습니다. 출력
# 정답을 50으로 지정
# 사용자에게 입력값 받기

# temp = int(input("지금 온도는? :"))
# if temp == 50:
#     print("정답!")
# else:
#     print("땡!")
# print("게임이 종료되었습니다.")

# input으로 받은 자료형은 문자열이라서 int()

# answer = 50
# user_answer = int(input("정답을 입력하세요:"))
# if answer == user_answer:
#     print("정답!")
# else:
#     print("땡!")
# print("게임 끝!")

# color = input("신호등이 무슨 색 인가요?")
# if color == "초록색":
# print("건너")
# if color == "빨간색":
# print("멈춰")
# else:
# print("다시 입력해")
# 위 처럼 하면 초록색 입력했을때 건너랑 다시 입력해가 같이 나옴

# 아래처럼 or 사용 + if문 중첩
# color = input("신호등이 무슨 색 인가요?")
# if color == "초록색" or color == "빨간색":
# if color == "초록색":
# print("건너")
# if color == "빨간색": # 이때는 else문과 동일하게 동작해서
# print("멈춰") # else를 쓰는게 더 효율적임.
# else:
# print("멈춰")
# 아래 print : 사용자 입력값이 "초록색"이거나 "빨간색"일때 무조건 출력
# print("이건 언제 실행될까?")
# else:
# print("다시 입력해")

# and 연산자 + if 중첩

# 사람 체온 판단
# 정상 체온 범위 : 35.2 ~ 36.9

# user_a = float(input("체온을 입력하세요 :"))
# if user_a >= 36.2 and user_a <= 36.9:
# print("당신은 정상체온입니다.")
# else:
# if user_a > 36.9:
# print("당신은 열이 나고 있습니다.")
# else:
# print("당신은 저체온입니다.")
# print("체온 판단 완료")

# 위의 체온 판단 if문 안에서 열이 나는지 저체온인지 판단하도록 수정
# user_a = float(input("체온을 입력하세요 :"))
# if user_a <= 36.2 or user_a >= 36.9:
# if user_a > 36.9:
# print("당신은 열이 나고 있습니다.")
# if user_a > 37.8:
# print("미열")
# else:
# print("고열")
# else:
# print("당신은 저체온입니다.")
# else:
# print("당신은 정상체온입니다.")
# print("체온 판단 완료")

# elif
# else와 if만으로 분기하기에는 불편하고
# if 중첩이 너무 많아져서 생김
# user_a = float(input("체온을 입력하세요 :"))
# if user_a <= 36.2:
#     print("당신은 저체온입니다.")
# elif user_a >= 36.9 and user_a < 37.8:
#     print("당신은 미열입니다. 주의하세요.")
# elif user_a >= 37.8:
#     print("당신은 고온입니다. 병원에 방문하세요")
# else:
#     print("당신은 정상체온입니다.")
# print("체온 확인 완료")

# if-elif-else 전체구조
# score = 82
# if score >= 90:
#     print("우수")
# elif score >= 70:
#     print("보통")
# else:
#     print("미흡")

# elif의 순서

# score = 50
# if score >= 90:
#     print("우수")
# elif score >= 70:
#     print("보통")
# elif score >= 50:
#     print("미흡")
# else:
#     print("비상")

# not 연산자
if not (3 == 5):
    print("출력됩니다.")
# 3과 5는 같지 않으니 False가 되지만
# 앞에 not이 있어서 False를 True로 뒤집어 if가 인식

# if문은 줄바꿈을 하지 않아도 : 을 기준으로 동작 자체는 가능
# 하지만 줄바꿈해서 가독성을 높이길 권장
# 탭은 아직 위의 코드가 끝나지 않았고 한 줄이라는 것을 명시

# 조건문 코드 읽기 절차
# 1. 변수 값 확인 : 조건에 쓰인 변수의 현재 값 찾기
# 2. 조건 대입 : 위에서부터 넣어 처음 참인 조건 찾기
# 3. 참인 블록의 들여 쓴 코드 따라가기

# temp = int(input("측정 온도? :"))
# if temp > 80:
#     print("위험")
# elif temp > 60:
#     print("주의")
# else:
#     print("정상")

# 실습 3. 두 조건을 모두 만족하는지 검증
# 내 답안
# ID = input("아이디 ? :")
# Password = int(input("비밀번호 ? :"))
# if ID == "admin" and Password == 1234:
#     print("성공")
# else:
#     print("실패")
# 모범 답안
# correct_id = "admin"
# correct_pw = "1234"
# user_id = input("아이디: ")
# user_pw = input("비밀번호: ")
# if user_id == correct_id and user_pw == correct_pw:
#     print("로그인 성공")
# else:
#     print("로그인 실패")

# 모범 답안처럼 변수를 늘려서 int 안쓰고 문자열로 해버리는게 낫겠다.

# 실습 5. 세 값으로 설비 종합 상태 판정하기
# 중첩 if와 논리연산(and·or)으로 세 값을 단계적으로 판정하기

# 내 답안
# temp = int(input("온도 ?:"))
# vib = float(input("진동 ?:"))
# current = float(input("전류 ?:"))
# if temp > 80 or vib > 4.0:
#     print("위험 : 즉시 정지")
# elif current > 60 and temp > 70:
#     print("주의 : 부하 점검")
# elif vib > 2.5:
#     print("주의 : 진동 관찰")
# else:
#     print("정상")

# 모범 답안
# temp = int(input("온도: "))
# vib = float(input("진동: "))
# current = int(input("전류: "))
# if temp > 80 or vib > 4.0:
# print("위험: 즉시 정지")
# else:
# # 1차: 하나라도 한계 초과면 즉시 위험
# # 위험이 아닌 값만 2차 세부 판정
# if current > 60 and temp > 70:
# print("주의: 부하 점검")
# elif vib > 2.5:
# print("주의: 진동 관찰")
# else:
# print("정상")

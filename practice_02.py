# =====================================================================
# 종합 실습 2. 실시간 측정값 입력 시스템
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

# 이 실습은 사용자한테 입력받는 거라 미리 주는 데이터 없음
# while로 계속 입력받다가 q 입력하면 종료 > 통계 출력

LIMIT = 100  # 임계값 (100 초과 시 즉시 경고)

# TODO 1. while로 "측정값: " 계속 입력받기, q면 break
#         (입력값은 숫자 아니면 q 라고 가정)
#         값은 리스트에 .append() 로 모으기
print(f"================== 실시간 측정값 입력 시스템 ==================")
print(f"측정값을 입력하세요. 종료하려면 q 입력.")
list_input = []
input_over = []
input_sum = 0
input_count = 0

while True:
    user_input = input("측정값 : ")
    if user_input != "":
        if user_input != "q":
            user_input = float(user_input)
            list_input.append(user_input)
            input_sum += user_input
            input_count += 1
            if user_input > LIMIT:
                input_over.append(user_input)
                print(f"🚨 임계값{LIMIT} 초과! 현재까지 초과 {len(input_over)}회")
        elif user_input == "q":
            if len(list_input) == 0:
                print("입력된 측정값이 없습니다.")
            break
    else:
        print(f'""')
avg = input_sum / input_count
avg_index = 0
input_min = float(sorted(list_input)[0])
input_max = float(sorted(list_input)[-1])

for i in list_input:
    if i > avg:
        avg_index += 1


print(f"------------------------------------------------------------")
print(f"총 입력 개수 : {len(list_input)}")
print(f"최댓값 : {input_max} / 최솟값 : {input_min}")
print(f"평균값 : {round((input_sum / input_count), 2)}")
print(f"임계값 초과 개수 : {len(input_over)}")
print(f"평균 초과 개수 : {avg_index}")
print(f"상위 3개 값 : {sorted((list_input), reverse=True)[:3]}")


# TODO 2. 입력값이 LIMIT 초과하면 즉시 경고 + 지금까지 초과 횟수 출력


# TODO 3. q로 끝난 뒤:
#   - 입력값이 하나도 없으면 "입력된 측정값이 없습니다." 출력하고 끝
#   - 값이 있으면 아래 출력
#       · 총 입력 개수 (len)
#       · 최댓값 / 최솟값 (반복문으로 직접 찾기)
#       · 평균값 (round, 소수 둘째 자리)
#       · 임계값 초과 개수
#       · 평균보다 큰 값의 개수  > 평균 먼저 구한 뒤 리스트 다시 돌기
#       · 상위 3개 값 (.sort(reverse=True) 후 슬라이싱 [:3])


# 도전) q 대신 그냥 Enter(빈 입력 "") 치면 무시하고 다시 받기

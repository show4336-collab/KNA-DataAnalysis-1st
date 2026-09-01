import pandas as pd

df = pd.read_csv(".venv/02-01_측정의_3요소_설비태그목록.csv")

# CASE A : MTR로 시작하는 태그
MTR_list = df[df["tag"].str.startswith("MTR")]

print(MTR_list[["tag", "description", "unit", "install_location", "sampling_sec"]])


# CASE B : HYD, FUR로 시작하는 태그
HYDFUR_list = df[df["tag"].str.startswith(("HYD", "FUR"))]

print(HYDFUR_list[["tag", "description", "unit", "install_location", "sampling_sec"]])


# 측정 샘플 데이터 불러오기
df_sample = pd.read_csv(
    ".venv/02-01_측정의_3요소_측정샘플.csv", parse_dates=["timestamp"]
)


# Step 2. 실제 저장 간격 확인
print(df_sample["timestamp"].diff().value_counts())


# Step 3. 값의 크기와 움직임 확인

# timestamp를 제외한 측정 태그 목록
tag_list = df_sample.columns.drop("timestamp")

result_df = df_sample[tag_list].agg(["min", "max", "mean"]).T

result_df.columns = ["최솟값", "최댓값", "평균"]

min_change_list = []

for tag in tag_list:
    change = df_sample[tag].diff().abs()
    min_change = change[change > 0].min()
    min_change_list.append(min_change)

result_df["값이 변한 최소 폭"] = min_change_list

print(result_df)

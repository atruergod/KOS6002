import random
import matplotlib.pyplot as plt

print("Hello World!")
print("제 이름은 고건욱입니다.")
print("내 고향은 전라남도입니다.")

# 1부터 100 사이의 정수 10개를 리스트로 생성합니다.
random_numbers = [random.randint(1, 100) for _ in range(10)]
print("\n랜덤 숫자 10개 생성:", random_numbers)

# 생성된 숫자들을 오름차순(작은 수에서 큰 수)으로 정렬합니다.
sorted_numbers = sorted(random_numbers)
print("정렬된 숫자:", sorted_numbers)

# 정렬된 숫자들을 선 그래프로 시각화합니다.
print("\n그래프를 생성합니다...")
plt.figure(figsize=(10, 6))  # 그래프 창의 크기를 조절합니다.
plt.plot(sorted_numbers, marker='o', linestyle='-', color='b')  # 데이터를 기반으로 선 그래프를 그립니다.
plt.title("Sorted Random Numbers")  # 그래프의 제목을 설정합니다.
plt.xlabel("Index")  # X축의 라벨을 설정합니다.
plt.ylabel("Value")  # Y축의 라벨을 설정합니다.
plt.grid(True)  # 그래프에 격자 무늬를 추가합니다.
plt.show()  # 그래프를 화면에 표시합니다.

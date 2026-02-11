# 대소문자 바꾸기
a = "Hello Python Programming...!"
print(a.upper())
print(a.lower())

# 문자열 양옆 공백 제거하기
input_a = """
    안녕하세요
문자열의 함수를 알아봅니다
"""
print(input_a)
print(input_a.strip())

# 문자열의 구성 파악하기
print("TrainA10".isalnum())
print("10".isdigit())

# 문자열 찾기
output_a = "안녕안녕하세요".find("안녕")
print(output_a)
output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)

# 문자열 내부 문자열 확인
print("안녕" in "안녕하세요")
print("잘가" in "안녕하세요")

# 문자열 자르기
a = "10 20 30 40 50".split(" ")
print(a)
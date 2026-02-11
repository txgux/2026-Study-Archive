# format() 함수의 다양한 형태
format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기 ".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

# 출력하기
print(format_a)
print(format_b)
print(format_c)
print(format_d)

# format()함수 활용
a = input("> 1번째 숫자: ")
b = input("> 2번째 숫자: ")
print()
print("{} + {} = {}".format(a, b, int(a) + int(b)))
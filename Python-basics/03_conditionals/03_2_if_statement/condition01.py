# 숫자의 끝자리로 짝수 홀수 구분

# 입력을 받습니다.
number = input("정수 입력> ")

# 마지막 자리 숫자를 추출
last_character = number[-1]

# 숫자로 변환하기
last_number = int(last_character)

# 짝수 확인
if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8:
    print("짝수입니다")

# 홀수 확인
if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9:
    print("홀수입니다")


# if last_number == 0 or 2 or 4 or 6 or 8 은 사용할 수 없는 코드

# or 연산자는 양쪽 피연산자가 불 자료형으로 들어올 것이라고 가정
# 따라서 양쪽 피연산자가 불 자료형이 아니라면, 강제로 불 자료형으로 변경한 뒤 계산
# 파이썬은 0을 제외한 모든 숫자를 True로 변환

# last_number에 어떤 값이 들어가는지와 상관없이 결과값이 항상 True (양쪽 피연산자 중 하나만 True여도 True)
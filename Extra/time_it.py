import timeit

# 초기 테스트 값 (처음으로 나눗셈이 커질때)
a = 10000000000000000

def Shift1() :
    global a
    tt = a
    tt <<= 2

def Shift2() :
    global a
    tt = a
    tt >>= 2

def mul() :
    global a
    tt = a
    tt *= 4

def div() :
    global a
    tt = a
    tt/=4

testa, testb, testc, testd = timeit.timeit(Shift1, number=10000000), timeit.timeit(Shift2, number=10000000), timeit.timeit(mul, number=10000000), timeit.timeit(div, number=10000000)

# 테스트 1 : 기본 속도 비교

print(f"좌쉬프트 : {testa:0.6f}")
print(f"우쉬프트 : {testb:0.6f}")
print(f"곱셉 : {testc:0.6f}")
print(f"나눗셈 : {testd:0.6f}\n")

a = float(a)

teste = timeit.timeit(div, number=10000000)

# 테스트 2 : 소수 형태로 나눗셈 연산

print(f"다른 연산 : {testa:0.6f}, {testb:0.6f}, {testc:0.6f}")
print(f"나눗셈 (소수) : {teste:0.6f}\n")

a = 2**53
testf = timeit.timeit(div, number=10000000)
a -= 1
testg = timeit.timeit(div, number=10000000)

# 테스트 3 : 정수로 표현 가능한 최대 소수값이 2^53-1이기에 2^53과 2^53 -1을 테스트

print(f"나눗셈 연산1 : {testf:0.6f}")
print(f"나눗셈 연산2 : {testg:0.6f}")
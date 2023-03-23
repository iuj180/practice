# 제어문은 조건문, 반복문 
# 조건문 (if문)

# 돈이 있으면 택시를 타고, 돈이 없으면 걸어간다.

money=True                         # money 는 불 자료형 
if money:                          # <, >, ==, !=, >=, <=
    print("택시를 타고 가라")       # and, or, not
else:                              # $, |
    print("걸어 가라")              # in, not in

# if문 기본구조

# if 조건문:              불자료형, Ture이면 아래 실행 flase면 else 밑에 실행
#    수행할 문장1
#    수행할 문장2
# else:
#    수행할 문장A
#    수행할 문장B

# 파이썬에서는 들여쓰기가 잘못되면 오류가 발생함
# 탭을 사용하여 들여쓰기 위치를 맞추어 주어야함

# 불자료형
# "python"    --> 참
# ""          --> 거짓
# [1, 2, 3]   --> 참
# []          --> 거짓
# ()          --> 거짓
# {}          --> 거짓
# 1           --> 참
# 0           --> 거짓
# None        --> 거짓

# 비교 연산자
# x<y    x가 y보다 작다
# x>y    x가 y보다 크다
# x==y   x와 y가 같다
# x!=y   x와 y가 같지 않다
# x>=y   x가 y보다 크거나 같다
# x<=y   x가 y보다 작거나 같다

a=1
b=2
if a!=b:
    print("택시를 타고 가라")
else:
    print("걸어가라")


money1=2000
if money1>=3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")


# and, or, not
# x or y       x와 y 둘중에 하나만 참이면 참이다  (or = |)
# x and y      x와 y 모두 참이어야 참이다  (and = &)
# not x        x가 거짓이면 참이다

money2=2000
card=1
if money2>=3000 or card:             # card=1, 1 이면 true
# if money2>=3000 | card:              or 랑 | 같은 의미
    print("택시를 타고 가라")
else:
    print("걸어가라")


if 1 in [1,2,3]:                  # 리스트에 1이 있다면 true
    print ("택시를 타고 가라")
else:
    print ("걸어가라")


if 1 not in [1,2,3]:               # 리스트에 1이 없다면 ture
    print ("택시를 타고 가라")
else:
    print ("걸어가라")


if 1 not in [1,2,3]:
    pass                           # true 일때 아무런 실행이 없을경우 사용
else:
    print ("걸어가라")



pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:              # 포켓 리스트에 money가 있으면 true
    print ('택시를 타고 가라')
else:
    print("걸어가라")


# 다중 조건 판단 elif
pocket1 =['paper', 'cellphone']
card1=False
a1=True
if 'money' in pocket1:
    pass
elif card1:
    print('택시를 타고가라')
elif a1:
    print('aa')
else:
    print('걸어라가')


# 조건부 표현식 (다른 언어에서는 3항 연산자 ?)
score=70
if score >=60:
    message='success'
else:
    message='failure'
print(message)

message="success" if score>=60 else 'failure'  # 위에 표현을 한줄로 표현가능
print(message)             #조건부 표현식쓸때 if--- else--- 다 써주어야 한다


## 반복문 (while문)

# while문 기본구조
# while <조건문>:          불자료형
#   <수행할 문장1>
#   <수행할 문장2>
#   <수행할 문장3>
#   ...

treeHit=0
while treeHit<10:
    treeHit=treeHit+1
    print('나무를 %d번 찍었습니다.' % treeHit)
    if treeHit==10:
        print('나무 넘어갑니다')


coffee=10
money=300
while money:
    print('돈을 받았으니 커피를 줍니다')
    coffee=coffee-1
    print('남은 커피의 양은 %d개입니다.' %coffee)
    if not coffee:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다')
        break      # while 문 빠져나올때 사용, while문이 true여도...


aa=0
while aa<10:
    aa=aa+1
    if aa%2==0:    # %2 2로 나누었을때, 나머지는 0이냐? 짝수냐? 
        continue   # continue를 만나면 아래로 내려가지 않고 while문 처음으로 돌아감
    print(aa)      # 위의 로직으로 홀수만 출력됨


# 무한 루프
#while True:
#    print('안녕하세요')    # 무한 실행됨. ctrl+c 눌러서 탈출


## 반복문 (for문)
# for문 기본구조

# for 변수 in 리스트 (또는 튜플, 문자열):
#   수핼할 문장1
#   수행할 문장2
#   ...

# 전형적인 for문
test_list=['one', 'two', 'three']
for i in test_list:
    print(i)

# 다양한 for문
a5=[(1,2), (3,4), (5,6)]
for (first, last) in a5:
    print(first)
    print(last)
    print(first + last)


marks=[90, 25, 67, 45, 80]  # 리스트
number=0
for mark in marks:
    number=number+1
    if mark>=60:
        print('%d번 학생은 합격입니다.' %number)
    else:
        print('%d번 학생은 불햡격입니다.' %number)


# for문과 continue

marks1=[90, 25, 67, 45, 80]
number1=0
for mark1 in marks1:
    number1=number1+1
    if mark1 <60: continue
    print('%d번 학생 축하합니다. 합격입니다.' %number1)


# for와 함께 자주사용하는 range 함수
sum1=0
for i in range(1, 11):     # range(이상, 미만), 1이상 11미만, 1~10
    sum1=sum1+i
print(sum1)

# 구구단 예제 (2중 for문)
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")      # end=" " 를 쓰면, 
    print('')


# 리스트 내포 (List comprehension)
z= [1, 2, 3, 4]
result=[]
for num in z:
    result.append(num*3)          # 리스트의 숫자에 3씩 곱한 리스트 만들기
print(result)

z1=[1,2,3,4]
result1=[num*3 for num in z1]     # 위에 세줄을 한줄로 표현
print(result1)


y=[1,2,3,4]
result2=[]
for num in y:
    if num%2==0:
        result2.append(num*3)
print(result2)

y1=[1,2,3,4]
result3=[num*3 for num in y1 if num%2==0]   # for문 안에 if문 들어있는 것도 한줄로 가능
print(result3)                              # 추가하고 싶은 것을 가장 앞에


result4=[]
for x in range(2, 10):
    for y in range(1,10):
        result4.append(x*y)
print(result4)

result5=[x*y for x in range(2,10) for y in range(1,10)]
print(result5)

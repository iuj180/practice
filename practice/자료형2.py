# 튜플 : 리스트와 거의 같음
# 리스트 : a=[1,2,3] --> 리스트안에 내용 추가 가능
# 튜플 : a=(1,2,3)   --> 리스트 내용을 바꿀수 없음 (고정됨)
# 튜플이 연산속도가 빠르다는데....글쎄...

t1=(1,2,'a','b')
# del t1[0]   튜플에서는 삭제가 안됨
# t1[0]='c'   튜플에서는 바꾸기도 안됨
print(t1[0] +1)   # 값을 변해서 출력은 가능하지만 변수 변경은 안됨

t2=(3,4)
print(t1+t2)
print(t1*3)

# 딕셔너리 (중요함)
# 키를 검색해서 값을 볼수 있다 (key를 통해 Value를 얻는다)
# API에 자주 활용됨
# 연관배열 또는 해시 라고 부름

dic = {'name': 'Eric', 'age': 15}
print(dic['name'])   # name 이라는 key를 넣으면 Eric이란 value가 출력됨

a={1:'a'}
a['name']="익명"   # 딕셔너리에 name 추가
print(a)
print(a['name'])

del a[1]   # 키 1을 삭제
print(a)

# a1={1:'a', 1:'b'}  키가 중복되면 오류 발생함 

# 딕셔너리는 키가 핵심

# 키 리스트 만들기

a2={1:'파랑구름', 2:'이현준', 3:'민준'}
print(a2.keys())    # 키만 리스트로 출력
print(a2.values())    # 값만 리스트로 출력
print(a2.items())     # 키,값 쌍으로 묶어서 리스트 출력
print(a2[1])          # 딕셔너리에 키1 출력
print(a2.get(1))      # 딕셔너리에 키1 출력
print(a2.get(4, '없음'))   # 딕셔너리에 키 4가 없을 경우, 없음 출력
print(1 in a2)     # a2 딕셔너리에 키 1이 있으면 true, 없으면 false 출력
for k in a2.keys():
    print(k)
for v in a2.values():
    print(v)
for k, v in a2.items():
    print("키는:" + str(k))
    print("밸류는 " + v)

a2.clear()
print(a2)     # 딕셔너리 비우기



# 집합 --> 파이썬에만 있음
# 집합에 관련된 것들을 쉽게 처리하기위해 만들어진 자료형
# 중복을 허용하지 않는다.
# 순서가 없다. 

s1=set([1,2,3])   # 집합 만들기
print(s1)
s2={1,2,3}        # 집합 만들기
print(type(s2))   # s2의 타입 확인하기 --> set
print(s2)         # 집합은 {} 로 표기

s3=[1,2,2,3,3]     # 리스트
newlist = list(set(s3))  # 리스트의 중복된 것을 set으로 제거후 다시 리스트로 만들기
print(newlist)

s4=set("Hello")    # 집합은 순서가 없고, 중복이 없다.
print(s4)

s5=set([1,2,3,4,5,6])
s6=set([4,5,6,7,8,9])
print(s5&s6)                 # 교집합 구하기
print(s5.intersection(s6))   # 교집합 구하기

print(s5|s6)                 # 합집합 구하기
print(s5.union(s6))          # 합집합 구하기

print(s5-s6)                 # 차집합 구하기 (s5)
print(s5.difference(s6))     # 차집합 구하기 (s5)

s7=set([1,2,3,4,5,6])
s7.add(7)                  # s7 집합에 7 추가
print(s7)
s7.update([7,8,9,10,11])   # s7 집합에 여러개 추가 (중복된 건 추가 안됨)
print(s7)


# 불 자료형 (boolean)
# 참(true), 거짓(false)

b1=True              # 불 자료형
print(type(b1))      # type 이름 bool

# "python"    --> 참
# ""          --> 거짓
# [1, 2, 3]   --> 참
# []          --> 거짓
# ()          --> 거짓
# {}          --> 거짓
# 1           --> 참
# 0           --> 거짓
# None        --> 거짓

b2="안녕"
if b2:
    print(b2)

b3=""
if b3:
    print(b3)


b4=[1,2,3,4]
while b4:
    b4.pop()            # b4 마지막게 튀겨나가서 없어질때까지 반복
    print(b4)


# 변수
# 파이썬에서 사용하는 변수는 객체를 가리키는것

c1=[1,2,3]       # c1에 [1,2,3] 이라는 값을 가지는 자료형이 자동으로 메모리에 생성
c2=c1            # c2에 c1의 메모리 주소를 똑같이 할당
c1[1]=4          # c1을 2번째 데이터를 4로 바꿈
print(c1)        # c1을 출력
print(id(c1))    # c1에 할당된 주소값 출력
print(c2)        # c2를 출력해도 c1과 동일한 주소를 가지고 있기에 바뀌 c1값을 가짐
print(id(c2))    # c2에 할당된 주소값 출력

d1=[1,2,3]
d2=d1[:]          # d1을 복사해서 가지고옴 d1의 주소할당이 아님
d1[1]=4
print(d1)
print(id(d1))
print(d2)
print(id(d2))


from copy import copy
e1=[1,2,3]
e2=copy(e1)
e1[1]=4
print(e1)
print(id(e1))
print(e2)
print(id(e2))

# 변수를 할당하는 방법

aa,bb=('python', 'life')   # 튜플 자료형
print(aa)
print(bb)

[aa1, bb1]=['python', 'life']
print(aa1)
print(bb1)

aa2=bb2='hello'
print(aa2)
print(bb2)

# 변수 바꾸기 (일반적인)
aaa1=3
bbb1=5

tmp=bbb1
bbb1=aaa1
aaa1=tmp

print(aaa1)
print(bbb1)

# 파이썬에서 변수 바꾸기 방법
aaa2=3                   
bbb2=5
aaa2, bbb2=bbb2, aaa2
print(aaa2)
print(bbb2)

# 문제 풀이
# 한 문장으로 만들어 출력하기
aaa3=['Life', 'is', 'too', 'short']
result =" ".join(aaa3)
print(result)

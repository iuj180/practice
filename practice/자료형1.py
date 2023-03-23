a=3
b=4
c=3.4
d=4.24e10

print(a)
print(c)
print(d)

print(type(a)) # 정수형 int
print(type(c)) # 실수형 float
print(type(d)) # 컴퓨터식 지수 표현 방식 float

print(a+b)  # 더하기
print(a-b)  # 빼기
print(a*b)  # 곱하기
print(a/b)  # 나누기
print(a//b) # 몫
print(a%b)  # 나머지
print(a**b) # 제곱

aa="Hello world"         # 문자열 만들기 4가지 방법
bb='Hello world'
cc="""Hello world"""
dd='''Hello world'''

print(aa)
print(bb)
print(cc)
print(dd)
print(type(aa))  # 문자열 str

ee="Python's favorite food is perl"
ff='Python"s favorite food is perl'   # 문장중간 " 사용
gg='Python\'s favorite food is perl'  # \' 사용

print(ee)
print(ff)
print(gg)

# \n 문자열 안에서 줄을 바꿀때 사용
# \t 문자열 사이에 텝 간격을 줄 때 사용
# \\ 문자 \ 를 그래로 표현할때 사용
# \' 작은따옴표(')를 그대로 표현할때 사용
# \" 큰따옴표(")를 그대로 표현할때 사용
# \r 캐리지 리턴 (줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
# \f 폼 피드 (줄바꿈 문자, 현재 커서를 다음줄로 이동)
# \a 삐소리 (출력할때 PC 삐소리)
# \b 백스페이스
# \000 널문자

a1='Life is too short\nYou need python'  # \n 줄바꾸기
a2='Life is too short\tYou need python'  # \t 텝간격
a3="""Life is too short
You need python
Really?"""              # """ 혹은 ''' 사용시 \n 안해도 줄바꿈됨

print(a1)
print(a2)
print(a3)

a4="Python "
a5="is fun!"

print(a4+a5)      # 문자열 더하기
print(a4*100)     # 문자열 여러번 출력하기



# 인덱싱 (중요함)
b1="Life is too short, You need Python"

print(b1[0])     # b1의 1번째 문자열 출력
print(b1[1])     # b1의 2번째 문자열 출력
print(b1[5])     # b1의 4번째 문자열 출력 
print(b1[6])     # b1의 5번째 문자열 출력(순서에 빈칸포함)
print(b1[-1])    # b1의 마지막에서 1번째 문자열 출력

# 슬랑이싱 (slicing)
# b1[이상:미만:간격]

print(b1[0:4])    # b1의 첫번째부터 3번째 문자열 출력

b2="20010331Rainy"

print(b2[0:4])
print(b2[:8])     # 앞에 비워있으면 무조건 처음부터 출력
print(b2[8:])     # 9번째부터 끝까지 출력
print(b2[::2])    # 처음부터 끝까지 2칸 간격 문자 출력

# 문자열 포매팅

# %s 문자열 (string)
# %c 문자 1개 (character)
# %d 정수 (integer)
# %f 부동소수 (floating-point)
# %o 8진수
# %x 16진수 
 # %% literal % (문자 '%' 자체)

c1="I eat %d apples." %3    # %d 자리에 뒤에 설정한 숫자 출력
c2= "I eat " + str(3) + " apples"    # 문자 + 숫자는 안됨 str()로 해주어야함  

print(c1)
print(c2)

number=10
day="three"
d1="I ate %d apples. so I was sick for %s day." % (number, day)

print(d1)


# 정렬과 공백  (쓸일 별로 없어)

e1="%10s" % "hi"    # 10칸이 띄어진후 hi 출력
e2="%-10sjane." % 'hi'  # jane 앞에 10칸을 띄어진후 앞에 hi 출력

print(e1)
print(e2)

# 소수점 표현

f1="%f" %3.43134324
f2="%0.4f" % 3.43134324  # 소수점 4번째자리까지 출력

print(f1)
print(f2)

g1="adsfadf asdfa asdfa {} asdfadf".format("안녕")
# {}에 .format(" ") 으로 설정된 문자열 입력하여 출력
g2="adsfadf {age} asdfa asdfa {name} asdfadf".format(name="이시영", age=3)

print(g1)
print(g2)

name="int"
g3= f"나의 이름은 {name}입니다."

print(g3)

# 문자열 개수 세기 (count)

aa1= "hobby"
aa1.count('b')
aa2="magic treeeeee".count('e')   # 변수에 함수포함하여 설정가능

print(aa1.count('b'))    # aa1에서 b의 개수를 세기
print(aa1.find('b'))     # aa1에서 b의 가장 먼저 있는 인덱스 출력
print(aa1.find('x'))     # aa1에 없는 문자를 찾으면 -1 출력
print(aa2)

# 위치 알려주기
aaa1="Life is too short"
aaa1.index('t')              # t 의 인덱스 위치 출력, 없으면 에러

aa2=",".join('abcd')           # abcd에 문자열 "," 삽입
aa3=",".join(["a", "b", "c"])   # 리스트 abc에 문자열 "," 삽입

print(aa2)
print(aa3)

bb1="hi"
bb2="HI"
bb3="    HI"
bb4="    HI    "
print(bb1.upper())       # 소문자를 대문자로
print(bb2.lower())       # 대문자를 소문자로
print(bb3.strip())       # 양쪽 공백 지우기
print(bb4.rstrip())      # 오른쪽 공백 지우기
print(bb4.lstrip())      # 왼쪽 공백 지우기

cc1="Life is too short"
print(cc1.replace("Life", "Your leg"))   # Life 를 Your leg로 바꾸기
print(cc1.split())       # 띄어쓰기 기준으로 단어 리스트로 만듬 (자름)

cc2="a:b:c:d"
print(cc2.split(":"))    # : 기준으로 리스트로 만들고 출력

cc3="3233-agv3-34ds-3dfg"
print(cc3.split("-"))      # - 기준으로 리스트로 만들고 출력
print(cc3.split("-")[2])   # - 기준으로 리스트로 만들고 2번째 출력

# 리스트명 = [요소1, 요소2, 요소3]
# 여러 요소를 하나의 변수로 관리하기 위해 사용

dd1="이시영"
dd3="int"
dd4="김정훈"
dd5="주니주니"

dd6=["이시영", "문재성", "int", "김정훈", "주니주니"]   # 여러변수를 리스트로 만들기
print(dd6[1])   # 리스트중 2번째 출력 (인덱싱)

dd7=[1, 2, "ing", ["김재원", "고양이"]]  # 리스트 안에 리스트를 만들수 있음

print(dd7)
print(dd7[3])     # 리스트 안에 리스트를 출력 (인덱싱)
print(dd7[3][1])  # 리스트 안에 리스트중 2번째 출력 (인덱싱)

dd8=[1, 2, 3, 4, 5]

print(dd8[0:3])   # 리스트에서 1번째부터 3번째까지 출력 (슬라이싱)

dd9=[1, 2, 3,]
dd10=[4, 5, 6]

print(dd9+dd10)   # 리스트 더하기
print(dd9*3)      # 리스트 내용 3번 곱하기

print(dd9[0]+dd10[0])   # dd9의 1번째와 dd10 1번째 더하기

ee1=["박주하", "잠수", "문재성"]
ee1[0]="한재성"    # ee1의 1번째를 한재성으로 교체
print(ee1)

ee2=["박주하", "잠수", "문재성"]
ee2[0:2]=["김정현", "김수환"]    # ee2의 1번째부터 2번째까지를 교체
print(ee2)

ee3=["박주하", "잠수", "문재성"]
del ee3[0]        # ee3의 1번째 삭제
print(ee3)

ee4=["박주하", "잠수", "문재성"]
ee4.append("김태현")        # ee4의 김태현 추가
print(ee4)

ee5=["박주하", "잠수", "문재성", "김태현"]
ee5.sort()                 # ee5 리스트 정렬
print(ee5)

ee6=[1,5,3]
ee6.sort()     # 오름차순 정렬
print(ee6)

ee7=[1,5,3]
ee7.reverse()
print(ee7)     # 순서를 거꾸로 정령

ee8=[1,5,3]
ee8.sort()
ee8.reverse()
print(ee8)     # 내림차순 정렬

ee9=[1,5,3]
print(ee9.index(1))  # 인덱스 표시, 해당 숫자 없으면 오류발생

ee10=[1,5,3]
ee10.insert(0,4)     # 0번째 인덱스에 4를 넣어라
print(ee10)

ee11=[1,5,3]
ee11.remove(1)       # 해당 숫자 없애기
print(ee11)

ee12=[1,5,3,1,1,1,1,]
ee12.remove(1)
print(ee12)          # 해당 하는 숫자 제일 처음것만 제거됨

ee13=[1,5,3]
ee13.pop()           # 리스트의 마지막 숫자 제거된 리스트 출력
print(ee13)

ee14=[1,5,3]
print(ee14.pop())    # 리스트의 마지막 숫자가 출력됨 (리스트에서 튀겨져 나온 숫자)

ee15=[1,5,3,1,1,1]
print(ee15.count(1))    # 리스트에 있는 1의 개수를 출력

ee16=[1,5,3,1,1,1]
ee16.extend([2,3])      # 리스트 뒤에 요소가 추가 
print(ee16)

ee17=[1,5,3,1,1,1]
ee17.append([2,3])      # 리스트 뒤에 리스트가 추가 
print(ee17)

# ff1의 i 만 대문자로 만들기
ff1="i study python wiht jocoding"
print(ff1.split()[0].upper()+ff1[1:])

ff2="i study python wiht jocoding"
print(ff2.split()[0])
print(ff2[1:])
print(ff2.split()[0].replace("i","I")+ff1[1:])

ff3="i study python wiht jocoding"
print(ff3.replace("i", "I"))    # 모든 i 가 대문자로 바뀜

gg1="%s" % "김종욱"
print(gg1 *10)
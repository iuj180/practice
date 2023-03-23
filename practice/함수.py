# # 인풋 --> 함수 --> 아웃풋
# # 프로그래밍에서 함수는 입력, 출력이 없을수 있음

# # 파이썬 함수 구조

# # def 함수명(매개변수)
# #   <수행할 문장1>
# #   <수행할 문장2>
# #   ...
# # return 리턴 값

# def sum(a,b):             # sum 이라는 함수를 정의, 함수 정의할때 def 사용
#     result=a+b
#     return result
# print(sum(1,2))           # sum(a,b) 함수 호출


# # 입력값이 없는 함수
# def say():
#     return 'Hi'
# print(say())

# # 결과값이 없는 함수
# def sum(a,b):
#     print('%d, %d의 합은 %d입니다.' %(a,b,a+b))
# sum(1,2)
# print(sum(1,2))           # 리턴값이 없는 함수여서 none 값 출력됨

# myList=[1,2,3]
# print(myList.append(4))   # append 라는 함수를 썼지만, 출력이 없는 함수임 --> return 값이 없다
# print(myList.pop())       # 위에 append로 4를 넣고, pop으로 빼네니 3출력 --> pop은 return 값이 있음


# # 입력값도 없고 출력값도 없는 함수
# def say():
#     print('Hi')
# print(say())              # 입력도 출력도 없어서 none 출력됨


# # 여러개의 입력값 함수
# def sum_many(*args):      # 여러 입력값 넣고 싶을 경우, 함수 매개변수에 *args 형식으로 씀
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# print(sum_many(1,2,3,4,5,6,7,8,9,10))

# # 키워드 파라미터
# def print_kwargs(**kwargs):               # **kwargs --> 딕셔너리
#     for k in kwargs.keys():
#         if(k=='name'):
#             print('당신의 이름은 :' + k)
# print(print_kwargs(a='1', b='2'))


# # 함수의 결과값은 언제나 하나이다
# def sum_and_mul(a,b):
#     return a+b, a*b, a-b

# print(sum_and_mul(1,2))
# print(sum_and_mul(1,2)[0])
    
# # 매개변수에 초기값 미리 설정하기
# def say_myself(name, old, man=True):           # man 인자에 true 로 미리 설정함, 중간에 있으면 매핑이 안됨
#     print('나의 이름은 %s 입니다.' %name)
#     print('나이는 %d살입니다.' %old)
#     if man:
#         print('남자입니다.')
#     else:
#         print('여자입니다.')
# say_myself('라이유튜브',20)                     # 함수설정시 man을 미리설정하지 않으면, 오류 출력됨
# say_myself('김은서', 9, False)                 # 순서를 맞추어야 함, 미리설정된 것은 맨 끝에 써주어야 매핑이 됨
# say_myself(old=25, name='김은서', man=False)   # 순서를 맞추지 않으면 각가 매핑해주어야함

# a=1
# a+=1           # a+=1 은 a=a+1 과 같은 의미임
# print(a)

# # 함수 안에 선언된 변수의 효력 범위

# a1=1                # 함수 밖에 있는 변수는 전역변수 --> 어디에서나 사용할 수 있음
# def vartest(a1):    # 함수내 변수는 지역변수 --> 함수 내에서만 사용되는 임시변수
#     a1=a1+1         # 만약 다음줄에 return a1 으로 해주면 a1에 a1+1이 들어가게 됨
# vartest(a1)
# print(a1)

# a2=1
# def vartest1(a2):
#     a2=a2+1
#     return a2       # a2+1을 a2에 할당
# a2=vartest1 (a2)    # a2변수에 vartest1 함수의 a2를 할당함
# print(a2)

# a3=1
# def vartest3():
#     global a3       # 전역변수로 선언하는 방법
#     a3=a3+1
# vartest3 ()
# print(a3)

# b=1
# myList = [1,2,3]
# def vartest4(b):           # 리스트에서는 함수 밖에 있는 변수도 쓸수 있다.
#     myList.append(b)
# vartest4(4)
# print(myList)


# # Lambda (함수명 = lambda 매개변수 : result)
# add=lambda a, b: a+b     # 아래 함수를 한줄로 정의--> 리스트에 함수를 넣을수 있다.
# result = add(3,4)
# print(result)

# def add(a,b):             
#     return a+b

# myList=[lambda a, b: a+b, lambda a, b: a*b]   # 리스트에 함수를 넣을수 있음
# print(myList[0](1,2))                         # 리스트안에 함수는 함수명이 없음, 인덱스 설정으로 출력


# # 사용자 입력과 출력
# # input 함수 사용  --> 내장함수 , def로 정의 하는 것은 사용자 정의함수

# aa=input('입력값을 넣어주세요: ')               # 입력값을 넣어야 함
# print(aa)

# number=input('숫자를 입력하세요: ')
# print(number)

# # print 함수  --> 내장함수
# print('life' 'is' 'too short')    # 단어 사이에 , 를 안써도 됨. 단, 단어가 붙어서 출력됨
# print('life', 'is', 'too short')  # 단어 사이에 , 를 쓰면 띄어쓰기가 됨

# for i in range(10):
#     print(i, end=' ')    # end=' '를 쓰면 i 출력하고 끝에 ' ' 출력되고, 한줄로 출력함


# # 파일 읽고 쓰기

# # 파일 생성하기 
# # 파일 열기 모드
# # r    --> 읽기모드 - 파일을 읽기만 할때 사용
# # w    --> 쓰기모드 - 파일에 내용을 쓸대 사용 (기존내용 삭제후 재작성)
# # a    --> 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬때 사용

# f=open("새파일.txt", 'w')   
# f.close()

# f=open("d:/blindcat/파일열기연습.txt", 'w', encoding='utf-8')  # encoding='utf-8' 해주면 한글이 안깨짐       
# for i in range(1,11):
#     data='%d번째 줄입니다. \n' %i   # \n 은 한줄 띄어주기
#     f.write(data)


# # readline() 함수  --> 텍스트 파일 내용에서 한줄 읽어오기
# f=open("파일열기연습.txt", 'r', encoding='utf-8')
# line=f.readline()    # readline() 함수는 파일에서 한줄씩 읽어오기
# print(line)
# # f.close()               # 파일을 open 하고 나면, 끝에 파일.close 해주어야 함

# f=open('파일열기연습.txt', 'r', encoding='utf-8')
# while True:                     # 파일에서 모든줄 가지고 오기
#     line=f.readline()
#     if not line: break          # 파일에 라인이 없으면 빠져 나오기
#     print(line)                 # \n이 들어가 있어서 한줄 띄기가 기본으로 출력 
# f.close()

# # readlines()  --> 텍스트 파일에서 모든 라인 읽어오기
# f=open('파일열기연습.txt', 'r', encoding='utf-8')
# lines=f.readlines()              # 리스트 형식의 데이터
# for line in lines:
#     print(line)                   # \n이 들어가 있어서 한줄 띄기가 기본으로 출력 
# f.close()

# f=open('파일열기연습.txt', 'r', encoding='utf-8')
# lines=f.readlines()              # 리스트 형식의 데이터
# for line in lines:
#     print(line, end="")          # end="" 를 써서 끝에 \n을 적용하지 않도록 함
# f.close()

# f=open('파일열기연습.txt', 'r', encoding='utf-8')
# lines=f.readlines()              # 리스트 형식의 데이터
# for line in lines:
#     print(line.strip("\n"))      # .strip("\n") 를 써서 끝에 \n을 적용하지 않도록 함
# f.close()

# f=open('파일열기연습.txt', 'r', encoding='utf-8')
# lines=f.readlines()              # 리스트 형식의 데이터
# for line in lines:
#     print(line.strip("\n"), end="")      # .strip("\n"), end="" 를 쓰면 한줄로 쓰기가 됨
# f.close()


# # read() 함수 --> 파일 내용 통채로 읽어오기
# f=open('파일열기연습.txt', 'r', encoding='utf-8')
# data=f.read()
# print(data)
# f.close()


# # 파일에 내용 추가하기
# f=open('파일열기연습.txt', 'a', encoding='utf-8')
# for i in range(11, 20):
#     data="%d번째 줄입니다. \n" %i
#     f.write(data)
# f.close()

# # with 문과 함께 사용하기 --> 할당한 변수가 지역변수여서 .close()를 하지 않아도 됨
# with open('foo.txt', 'w') as f:    # 파일을 만들어서 f라는 변수에 할당 (지역변수)
#     f.write("Life is too short, you need python")

# with open('연습1.txt', 'w', encoding='utf-8') as z:
#     for i in range(0,2500):
#         z.write("연습\n")

# aaaa=input('a값을 입력해주세요.')
# bbbb=input('b값을 입력해주세요.')
# def sum(aaaa,bbbb):
#     print('덧셈을 하겠습니다.')
#     print('결과는 : ' + str(aaaa+bbbb))

# print(sum(aaaa,bbbb))


# def print_kwargs(**kwargs):
#     for k,v in kwargs.items():
#         if(k=='name'):
#             print('이름은 : ' + v)
#         elif k=='age':
#             print('나이는 : ' + v)

# print_kwargs(name='김은서', age='15')

# a=lambda *arg: arg
# print(a(1,2,3))

# a=lambda **kwargs: kwargs
# print(a(name="hi"))


# immutable (정수, 실수, 문자열, 튜플) --> 변하지 않는 자료형
a=1                     # 전역변수
def vartest(a):
    a=a+1               # 지역변수
vartest(a)
print(a)                # a는 정수여서 바뀌지 않는 자료형임으로 지역변수에서 변경된 것이 전역변수에 영향이 없음

# mutable (리스트, 딕셔너리, 집합) --> 변하는 자료형
b=[1,2,3]               # 전역변수
def vartest2(b):        
    b=b.append(4)       # 지역변수
vartest2(b)
print(b)

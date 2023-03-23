# # 클래스
# # 반복되는 변수 & 메세드(함수)를 미리 정해놓은 틀(설계도)
# # 클래스는 도대체 왜 필요한가?

# result=0
# def add(num):              # 더하기 함수
#     global result          # global 을 써주면 result는 전역변수가 됨 (함수안에 있지만)
#     result += num
#     return result

# print(add(3))
# print(add(4))

# # 두개의 계산기 --> 함수를 두개를 만들어줘야 하니 불편해 이럴때 클래스를 만듬
# result1=0
# result2=0

# def add1(num):
#     global result1
#     result1 += num
#     return result1

# def add2(num):
#     global result2
#     result2 += num
#     return result2

# print(add1(3))
# print(add1(4))
# print(add2(3))
# print(add2(7))

# # 클래스를 이용한 계산기
# class Calculator:              # 클래스는 앞글자를 대문자로 쓴다
#     def __init__(self):        # 클래스를 처음만들때 쓰는 초기값 변수 정의
#         self.result=0

#     def add(self, num):
#         self.result += num
#         return self.result

# cal1 = Calculator()            # 정의해놓은 클래스를 사용하는것으로 cal1 변수 정의
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))


# # 사칙연산 클래스1
# class FourCal:                 # 클래스 만들기
#     pass                       # pass 는 아무것도 안한다는것

# a=FourCal()
# print(a)
# print(type(a))

# # 사칙연산 클래스2
# class FourCal:
#     def setdata(self, first, second):      # 클래스 안에 있는 함수를 "메소드" 라고 함
#         self.first = first                 
#         self.second = second

# a=FourCal()
# a.setdata(1,2)           # a --> self, 1 --> first, 2 --> second
# print(a.first)
# print(a.second)

# # 사칙연산 클래스3
# class FourCal:
#     def setdata(self, first, second):      # 클래스 안에 있는 함수를 "메소드" 라고 함
#         self.first = first                 
#         self.second = second
#     def add(self):
#         result=self.first+self.second
#         return result

# a=FourCal()              # a를 인스턴스라고 한다
# a.setdata(4,2)           # a --> self, 4 --> first, 2 --> second
# print(a.add())

# # 생성자 (Constructor) --> __init__
# class FourCal:
#     def __init__(self, first, second):    # __init__ --> 클래스를 만들면 가장 처음으로 수행하는 것
#         self.first=first
#         self.second=second
#     def setdata(self, first, second):
#         self.first = first                 
#         self.second = second
#     def add(self):
#         result=self.first+self.second
#         return result
#     def mul(self):
#         result=self.first*self.second
#         return result
#     def sub(self):
#         result=self.first-self.second
#         return result
#     def div(self):
#         result=self.first/self.second
#         return result

# a=FourCal(1,2)           # 클래스 __init__ 을 썼기때문에 first, second에 값을 넣어줘야 한다.
# print(a.add())

# # 클래스의 상속  --> 만들어진 클래스를 가져다 쓰는것
# FourCal <-- MoreFourCal1
#         <-- MoreFourCal2
# class MoreFourCal(FourCal):          # FourCal 클래스를 상속함, __init__ 를 안써도 되고, 변형을 해도 됨
#     pass
# a=MoreFourCal(4,2)
# a.add()
# print(a.add())

# # 클래스의 상속2 - 메서드 추가
# class MoreFourCal(FourCal):
#     def pow(self):                     # FourCal 클래스를 상속받고, MoreFourCal 클래스에 pow 메서드 추가
#         result=self.first ** self.second
#         return result

# a=MoreFourCal(4,2)
# print(a.pow())

# # 메서드 오버라이딩  --> 덮어쓰기
# class SafeFourCal(FourCal):
#     def div(self):                      # 부모 클래스에도 있고, 자식 클래스에도 있으면 자식 클래스에 있는 것이 우선이여서 변형 가능
#         if self.second==0:
#             return 0
#         else:
#             return self.first / self.second

# a=SafeFourCal(4,0)                     # FourCal(4,0)으로 하면 오류생김
# print(a.div())                         # 나누기는 float 자료형임, 그래서 소수점으로 출력


# # 클래스 변수, 객체 변수
# # 클래스 변수 : 클래스에서 공통으로 사용하는 변수
# class Family:
#     lastname = '김'                      # 클래스 변수
#     def __init__(self, first, secon):    
#         self.lasname = '김'              # 객체 변수

# Family.lastname = '박'                   # 클래스 밖에서 변경할수 있음
# print(Family.lastname)

# a=Family()
# b=Family()
# print(a.lastname)
# print(b.lastname)

# # 모듈이란?
# # 미리 만들어 놓은 ***.py 파일 (함수, 변수, 클래스)

# # 모듈 만들고 불러 보기
# import mod1               # mod1.py 파일 불러오기
# print(mod1.add(1,2))

# # from 모듈이름 import 모듈함수
# from mod1 import add     # mod1.py 파일에서 add1 함수만 가져오기
# print(add(1,2))

# # if __name__ == '__main__': 의 의미 --> 그파일을 실행하려고 하면 메인
# import mod1

# # sys.path.append("경로")   --> 파일이 다른 경로에 있을 경우
# import sys
# print(sys.path)

# import sys
# sys.path.append("D:\\blindcat\\subfolder")
# import mod2
# print(mod2.add(3,4))


# 패키지란? 모듈 여러개를 모아 놓은 것
#__init__.py  --> 파이썬을 표현하는 패키지 파일

# 패키지의 구조
# game\                    --> game 폴더
#    __init__.py           --> 패키지 표현 파일, 파이썬 3.3 이후에는 없어도 된다고하나, 하위버전 호환성때문에 만듦
#    sound\                --> game 폴더 아래 sound 폴더
#        __init__.py       --> 패키지 표현 파일
#    graphic\              --> game 폴더 아래 graphic 폴더
#        __init__.py       --> 패키지 표현 파일


# import game.sound.echo           # --> game 폴더>sound폴더>echo파일
# game.sound.echo.echo_test()

# from game.sound import echo      # --> game 폴더>sound폴더 중에 echo파일만 가져온다
# from game.sound.echo import echo_test  # --> game폴더>sound폴더>echo파일중에 echo_test 함수만 가져온다
# from game.sound.echo import echo_test as e  #--> 패키지 이름을 e로 치환
# e()
# from game.sound import *   # game>sound 폴더안에 모든것을 다 가져와라
#                            # 단, sound 폴더에 __init__.py 파일에 지정해야함
#                            # __init__.py파일안에 __all__ =['echo'] 이런식으로 설정하는 것임



# # relative 패키지
# from ..sound.echo import echo_test  # .. 은 이전폴더로 가는 방법 
#                                     # --> 이전폴더로 가고 sound 폴더로 가서
#                                     # echo.py 안에 echo_test를 가져와라
#                                     # 



# # 예외처리
# # 오류가 발생했을때 어떻게 할지 정하는 것

# # try:
# #   #오류가 발생할수 있는 구문
# # excep Exception as e:
# #   #오류 발생
# # else:
# #   #오류 발생하지 않음
# # finally:
# #   #무조건 마지막에 실행

# f=open("없는파일", 'r')         # 없는 파일.py 이 없으니 오류가 발생함


# try:
#     4/0                             # 0으로 나눌수 없으니, 실행해 보면 zerodivisonerror가 발생함
# except ZeroDivisionError as e:      # ZeroDivisionError 에러가 발생하면 넘어간다
#     print(e)                        # 에러명을 출력
# print("안녕")                       # 프로그램이 멈추지 않고 다음행이 진행된다


# try:
#     f=open('foo1.txt','r')
# except FileNotFoundError as e:
#     print (str(e))
# else:
#     data=f.read()
#     print(data)
#     f.close


# # except Exception as e:     # Exception 을 쓰면 어떤 오류도 다 잡을수 있다

try:
    a=[1,2]
    print(a[3])
    4/0
except ZeroDivisionError:                   # 여러개의 except를 적용할수 있다
    print("0으로 나눌수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")             # 여러개의 except를 적용할수 있다


try:
    f=open("나없는파일",'r')
except FileNotFoundError:
    pass                                    # 오류가 발생해도 그냥 지나가라


# 오류를 일부로 발생시키기

class Bird:
    def fly(self):
        raise NotImplementedError           # raise 에러명 사용

class Eagle(Bird):
    def fly(self):
        print("verry fast")

eagle=Eagle()
eagle.fly()

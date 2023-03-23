### 파이썬 시작하기
print("Hello World")
print("Mary's cosmetics")

print('신씨가 소리질렀다. "도둑이야."')

print("C:\Windows")

print("안녕하세요.\n만나서\t\t반갑습니다.")

print("오늘은", "일요일")

print("naver;kakao;sk;samsung")
print("naver", "kakao", "sk", "samsung", sep=";")
print("naver", "kakao", "sk", "samsung", sep="/")

print("first");print("seceon")
print("first", end=" "); print("second")

print(5/3)



### 파이썬 변수
삼성전자=50000
주식=10
총평가금액=삼성전자*주식
print(총평가금액)

시가총액=298000000000000
현재가=50000
PER=15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

s="hello"
t="python"
print(s+"!", t)

2+2*3

a=128
print (type(a))

a="132"
print(type(a))

num_str="720"
num_int=int(num_str)
print(num_int+1, type(num_int))

num=100
result=str(num)
print(result, type(result))

문자열="15.79"
실수=float(문자열)
print(실수, type(실수))

월이용료=48584
할부=36
총금액=월이용료*할부
print(총금액)


### 파이썬 문자열
letters='python'
print(letters[0], letters[2])

license_plate='24가 2210'
print(license_plate[3:])
print(license_plate[4:])
print(license_plate[-4:])
print(license_plate[-3:])

string="홀짝홀짝홀짝"
print(string[0::2])

string="PYTHON"
print(string[::-1] )

phone_number="010-111-2222"
print(phone_number.replace("-", " "))
print(phone_number.replace("-", ""))

url="http://sharebook.kr"
url_split=url.split('.')
print(url[-2::])
print(url_split)
print(url_split[-1])

lang='python'
lang[0]='P'   #--> 문자열은 수정되지 않음
print(lang)

string='abcdef3agdd3a32dga'
print(string.replace('a','A'))

string='abcd'
string.replace('b','B')    #--> 문자열은 수정되지 않음
print(string)

a='3'
b='4'
print(a+b)

print('Hi'*3)
print('-'*80)

t1='python'
t2='java'
t3=t1+' '+t2+' '
print(t3*4)

name1='김민수'
age1=10
name2="이철희"
age2=13
print('이름:',name1,'나이: ',age1)
print('이름: %s 나이 : %d' % (name1, age1))
print('이름: %s 나이 : %d' % (name2, age2))
print('이름:{} 나이: {}'.format(name1, age1))
print('이름:{} 나이: {}'.format(name2, age2))
print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')

상장주식수='5,969,782,550'
컴마제거=상장주식수.replace(",","")
타입변환=int(컴마제거)
print(타입변환, type(타입변환))

분기 = '2020/03(E) (IFRS연결)'
print(분기[:7])

data="   삼성전자   "
공백제거=data.replace(" ", "")
print(공백제거)
공백제거2=data.strip()
print(공백제거2)

ticker = 'btc_krw'
print(ticker)
print(ticker.upper())

ticker = 'BTC_KRW'
print(ticker)
print(ticker.lower())

a='hello'
print(a.capitalize())

file_name='보고서.xlsx'
file_name.endswith('xlsx')
file_name.endswith(('xlsx','xls'))

file_name='2020_보고서.xlsx'
file_name.endswith('2020')

a='hello world'
print(a.split(" "))
print(a)
a.split()
print(a)

ticker='btc_krw'
print(ticker.split("_"))

date='2020-05-01'
print(date.split("-"))

data='    039490     '
print(data.replace(" ", ""))
print(data.strip())
print(data.rstrip())

### 파이썬 리스트
movie_rank=['닥터 스트레인지', '스플릿', '럭키']
movie_rank.append('배트맨')
print(movie_rank)

movie_rank.insert(1,'수퍼맨')
print(movie_rank)

movie_rank=['닥터 스트레인지', '수퍼맨', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

lang1=['c','c++', 'java']
lang2=['pytho', 'go', 'c#']
lang=lang1+lang2
print(lang)

nums=[1,2,3,4,5,6,7]
print('max:', max(nums))
print('min:', min(nums))
print(sum(nums))

cook=['피자', '김밥', '만두', '양념치키', '족박', '피자', '김치만두', '쫄면', '소시지', '라면', '팥빙수', '김치전']
print(len(cook))

nums=[1,2,3,4,5]
average=sum(nums)/len(nums)
print(average)

price=['20180728',100,130,140,150,160,170]
print(price[1:])

nums=[1,2,3,4,5,6,7,8,9,10]
print(nums[0::2])
print(nums[1::2])

nums=[1,2,3,4,5]
print(nums[::-1])

interest=['삼성전자', 'LG전자', 'Naver']
print(interest[0::2])  #--> 슬라이싱
print(interest[0], interest[2])  #--> 리스트

interest=['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest)
print(" ".join(interest))
print("/".join(interest))
print("\n".join(interest))

string='삼성전자/LG전자/Naver'
interest="/".join(string)
print(interest)
interest=string.split("/")
print(interest)

data=[2,4,3,1,5,10,9]
print(data.sort())
data.sort()
print(data)


### 파이썬 튜플
my_varialbe=(1)
print(my_varialbe, type(my_varialbe))

movie_rank=('닥터 스트레이지', '스플릿', '럭키')
print(movie_rank)

nums=(1)
print(type(nums))

t=(1,2,3)
t[0]='a'  # --> 튜플은 원소 추가, 변경 불가

t=1,2,3,4
print(type(t))

t=('a','b','c')
t=('A','b','c')

interest=('삼성전자','LG전자','SK Hynix')
print(interest, type(interest))
data=list(interest)
print(data, type(data))

temp=('apple','banana','cake')
a,b,c=temp
print(a,b,c)

data=tuple(range(2,100,2))
print(data)


### 파이썬 딕셔너리
a,b,*c=(0,1,2,3,4,5)
a
b
c

scores=[8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_scores, a, b, _=scores
print(valid_scores)

scores=[8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_scores, b=scores
print(valid_scores)

temp=dict()
print(temp)
temp2={}
print(temp2)

name={'메로나', '폴라포', '빵빠레'}
cost={1000,1200,1800}
ice_cream={'메로나': 1200, '폴라포': 1200, '빵빠레': 1800}
print(ice_cream)

ice_cream['죠스바']=1200
ice_cream['월드콘']=1500
print(ice_cream)

ice={'메로나': 1000,'폴라포': 1200,'빵빠레': 1800,'죠스바': 1200, '월드콘': 1500}
print('메로나 가격: ', ice['메로나'])
print('죠스바 가격: ', ice['죠스바'])

ice['메로나']=2000
print(ice)

del ice['메로나']
print(ice)

icecream={'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나':1000}
icecream['누가바']
icecream['폴라포']

inventory={'메로나': [300, 30], '비비빅': [400, 3], '죠스바': [250, 100]}
print(inventory)
print(inventory['메로나'][0],'원')
print(inventory['비비빅'][1],'개')

inventory['월드콘']=[500,7]
print(inventory)

icecream={'탱크보이':1200, '폴라포':1200, '빵빠레':1800, '월드콘':1500, '메로나':1000}
name=list(icecream.keys())
print(name)
price=list(icecream.values())
print(price)

print(sum(icecream.values()))
print(sum(price))

icecream={'탱크보이':1200, '폴라포':1200, '빵빠레':1800, '월드콘':1500, '메로나':1000}
new_product={'팥빙수':2700, '아맛나':1000}
print(icecream)
icecream.update(new_product)
print(icecream)

keys=('apple', 'pear', 'peach')
vals=(300,250,400)
result=dict(zip(keys,vals))
print(result)

date=['09/05', '09/06', '09/07', '09/08', '09/09']
close_price=[10500, 10300, 10100, 10800, 11000]
close_table=dict(zip(date, close_price))
print(close_table)


### 파이썬 분기문
print(3==5)
print(3<5)

x=4
print(1<x<5)

print((3==3) and (4!=3))

print(3>=4)

if 4<3:
    print("Hello World")

if 4<3:
    print("Hello World")
else:
    print("Hi, there")

if True:
    print("1")
    print("2")
else:
    print("3")
print("4")

if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")

user=input("입력:")
print(user*2)

user=input("숫자를 입력하세요:")
print(int(user)+10)

num=input('숫자를 입력하세요:')
if int(num)%2==0:
    print('짝수')
else:
    print('홀수')

num=input('숫자를 입력하세요:')
if int(num)+20>255:
    print('출력값: 255')
else:
    print('출력값:', int(num)+20)

user=input('숫자를 입력하세요')
num=int(user)+20
if num>255:
    print('출력값: 255')
else:
    print('출력값:', num)

user=input('숫자를 입력하세요')
num=int(user)-20
if num<0:
    print('출력값: 0')
elif num>255:
    print('출력값: 255')
else:
    print('출력값:',num)

time=input('시간을 입력하세요 mm:ss ')
print(time)
if time[-2:]=="00":
    print(time[0:2],"시 정각 입니다")
else:
    print('정각이 아닙니다')

fruit=['사과', '포도', '홍시']
user=input("좋아하는 과일은? ")
if user in fruit:
    print("정답입니다")
else:
    print("오답입니다")

warn_investiment_list=['Microsoft', 'Google', 'Naver', 'Kakao', 'Samsung', 'LG']
user=input('투자 종목은? ')
if user in warn_investiment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

fruit={'봄':'딸기', '여름':'토마토', '가을':'사과'}
user=input('좋아하는 계절은? ')
if user in fruit:
    print("제가 좋아하는 계절은", user)
    print('정답입니다.')
else:
    print('오답입니다')

fruit={'봄':'딸기', '여름':'토마토', '가을':'사과'}
user=input('좋아하는 과일은? ')
if user in fruit.values():
    print('정답입니다.')
else:
    print('오답입니다.')

user=input('문자 하나를 입력하세요 ')
if user.islower():
    print(user.upper())
else:
    print(user.lower())

score=input('학점은? ')
if 0<=int(score)<=20:         # 앞에서 int(score)를 해주고, score만 쓰는게 효율적
    print('grade is E')
elif 21<=int(score)<=40:
    print('grade is D')
elif 41<=int(score)<=60:
    print('grade is C')
elif 61<=int(score)<=80:
    print('grade is B')
elif 81<=int(score)<=100:
    print('grade is A')
else:
    print('다시 입력하세요')

rate={'달러':1167, '엔':1.096, '유로':1268, '위안':171}
user=input('금액을 입력하세요. (금액_통화명) ')
num, currency = user.split(" ")
print(float(num)*rate[currency], '원')

user1=input('숫자1? ')
user2=input('숫자2? ')
user3=input('숫자3? ')
user1=int(user1)
user2=int(user2)
user3=int(user3)
if user1>user2 and user1>user3:
    print(user1)
elif user2>user1 and user2>user3:
    print(user2)
else:
    print(user3)

telecom={'011':'SKT','016':'KT', '019':'LGU', '010':'알수없음' }
user=input('전화번호를 입력하세요 ')
num=user[:3]
str(num)
print('당신은',telecom[num], '사용자입니다')

user=input('전화번호를 입력하세요 ')
num=user[:3]     # num=user.split("-")[0]
if num=='011':
    com='SKT'
elif num=='016':
    com='KT'
elif num=='019':
    com='LGU'
else:
    com='알수없음'
print(f'당신은 {com} 사용자입니다.')

우편번호=input('우편번호: ')
if 우편번호[:3] in ['010', '011', '012']:
    print('강북구')
elif 우편번호[:3] in ['013', '014', '015']:
    print('노원구')
elif 우편번호[:3] in ['016', '017', '018', '019']:
    print('노원구')
else:
    print('다시입력하세요')

주민등록번호=input('주민등록번호 : ')
주민번호=주민등록번호.split('-')[1]
뒷번호=주민번호[0]
if 뒷번호[0] in ['1', '3']:
    print('남자')
elif 뒷번호[0] in ['2','4']:
    print('여자')
else:
    print('다시입력하세요')
print(뒷번호)

주민등록번호=input('주민등록번호 : ')
주민번호=주민등록번호.split('-')[1]
지역번호=주민번호[1:3]
if 지역번호 in ['00', '01', '02', '03', '04', '05', '06', '07']:
    print('서울')
elif 지역번호 in ['09', '10', '11', '12']:
    print('부산')
else:
    print('타지역입니다.')

주민등록번호=input('주민등록번호 : ')
지역번호=int(주민번호[1:3])
if 0<=지역번호<=8:
    print('서울')
elif 9<=지역번호<=12:
    print('부산')
else:
    print('타지역입니다.')

주민등록번호=input('주민등록번호 : ')
주민번호=int(주민등록번호.replace('-',""))
print(주민번호)
계산1차=주민번호[0]*2+주민번호[1]*3+주민번호[2]*4+주민번호[3]*5+주민번호[4]*6+주민번호[5]*7+주민번호[6]*8+주민번호[7]*9+주민번호[8]*2+주민번호[9]*3+주민번호[10]*4+주민번호[11]*5
계산2차=11-(계산1차%11)

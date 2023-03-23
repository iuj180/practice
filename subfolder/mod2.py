#mod1.py
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

print(__name__)               # 다른 파일에서 mod1.py 파일을 import 할때 mod1 파일이름이 출력됨
if __name__ == "__main__":    # 내가 실행하는 파일에서만 실행됨 --> mod1.py 에서만 실행됨
    print(add(1,4))
    print(add(4,2))

# 패키지란? 모듈 여러개를 모아놓은것
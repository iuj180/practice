# Header (모듈 Import하는 작업)
import pygame, sys
from pygame.locals import*   # 유용한 상수들을 선언없이 사용하기 위해 필수 ex) quit, exit 등

# Initail 문 (무한반복문 이전 문장들, 전역변수 한번 초기화, 몇몇함수 한번 호출, 주로 색상같은 전역변수들)
white = (255,255,255)       # 색상 변수 선언
red = (255,0,0)             # 색상 변수 선언
green = (0,255,0)           # 색상 변수 선언
pygame.init()               # 나중에 사용할 함수를 위해 가장 앞서서 호출되어야 함
pygame.display.set_caption("Hello World Project")
myScreen = pygame.display.set_mode((640,480))                         # 캔버스 생성 (640 x 480 크기)
myTextFont = pygame.font.Font("HoonWhitecatR.ttf",32)                 # 해당 폰트로 32 크기로 설정
myText = myTextFont.render("Hello World!", True, red, green)          # render함수는 텍스트 내용과 색상을 정할수 있다
myTextArea = myText.get_rect()                                        # get_rect() 함수는 텍스트의 폰트 크기와 텍스트 크기 고려 적절한 직사각형 공간을 반환
myTextArea.center = (320, 240)

# Always 문 (무한반복문, 전역변수 계속 업데이트, 몇몇함수 계속 호출)
while True:
    myScreen.fill(white)                     # fill 함수는 캔버스를 단색으로 채우는 기능
    myScreen.blit(myText, myTextArea)        # blit 함수는 특정 객체를 특정 위치에 그리는 기능, blit이 fill 다음에 수행되어야 함

# Event 문 (모든 이벤트를 체크하는 반복문)
    for event in pygame.event.get():         # pygame.event.get() 함수는 Always문에서 발생한 이벤트들의 배열을 반환, 시간순으로 정렬
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()            # 일반적으로 다른 변수/함수의 처리가 끝난 이후에 호출, 처리의 결과물을 스크린에 출력하는 함수
                                       # 이함수가 Always 문 마지막에 실행되지 않으면, 출력되는 화면과 게임 내부 데이터가 서로 일치하지 않음


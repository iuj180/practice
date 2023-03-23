# Header (모듈 Import하는 작업)
import pygame, sys
from pygame.locals import*   # 유용한 상수들을 선언없이 사용하기 위해 필수 ex) quit, exit 등

# Initail 문 (무한반복문 이전 문장들, 전역변수 한번 초기화, 몇몇함수 한번 호출, 주로 색상같은 전역변수들)
maxHP = 10
white = (255,255,255)       # 색상 변수 선언
gray = (127, 127, 127)      # 색상 변수 선언
black = (0, 0, 0)           # 색상 변수 선언
red = (255,0,0)             # 색상 변수 선언
green = (0,255,0)           # 색상 변수 선언
blue = (0, 0, 255)          # 색상 변수 선언
pygame.init()               # 나중에 사용할 함수를 위해 가장 앞서서 호출되어야 함
pygame.display.set_caption("HP bar Project")
width = 640                 # 가로 길이 
height = 480                # 세로 길이
myScreen = pygame.display.set_mode((width, height))                     # 캔버스 생성 (width x height)
myTextFont = pygame.font.Font("HoonWhitecatR.ttf",32)                 # 해당 폰트로 32 크기로 설정
myText = myTextFont.render((str(maxHP) + "/" + str(maxHP)), True, red, white)          # render함수는 텍스트 내용과 색상을 정할수 있다
myTextArea = myText.get_rect()                                        # get_rect() 함수는 텍스트의 폰트 크기와 텍스트 크기 고려 적절한 직사각형 공간을 반환
myTextArea.center = (width/2, height/2)
fpsClock = pygame.time.Clock()                   # 게임이 시작되기 이전 속도를 고정시키는 기능

def main():                                      # Always 문과 Event문을 main 함수로 만듬
    HP = 5
    
    # Always 문 (무한반복문, 전역변수 계속 업데이트, 몇몇함수 계속 호출)
    while True:
        myText = myTextFont.render((str(HP) + "/" + str(maxHP)), True, red, gray)
        myScreen.fill (gray)                             # fill 함수는 캔버스를 단색으로 채우는 기능
        myScreen.blit(myText, myTextArea)                # blit 함수는 특정 객체를 특정 위치에 그리는 기능, blit이 fill 다음에 수행되어야 함
        drawHP(HP)

       # Event 문 (모든 이벤트를 체크하는 반복문)
        for event in pygame.event.get():                 # pygame.event.get() 함수는 Always문에서 발생한 이벤트들의 배열을 반환, 시간순으로 정렬
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:                  # KEYDOWN 은 키는 이전에는 눌리지 않았지만, 지금은 눌렸다 의미
                if event.key == K_UP:                    # 위로 가는 키 눌렀을 경우, 위로
                    if HP !=10:
                        HP = HP + 1
                elif event.key == K_DOWN:
                    if HP != 0:
                        HP = HP - 1
        pygame.display.update()                          # 일반적으로 다른 변수/함수의 처리가 끝난 이후에 호출, 처리의 결과물을 스크린에 출력하는 함수
                                                         # 이함수가 Always 문 마지막에 실행되지 않으면, 출력되는 화면과 게임 내부 데이터가 서로 일치하지 않음
        fpsClock.tick(60)                                # 1초에 화면이 60번 바뀌는 것 설정, tick 함수는 pygame.display.update()보다 나중에 나와야함
                                                         # tick 함수는 화면이 몇번 업데이트 되었는지 계산함

def drawHP(HP):                                                  # 새로운 함수 만듬
    r = int((height - 40) / maxHP)

    pygame.draw.rect(myScreen, black, (20, 20, 20, 20 + ((maxHP - 0.5) * r)))         # 큰 검은색 직사각형 그림
                                                                                      # pygame.draw.rect 함수에서 위치 변수로 4개의 매개변수 사용 (첫번째 캔버스 변수, 두번째 색상변수, 네번째 두께 변수)
    for i in range(maxHP):
        if HP >= (maxHP - i):
            pygame.draw.rect(myScreen, red, (20, 20 + (i * r), 20, r))                # 현재 HP를 따져서 작은 빨간색 직사각형을 0개 또는 최대 개수만큼 그림
        pygame.draw.rect(myScreen, white, (20, 20 + (i * r), 20, r), 1)               # 작은 직사각형들에 하얀 테두리 그림
    return

if __name__ == '__main__':                            # mian 함수를 프로그램이 찾을수 있도록 처리
    main()
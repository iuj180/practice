# Header (모듈 Import하는 작업)
import pygame, sys, random
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
pygame.display.set_caption("Array buttons Project")
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
    board, b_red, b_black = generateBoard(5, 5)
    
    # Always 문 (무한반복문, 전역변수 계속 업데이트, 몇몇함수 계속 호출)
    while True:
        myText = myTextFont.render((str(HP) + "/" + str(maxHP)), True, red, gray)
        myScreen.fill (gray)                             # fill 함수는 캔버스를 단색으로 채우는 기능
        myScreen.blit(myText, myTextArea)                # blit 함수는 특정 객체를 특정 위치에 그리는 기능, blit이 fill 다음에 수행되어야 함
        drawHP(HP)
        drawButtons()
        drawBoard(board)

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
            elif event.type == MOUSEBUTTONUP:                              # MOUSEBUTTNUP 마우스 버튼 눌렀을때 이벤트 시작
                x, y = event.pos                                           # 마우스 클릭 위치 좌표
                if pygame.Rect(270,425,45,45).collidepoint(x,y):           # 마우스를 클릭한 좌표와 설정한 좌표가 동일 위치면
                    if b_red >= b_black:
                        if HP != 10:
                            HP = HP + 1
                        board, b_red, b_black = generateBoard(10, 10)
                    elif b_red < b_black:
                        if HP != 0:
                            HP = HP - 1
                        board, b_red, b_black = generateBoard(10, 10)

                elif pygame.Rect (325,425, 45, 45).collidepoint(x, y):
                    if b_red <= b_black:
                        if HP != 0:
                            HP = HP + 1
                        board, b_red, b_black = generateBoard(10, 10)
                    elif b_red > b_black:
                        if HP != 0:
                            HP = HP - 1
                        board, b_red, b_black = generateBoard(10, 10)

        pygame.display.update()                          # 일반적으로 다른 변수/함수의 처리가 끝난 이후에 호출, 처리의 결과물을 스크린에 출력하는 함수
                                                         # 이함수가 Always 문 마지막에 실행되지 않으면, 출력되는 화면과 게임 내부 데이터가 서로 일치하지 않음
        fpsClock.tick(60)                                # 1초에 화면이 60번 바뀌는 것 설정, tick 함수는 pygame.display.update()보다 나중에 나와야함
                                                         # tick 함수는 화면이 몇번 업데이트 되었는지 계산함

def drawHP(HP):                                                                       # 새로운 함수 만듬 ; HP 박스 표현하기
    r = int((height - 40) / maxHP)

    pygame.draw.rect(myScreen, gray, (20, 20, 20, 20 + ((maxHP - 0.5) * r)))         # 큰 검은색 직사각형 그림
                                                                                      # pygame.draw.rect 함수에서 위치 변수로 4개의 매개변수 사용 (첫번째 캔버스 변수, 두번째 색상변수, 네번째 두께 변수)
    for i in range(maxHP):
        if HP >= (maxHP - i):
            pygame.draw.rect(myScreen, blue, (20, 20 + (i * r), 20, r))                # 현재 HP를 따져서 작은 빨간색 직사각형을 0개 또는 최대 개수만큼 그림
        pygame.draw.rect(myScreen, white, (20, 20 + (i * r), 20, r), 1)               # 작은 직사각형들에 하얀 테두리 그림
    return

def drawButtons():                                                                    # 버튼 (정사각형) 그리기
    r = 45
    r_margin = 10
    colors = [red, black]

    num = 2
    margin = int((width - ((r * num) + (r_margin * (num - 1)))) / 2)
    for i in range(0, num):
        left = margin + (i * r) + (i * r_margin)
        up = height - r - 10
        pygame.draw.rect(myScreen, colors[i], (left, up, r, r))                        # 정사각형 그리기
        pygame.draw.rect(myScreen, gray, (left + 2, up + 2, r - 4, r - 4), 2)

def generateBoard(width, height):                            # 무작위로 만들어진 2차원 배열과 빨간 블럭, 검은 블럭 개수를 반환
    board = []
    b_red = 0
    b_black = 0

    for x in range(width):
        column = []
        for y in range(height):
            column.append(random.randint(0,1))
        board.append(column)

    for x in range(width):
        for y in range(height):
            if (board[x][y] == 1):
                b_red = b_red + 1
            elif (board[x][y] == 0):
                b_black = b_black + 1
    
    return board, b_red, b_black

def drawBoard(board):
    r = 50
    b_width = 5
    b_height = 5
    l_margin = int((width - (b_width * r)) / 2)
    u_margin = int((height - (b_height * r)) / 2)

    for x in range(5):
        for y in range(5):
            left = x * r + l_margin
            up = y * r + u_margin
            if board[x][y] == 1:
                color = red
            elif board[x][y] == 0:
                color = black
            pygame.draw.rect(myScreen, color, (left, up, r, r))                 # pygame.draw.rect(Surface, color, Rect, width)
                                                                                # Rect[x축, y축, 가로, 세로] 형태, width 는 사각형 선의 크기 (기본 0 ; 채우기)
    left = l_margin
    up = u_margin
    pygame.draw.rect(myScreen, white, (left-1, up-1, r*5+1, r*b_height + 1), 1)


if __name__ == '__main__':                            # mian 함수를 프로그램이 찾을수 있도록 처리
    main()
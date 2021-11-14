#7조 모노폴리 파이썬 프로그래밍

import pygame as pg
import time


pg.init() #초기화

pg.mixer.init()
pg.display.init()
playlist = list()
playlist.append('first_bgmusic.mp3')

pg.mixer.music.load(playlist.pop())
pg.mixer.music.set_endevent(pg.USEREVENT)
pg.mixer.music.play()
player_number = 2
dollar = 2000

#화면 크기
screen_width = 800 # 가로크기
screen_height = 800 # 세로크기
screen = pg.display.set_mode((screen_width, screen_height))

#게임 폰트
game_font  = pg.font.Font(None, 60)

sunkual_font  = pg.font.Font(None, 80)






#화면 타이틀 설정
pg.display.set_caption("성결마블")


#이미지 불러오기
less_img = pg.image.load("left.png") #화살표 왼쪽
more_img = pg.image.load("right.png") #화살표 오른쪽

start_img = pg.image.load("start.png") # start 이미지





#버튼 클래스
class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        action = False
        #마우스 포지션
        pos = pg.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image,(self.rect.x, self.rect.y))

        return action






less_dollar_button = Button(460,360,less_img)
more_dollar_button = Button(660,360,more_img)

start_button = Button(320,500,start_img)





#이벤트 루프
running = True # 지속적인 게임 운영
while running:
    for event in pg.event.get():
        if event.type == pg.USEREVENT:
            if len(playlist) > 0:
                pg.mixer.music.queue(playlist.pop())
    
    screen.fill((0,0,0))
    

    if less_dollar_button.draw():
        dollar -= 100
        if dollar < 1500:
            dollar = 2500
    if more_dollar_button.draw():
        dollar += 100
        if dollar > 2500:
            dollar = 1500

    if start_button.draw():
        import board



    for event in pg.event.get():
        if event.type == pg.QUIT: #창종료로 인한 게임종료
            running = False # 반복문 탈출



    
    num2 = game_font.render(str(int(dollar)),True,(255,255,255))
    
    screen.blit(num2,(530,360))
    

    screen.blit((sunkual_font.render(("SUNGKYUAL MARVEL"),True,(150,150,0))),(110,50))
    screen.blit((game_font.render(("Player : 2"),True,(255,255,255))),(100,240))
    screen.blit((game_font.render(("Goal ASSET :    $"),True,(255,255,255))),(100,360))

    pg.display.update() #게임화면 다시 그리기       

#게임 종료
pg.quit()
###7조 모노폴리 파이썬 프로그래밍

from os import times
import pygame as pg
import random
import time

pg.init() #초기화

#화면 크기
screen_width = 1000 # 가로크기
screen_height = 800 # 세로크기
screen = pg.display.set_mode((screen_width, screen_height))

#배경이미지
background = pg.image.load("background.png")


# 캐릭터 불러오기
character1 = pg.image.load("C:/Users/changjo/Documents/GitHub/seeeeeeeeveeeeeen/character/car1.png")
character2 = pg.image.load("C:/Users/changjo/Documents/GitHub/seeeeeeeeveeeeeen/character/car2.png")
character3 = pg.image.load("C:/Users/changjo/Documents/GitHub/seeeeeeeeveeeeeen/character/car3.png")
character4 = pg.image.load("C:/Users/changjo/Documents/GitHub/seeeeeeeeveeeeeen/character/car4.png")

character1_size = character1.get_rect().size
character2_size = character2.get_rect().size
character3_size = character3.get_rect().size
character4_size = character4.get_rect().size

character1_width = character1_size[0]
character1_height = character1_size[1]
character2_width = character2_size[0]
character2_height = character2_size[1]
character3_width = character3_size[0]
character3_height = character3_size[1]
character4_width = character4_size[0]
character4_height = character4_size[1]

character1_x_pos = screen_width / 32
character1_y_pos = screen_height / 1.05
character2_x_pos = screen_width / 17
character2_y_pos = screen_height / 1.05
character3_x_pos = screen_width / 12
character3_y_pos = screen_height / 1.05
character4_x_pos = screen_width / 9.5
character4_y_pos = screen_height / 1.05

#주사위 위치
dice0= pg.image.load("C:/Users/changjo/Documents/GitHub/seeeeeeeeveeeeeen/dice/dice1.png")
dice1= pg.image.load("C:/Users/changjo/Documents/GitHub/seeeeeeeeveeeeeen/dice/dice2.png")
dice2= pg.image.load("C:/Users/changjo/Documents/GitHub/seeeeeeeeveeeeeen/dice/dice3.png")
dice3= pg.image.load("C:/Users/changjo/Documents/GitHub/seeeeeeeeveeeeeen/dice/dice4.png")
dice4= pg.image.load("C:/Users/changjo/Documents/GitHub/seeeeeeeeveeeeeen/dice/dice5.png")
dice5= pg.image.load("C:/Users/changjo/Documents/GitHub/seeeeeeeeveeeeeen/dice/dice6.png")

dice = [dice0,dice1,dice2,dice3,dice4,dice5]

#구매하기
buy = pg.image.load("C:/Users/changjo/Documents/GitHub/seeeeeeeeveeeeeen/buy.png")
#주사위 굴리기
roll = pg.image.load("C:/Users/changjo/Documents/GitHub/seeeeeeeeveeeeeen/roll.png")

#버튼
class button1():
    def __init__(self, x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pg.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                
                self.clicked = True
                action = True
                screen.blit(dice[random.randrange(0,6)],(550,370))
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


buy_button = button1(330,230,buy,1)
roll_button = button1(170,330,roll,1)


#화면 타이틀 설정
pg.display.set_caption("성결마블")

#글씨 표시
#player number
gulimfont = pg.font.SysFont('굴림', 30) # 서체 설정
playernumber = gulimfont.render('player1 : ' , 1, (255,255,255))  # .render() 함수에 내용과 안티앨리어싱, 색을 전달하여 글자 이미지 생성
playerrect = playernumber.get_rect() # 생성한 이미지의 rect 객체를 가져온다
playerrect.center = (screen_width / 1.12, screen_height / 16) # 해당 rect의 중앙을 화면 중앙에 맞춘다

#글씨 표시
#player number
playernumber1 = gulimfont.render('player2 : ' , 1, (255,255,255))  # .render() 함수에 내용과 안티앨리어싱, 색을 전달하여 글자 이미지 생성
playerrect1 = playernumber1.get_rect() # 생성한 이미지의 rect 객체를 가져온다
playerrect1.center = (screen_width / 1.12, screen_height *4/ 16) # 해당 rect의 중앙을 화면 중앙에 맞춘다

#글씨 표시
#player number
playernumber2 = gulimfont.render('player3 : ' , 1, (255,255,255))  # .render() 함수에 내용과 안티앨리어싱, 색을 전달하여 글자 이미지 생성
playerrect2 = playernumber2.get_rect() # 생성한 이미지의 rect 객체를 가져온다
playerrect2.center = (screen_width / 1.12, screen_height *7/ 16) # 해당 rect의 중앙을 화면 중앙에 맞춘다

#글씨 표시
#player number
playernumber3 = gulimfont.render('player4 : ' , 1, (255,255,255))  # .render() 함수에 내용과 안티앨리어싱, 색을 전달하여 글자 이미지 생성
playerrect3 = playernumber3.get_rect() # 생성한 이미지의 rect 객체를 가져온다
playerrect3.center = (screen_width / 1.12, screen_height*10 / 16) # 해당 rect의 중앙을 화면 중앙에 맞춘다

#winner goal asset
goalasset = gulimfont.render('goal asset : ', 1 , (255,255,255))  # .render() 함수에 내용과 안티앨리어싱, 색을 전달하여 글자 이미지 생성
assetrect = goalasset.get_rect() # 생성한 이미지의 rect 객체를 가져온다
assetrect.center = (screen_width/ 1.12, screen_height*6/8 +50)
import player
player.num2 = gulimfont.render(str(int(player.dollar)),True,(255,255,255))



#메인 루프

running = True
while running:

    if buy_button.draw():
        print("buy")
    if roll_button.draw():
        
        print('roll')
        
    for event in pg.event.get():
        if event.type == pg.QUIT: #창종료로 인한 게임종료
            running = False # 반복문 탈출

    screen.fill((0,0,0))
    screen.blit(background, (0,0)) #게임 배경 설정
    screen.blit(character1,(character1_x_pos,character1_y_pos))
    screen.blit(character2,(character2_x_pos,character2_y_pos))
    screen.blit(character3,(character3_x_pos,character3_y_pos))
    screen.blit(character4,(character4_x_pos,character4_y_pos))
        
        
        #if roll_button.draw() == True:
        #    screen.blit(dice[random.randrange(1,7)],(550,370))
    screen.blit(buy, (330,230))
    screen.blit(roll, (170,330))
    screen.blit(playernumber,playerrect)
    screen.blit(playernumber1,playerrect1)
    screen.blit(playernumber2,playerrect2)
    screen.blit(playernumber3,playerrect3)
    screen.blit(goalasset, assetrect)
    screen.blit(player.num2, (screen_width/ 1.12, screen_height*6/8+80))
    pg.display.update() #지속적으로 배경 표시


#게임 종료
pg.quit()
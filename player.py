#7조 모노폴리 파이썬 프로그래밍

import pygame as pg


pg.init() #초기화


player_number = 1

#화면 크기
screen_width = 980 # 가로크기
screen_height = 680 # 세로크기
screen = pg.display.set_mode((screen_width, screen_height))

#게임 폰트
game_font  = pg.font.Font(None, 60)





#화면 타이틀 설정
pg.display.set_caption("7조 모노폴리")

#버튼 불러오기
less_player_img = pg.image.load("C:/Users/changjo/Desktop/모노폴리/left.png")
more_player_img = pg.image.load("C:/Users/changjo/Desktop/모노폴리/right.png")


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


less_player_button = Button(300,240,less_player_img)
more_player_button = Button(400,240,more_player_img)




#이벤트 루프
running = True # 지속적인 게임 운영
while running:
    
    screen.fill((0,0,0))

    if less_player_button.draw(): 
        player_number-=1
    if more_player_button.draw():
        player_number+=1
    
    for event in pg.event.get():
        if event.type == pg.QUIT: #창종료로 인한 게임종료
            running = False # 반복문 탈출



    
    num = game_font.render(str(int(player_number)),True,(255,255,255))
    
    screen.blit(num,(360,240))
    screen.blit((game_font.render(("Player :"),True,(255,255,255))),(100,240))
    
    pg.display.update() #게임화면 다시 그리기       

#게임 종료
pg.quit()
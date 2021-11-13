#-*- coding utf-8 -*-
###7조 모노폴리 파이썬 프로그래밍

import pygame as pg
import random
import time



pg.init() #초기화


#FPS
clock = pg.time.Clock()

#화면 크기
screen_width = 1000 # 가로크기
screen_height = 800 # 세로크기
screen = pg.display.set_mode((screen_width, screen_height))

#배경이미지
background = pg.image.load("background.png")


# 캐릭터 불러오기
character1 = pg.image.load("character/car1.png")
character2 = pg.image.load("character/car2.png")
character3 = pg.image.load("character/car3.png")
character4 = pg.image.load("character/car4.png")





character1_x_pos = 5    
character1_y_pos = 770      
    
character2_x_pos = 35
character2_y_pos = 770

character3_x_pos = 65
character3_y_pos = 770

character4_x_pos = 95
character4_y_pos = 770

#주사위 위치
dice1= pg.image.load("dice/dice1.png")
dice2= pg.image.load("dice/dice2.png")
dice3= pg.image.load("dice/dice3.png")
dice4= pg.image.load("dice/dice4.png")
dice5= pg.image.load("dice/dice5.png")
dice6= pg.image.load("dice/dice6.png")

dice = [dice1,dice2,dice3,dice4,dice5,dice6]

#구매하기
buy = pg.image.load("buy.png")
#주사위 굴리기
roll = pg.image.load("roll.png")

#버튼
import player
buy_button = player.Button(330,230,buy)
roll_button = player.Button(170,330,roll)



#화면 타이틀 설정
pg.display.set_caption("성결마블")

#글씨 표시
gulimfont = pg.font.SysFont('굴림', 30) # 서체 설정




import player
player.num2 = gulimfont.render(str(int(player.dollar)),True,(255,255,255))





    

#30,137,244,351,458,565,672 (한칸에 107)
#765,653.5,542,430.5,319,207.5,96 (한칸에 111.5)


#맵 배열 
map = {0:(5,770), 1:(5,657), 2:(5,545), 3:(5,434), 4:(5,322), 5:(5,210), 6:(5,96), 
 7:(120,96), 8:(240,96), 9:(360,96), 10:(480,96), 11:(590,96), 12:(710,96), 
 13:(710,210), 14:(710,322), 15:(710,434), 16:(710,545), 17:(710,657), 18:(710,770), 
 19:(590,770), 20:(480,770), 21:(360,770), 22:(240,770), 23:(120,770)}


#맵 이름
map_name = ['출발','정문','흡연장','주차장','매점','식당','모인 학생회비 획득',
'풋살장','테니스장','운동장','카페','미소과 사무실','감옥',
'학사관리과','부속유치원','학술정보관','재림관','중생관','학생회비',
'학생회관','성결관','기념관','미소학과장실','총장실']

#땅 가격
map_price = [100,50,60,70,80,90,0,
             110,120,130,140,150,0,
             160,170,180,190,200,0,
             250,260,270,280,290]


#플레이어 좌표
character1_x_pos = 5    
character1_y_pos = 770      
    
character2_x_pos = 35
character2_y_pos = 770

character3_x_pos = 65
character3_y_pos = 770

character4_x_pos = 95
character4_y_pos = 770

#주사위 위치
dice_1= pg.image.load("dice/dice1.png")
dice_2= pg.image.load("dice/dice2.png")
dice_3= pg.image.load("dice/dice3.png")
dice_4= pg.image.load("dice/dice4.png")
dice_5= pg.image.load("dice/dice5.png")
dice_6= pg.image.load("dice/dice6.png")



#주사위 생성
dice = 0



#플레이어 재산
character1_asset = 1000
character2_asset = 1000
character3_asset = 1000
character4_asset = 1000


#플레이어가 가지고 있는 땅
character1_property = {}
character2_property = {}
character3_property = {}
character4_property = {}


# 현재 총 세금
total_tax = 0



# 주사위 결과에 따른 플레이어의 이동거리 계산
p1_move = 0
p2_move = 0
p3_move = 0
p4_move = 0


#감옥 가기
go_to_prison_1p = False
go_to_prison_2p = False
go_to_prison_3p = False
go_to_prison_4p = False


#다음 턴
turn = 1

#지금까지 총 턴
turn_number = 0
    
pg.display.init()
'''
pg.mixer.init()


playlists = list()
playlists.append('bg1.mp3')
playlists.append('bg2.mp3')
playlists.append('bg3.mp3')
playlists.append('bg4.mp3')

pg.mixer.music.load(playlists.pop())
pg.mixer.music.set_endevent(pg.USEREVENT)
pg.mixer.music.play()
'''
#메인 루프
running = True

while running:
    dt = clock.tick(10) #프레임 설정
    '''
        for events in pg.event.get():
            if events.type == pg.USEREVENT:
                if len(playlists) > 0:
                    pg.mixer.music.queue(playlists.pop())
        for events in pg.event.get():
            if events.type == pg.USEREVENT:
                if len(playlists) > 0:
                    pg.mixer.music.queue(playlists.pop())'''
    for event in pg.event.get():
         if event.type == pg.QUIT: #창종료로 인한 게임종료
            running = False # 반복문 탈출
            
    screen.fill((0,0,0))
    screen.blit(background, (0,0)) #게임 배경 설정
    
    if buy_button.draw():
        print("buy")

    
    
    if roll_button.draw():
        print("roll")
        dice = random.randint(1,6)

        
        #player 1 
        if turn==1:
              
            p1_move += dice
            if p1_move >= 24:
                p1_move -= 24
            
            if character1_asset < abs(map_price[p1_move]):
                if p1_move <= 0:
                    character1_asset = 0

                turn = 2    

            else:
                character1_x_pos = map[p1_move][0]
                character1_y_pos = map[p1_move][1]

                #감옥
                if go_to_prison_1p:
                    dice = 0
                    p1_move = 12 
                    prison_count_1p -= 1
                    

                    if prison_count_1p == 0:
                        go_to_prison_1p = False

                    character1_x_pos = map[p1_move][0]
                    character1_y_pos = map[p1_move][1]
                    
                elif p1_move == 12:
                    go_to_prison_1p = True
                    prison_count_1p = 2

                
                #학생회비
                elif p1_move == 18:
                    total_tax += character1_asset *3 / 100
                    character1_asset = character1_asset*97/100    
                
                #모인 학생회비 얻기
                elif p1_move == 6:
                    character1_asset += total_tax
                    total_tax = 0

                
                
                turn = 2
                    

    
           
        #player 2    
        elif turn == 2:
            p2_move += dice
            
            if p2_move >= 24:
                p2_move -= 24
            
            if character2_asset < abs(map_price[p2_move]):
                if p2_move <= 0:
                    character2_asset = 0

                turn = 1    

            else:
                character2_x_pos = map[p2_move][0]+30
                character2_y_pos = map[p2_move][1]

                #감옥
                if go_to_prison_2p:
                    dice = 0
                    p2_move = 12 
                    
                    prison_count_2p -= 1
                    
                    if prison_count_2p == 0:
                        go_to_prison_2p = False

                    character2_x_pos = map[p2_move][0]+30
                    character2_y_pos = map[p2_move][1]

                    

                elif p2_move == 12:
                    go_to_prison_2p = True
                    prison_count_2p = 2

                #학생회비
                elif p2_move == 18:
                    total_tax += character2_asset *3 / 100
                    character2_asset = character2_asset*97/100    
                
                #모인 학생회비 얻기
                elif p2_move == 6:
                    character2_asset += total_tax
                    total_tax = 0

                    
                
                
                
                
                turn_number +=1 #턴 횟수
                turn = 1 #player1으로
          

        if turn_number == 30: #30턴이 지나면 끝남
            break
        
        time.sleep(0.3) 
        
     
    
    
    if turn == 1: #player1 turn 폰트
        player1_turn = gulimfont.render(str("player1 turn"),True,(255,255,255))
        screen.blit(player1_turn,(810,770)) 
        
        
    
    elif turn == 2: #player2 turn 폰트
        
        player2_turn = gulimfont.render(str("player2 turn"),True,(255,255,255))
        screen.blit(player2_turn,(810,770))
        
        
        
    '''if player.player_number == 3:
            screen.blit(character1,(character1_x_pos,character1_y_pos))
            screen.blit(character2,(character2_x_pos,character2_y_pos))
            screen.blit(character3,(character3_x_pos,character3_y_pos))

        
        if player.player_number == 4:
            screen.blit(character1,(character1_x_pos,character1_y_pos))
            screen.blit(character2,(character2_x_pos,character2_y_pos))
            screen.blit(character3,(character3_x_pos,character3_y_pos))
            screen.blit(character4,(character4_x_pos,character4_y_pos))    
        '''

    #플레이어 위치
    screen.blit(character1,(character1_x_pos,character1_y_pos))    
    screen.blit(character2,(character2_x_pos,character2_y_pos))    
    
    #남은 턴 횟수
    total_turn = 30 - turn_number

    turn_num = gulimfont.render(str(int(total_turn)),True,(255,255,255))
    screen.blit(turn_num,(820,16))
    
    
    #플레이어가 가지고 있는 건물 
    player1 = gulimfont.render("player1 : ",True,(255,255,255))
    player2 = gulimfont.render("player2 : ",True,(255,255,255))
    player3 = gulimfont.render("player3 : ",True,(255,255,255))
    player4 = gulimfont.render("player4 : ",True,(255,255,255))
        
    screen.blit(player1,(850,16))
    screen.blit(player2,(850,156))
    screen.blit(player3,(850,306))
    screen.blit(player4,(850,456))
        
        

    #플레이어 우승목표 자산
    goal_asset = gulimfont.render("goal asset :   $",True,(255,255,255))

    screen.blit(goal_asset,(810,670))
    screen.blit(player.num2, (950,670))
        
        
        

        
    #플레이어 자산 표시
    player1_asset = player.game_font.render(('$'+str(int(character1_asset))),True,(0,0,0),(255,255,255))
    screen.blit(player1_asset,(270,535))

    player2_asset = player.game_font.render(('$'+str(int(character2_asset))),True,(0,0,0),(255,255,255))
    screen.blit(player2_asset,(420,535))


    # 모인 세금 표시
    total_tax1 = gulimfont.render(('total tax : $'+str(int(total_tax))),True,(255,255,255))
    screen.blit(total_tax1,(830, 600))
        

    #주사위 위치
    if dice == 1:
        screen.blit(dice_1, (550,380))
    elif dice == 2:
        screen.blit(dice_2, (550,380))
    elif dice == 3:
        screen.blit(dice_3, (550,380))
    elif dice == 4:
        screen.blit(dice_4, (550,380))
    elif dice == 5:
        screen.blit(dice_5, (550,380))
    elif dice == 6:
        screen.blit(dice_6, (550,380))




    pg.display.update() #지속적으로 배경 표시


    


#게임 종료
pg.quit()
#-*- coding utf-8 -*-
###7조 모노폴리 파이썬 프로그래밍

import pygame as pg
import random
import time
import numpy as np

from pygame import display



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
#턴 종료
end = pg.image.load("end.png")

#버튼
import player
buy_button = player.Button(330,230,buy)
roll_button = player.Button(170,330,roll)
end_buttom = player.Button(500,130,end)



#화면 타이틀 설정
pg.display.set_caption("성결마블")

#글씨 표시
gulimfont = pg.font.SysFont('굴림', 30) # 서체 설정
gulimmini = pg.font.SysFont('굴림', 18)
warnfont = pg.font.SysFont('굴림', 50)


player.num2 = gulimfont.render(str(int(player.dollar)),True,(255,255,255))





    

#30,137,244,351,458,565,672 (한칸에 107)
#765,653.5,542,430.5,319,207.5,96 (한칸에 111.5)


#맵 배열 
#[][2] 소유 여부 1: 1번플레이어 , 2: 2번블레이어, 3: 3번플레이어, 4: 4번플레이어, 0: 무소유 5: 구매 불가
map = {0:[5,770,5], 1:[5,657,0], 2:[5,545,0], 3:[5,434,0], 4:[5,322,0], 5:[5,210,0], 6:[5,96,5], 
 7:[120,96,0], 8:[240,96,0], 9:[360,96,0], 10:[480,96,0], 11:[590,96,0], 12:[710,96,5], 
 13:[710,210,0], 14:[710,322,0], 15:[710,434,0], 16:[710,545,0], 17:[710,657,0], 18:[710,770,5], 
 19:[590,770,0], 20:[480,770,0], 21:[360,770,0], 22:[240,770,0], 23:[120,770,0]}
#0,6,12,18 모서리


#map[][2] == 1
#맵 이름
map_name = ['출발','Enter','Smoking','Parking','Store','Restaurant','모인 학생회비 획득',
'Futsal','Tennis','PlayGround','Cafe','MisoOffice','감옥',
'AMD','Kindergarten','Library','JaeLim','Joong','학생회비',
'StudentHall','Sungkyul','GiNyeom','MisoBoss','MainBoss']

#땅 가격
map_price = [0,50,60,70,80,90,0,
             110,120,130,140,150,0,
             160,170,180,190,200,0,
             250,260,270,280,290]


#플레이어 좌표
character1_x_pos = 5    
character1_y_pos = 770      
    
character2_x_pos = 35
character2_y_pos = 770

#주사위 위치
dice_1= pg.image.load("dice/dice1.png")
dice_2= pg.image.load("dice/dice2.png")
dice_3= pg.image.load("dice/dice3.png")
dice_4= pg.image.load("dice/dice4.png")
dice_5= pg.image.load("dice/dice5.png")
dice_6= pg.image.load("dice/dice6.png")



#주사위 생성
dice = 0

winner = ''

#플레이어 재산
character1_asset = 1000
character2_asset = 1000



# 현재 총 세금
total_tax = 0

#목표 자산 도달 우승함수

    
# 주사위 결과에 따른 플레이어의 이동거리 계산
p1_move = 0
p2_move = 0


#감옥 가기
go_to_prison_1p = False
go_to_prison_2p = False

#반복
re = False

#다음 턴
turn = 1

#지금까지 총 턴
turn_number = 0

#bgm
pg.display.init()
pg.mixer.init()

playlists = list()
playlists.append('bg4.mp3')


pg.mixer.music.load(playlists.pop())
pg.mixer.music.set_endevent(pg.USEREVENT)
pg.mixer.music.play()




sum_1 = 0
sum_2 = 0
#메인 루프
running = True

while running:
    dt = clock.tick(10) #프레임 설정
    for events in pg.event.get():
        if events.type == pg.USEREVENT:
            if len(playlists) > 0:
                pg.mixer.music.queue(playlists.pop())
    
    for event in pg.event.get():
        if event.type == pg.QUIT: #창종료로 인한 게임종료
            running = False # 반복문 탈출
            
    screen.fill((0,0,0))
    screen.blit(background, (0,0)) #게임 배경 설정
    
    #소유한 땅
    player1_build = []
    player2_build = []

    player1_price = []
    player2_price = []

    for i in range(1,24):
        if map[i][2] == 1:
            player1_build.append(map_name[i])
            player1_price.append(map_price[i])
            
        if map[i][2] == 2:
            player2_build.append(map_name[i])
            player2_price.append(map_price[i])
            
    
    #주사위 굴리기
    if roll_button.draw():
        
        print("roll")
        dice = random.randint(1,6)
        
        
        #player 1 
        if turn==1:
              
            p1_move += dice
            if p1_move >= 24:
                p1_move -= 24
            
                #월급
                if p1_move == 0:
                    character1_asset += 100
                
                    character1_x_pos = map[p1_move][0]
                    character1_y_pos = map[p1_move][1]

                elif p1_move == 1:
                    if dice >= 2:
                        character1_asset += 100

                    character1_x_pos = map[p1_move][0]
                    character1_y_pos = map[p1_move][1]

                elif p1_move == 2:
                    if dice >= 3:
                        character1_asset += 100
                    
                    character1_x_pos = map[p1_move][0]
                    character1_y_pos = map[p1_move][1]
                elif p1_move == 3:
                    if dice >= 4:
                        character1_asset += 100
                    
                    character1_x_pos = map[p1_move][0]
                    character1_y_pos = map[p1_move][1]

                elif p1_move == 4:
                    if dice >= 5:
                        character1_asset += 100
                    
                    character1_x_pos = map[p1_move][0]
                    character1_y_pos = map[p1_move][1]

                elif p1_move == 5:
                    if dice == 6:
                        character1_asset += 100

                    character1_x_pos = map[p1_move][0]
                    character1_y_pos = map[p1_move][1]

            
            else:
                character1_x_pos = map[p1_move][0]
                character1_y_pos = map[p1_move][1]

                #감옥
                if go_to_prison_1p:
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
                    
                    if character1_asset >= player.dollar:
                        winner = 'Player1 is'
                        import ending
                        running = False
                    
                    if character2_asset >= player.dollar:
                        winner = 'Player2 is'
                        import ending
                        running = False

                
                elif (map[p1_move][0],map[p1_move][1] == character1_x_pos,character1_y_pos) and  (map[p1_move][2] == 2):
                    
                    character2_asset += map_price[p1_move]/2

                    if character1_asset >= player.dollar:
                        winner = 'Player1 is'
                        import ending
                        running = False
                    
                    if character2_asset >= player.dollar:
                        winner = 'Player2 is'
                        import ending
                        running = False
                    
                    if character1_asset >= map_price[p1_move]/2:
                        character1_asset -= map_price[p1_move]/2

                    elif character1_asset < map_price[p1_move]/2:
                        for l in range(0,24):
                            if map[l][2] == 1:
                                sum_1 += map_price[l]
                                if (sum_1 + character1_asset) < map_price[p1_move]/2:
                                    
                                    winner = 'player2  is'
                                    import ending
                                    running = False
                                
                                elif (sum_1 + character1_asset) >= map_price[p1_move]/2:
                                    character1_asset-=map_price[p1_move]/2
                                

                    
                        
                    
                        
                                            
                                        
                               

                
                        
                    
                        
                   
                    

    
           
        #player 2    
        elif turn == 2:
            p2_move += dice
            
            if p2_move >= 24:
                p2_move -= 24 

                #월급
                if p2_move == 0:
                    character2_asset += 100
                
                    character2_x_pos = map[p2_move][0]+30
                    character2_y_pos = map[p2_move][1]

                elif p2_move == 1:
                    if dice >= 2:
                        character2_asset += 100

                    character2_x_pos = map[p2_move][0]+30
                    character2_y_pos = map[p2_move][1]

                elif p2_move == 2:
                    if dice >= 3:
                        character2_asset += 100
                    
                    character2_x_pos = map[p2_move][0]+30
                    character2_y_pos = map[p2_move][1]
                
                elif p2_move == 3:
                    if dice >= 4:
                        character2_asset += 100
                    
                    character2_x_pos = map[p2_move][0]+30
                    character2_y_pos = map[p2_move][1]

                elif p2_move == 4:
                    if dice >= 5:
                        character2_asset += 100
                    
                    character2_x_pos = map[p2_move][0]+30
                    character2_y_pos = map[p2_move][1]

                elif p2_move == 5:
                    if dice == 6:
                        character2_asset += 100

                    character2_x_pos = map[p2_move][0]+30
                    character2_y_pos = map[p2_move][1]
            
            
            else:
                character2_x_pos = map[p2_move][0]+30
                character2_y_pos = map[p2_move][1]

                #감옥
                if go_to_prison_2p:
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
               
                    
                elif (map[p2_move][0]+30,map[p2_move][1] == character2_x_pos,character2_y_pos) and  (map[p2_move][2] == 1):
                    
                    character1_asset += map_price[p2_move]/2

                    if character1_asset >= player.dollar:
                        winner = 'Player1 is'
                        import ending
                        running = False
                    
                    if character2_asset >= player.dollar:
                        winner = 'Player2 is'
                        import ending
                        running = False
                    
                    
                    
                    if character2_asset >= map_price[p2_move]/2:
                        character2_asset -= map_price[p2_move]/2

                    elif character2_asset < map_price[p2_move]/2:
                        for l in range(0,24):
                            if map[l][2] == 2:
                                sum_2 += map_price[l]
                                if (sum_2 + character2_asset) < map_price[p2_move]/2:
                                    
                                    winner = 'player1  is'
                                    import ending
                                    running = False
                                
                                elif (sum_2 + character2_asset) >= map_price[p2_move]/2:
                                    character2_asset-=map_price[p2_move]/2
                        
                
                                        
                        
                        
                
             
        time.sleep(0.3)
        

        
        
        
    
    #구매 버튼
    if buy_button.draw():
        print("buy")

        #player 1
        if turn == 1:
            for i in range(0,24):               #map[땅 숫자][2] 소유 여부  0: 무소유 1: 1번플레이어 , 2: 2번블레이어, 5: 구매 불가
                    
                    #플레이어 자산이 땅가격보다 낮을 때
                if (character1_asset < map_price[i] )and map[i][2] == 0:
                    
                    no = warnfont.render("You don't have enough money!",True,(255,255,255),(0,0,0))
                    screen.blit(no,(185,465))
                    

                    pg.display.update()
                    pg.time.delay(1500)
                    
                    break

                #무소유일 경우 구매   
                elif (character1_x_pos,character1_y_pos) == (map[i][0],map[i][1]) and map[i][2] == 0:
                    character1_asset -= map_price[i]
                    
                    yes = warnfont.render("Complete!",True,(255,255,255),(0,0,0))
                    screen.blit(yes,(300,465))
                        
                    map[i][2] = 1
                        
                    pg.display.update()
                    pg.time.delay(1500)

                    break

                #이미 소유한 땅일 경우 경고 출력
                elif (character1_x_pos,character1_y_pos) == (map[i][0],map[i][1]) and map[i][2] != 0 :

                    warn = warnfont.render("You can't buy this place!",True,(255,255,255),(0,0,0))
                    screen.blit(warn,(185,465))

                    pg.display.update()
                    pg.time.delay(1500) 

                    break  
        
        
        #player 2
        if turn == 2:
            for i in range(0,24):               #map[땅 숫자][2] 소유 여부  0: 무소유 1: 1번플레이어 , 2: 2번블레이어, 5: 구매 불가
                    
                    #플레이어 자산이 땅가격보다 낮을 때
                if (character2_asset < map_price[i] )and map[i][2] == 0:
                    
                    no = warnfont.render("You don't have enough money!",True,(255,255,255),(0,0,0))
                    screen.blit(no,(185,465))
                    

                    pg.display.update()
                    pg.time.delay(1500)
                    break

                #무소유일 경우 구매   
                elif (character2_x_pos,character2_y_pos) == (map[i][0]+30,map[i][1]) and map[i][2] == 0:
                    character2_asset -= map_price[i]
                    
                    yes = warnfont.render("Complete!",True,(255,255,255),(0,0,0))
                    screen.blit(yes,(300,465))
                        
                    map[i][2] = 2
                        
                    pg.display.update()
                    pg.time.delay(1500)

                    break

                #이미 소유한 땅일 경우 경고 출력
                elif (character2_x_pos,character2_y_pos) == (map[i][0]+30,map[i][1]) and map[i][2] != 0 :

                    warn = warnfont.render("You can't buy this place!",True,(255,255,255),(0,0,0))
                    screen.blit(warn,(185,465))

                    pg.display.update()
                    pg.time.delay(1500) 

                    break   
                
                
                    

    

    
    
    
    #턴 종료 
    if end_buttom.draw():
            if turn == 1:
                turn = 2
            else:
                turn = 1
                turn_number +=1 #턴 횟수
            if total_turn == 1: #30턴이 지나면 끝남
                if character1_asset > character2_asset:
                    winner = 'Player1 is'
                    import ending
                elif character2_asset > character1_asset:
                    winner = 'Player2 is'
                    import ending
                else:
                    winner = 'Both are'
                    import ending
    
    
        
     
    
    
    if turn == 1: #player1 turn 폰트
        player1_turn = gulimfont.render(str("player1 turn"),True,(220,0,0))
        screen.blit(player1_turn,(130,130)) 
        
        
    
    elif turn == 2: #player2 turn 폰트
        
        player2_turn = gulimfont.render(str("player2 turn"),True,(255,255,0))
        screen.blit(player2_turn,(130,130))
        
        

    #플레이어 위치
    screen.blit(character1,(character1_x_pos,character1_y_pos))    
    screen.blit(character2,(character2_x_pos,character2_y_pos))    
    
    
    #남은 턴 횟수
    total_turn = 30 - turn_number

    turn_num = gulimfont.render(str(int(total_turn)),True,(255,255,255))
    screen.blit(turn_num,(820,16))
    
    

    #플레이어 남은 돈
    player1 = gulimfont.render("player1 : ",True,(255,255,255))
    screen.blit(player1,(850,16))

    player2 = gulimfont.render("player2 : ",True,(255,255,255))
    screen.blit(player2,(850,156))

    #플레이어 자산 표시
    player1_asset = player.game_font.render(('$'+str(int(character1_asset))),True,(255,255,255))
    screen.blit(player1_asset,(850,50))

    player2_asset = player.game_font.render(('$'+str(int(character2_asset))),True,(255,255,255))
    screen.blit(player2_asset,(850,190))

    
    
    #플레이어가 가지고 있는 건물 
    player1_b =  gulimmini.render(("Player1"),True,(200,0,0)) 
    screen.blit(player1_b,(150,525))
    
    player1_bd = gulimmini.render(str(player1_build),True,(255,255,255)) 
    screen.blit(player1_bd,(150,550))
    
    
    player2_b =  gulimmini.render(("Player2"),True,(255,255,0)) 
    screen.blit(player2_b,(150,590))
    
    player2_bd = gulimmini.render(str(player2_build),True,(255,255,255))
    screen.blit(player2_bd,(150,615))
    


        
    
    
    # 모인 세금 표시
    total_tax1 = gulimfont.render(('total tax : $'+str(int(total_tax))),True,(255,255,255))
    screen.blit(total_tax1,(830, 600))    
        

    #플레이어 우승목표 자산
    goal_asset = gulimfont.render("goal asset :   $",True,(255,255,255))

    screen.blit(goal_asset,(810,670))
    screen.blit(player.num2, (950,670))
        
        
    #부동산 표시
    estate = player.game_font.render("Player's estates",True,(0,0,0),(255,255,255))
    screen.blit(estate,(250,465))
       
    


    
        

    #주사위 위치
    if dice == 1:
        screen.blit(dice_1, (500,330))
    elif dice == 2:
        screen.blit(dice_2, (500,330))
    elif dice == 3:
        screen.blit(dice_3, (500,330))
    elif dice == 4:
        screen.blit(dice_4, (500,330))
    elif dice == 5:
        screen.blit(dice_5, (500,330))
    elif dice == 6:
        screen.blit(dice_6, (500,330))





    pg.display.update() #지속적으로 배경 표시


    


#게임 종료
pg.quit()

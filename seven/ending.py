#-*- coding utf-8 -*-
###7조 모노폴리 파이썬 프로그래밍

import pygame as pg

pg.init() #초기화


#화면 타이틀 설정
pg.display.set_caption("Congratulations!!")

#글씨 표시
gulimfont = pg.font.SysFont('굴림', 30) # 서체 설정

#화면 크기
screen_width = 800# 가로크기
screen_height = 800 # 세로크기
screen = pg.display.set_mode((screen_width, screen_height))

running = True # 지속적인 게임 운영
while running:
    
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT: #창종료로 인한 게임종료
            running = False # 반복문 탈출
    import board
    win = gulimfont.render(board.winner,True, (255,255,255))
    ending_ment = gulimfont.render(' ! winner !',True,(255,0,0))
    screen.blit(ending_ment,(450,385))
    screen.blit(win,(270,385))

    pg.display.update() #지속적으로 배경 표시


    


#게임 종료
pg.quit()         
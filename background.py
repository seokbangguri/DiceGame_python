#-*- coding utf-8 -*-
###7조 모노폴리 파이썬 프로그래밍

import pygame as pg
import random

pg.init() #초기화

#화면 크기
screen_width = 800 # 가로크기
screen_height = 800 # 세로크기
screen = pg.display.set_mode((screen_width, screen_height))

#배경이미지
background = pg.image.load("/Users/hongseogjin/Desktop/monopoly/background.png")


# 캐릭터 불러오기
character1 = pg.image.load("/Users/hongseogjin/Desktop/monopoly/character/car1.png")
character2 = pg.image.load("/Users/hongseogjin/Desktop/monopoly/character/car2.png")
character3 = pg.image.load("/Users/hongseogjin/Desktop/monopoly/character/car3.png")
character4 = pg.image.load("/Users/hongseogjin/Desktop/monopoly/character/car4.png")

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

character1_x_pos = screen_width / 5
character1_y_pos = screen_height / 4
character2_x_pos = screen_width / 5
character2_y_pos = screen_height / 4
character3_x_pos = screen_width / 5
character3_y_pos = screen_height / 4
character4_x_pos = screen_width / 5
character4_y_pos = screen_height / 4

#화면 타이틀 설정
pg.display.set_caption("성결마블")

#이벤트 루프
running = True # 지속적인 게임 운영
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT: #창종료로 인한 게임종료
            running = False # 반복문 탈출
            
    screen.blit(background, (0,0)) #게임 배경 설정
    pg.display.update() #지속적으로 배경 표시


#게임 종료
pg.quit()
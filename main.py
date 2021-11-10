#7조 모노폴리 파이썬 프로그래밍

import pygame as pg
import random

pg.init() #초기화

#화면 크기
screen_width = 980 # 가로크기
screen_height = 680 # 세로크기
pg.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pg.display.set_caption("7조 모노폴리")

#이벤트 루프
running = True # 지속적인 게임 운영
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT: #창종료로 인한 게임종료
            running = False # 반복문 탈출
                

#게임 종료
pg.quit()
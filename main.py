import pygame
import sys
import random
import math
from time import time
from pygame.locals import *
from back import Back           #　背景用スプライト
from player import Player       #　主人公用スプライト
from enemy01 import Enemy01           #　敵一号用スプライト
from enemy02 import Enemy02           #　敵二号
from shot import Shot           #　ショット用スプライト
from display import Display          #　ショット用スプライト
from lock import Lock
from move import Move
from motion import Motion
from boss import Boss
from beacon import Beacon
from shot2 import Shot2 
from random import choice
from pygame import mixer
from mob import Mob

img_bg = pygame.image.load("./image/bgimage.png")
img_player = pygame.image.load("./image/player1.png")
img_weapon = pygame.image.load("./image/bullet.png")
img_weapon2g = pygame.image.load("./image/bullet.png")
img_weapon3g = pygame.image.load("./image/bullet.png")
img_weapon4g = pygame.image.load("./image/bullet.png")
img_weapon5g = pygame.image.load("./image/bullet.png")
img_weapon2 = pygame.transform.rotozoom(img_weapon2g,60,1)
img_weapon3 = pygame.transform.rotozoom(img_weapon3g,-60,1)
img_weapon4 = pygame.transform.rotozoom(img_weapon4g,70,1)
img_weapon5 = pygame.transform.rotozoom(img_weapon5g,70,1)
img_enemy = [
    pygame.image.load("./image/enemy1.png"),   #敵画像
    pygame.image.load("./image/e_bullet.png")  #敵の攻撃弾画像
]
img_item = [
    pygame.image.load("./image/star.png")
]
img_explode = [
    None,
    pygame.image.load("./image/explode1.png"),
    pygame.image.load("./image/explode2.png"),
    pygame.image.load("./image/explode3.png"),
    pygame.image.load("./image/explode4.png"),
    pygame.image.load("./image/explode5.png"),
    pygame.image.load("./image/explode6.png"),
    pygame.image.load("./image/explode7.png")
]
img_item_2 = [
    pygame.image.load("./image/time.png")
]
img_gauge = pygame.image.load("./image/gauge.png")#体力ゲージ
back05 = pygame.image.load("./image/back01.png")
WHITE = (255,255,255)
bg_y = 0
px = 320 #プレイヤーのX座標
py = 400 #プレイヤーのY座標
bx = 0 #弾のX座標
by = 0 #弾のY座標
t = 0 #タイマー変数
gtime = time()
gtime2 = 0
gtime3 = 0
space = 0
score = 0

# 主人公の弾の設定
p_speed = 10 
BULLET_MAX = 100 #弾の最大値
BULLET_MAX2 = 100
BULLET_MAX3 = 100  #弾の最大値

ENEMY_MAX = 100  #敵の最大数
ITEM_MAX = 100
ENEMY_BULLEET = 1
bull_n = 0
bull_n2 = 0
bull_n3 = 0
bull_x =[0]*BULLET_MAX
bull_y =[0]*BULLET_MAX
bull_f =[False]*BULLET_MAX
bull_f2 =[False]*BULLET_MAX
bull_f3 =[False]*BULLET_MAX
bull_x2 =[0]*BULLET_MAX2
bull_y2 =[0]*BULLET_MAX2
bull_x3 =[0]*BULLET_MAX3
bull_y3 =[0]*BULLET_MAX3

SHOT1 = False
SHOT2 = False
SHOT3 = False
S1 = False
S2 = False
S3 = False
S4 = False

# エネミーの設定
ebull_n = 0
ebull_x = [0]*ENEMY_MAX
ebull_y = [0]*ENEMY_MAX
ebull_a = [0]*ENEMY_MAX
ebull_f =[False]*ENEMY_MAX
ebull_f2 = [False]*ENEMY_MAX
e_list = [0]*ENEMY_MAX
e_speed = [0]*ENEMY_MAX
e_life = [0]*ENEMY_MAX

# アイテムの設定
ibull_n = 0
ibull_x = [0]*ITEM_MAX
ibull_y = [0]*ITEM_MAX
ibull_a = [0]*ITEM_MAX
ibull_f =[False]*ITEM_MAX
ibull_f2 = [False]*ITEM_MAX
i_list = [0]*ITEM_MAX
i_speed = [0]*ITEM_MAX

# アイテムの設定2
ibull_n_1 = 0
ibull_x_1 = [0]*ITEM_MAX
ibull_y_1 = [0]*ITEM_MAX
ibull_a_1 = [0]*ITEM_MAX
ibull_f_1 =[False]*ITEM_MAX
ibull_f2_1 = [False]*ITEM_MAX
i_list_1 = [0]*ITEM_MAX
i_speed_1 = [0]*ITEM_MAX

# エフェクトの設定
EFFECT_MAX = 100     #エフェクトの最大数
e_n = 0
e_l = [0]*EFFECT_MAX
e_x = [0]*EFFECT_MAX #エフェクトのX座標
e_y = [0]*EFFECT_MAX #エフェクトのY座標

p_gauge = 100        #HP
enelgy_count = 0
p_invincible = 0     #無敵状態を管理する

idx = 0#インデックス（ゲーム状態を管理する）

def main():
    title_1 = True
    ranking_1 = False
    main_1 = False
    main_5 = False
    choice = False
    secret = False
    wa = 0
    score_list = []
    m_x,m_y = 288,288
    nomber = 0
    score_y = 32
    score_x = 32
    life_5 = 3
    time_5 = 30
    count_5 = 0
    title = pygame.image.load("./image/title.png")
    lock = Lock("./image/lock-on2.png",m_x,m_y)
    back = Back("./image/back01.png")
    #blue = ["./image/player1_1.png","./image/player2_2.png"]
    #player = Player(blue, -20, 240)
    fire = ["./image/enemy_5.png","./image/enemy_5.png"]
    enemy1list = []
    for i in range(3):
        enemy01 = Enemy01(fire, -64, 288)
        enemy1list.append(enemy01)
    shotlist = []
    for i in range(30):
        shot = Shot("./image/shot01.png",-64,-64)
        shotlist.append(shot)
    life_image1 = Display("./image/life01.png", 0, 0)
    life_image2 = Display("./image/life01.png", 64, 0)
    life_image3 = Display("./image/life01.png", 128, 0)

    global t,bg_y,idx,score,p_gauge,p_gauge02,p_invincible,px,py
    pygame.init()
    pygame.display.set_caption("Betoronome")
    screen = pygame.display.set_mode((640,480))
    clock = pygame.time.Clock()

    group_5 = pygame.sprite.Group()
    group_5_1 = pygame.sprite.Group()
    group_5.add(back)
    for enemy01 in enemy1list:
        group_5.add(enemy01)
    for shot in shotlist:
        group_5.add(shot)
    group_5_1.add(lock)

    B_x,B_y = 832,288
    group_5_sh = pygame.sprite.Group()
    group_5_im = pygame.sprite.Group()
    group_5_be = pygame.sprite.Group()
    barrier = Lock("./image/shield.png",-640,-640)
    beam = Motion("./image/beam.png",B_x,B_y)
    warninglist = ["./image/image_5.png","./image/image_5_2.png"]
    warning = Move(warninglist,-640,-640)
    group_5_sh.add(barrier)
    group_5_im.add(warning)
    group_5_be.add(beam)
    beamcount = 0
    shieldcount = 0
    shieldcount2= 0
    shieldcount3 = 0
    warningcount = 0
    num2 = 0
    timecount = 0
    addcount = 0

    life_group3 = pygame.sprite.Group()
    life_group2 = pygame.sprite.Group()
    life_group1 = pygame.sprite.Group()
    life_group3.add(life_image1)
    life_group3.add(life_image2)
    life_group3.add(life_image3)
    life_group2.add(life_image1)
    life_group2.add(life_image2)
    life_group1.add(life_image1)

    player_1 = pygame.image.load("./image/player1_choice.png")
    player_2 = pygame.image.load("./image/player2_choice.png")
    player_3 = pygame.image.load("./image/player3_choice.png")

    ship_5 = ["./image/ship_5.png","./image/ship_5.png"]
    shiplist = []
    for i in range(2):
        ship01 = Enemy02(ship_5, -64, 288)
        shiplist.append(ship01)
    group_5_ship = pygame.sprite.Group()
    for ship01 in shiplist:
        group_5_ship.add(ship01)

    font_5 = pygame.font.SysFont("msgothicmsuigothicmspgothic",30, bold = True)
    #font_5 = pygame.font.SysFont("msgothic",30, bold = True)
    font_boss = pygame.font.SysFont("msgothicmsuigothicmspgothic",20, bold = True)

    bulletcount = 0

    chain = pygame.image.load("./image/chain.png")
    chaincount = 0
    chain1  = 0
    chain2  = 0
    chain3  = 0
    chain4  = 0

    # 音楽の設定
    music =  [
        "./music/dance.mp3",
        "./music/yokoku.mp3",
        "./music/run.mp3",
        "./music/newspaper.mp3",
        "./music/digitalworld.mp3",
        "./music/dawnofwar.mp3",
        "./music/gameover.mp3",  
    ]
    mixer.music.load(music[0])
    mixer.music.set_volume(0.5) #音量
    mixer.music.play() 

    boss_bg = pygame.image.load("./image/boss_bg.png")
    group_se_pl = pygame.sprite.Group()
    group_se_bo = pygame.sprite.Group()
    group_se_be = pygame.sprite.Group()
    group_se_mob1 = pygame.sprite.Group()
    group_se_mob2 = pygame.sprite.Group()
    group_se_mob3 = pygame.sprite.Group()
    shotlist = []
    for i in range(12):
        shot = Shot("./image/shot01.png",-64,-64)
        shotlist.append(shot)
    for shot in shotlist:
        group_se_pl.add(shot)
    player = ["./image/player_boss.png","./image/player_boss.png"]
    player = Player(player, 288, 416)
    group_se_pl.add(player)
    mutekitime = 0
    for shot in shotlist:
        group_se_pl.add(shot)
    bosslevel = 0
    boss_shotlist = []
    boss_shotlist1 = []
    boss_shotlist2 = []
    for i in range(30):
        shot = Shot2("./image/boss_shot.png",-64,-64,32,32,8)
        boss_shotlist.append(shot)
    for shot in boss_shotlist:
        group_se_bo.add(shot)
    boss = ["./image/boss0_1.png","./image/boss0_2.png"]
    boss = Boss(boss, 230, -128,10,64,64,4,10)
    group_se_bo.add(boss)
    beaconlist = []
    beacon = ("./image/beacon.png")
    beacon1 = Beacon(beacon,boss.rect.x - 16 - 16,boss.rect.y + 64 - 16)
    beacon2 = Beacon(beacon,boss.rect.x + 64 - 16,boss.rect.y - 16 - 16)
    beacon3 = Beacon(beacon,boss.rect.x + 144 - 16,boss.rect.y + 64 - 16)
    beacon4 = Beacon(beacon,boss.rect.x + 64 - 16,boss.rect.y + 144 - 16)
    group_se_be.add(beacon1)
    group_se_be.add(beacon2)
    group_se_be.add(beacon3)
    group_se_be.add(beacon4)
    mob1 = ["./image/mob1.png","./image/mob1.png"]
    mob1list = []
    for i in range(2):
        mob01 = Mob(mob1,700,288,32,32,6,40)
        mob1list.append(mob01)
    for mob01 in mob1list:
        group_se_mob1.add(mob01)
    mob2 = ["./image/mob2.png","./image/mob2.png"]
    mob2list = []
    for i in range(2):
        mob02 = Mob(mob2,700,288,32,32,8,40)
        mob2list.append(mob02)
    for mob02 in mob2list:
        group_se_mob2.add(mob02)
    mob3 = ["./image/mob3.png","./image/mob3.png"]
    mob3list = []
    for i in range(3):
        mob03 = Mob(mob3,700,288,32,32,12,40)
        mob3list.append(mob03)
    for mob03 in mob3list:
        group_se_mob3.add(mob03)
    shotlist_m1 = []
    for i in range(2):
        shot = Shot2("./image/mob_bull.png",-64,-64,16,16,8)
        shotlist_m1.append(shot)
    for shot in shotlist_m1:
        group_se_mob1.add(shot)
    shotlist_m2 = []
    for i in range(4):
        shot = Shot2("./image/mob_bull.png",-64,-64,16,16,12)
        shotlist_m2.append(shot)
    for shot in shotlist_m2:
        group_se_mob2.add(shot)
    shotlist_m3 = []
    for i in range(6):
        shot = Shot2("./image/mob_bull.png",-64,-64,16,16,16)
        shotlist_m3.append(shot)
    for shot in shotlist_m3:
        group_se_mob3.add(shot)

    stage = "No"

    bulletspeed = 32

    count_bo = 0
    time_bo = 60
    clearscore = 500
    boss_score = 0
    scroll_y = 0
    score_count = 0
    score_count2 = 0
    score_judge = "YES"

    while True:
        while title_1:
            img_bg = pygame.image.load("./image/bgimage.png")
            img_player = pygame.image.load("./image/player1.png")
            img_weapon = pygame.image.load("./image/bullet.png")
            img_weapon2g = pygame.image.load("./image/bullet.png")
            img_weapon3g = pygame.image.load("./image/bullet.png")
            img_weapon4g = pygame.image.load("./image/bullet.png")
            img_weapon5g = pygame.image.load("./image/bullet.png")
            img_weapon2 = pygame.transform.rotozoom(img_weapon2g,20,1)
            img_weapon3 = pygame.transform.rotozoom(img_weapon3g,-20,1)
            img_weapon4 = pygame.transform.rotozoom(img_weapon4g,-50,1)
            img_weapon5 = pygame.transform.rotozoom(img_weapon5g,50,1)
            img_enemy = [
                pygame.image.load("./image/enemy1.png"),   #敵画像
                pygame.image.load("./image/e_bullet.png")  #敵の攻撃弾画像
            ]
            img_explode = [
                None,
                pygame.image.load("./image/explode1.png"),
                pygame.image.load("./image/explode2.png"),
                pygame.image.load("./image/explode3.png"),
                pygame.image.load("./image/explode4.png"),
                pygame.image.load("./image/explode5.png"),
                pygame.image.load("./image/explode6.png"),
                pygame.image.load("./image/explode7.png")
            ]
            img_gauge = pygame.image.load("./image/gauge.png")#体力ゲージ
            img_gauge02 = pygame.image.load("./image/gauge02.png")#体力ゲージ
            back05 = pygame.image.load("./image/back01.png")
            WHITE = (255,255,255)
            bg_y = 0
            px = 320 #プレイヤーのX座標
            py = 400 #プレイヤーのY座標
            bx = 0 #弾のX座標
            by = 0 #弾のY座標
            t = 0 #タイマー変数
            space = 0
            score = 0

            BULLET_MAX = 100 #弾の最大値
            BULLET_MAX2 = 100 #弾の最大値
            BULLET_MAX3 = 100 #弾の最大値

            ENEMY_MAX = 100  #敵の最大数
            ENEMY_BULLEET = 1

            # 弾の設定
            bull_n = 0
            bull_n2 = 0
            bull_n3 = 0
            bull_x =[0]*BULLET_MAX
            bull_y =[0]*BULLET_MAX
            bull_x2 =[0]*BULLET_MAX2
            bull_y2 =[0]*BULLET_MAX2
            bull_x3 =[0]*BULLET_MAX3
            bull_y3 =[0]*BULLET_MAX3
            bull_f =[False]*BULLET_MAX
            bull_f2 =[False]*BULLET_MAX
            bull_f3 =[False]*BULLET_MAX
            b_speed = 12
            bullets = 5
            beam1 = 2

            # エネミーの設定
            ebull_n = 0
            ebull_x = [0]*ENEMY_MAX
            ebull_y = [0]*ENEMY_MAX
            ebull_a = [0]*ENEMY_MAX
            ebull_f =[False]*ENEMY_MAX
            ebull_f2 = [False]*ENEMY_MAX
            e_list = [0]*ENEMY_MAX
            e_speed = [0]*ENEMY_MAX
            e_life = [0]*ENEMY_MAX

            # エフェクトの設定
            EFFECT_MAX = 100     #エフェクトの最大数
            e_n = 0
            e_l = [0]*EFFECT_MAX
            e_x = [0]*EFFECT_MAX #エフェクトのX座標
            e_y = [0]*EFFECT_MAX #エフェクトのY座標

            p_gauge = 100        #HP
            p_gauge02 = 0      #エネルギー
            enelgy_count = 0
            p_invincible = 0     #無敵状態を管理する

            idx = 0#インデックス（ゲーム状態を管理する）

            def set_bullet():    #弾のスタンバイ
                global bull_n
                bull_f[bull_n] = True
                bull_x[bull_n] = px-8
                bull_y[bull_n] = py-16
                bull_n = (bull_n+1)%BULLET_MAX

            def set_bullet1_2():    #弾のスタンバイ
                global bull_n
                bull_f[bull_n] = True
                bull_f2[bull_n] = True
                bull_x[bull_n] = px+3
                bull_y[bull_n] = py-16
                bull_x2[bull_n] = px-15
                bull_y2[bull_n] = py-16
                bull_n = (bull_n+1)%BULLET_MAX

            def set_bullet2():    #弾のスタンバイ
                global bull_n
                bull_f[bull_n] = True
                bull_f2[bull_n] = True
                bull_f3[bull_n] = True
                bull_x[bull_n] = px-8
                bull_y[bull_n] = py-16
                bull_x2[bull_n] = px-8   # 発射位置x
                bull_y2[bull_n] = py-16  # 発射位置y
                bull_x3[bull_n] = px-8   # 発射位置x
                bull_y3[bull_n] = py-16  # 発射位置y
                bull_n = (bull_n+1)%BULLET_MAX

            def move_bullet(screen): #ワンショット
                for i in range(BULLET_MAX):
                    if bull_f[i] == True:
                        bull_y[i] = bull_y[i] - bulletspeed
                        screen.blit(img_weapon,[bull_x[i],bull_y[i]])
                        if bull_y[i] < 0:
                            bull_f[i] = False

            def move_bullet1_2(screen): #ダブルショット
                for i in range(BULLET_MAX):
                    if bull_f[i] == True:
                        bull_y[i] = bull_y[i] - 32
                        screen.blit(img_weapon,[bull_x[i],bull_y[i]])
                    if bull_f2[i] == True:
                        bull_y2[i] = bull_y2[i] - 32
                        screen.blit(img_weapon,[bull_x2[i],bull_y2[i]])
                    if bull_y[i] < 0:
                        bull_f[i] = False
                    if bull_y2[i] < 0:
                        bull_f2[bull_n] = False

            def move_bullet2(screen): #弾を飛ばす
                for i in range(BULLET_MAX):
                    if bull_f[i] == True :
                        bull_y[i] = bull_y[i] - 20     # 真っすぐ
                        screen.blit(img_weapon,[bull_x[i],bull_y[i]])
                    if bull_f2[i] == True :
                        bull_y2[i] = bull_y2[i] - 20   # 左
                        bull_x2[i] = bull_x2[i] - 5
                        screen.blit(img_weapon2,[bull_x2[i],bull_y2[i]])
                    if bull_f3[i] == True :
                        bull_y3[i] = bull_y3[i] - 20   # 右
                        bull_x3[i] = bull_x3[i] + 5
                        screen.blit(img_weapon3,[bull_x3[i],bull_y3[i]])
                    if bull_y[i] < 0:
                        bull_f[i] = False
                    if bull_y2[i] < 0:
                        bull_f2[i] = False
                    if bull_y3[i] < 0:
                        bull_f3[i] = False
                        
            def move_player(screen,key,clear):
                global px,py,space,p_gauge,p_gauge02,p_invincible, idx,t,SHOT1,SHOT2,SHOT3,p_speed,img_player,score
                if key[pygame.K_UP] == 1:
                    img_player = pygame.image.load(playerlist[0])
                    py = py - p_speed_max
                    if py < 20:
                        py = 20
                if key[pygame.K_DOWN] == 1:
                    img_player = pygame.image.load(playerlist[0])
                    py = py + p_speed_max
                    if py > 460:
                        py = 460
                if key[pygame.K_LEFT] == 1:
                    img_player = pygame.image.load(playerlist[1])
                    px = px - p_speed_max
                    if px < 20:
                        px = 20
                if key[pygame.K_RIGHT] == 1:
                    img_player = pygame.image.load(playerlist[2])
                    px = px + p_speed_max
                    if px > 620:
                        px = 620
                if key[pygame.K_RIGHT] == 0 and key[pygame.K_LEFT] == 0:
                    img_player = pygame.image.load(playerlist[0])
                space = (space+1)*key[pygame.K_SPACE]
                if space%5 == 1: #5フレーム毎に弾を飛ばす
                    if bulletcount == 0:
                        set_bullet()
                    if bulletcount != 0:
                        set_bullet2()
                if p_invincible%2 == 0:         #無敵状態なら点滅させる
                    screen.blit(img_player,[px-16,py-16])
                if p_invincible > 0:
                    p_invincible = p_invincible - 1 #無敵時は当たり判定を無効にする
                    return
                elif idx == 1:
                    for i in range(ENEMY_MAX):
                        if ebull_f[i] == True:
                            w = img_enemy[e_list[i]].get_width()
                            h = img_enemy[e_list[i]].get_height()
                            r = int((w+h)/4+(32+32)/4)
                            if distance(ebull_x[i],ebull_y[i],px,py) < r*r:#敵及び敵の攻撃に接触
                                effect(px,py)
                                p_gauge = p_gauge - 20 #ダメージを受ける
                                if p_gauge02 > 0:
                                    p_gauge02 = p_gauge02 - 20 #エネルギを減らす
                                if p_gauge <= 0 and clear > score:
                                    idx = 2
                                    t = 0
                                if p_gauge <= 0 and clear <= score:
                                    idx = 3
                                    t = 0
                                if p_invincible == 0:
                                    p_invincible = 12  #無敵時間
                                ebull_f[i] = False
                                ebull_f2[i] = False
                    for i in range(ITEM_MAX):
                        if ibull_f[i] == True:
                            w = img_item[i_list[i]].get_width()
                            h = img_item[i_list[i]].get_height()
                            r = int((w+h)/4+(32+32)/4)
                            if distance(ibull_x[i],ibull_y[i],px,py) < r*r:#敵及び敵の攻撃に接触
                                if p_invincible == 0:
                                    p_invincible = 100  #無敵時間
                                ibull_f[i] = False
                                ibull_f2[i] = False
                    

            def set_enemy(x,y,a,enemy,speed,elife):
                global ebull_n
                while True:
                    if ebull_f[ebull_n] == False:
                        ebull_f[ebull_n] = True
                        ebull_x[ebull_n] = x  # 弾の発射位置
                        ebull_y[ebull_n] = y  # 弾の発射位置
                        ebull_a[ebull_n] = a  # 敵の進行する方向の角度
                        e_list[ebull_n] = enemy 
                        e_speed[ebull_n] = speed # 敵機のスピード
                        e_life[ebull_n] = elife
                        break
                    ebull_n = (ebull_n+1)%ENEMY_MAX

            def move_enemy(screen,clear,time):
                global score, p_gauge02, idx, t,S1,S2,S3,S4
                for i in range(ENEMY_MAX):
                    if ebull_f[i] == True:
                        png = e_list[i]
                        ebull_x[i] = ebull_x[i] + e_speed[i]*math.cos(math.radians(ebull_a[i]))
                        ebull_y[i] = ebull_y[i] + e_speed[i]*math.sin(math.radians(ebull_a[i]))
                        if e_list[i] == 0 and ebull_y[i] < 100 and ebull_f2[i] == False and S1 == True: # 弾を発射
                            set_enemy(ebull_x[i],ebull_y[i],90,1,15,1)   # 直進     (x座標,y座標,角度,弾,スピード,弾の体力)
                            ebull_f2[i] = True
                        if e_list[i] == 0 and ebull_y[i] < 100 and ebull_f2[i] == False and S2 == True: # 弾を発射
                            set_enemy(ebull_x[i],ebull_y[i],90,1,15,1)   # 直進
                            ebull_f2[i] = True
                        if e_list[i] == 0 and ebull_y[i] < 200 and ebull_f2[i] == False and S3 == True: # 弾を発射
                            if t % 20 == 0:
                                set_enemy(ebull_x[i],ebull_y[i],75,1,6,1)   # 左　　　角度をいじれば弾の方向を変えられます
                                set_enemy(ebull_x[i],ebull_y[i],105,1,6,1)  # 右
                        if e_list[i] == 0 and ebull_y[i] < 150 and ebull_f2[i] == False and S4 == True: # 弾を発射
                            if t % 40 == 0:
                                set_enemy(ebull_x[i],ebull_y[i],90,1,4,1)   # 直進
                                set_enemy(ebull_x[i],ebull_y[i],75,1,4,1)   # 左
                                set_enemy(ebull_x[i],ebull_y[i],105,1,4,1)  # 右
                        if ebull_x[i] < -40 or ebull_x[i] > 680 or ebull_y[i] < -40 or ebull_y[i] > 520:#画面外に敵が消える
                            ebull_f[i] = False
                            ebull_f2[i] = False
                        if e_list[i] != ENEMY_BULLEET:
                            w = img_enemy[e_list[i]].get_width()
                            h = img_enemy[e_list[i]].get_height()
                            r = int((w+h)/4)+8
                            for n in range(BULLET_MAX):
                                if bull_f[n] == True and distance(ebull_x[i]-16, ebull_y[i]-16, bull_x[n], bull_y[n]) < r*r :
                                    bull_f[n] = False
                                    effect(ebull_x[i],ebull_y[i])  #エフェクト発生
                                    e_life[i] -= 1
                            for n in range(BULLET_MAX2):
                                if bull_f2[n] == True and distance(ebull_x[i]-16, ebull_y[i]-16, bull_x2[n], bull_y2[n]) < r*r:
                                    bull_f2[n] = False
                                    effect(ebull_x[i],ebull_y[i])  #エフェクト発生
                                    e_life[i] -= 1
                            for n in range(BULLET_MAX3):
                                if bull_f3[n] == True and distance(ebull_x[i]-16, ebull_y[i]-16, bull_x3[n], bull_y3[n]) < r*r :
                                    bull_f3[n] = False
                                    effect(ebull_x[i],ebull_y[i])  #エフェクト発生
                                    e_life[i] -= 1
                        if e_life[i] == 0:
                            score = score + 10#スコア加算
                            if score >= 5000:
                                idx = 3
                                t = 0
                            ebull_f[i] = False
                            ebull_f2[i] = False
                        rz = pygame.transform.rotozoom(img_enemy[png],-180,1.0)
                        screen.blit(rz,[ebull_x[i]-rz.get_width()/2,ebull_y[i]-rz.get_height()/2])

            def set_item(x,y,a,item,speed):
                global ibull_n
                while True:
                    if ibull_f[ibull_n] == False:
                        ibull_f[ibull_n] = True
                        ibull_x[ibull_n] = x
                        ibull_y[ibull_n] = y
                        ibull_a[ibull_n] = a
                        i_list[ibull_n] = item
                        i_speed[ibull_n] = speed
                        break
                    ibull_n = (ibull_n+1)%ITEM_MAX
                    
            def move_item(screen):
                global idx, t
                for i in range(ITEM_MAX):
                    if ibull_f[i] == True:
                        png = i_list[i]
                        ibull_x[i] = ibull_x[i] + i_speed[i]*math.cos(math.radians(ibull_a[i]))
                        ibull_y[i] = ibull_y[i] + i_speed[i]*math.sin(math.radians(ibull_a[i]))
                        if ibull_x[i] < -40 or ibull_x[i] > 680 or ibull_y[i] < -40 or ibull_y[i] > 520:#画面外に敵が消える
                            ibull_f[i] = False
                            ibull_f2[i] = False
                        vz = pygame.transform.rotozoom(img_item[png],-180,1.0)
                        screen.blit(vz,[ibull_x[i]-vz.get_width()/2,ibull_y[i]-vz.get_height()/2])

            def set_item2(x,y,a,item,speed):
                global ibull_n_1
                while True:
                    if ibull_f_1[ibull_n_1] == False:
                        ibull_f_1[ibull_n_1] = True
                        ibull_x_1[ibull_n_1] = x
                        ibull_y_1[ibull_n_1] = y
                        ibull_a_1[ibull_n_1] = a
                        i_list_1[ibull_n_1] = item
                        i_speed_1[ibull_n_1] = speed
                        break
                    ibull_n_1 = (ibull_n_1+1)%ITEM_MAX
                    
            def move_item2(screen):
                global idx, t
                for i in range(ITEM_MAX):
                    if ibull_f_1[i] == True:
                        png = i_list_1[i]
                        ibull_x_1[i] = ibull_x_1[i] + i_speed_1[i]*math.cos(math.radians(ibull_a_1[i]))
                        ibull_y_1[i] = ibull_y_1[i] + i_speed_1[i]*math.sin(math.radians(ibull_a_1[i]))
                        if ibull_x_1[i] < -40 or ibull_x_1[i] > 680 or ibull_y_1[i] < -40 or ibull_y_1[i] > 520:#画面外に敵が消える
                            ibull_f_1[i] = False
                            ibull_f2_1[i] = False
                        vz = pygame.transform.rotozoom(img_item_2[png],-180,1.0)
                        screen.blit(vz,[ibull_x_1[i]-vz.get_width()/2,ibull_y_1[i]-vz.get_height()/2])

            def effect(x,y):#エフェクトを描画する準備を行う関数
                global e_n
                e_l[e_n] = 1
                e_x[e_n] = x
                e_y[e_n] = y
                e_no = (e_n+1)%EFFECT_MAX
                        
            def draw_effect(screen):#エフェクトを描画する関数
                for i in range(EFFECT_MAX):
                    if e_l[i] > 0:
                        rz = pygame.transform.rotozoom(img_explode[e_l[i]],0,0.5)#画像を縮小させる
                        screen.blit(rz,[e_x[i]-30,e_y[i]-30])
                        e_l[i] = e_l[i] + 1
                        if e_l[i] == 8:
                            e_l[i] = 0

            def distance(x1, y1, x2, y2):
                return((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

            def draw_text(screen,x,y,text,size,col):#文字表示の関数
                font = pygame.font.Font(None,size)
                s = font.render(text,True,col)
                x = x - s.get_width()/2
                y = y - s.get_height()/2
                screen.blit(s,[x,y])

            def draw_text2(screen,x,y,text,size,col):#文字表示の関数
                font = pygame.font.Font(None,size)
                s = font.render(text,True,col)
                #x = x - s.get_width()/2
                #y = y - s.get_height()/2
                screen.blit(s,[x,y])
            global S1,S2,S3,S4
            
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            screen.fill((0,0,0))
            #draw_text(screen,320,100,"Betoronome",100,WHITE)
            screen.blit(title,(60,20))
            draw_text(screen,510,190,"F1:Ranking",40,WHITE)
            draw_text(screen,500,230,"F2:Stage1",40,WHITE)
            draw_text(screen,500,270,"F3:Stage2",40,WHITE)
            if chaincount < 1:
                screen.blit(chain,(440,260))
            draw_text(screen,500,310,"F4:Stage3",40,WHITE)
            if chaincount < 2:
                screen.blit(chain,(440,300))
            draw_text(screen,500,350,"F5:Stage4",40,WHITE)
            if chaincount < 3:
                screen.blit(chain,(440,340))
            draw_text(screen,530,430,"ESC:MiniGame",40,WHITE)
            draw_text(screen,525,390,"F6:BossStage",40,WHITE)
            if chaincount < 4:
                screen.blit(chain,(460,380))
            pygame.display.update() 
            pressed = pygame.key.get_pressed()
            if pressed[K_F1]:
                title_1 = False
                ranking_1 = True
            if pressed[K_F2]:
                img_bg = pygame.image.load("./image/bgimage.png")#背景画像
                img_enemy = [
                    pygame.image.load("./image/enemy1.png"),   #敵画像
                    pygame.image.load("./image/e_bullet.png")  #敵の攻撃弾画像
                ]
                S1 = True
                S2 = False
                S3 = False
                S4 = False
                chain1 = 1
                stage = "No"
                clearscore = 400
                title_1 = False
                choice = True
                main_1 = True
            if pressed[K_F3] and chaincount >= 1:
                img_bg = pygame.image.load("./image/back02.png")
                img_enemy = [
                    pygame.image.load("./image/enemy02.png"),   #敵画像
                    pygame.image.load("./image/enemy_at.png")  #敵の攻撃弾画像
                ]
                # p_speed = 5
                S1 = False
                S2 = True
                S3 = False
                S4 = False
                chain2 = 1
                stage = "No"
                clearscore = 450
                title_1 = False
                choice = True
                main_1 = True
            if pressed[K_F4] and chaincount >= 2:
                img_bg = pygame.image.load("./image/back03.png")
                img_enemy = [
                    pygame.image.load("./image/enemy03.png"),   #敵画像
                    pygame.image.load("./image/e_bullet.png")  #敵の攻撃弾画像
                ]
                S1 = False
                S2 = False
                S3 = True
                S4 = False
                chain3 = 1
                stage = "No"
                clearscore = 500
                title_1 = False
                choice = True
                main_1 = True
            if pressed[K_F5] and chaincount >= 3:
                img_bg = pygame.image.load("./image/back04.png")
                img_enemy = [
                    pygame.image.load("./image/enemy1.png"),   #敵画像
                    pygame.image.load("./image/e_bullet.png")  #敵の攻撃弾画像
                ]
                S1 = False
                S2 = False
                S3 = False
                S4 = True
                chain4 = 1
                stage = "No"
                clearscore = 500
                title_1 = False
                choice = True
                main_1 = True
            if pressed[K_ESCAPE]:
                mixer.music.load(music[2])
                mixer.music.play()
                title_1 = False
                main_5 = True
            if pressed[K_F6] and chaincount >= 4: # and chaincount >= 4
                mixer.music.load(music[5])
                mixer.music.play() 
                choice = True
                stage = "Yes"
                secret = True
                title_1 = False

        while ranking_1:
            pygame.display.update()
            screen.fill((0,0,0))
            file01 = open("./score.txt", "r")   #読み取り専用
            list = file01.readlines()         #リストとして読み込む
            for i in list:
                i = i.strip()
                i = int(i)
                score_list.append(i)
            list = sorted(score_list,reverse=True)
            for data in list:
                score_count += 1
            for data in list:
                nomber += 1
                if data != " ":
                    score_tx = "No." + str(nomber) + "  " + str(data)
                draw_text2(screen,score_x,score_y + scroll_y,score_tx,60,WHITE)
                score_y += 64
                score_count2 += 1
                if score_count == score_count2:
                    if score_y + scroll_y <= 480:
                        score_judge = "NO"
                    if score_y + scroll_y > 480:
                        score_judge = "YES"
            file01.close()
            score_list = []
            score_y = 32
            score_x = 32
            nomber = 0
            #draw_text(screen,450,250,"Plaese SpaceKey",50,WHITE)
            pressed = pygame.key.get_pressed()
            if pressed[K_SPACE]:
                scroll_y = 0
                ranking_1 = False
                title_1 = True          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 4:
                    if scroll_y < 0:
                        scroll_y += 5
                if event.type == MOUSEBUTTONDOWN and event.button == 5:
                    if score_judge == "YES":
                        scroll_y -= 5

        while choice:
            global SHOT1,SHOT2,SHOT3,p_speed_max
            pygame.display.update()
            screen.fill((0,0,0))
            ruletext1 = font_5.render("カーソルキーで移動", True, "white") 
            screen.blit(ruletext1, (170,30))
            ruletext2 = font_5.render("スペースキーで弾を発射", True, "white") 
            screen.blit(ruletext2, (170,70))
            draw_text(screen,120,170,"F8",60,WHITE)
            draw_text(screen,320,170,"F9",60,WHITE)
            draw_text(screen,520,170,"F10",60,WHITE)
            screen.blit(player_1,(90,200))
            screen.blit(player_2,(290,200))
            screen.blit(player_3,(490,200))
            parametertext1 = font_boss.render("攻撃", True, "white") 
            parametertext2 = font_boss.render("速度", True, "white") 
            parametertext3 = font_boss.render("体力", True, "white")
            screen.blit(parametertext3,(5,310))
            screen.blit(parametertext1,(5,350))
            screen.blit(parametertext2,(5,390)) 
            parameter_1 = pygame.image.load("./image/parameter1.png")
            parameter_2 = pygame.image.load("./image/parameter2.png")
            parameter_3 = pygame.image.load("./image/parameter3.png")
            parameter_4 = pygame.image.load("./image/parameter4.png")
            parameter_5 = pygame.image.load("./image/parameter5.png")
            parameter_6 = pygame.image.load("./image/parameter6.png")
            if stage == "No":
                screen.blit(parameter_1,(60,300))
                screen.blit(parameter_2,(260,300))
                screen.blit(parameter_3,(460,300))
            if stage == "Yes":
                screen.blit(parameter_4,(60,300))
                screen.blit(parameter_5,(260,300))
                screen.blit(parameter_6,(460,300))
            pressed = pygame.key.get_pressed()
            if pressed[K_F8]:
                playerlist = ["./image/player1.png","./image/player1-x.png","./image/player1+x.png"]
                img_player = pygame.image.load(playerlist[0])
                group_se_pl.empty()
                player = ["./image/player1.png","./image/player1.png","./image/player1-x.png","./image/player1+x.png"]
                player = Player(player, 288, 416,32,32,1,100,10,8)
                group_se_pl.add(player)
                shotlist = []
                for i in range(30):
                    shot = Shot("./image/shot01.png",-64,-64,16,16,10)
                    shotlist.append(shot)
                for shot in shotlist:
                    group_se_pl.add(shot)
                bulletspeed = 32
                img_gauge = pygame.image.load("./image/gauge.png")#体力ゲージ
                p_gauge_max = 100
                p_speed_max = 10
                choice = False 
                SHOT1 = True
                SHOT2 = False
                SHOT3 = False
            if pressed[K_F9]:
                playerlist = ["./image/player2.png","./image/player2-x.png","./image/player2+x.png"]
                img_player = pygame.image.load(playerlist[0])
                group_se_pl.empty()
                player = ["./image/player2.png","./image/player2.png","./image/player2-x.png","./image/player2+x.png"]
                player = Player(player, 288, 416,32,32,1,160,6,10)
                group_se_pl.add(player)
                shotlist = []
                for i in range(30):
                    shot = Shot("./image/shot01.png",-64,-64,16,16,12)
                    shotlist.append(shot)
                for shot in shotlist:
                    group_se_pl.add(shot)
                bulletspeed = 16
                img_gauge = pygame.image.load("./image/gauge2.png")#体力ゲージ
                p_gauge_max = 160
                p_speed_max = 5
                choice = False 
                SHOT1 = False
                SHOT2 = True
                SHOT3 = False
            if pressed[K_F10]:
                playerlist = ["./image/player3.png","./image/player3-x.png","./image/player3+x.png"]
                img_player = pygame.image.load(playerlist[0])
                group_se_pl.empty()
                player = ["./image/player3.png","./image/player3.png","./image/player3-x.png","./image/player3+x.png"]
                player = Player(player, 288, 416,32,32,2,60,8,8)
                group_se_pl.add(player)
                shotlist = []
                for i in range(30):
                    shot = Shot("./image/shot01.png",-64,-64,16,16,8)
                    shotlist.append(shot)
                for shot in shotlist:
                    group_se_pl.add(shot)
                bulletspeed = 24
                img_gauge = pygame.image.load("./image/gauge3.png")#体力ゲージ
                p_gauge_max = 60
                p_speed_max = 20
                choice = False 
                SHOT1 = False
                SHOT2 = False
                SHOT3 = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        while main_1:
            t=t+1
            if p_gauge02 <= 80:
                bulletcount = 0
            if p_gauge02 >= 100:
                bulletcount = 1
                enelgy_count += 1 
                if enelgy_count % 100 == 0:
                    p_gauge02 = p_gauge02 -100 
                    enelgy_count = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            bg_y = (bg_y+16)%480
            screen.blit(img_bg,[0,bg_y-480])
            screen.blit(img_bg,[0,bg_y])
            key = pygame.key.get_pressed()
            if idx == 0:#タイトル画面（仮）
                draw_text(screen,320,240,"Shooting",100,WHITE)
                draw_text(screen,320,340,"PRESS SPACE!",80,WHITE)
                if key[pygame.K_SPACE] == 1:
                    idx = 1
                    t = 0
                    score = 0
                    px = 320
                    py = 400
                    p_speed = p_speed_max
                    p_gauge = p_gauge_max
                    p_gauge02 = 0
                    p_invincible = 0
                    count_bo = 0
                    time_bo = 60   
                    if p_gauge_max == 100:
                        img_gauge = pygame.image.load("./image/gauge.png")
                    if p_gauge_max == 160:
                        img_gauge = pygame.image.load("./image/gauge2.png")
                    if p_gauge_max == 60:
                        img_gauge = pygame.image.load("./image/gauge3.png")
                    for i in range(BULLET_MAX):
                        bull_f[i] = False
                    for i in range(ENEMY_MAX):
                        ebull_f[i] = False
                    if S1 == True:
                        mixer.music.load(music[1])
                        mixer.music.play() 
                    if S2 == True:
                        mixer.music.load(music[2])
                        mixer.music.play()
                    if S3 == True:
                        mixer.music.load(music[3])
                        mixer.music.play()
                    if S4 == True:
                        mixer.music.load(music[4])
                        mixer.music.play() 

            if idx == 1:#ゲームプレイ中
                count_bo += 1
                if count_bo % 34 == 0 and time_bo > 0:
                    time_bo -= 1
                draw_text(screen,580,45,f"TIME:{time_bo}",30,WHITE)
                move_player(screen,key,clearscore)
                if bulletcount == 0:
                    move_bullet(screen)
                if bulletcount != 0:
                    move_bullet2(screen)
                if S1 == True: 
                    if t%30 == 0:#30フレームにつき敵1体出現
                        set_enemy(random.randint(20,620),-10,90,0,6,1) # (x座標,y座標,角度,エネミー,スピード,エネミーの体力)
                if S2 == True:
                    if t%30 == 0:#30フレームにつき敵1体出現
                        set_enemy(random.randint(20,620),-10,90,0,6,3) # (x座標,y座標,角度,エネミー,スピード,エネミーの体力)
                if S3 == True: 
                    if t%30 == 0:#30フレームにつき敵1体出現
                        set_enemy(random.randint(20,620),-10,90,0,4,2) # (x座標,y座標,角度,エネミー,スピード,エネミーの体力)
                if S4 == True:
                    if t%30 == 0:#30フレームにつき敵1体出現
                        set_enemy(random.randint(20,620),-10,90,0,2,4) # (x座標,y座標,角度,エネミー,スピード,エネミーの体力)
                move_enemy(screen,clearscore,time_bo)
                if t%300 == 0:#300フレームにつきアイテム出現
                    set_item(random.randint(20,620),-10,90,0,6)
                if t%500 == 0:#3000フレームにつきアイテム出現
                    set_item2(random.randint(20,620),-10,90,0,6)
                move_item(screen)
                move_item2(screen)
                for i in range(ITEM_MAX):
                    if ibull_f_1[i] == True:
                        w = img_item_2[i_list_1[i]].get_width()
                        h = img_item_2[i_list_1[i]].get_height()
                        r = int((w+h)/4+(32+32)/4)
                        if distance(ibull_x_1[i],ibull_y_1[i],px,py) < r*r:#敵及び敵の攻撃に接触
                            time_bo += 10
                            if time_bo > 60:
                                time_bo = 60
                            ibull_f_1[i] = False
                            ibull_f2_1[i] = False
                if score >= clearscore and time_bo <= 0:
                    idx = 3
                    t = 0
                if score < clearscore and time_bo <= 0:
                    idx = 2
                    t = 0
                if p_gauge <= 0 and clearscore <= score:
                    idx = 3
                    t = 0
                if p_gauge <= 0 and clearscore > score:
                    idx = 2
                    t = 0
                if score >= 3000:
                    idx = 3
                    t = 0


            if idx == 2:#ゲームオーバー
                mixer.music.load(music[5])
                mixer.music.play()
                draw_text(screen,320,240,"GAMEOVER",100,WHITE)
                draw_text(screen,320,340,"1:CONTINUE",50,WHITE)
                draw_text(screen,310,400,"2:TITLE",50,WHITE)
                pressed = pygame.key.get_pressed()
                if pressed[K_1]:
                    mixer.music.load(music[0])
                    mixer.music.play() 
                    file = open("./score.txt","a")
                    file.write(str(score) + '\n')
                    file.close()
                    count_bo = 0
                    time_bo = 60   
                    idx = 0
                    t = 0
                if pressed[K_2]:
                    file = open("./score.txt","a")
                    file.write(str(score) + '\n')
                    file.close()
                    count_bo = 0
                    time_bo = 60   
                    idx = 0
                    t = 0
                    title_1 = True
                    main_1 = False
            if idx == 3:#ゲームクリア
                draw_text(screen,320,240,"GAMECLEAR",100,WHITE)
                draw_text(screen,320,340,"1:TITLE",50,WHITE)
                pressed = pygame.key.get_pressed()
                if pressed[K_1]:
                    mixer.music.load(music[0])
                    mixer.music.play() 
                    if chain1 == 1 and chaincount == 0:
                        chaincount += 1
                        chain1 = 0
                    if chain2 == 1 and chaincount == 1:
                        chaincount += 1
                        chain2 = 0
                    if chain3 == 1 and chaincount == 2:
                        chaincount += 1
                        chain3 = 0
                    if chain4 == 1 and chaincount == 3:
                        chaincount += 1
                        chain4 = 0
                    count_bo = 0
                    time_bo = 60   
                    file = open("./score.txt","a")
                    file.write(str(score) + '\n')
                    file.close()
                    idx = 0
                    t = 0
                    title_1 = True
                    main_1 = False
            draw_effect(screen)
            if idx == 1:#ゲームプレイ中のみ体力ゲージとスコアを表示する  
                #screen.blit(img_gauge,(10,450))  #体力ゲージ
                #screen.blit(img_gauge02,(10,430))#エネルギーゲージ
                if p_gauge_max == 160:
                    screen.blit(img_gauge,(10,450))  #体力ゲージ
                    screen.blit(img_gauge02,(10,420))#エネルギーゲージ
                    pygame.draw.rect(screen,(32,32,32),[10+p_gauge*2,450,(p_gauge_max-p_gauge)*2,25]) #ダメージを受けたら矩形で塗りつぶす
                    pygame.draw.rect(screen,(32,32,32),[10+p_gauge02*2,420,(100-p_gauge02)*2,25]) #ダメージを受けたら矩形で塗りつぶす
                    draw_text(screen, 580, 20, "SCORE" + str(score), 30, WHITE)
                elif p_gauge_max == 60:
                    screen.blit(img_gauge,(10,450))  #体力ゲージ
                    screen.blit(img_gauge02,(10,420))#エネルギーゲージ
                    pygame.draw.rect(screen,(32,32,32),[10+p_gauge*2,450,(p_gauge_max-p_gauge)*2,25]) #ダメージを受けたら矩形で塗りつぶす
                    pygame.draw.rect(screen,(32,32,32),[10+p_gauge02*2,420,(100-p_gauge02)*2,25]) #ダメージを受けたら矩形で塗りつぶす
                    draw_text(screen, 580, 20, "SCORE" + str(score), 30, WHITE)
                else:
                    screen.blit(img_gauge,(10,450))  #体力ゲージ
                    screen.blit(img_gauge02,(10,430))#エネルギーゲージ
                    pygame.draw.rect(screen,(32,32,32),[10+p_gauge*2,450,(p_gauge_max-p_gauge)*2,25]) #ダメージを受けたら矩形で塗りつぶす
                    pygame.draw.rect(screen,(32,32,32),[10+p_gauge02*2,430,(100-p_gauge02)*2,25]) #ダメージを受けたら矩形で塗りつぶす
                    draw_text(screen, 580, 20, "SCORE" + str(score), 30, WHITE)
            pygame.display.update()
            clock.tick(30)

        while main_5:
            #時間カウント
            count_5 += 1
            if count_5 % 40 == 0 and time_5 > 0:
                time_5 -= 1

            #　描画処理と更新処理
            group_5.update()
            group_5.draw(screen)
            group_5_ship.update()
            group_5_ship.draw(screen)

            #life回復判定
            for ship01 in shiplist:
                if ship01.rect.x < 0 and life_5 > 0 and time_5 > 0:
                    if life_5 < 3:
                        life_5 += 1
                    num = random.randint(0,6)
                    ship01.rect.y = num * 64
                    ship01.rect.x = 800 + 64 * num
            
            #回復アイテムの撃墜判定
            for enemy01 in enemy1list:
                for ship01 in shiplist:
                    if pygame.sprite.collide_rect(enemy01,ship01):
                        if ship01.rect.x < 640:
                            num = random.randint(0,6)
                            ship01.rect.y = num * 64
                            ship01.rect.x = 800 + 64 * num
            
            #回復アイテムの撃墜判定
            for ship01 in shiplist:
                if pygame.sprite.collide_rect(beam,ship01):
                    if ship01.rect.x < 640:
                        num = random.randint(0,6)
                        ship01.rect.y = num * 64
                        ship01.rect.x = 800 + 64 * num

            #画面外との当たり判定
            for enemy01 in enemy1list:
                if enemy01.rect.x < 0 and life_5 > 0 and time_5 > 0:
                    num = random.randint(0,6)
                    life_5 -= 1
                    enemy01.rect.y = num * 64
                    enemy01.rect.x = 640 + 64 * num
                    
            #残りlife表示
            if life_5 == 3:
                life_group3.update()
                life_group3.draw(screen)
            
            if life_5 == 2:
                life_group2.update()
                life_group2.draw(screen)
            
            if life_5 == 1:
                life_group1.update()
                life_group1.draw(screen)

            #マウスカーソルに画像を表示
            group_5_1.empty()
            lock = Lock("./image/lock-on2.png",m_x,m_y)
            group_5_1.add(lock)
            group_5_1.update()
            group_5_1.draw(screen)

            #残り時間表示
            draw_text(screen,580,30,f"TIME:{time_5:>2}",30,WHITE)
            
            #GameCLEAR時の処理
            if time_5 == 0:
                beam.rect.x = -640
                barrier.rect.y = -640
                screen.fill((0,0,0))
                draw_text(screen,320,100,"GameClear",100,WHITE)
                draw_text(screen,310,400,"1:TITLE",50,WHITE)
                pressed = pygame.key.get_pressed()
                if pressed[K_1]:
                    mixer.music.load(music[0])
                    mixer.music.play()
                    time_5 = 30
                    life_5 = 3
                    title_1 = True
                    main_5 = False

            #ゲームオーバー時の処理   
            if life_5 == 0:
                barrier.rect.y = -640
                beam.rect.x = -640
                screen.fill((0,0,0))
                draw_text(screen,320,100,"GameOver",100,WHITE)
                draw_text(screen,320,340,"1:CONTINUE",50,WHITE)
                draw_text(screen,310,400,"2:TITLE",50,WHITE)
                pressed = pygame.key.get_pressed()
                if pressed[K_1]:
                    mixer.music.load(music[2])
                    mixer.music.play()
                    time_5 = 30
                    life_5 = 3
                    for enemy01 in enemy1list:
                        num = random.randint(0,6)
                        enemy01.rect.y = num * 64
                        enemy01.rect.x = 640 + 64 * num
                    for ship1 in shiplist:
                        num = random.randint(0,6)
                        ship1.rect.y = num * 64
                        ship1.rect.x = 640 + 64 * num
                    num = random.randint(0,6)
                    beam.rect.y = num * 64
                    beam.rect.x = 800 + 64 * num
                    main_5 = True
                if pressed[K_2]:
                    mixer.music.load(music[0])
                    mixer.music.play()
                    title_1 = True
                    main_5 = False

            #beam発射
            if life_5 >= 1:
                group_5_be.update()
                group_5_be.draw(screen)
                if beam.rect.x < 0 and life_5 > 0:
                    life_5 -= 1
                    num1 = random.randint(0,6)
                    num2 = random.randint(0,15)
                    beam.rect.y = num1 * 64
                    beam.rect.x = 800 + 64 * num2

            #シールド表示
            if shieldcount != 0:
                    group_5_sh.update()
                    group_5_sh.draw(screen)
                    shieldcount2 += 1
                    if shieldcount2 >= 20:
                        shieldcount = 0
                        shieldcount2 = 0
                        group_5_sh.empty()
                        barrier = Lock("./image/shield.png",-640,-640)
                        group_5_sh.add(barrier)
                        group_5_sh.update()
                        group_5_sh.draw(screen)

            #ビームとシールドの当たり判定
            if pygame.sprite.collide_rect(beam,barrier):
                beam.rect.x = -640

            pygame.display.update()
            pygame.time.wait(25)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #マウスの位置情報の取得
                if event.type == MOUSEMOTION:
                    M_x,M_y = event.pos
                    M_x -= 16
                    M_y -= 16
                    m_x,m_y = M_x,M_y
                    group_5_1.empty()
                    lock = Lock("./image/lock-on2.png",m_x,m_y)
                    group_5_1.add(lock)
                    group_5_1.update()
                    group_5_1.draw(screen)

                if event.type == MOUSEBUTTONDOWN:
                    mouse =  pygame.mouse.get_pressed()
                    #マウスの左クリック時
                    if mouse[0]:
                        for enemy01 in enemy1list:
                            if pygame.sprite.collide_rect(enemy01,lock):
                                enemy01.rect.x = -640
                    #マウス右クリック時
                    if mouse[2] and shieldcount == 0:                   #左クリックされたなら
                        shieldcount += 1
                        B_x,B_y = event.pos
                        B_x,B_y = B_x-16,B_y-16
                        group_5_sh.empty()
                        barrier = Lock("./image/shield.png",B_x,B_y)
                        group_5_sh.add(barrier)
                        group_5_sh.update()
                        group_5_sh.draw(screen)
        
        while secret:
            global life_gage
            screen.blit(boss_bg,(0,0))
            group_se_pl.update()
            group_se_pl.draw(screen)
            group_se_bo.update()
            group_se_bo.draw(screen)
            #group_se_be.update()
            #group_se_be.draw(screen)

            #　beaconと自機攻撃の当たり判定
            for shot01 in shotlist:
                if pygame.sprite.collide_rect(beacon1,shot01):
                    num = random.randint(0,6)
                    shot01.rect.y = num * 64
                    shot01.rect.x = 800 + 64 * num
            #　ボスと自機攻撃の当たり判定
            for shot01 in shotlist:
                if pygame.sprite.collide_rect(boss,shot01):
                    num = random.randint(0,6)
                    shot01.rect.y = num * 64
                    shot01.rect.x = 800 + 64 * num
                    if boss.life > 0 and boss.rect.y >= 32:
                        boss.life -= player.atack
                        boss_score += 10
            #　ボスと自機の当たり判定
            if pygame.sprite.collide_rect(boss,player):
                num = random.randint(0,6)
                shot01.rect.y = num * 64
                shot01.rect.x = 800 + 64 * num
                if player.life > 0 and mutekitime >= 40:
                    player.life -= 20
                    mutekitime = 0
            
            mutekitime += 1

            #　ボス表示切替処理
            if boss.life <= 0  and boss.rect.y < -(boss.rect.height):
                for mob01 in mob1list:
                    num = random.randint(0,20)
                    mob01.rect.y = num * -64
                    mob01.rect.x = 32 * num
                for mob02 in mob2list:
                    num = random.randint(0,20)
                    mob02.rect.y = num * -64
                    mob02.rect.x = 32 * num
                for mob03 in mob3list:
                    num = random.randint(0,20)
                    mob03.rect.y = num * -64
                    mob03.rect.x = 32 * num
                for shot01 in shotlist_m1:
                    num = random.randint(0,6)
                    shot01.rect.y = num * 64
                    shot01.rect.x = 800 + 64 * num
                for shot01 in shotlist_m2:
                    num = random.randint(0,6)
                    shot01.rect.y = num * 64
                    shot01.rect.x = 800 + 64 * num
                for shot01 in shotlist_m3:
                    num = random.randint(0,6)
                    shot01.rect.y = num * 64
                    shot01.rect.x = 800 + 64 * num
                if bosslevel == 0:
                    boss_score += 100
                if bosslevel == 1:
                    boss_score += 200
                if bosslevel == 2:
                    boss_score += 300
                bosslevel += 1
                if bosslevel == 1:
                    group_se_bo.empty()
                    boss = ["./image/boss1_1.png","./image/boss1_2.png"]
                    boss = Boss(boss, 230, -128,20,96,96,6,8)
                    group_se_bo.add(boss)
                    boss_shotlist1 = []
                    for i in range(30):
                        shot = Shot2("./image/boss_shot_1.png",-64,-64,32,32,10)
                        boss_shotlist1.append(shot)
                    for shot01 in boss_shotlist1:
                        group_se_bo.add(shot01)
                if bosslevel == 2:
                    group_se_bo.empty()
                    boss = ["./image/boss2_1.png","./image/boss2_2.png"]
                    boss = Boss(boss, 230, -128,30,128,128,8,5)
                    group_se_bo.add(boss)
                    boss_shotlist2 = []
                    for i in range(30):
                        shot = Shot2("./image/boss_shot_2.png",-64,-64,32,32,12)
                        boss_shotlist2.append(shot)
                    for shot02 in boss_shotlist2:
                        group_se_bo.add(shot02)

            if boss.life > 0:
                #　ボス1の攻撃判定
                for shot01 in boss_shotlist:
                    if pygame.sprite.collide_rect(player,shot01):
                        num = random.randint(0,6)
                        shot01.rect.y = num * 64
                        shot01.rect.x = 800 + 64 * num
                        if player.life > 0 and boss.life > 0:
                            player.life -= 20
                #　ボス2の攻撃判定
                for shot01 in boss_shotlist1:
                    if pygame.sprite.collide_rect(player,shot01):
                        num = random.randint(0,6)
                        shot01.rect.y = num * 64
                        shot01.rect.x = 800 + 64 * num
                        if player.life > 0 and boss.life > 0:
                            player.life -= 20
                #　ボス3の攻撃判定
                for shot01 in boss_shotlist2:
                    if pygame.sprite.collide_rect(player,shot01):
                        num = random.randint(0,6)
                        shot01.rect.y = num * 64
                        shot01.rect.x = 800 + 64 * num
                        if player.life > 0 and boss.life > 0:
                            player.life -= 20
                if bosslevel == 0:
                    for shot01 in shotlist_m1:
                        if pygame.sprite.collide_rect(player,shot01):
                            num = random.randint(0,6)
                            shot01.rect.y = num * 64
                            shot01.rect.x = 800 + 64 * num
                            if player.life > 0 and boss.life > 0:
                                player.life -= 20
                if bosslevel == 1:
                    for shot01 in shotlist_m2:
                        if pygame.sprite.collide_rect(player,shot01):
                            num = random.randint(0,6)
                            shot01.rect.y = num * 64
                            shot01.rect.x = 800 + 64 * num
                            if player.life > 0 and boss.life > 0:
                                player.life -= 20
                if bosslevel == 2:
                    for shot01 in shotlist_m3:
                        if pygame.sprite.collide_rect(player,shot01):
                            num = random.randint(0,6)
                            shot01.rect.y = num * 64
                            shot01.rect.x = 800 + 64 * num
                            if player.life > 0 and boss.life > 0:
                                player.life -= 20
            
            if bosslevel <= 2:
                if player.speed == 10:
                    img_gauge = pygame.image.load("./image/gauge.png")#体力ゲージ
                    life_gage = 100
                if player.speed == 12:
                    img_gauge = pygame.image.load("./image/gauge2.png")#体力ゲージ
                    life_gage = 160
                if player.speed == 8:
                    img_gauge = pygame.image.load("./image/gauge3.png")#体力ゲージ
                    life_gage = 60
                screen.blit(img_gauge,(10,450))  #体力ゲージ
                pygame.draw.rect(screen,(32,32,32),[10+player.life*2,450,(player.life_max-player.life)*2,25]) #ダメージを受けたら矩形で塗りつぶす
                #draw_text(screen, 580, 20, "SCORE" + str(score), 30, WHITE)

            if bosslevel == 0 and boss.life > 0:
                group_se_mob1.update()
                group_se_mob1.draw(screen)
            if bosslevel == 1 and boss.life > 0:
                group_se_mob2.update()
                group_se_mob2.draw(screen)
            if bosslevel == 2 and boss.life > 0:
                group_se_mob3.update()
                group_se_mob3.draw(screen)

            for mob01 in mob1list:
                if pygame.sprite.collide_rect(player,mob01):
                    num = random.randint(0,20)
                    mob01.rect.y = num * -64
                    mob01.rect.x = 32 * num
                    if player.life > 0 and boss.life > 0:
                        player.life -= 20
            for mob02 in mob2list:
                if pygame.sprite.collide_rect(player,mob02):
                    num = random.randint(0,20)
                    mob02.rect.y = num * -64
                    mob02.rect.x = 32 * num
                    if player.life > 0 and boss.life > 0:
                        player.life -= 20
            for mob03 in mob3list:
                if pygame.sprite.collide_rect(player,mob03):
                    num = random.randint(0,20)
                    mob03.rect.y = num * -64
                    mob03.rect.x = 32 * num
                    if player.life > 0 and boss.life > 0:
                        player.life -= 20
            for shot01 in shotlist:
                for mob01 in mob1list:
                    if pygame.sprite.collide_rect(mob01,shot01):
                        num = random.randint(0,20)
                        mob01.rect.y = num * -64
                        mob01.rect.x = 32 * num
                        score += 10
            for shot01 in shotlist:
                for mob02 in mob2list:
                    if pygame.sprite.collide_rect(mob02,shot01):
                        num = random.randint(0,20)
                        mob02.rect.y = num * -64
                        mob02.rect.x = 32 * num
                        score += 10
            for shot01 in shotlist:
                for mob03 in mob3list:
                    if pygame.sprite.collide_rect(mob03,shot01):
                        num = random.randint(0,20)
                        mob03.rect.y = num * -64
                        mob03.rect.x = 32 * num
                        score += 10
            for shot01 in shotlist_m1:
                if pygame.sprite.collide_rect(player,shot01):
                    num = random.randint(0,6)
                    shot01.rect.y = num * 64
                    shot01.rect.x = 800 + 64 * num
                    if player.life > 0 and boss.life > 0:
                        player.life -= 20
            for shot01 in shotlist_m2:
                if pygame.sprite.collide_rect(player,shot01):
                    num = random.randint(0,6)
                    shot01.rect.y = num * 64
                    shot01.rect.x = 800 + 64 * num
                    if player.life > 0 and boss.life > 0:
                        player.life -= 20
            for shot01 in shotlist_m3:
                if pygame.sprite.collide_rect(player,shot01):
                    num = random.randint(0,6)
                    shot01.rect.y = num * 64
                    shot01.rect.x = 800 + 64 * num
                    if player.life > 0 and boss.life > 0:
                        player.life -= 20

            if bosslevel <= 2:
                #　ライフ表示
                draw_text(screen,560,30,f"BOSS_LIFE:{boss.life:>2}",30,WHITE)
            draw_text(screen,560,60,f"SCORE:{boss_score}",30,WHITE)

            if bosslevel >= 3:
                draw_text(screen,320,200,"congratulation",80,WHITE)
                draw_text(screen,320,300,"Please DeleteKey",60,WHITE)

            if player.life <= 0:
                boss.rect.x = 1280
                draw_text(screen,320,200,"GameOver",80,WHITE)
                draw_text(screen,320,300,"DeleteKey:Title",60,WHITE)

            #プレイヤーとショットの関連付け
            player.setshot(shotlist)
            if bosslevel == 0:
                boss.setshot2(boss_shotlist)
                for mob01 in mob1list:
                    mob01.setshot(shotlist_m1)
            if bosslevel == 1:
                boss.setshot2(boss_shotlist1)
                for mob02 in mob2list:
                    mob02.setshot(shotlist_m2)
            if bosslevel == 2:    
                boss.setshot2(boss_shotlist2)
                for mob03 in mob3list:
                    mob03.setshot(shotlist_m3)
                

            pygame.display.update()
            pygame.time.wait(25)

            #　DELETEキーでタイトル画面に
            pressed = pygame.key.get_pressed()
            if player.life <= 0 or bosslevel >= 3:
                if pressed[K_DELETE]:
                    file = open("./score.txt","a")
                    file.write(str(boss_score) + '\n')
                    file.close()
                    for mob01 in mob1list:
                        num = random.randint(0,20)
                        mob01.rect.y = num * -64
                        mob01.rect.x = 32 * num
                    for mob02 in mob2list:
                        num = random.randint(0,20)
                        mob02.rect.y = num * -64
                        mob02.rect.x = 32 * num
                    for mob03 in mob3list:
                        num = random.randint(0,20)
                        mob03.rect.y = num * -64
                        mob03.rect.x = 32 * num
                    for shot01 in shotlist_m1:
                        num = random.randint(0,6)
                        shot01.rect.y = num * 64
                        shot01.rect.x = 800 + 64 * num
                    for shot01 in shotlist_m2:
                        num = random.randint(0,6)
                        shot01.rect.y = num * 64
                        shot01.rect.x = 800 + 64 * num
                    for shot01 in shotlist_m3:
                        num = random.randint(0,6)
                        shot01.rect.y = num * 64
                        shot01.rect.x = 800 + 64 * num
                    boss.rect.y = -288
                    boss.rect.x = 288
                    bosslevel = 0
                    boss_score = 0
                    mixer.music.load(music[0])
                    mixer.music.play()
                    secret = False
                    title_1 = True
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()
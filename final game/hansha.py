import pygame
import random
import sys
import math
import base64, io
import pygame

# ── Base64 데이터 ──
IDLE_SHEET_B64 = "iVBORw0KGgoAAAANSUhEUgAAAQAAAABACAYAAAD1Xam+AAAAAXNSR0IArs4c6QAABGVJREFUeJzt3b9v20YYxvFHRTx2MipKQOAlho0A9ZoC6SAX3j14yqAlQwGjW/8CO3uRrtq6eM6gPag1tP9AphjxYhSwpCBTgmZoEXawjznT+uWoR93x/X4AI7J1lPTw5b0iJUqRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAbBpV32GzleWT/j4ejip/LIB1lUy68qS/9+vvt8b8+/MPxeU6NwPrDZD8ceUPfqcu8KRJP4lrBHXaIKw3QPLHm7+SBuACf/Pgq5lj355/kmrWBKw3QPLHnT/onTRbWd7uD/T2/NPcye/srW9Lkk6+b9ViI6ABkj/m/IvNyiXsrW/ryaOHd16u3R9MPV5KhWuAWqD4bsyTRw/V/WNYwaMLj/zx5w/eAO7CPfv7l1NvApYboMgfff7gDeDlu9czr99b3y5+ysu47mlFHRvgXZC/+vz3Qt64zw83jd8s5jWOVLx893pm9knXuWXa/YEu9zuBH2FY5I87fyUNoC6TeRlWG6BD/jjzV7YH8KXa/YG038lTfkW4bhvzXZE/3vxRvQiI2+ryYtiXIn/Y/DQAwDAaAGAYDQAwjAYAGEYDAAwL2gDGw1Ej9RM5gDpjDyAg6w2Q/PHnr6QBuJVwcXo2d+zF6VkxbpHxiNt4OIriNjBZ8DMBx8NRwz+R4eL0TP+M/5IkrTXv3xjr/n417vP4tesPRaR4NuB4OGpov5O3+4OioS2S378u5fzNVva/3EaqTSD2+lf2nYD+J/v8JjDNWvO+Nna3it/9XanUJgL5s+UmwPMfpQRzOzHXv9IvBZ328d7yrr4fvOxyv5PchkD+eCdAFWKuf/BDgGYry0fHzyRJ2X5H7pnADzkrsM8dDqTEen7n8jq7iryfMy8yAdyysb+oVhZ7/YM2gOLYv3sgnbwo/r6xu1UUfZHwbqzbFUyF9fxKYAKElEL9g+1KufCjN68kSdnmzo3r/+4eSROOA8s2drdudf0UdgGt51d5HZy8UHZ8VDyTLzMBUsifSv2DNgAXXt4K+PjLoSTpffeZG7fQ7aVQdB/505gAoaRS/+CvAZQL73x9crUBfJyz/PWKir7g01jO708Ax02AD92fpAUmwOXzq39TmPSTxF7/oA3AhXfFa7ay/NvH3y207Pnjp5Kk94lu/CK/lMAECCmF+gdrAMt0bBc+1a4v8kuJTIBQUql/pSt3xn+M6I9JfsOfhvxZ/uDP3+aOq0sDLIux/itZwTfeGjo+krssSY3Dw5U9rqpYzR/jBFgFq/UvNFtZnn8YFz/+7xa+AJL8WZ73enne6+X+5bzXyyXZyB9J/aP/WnDUVPdAkjTqHijb3CneMWgeHyX7wZ8U8X0AgGE0AMAwGgBg2MoawLQTRKywnt+6WOq/kgZQ97d55rGeXxFNgFWIqf4cAqByMU0A62gAgGHRNADLu4Qiv3mrqv9Kd8XcWU/lbw62sotoOb//eXm38Y/evFK2uWMivyKpv4kVjTjFMAEAAAAAAAAs+A+P1IuvjEECZgAAAABJRU5ErkJggg=="

LEFT_SHEET_B64 = "iVBORw0KGgoAAAANSUhEUgAAAMAAAABACAYAAABMbHjfAAAAAXNSR0IArs4c6QAAA6BJREFUeJzt3L1O21AYBuDXFdnaCdUOEmJpBUJqVyqxhIo9QyeGLB0qRd16BcBe0TUXwNyBvSoMvYJORWVBlUiMOhGVoVXdITnWiYmDUzh//t5HikgcJ/Z77M/HfwEgIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiCkhke4JxM8mmDU/7A+vzYpvk7PA0v5UJF4MvfPh8Y5w/717mz+u0QkjOjgDyG5+YaoBpwadRjVGHFUFydgSS30oBqAZ4/OTBzHEvz/4CNVoRJGdHIPlnz9Udxc0kWzo6ASo0gBpnZ2MdnS99k7NlheTsCCi/0QIAgO3FNexsrM/9uaWjk9KDplBIzo5A8hsvgHlsL67deF6HFaEKydnhML/xAvj089vM97cX1/JH8TOqCw2V5OwIJP+ClakUKryM3mC3NV5IJGeH5/mtFEDdFug8JGdHAPm9OgaYpi4HhP9DcnZYyu99ARCZxAIg0VgAJBoLgERjAZBoLABD0v4gumi37vw9oZ4JCiW/0QK4r0YIFfP7n589AIlm/Epw2h9EaLeypaMTnB+fAgB+pz8AAI14eWJcNbz4XmN8Y1SI98gzv9/5rf0kUr+56fz4dCLsNI14GStbq/lrvSsNbUVgfn/zW/1NcNkdfmrLoOjBiy7arSBXADC/l/mN7wLFzSQb7O0DAJJ2C6or1EPOCqw7Pz5Fw9icmiE9P0ZbbGS9npf5jRZAfvqq8wo4/JgPX9lazau+Sng1buPgjbF5NUF6/jI+5TfWlaqFP/j+FQCQPH0+8f6vzi4w5UCoaGVrFcVTaSHsAkjPr8myYQoU2sCX/EZ7ALXwddfvuwCAYectMFpRZn7HxcHob2ALHWD+qXzLb/wYoLjlUx4djrYA17d8/qqzDxf/we6+SM9fxpf8RgtALXxVvXEzyZ5tvqj02bPN1wCAq4AXvvT8SvQwBsZbe9/yGyuAu3RZKnzI3b70/Bo9Q6V7emzmt9rAM/45qj5OXRb8DczvX34nDT1xbnxvF+o5AETdrrP5skV6fgBZ1uvlL6JuF+q1iPxxM8myYZo/9Nch3vo7L+n5x6dGJx5qWNXdpPvCu0FJNBYAeWV80cxaL8ACIBcidWrUNRYAecdmL+CsAMqukEohPX9RNkzholdwUgB1Pc9dlfT8Y17sBnEXiJxyXQQsAHLJeU/oTQFI3yeWnl9ns1dwWoHqqmfaH0T6FVAp+8jS84+Vne2R1AZERERERERE5v0Dq6GKRN7L9BkAAAAASUVORK5CYII="

RIGHT_SHEET_B64 = "iVBORw0KGgoAAAANSUhEUgAAAMAAAABACAYAAABMbHjfAAAAAXNSR0IArs4c6QAAA69JREFUeJzt3L9O21AUBvDPFdnohGobCbG0AiG1K5VYQsWeoRNDlg6VWPsEhL1qX4K5A3vVMPQJOjUqS1SJOBUTqAyt6g5wrWvjBBK418c+309CihMn8Xd8j/8kDgARERERERERERERERERERERERERERERERFRjQS+3zCMo7Ts/vEo8b4sVdFeA0n5vbxhMfDCxy835vn77lV2u4kDQXsNpOZ3/iYmeFngMqYITRoA2msgOb+XBjDBnzx9NHXeXyf/gIYOAM01kJx/+tLcUxhH6fLRMXCH4Gae3c0NdL+OXC6WV9prID2/0wYAgJ2ldexubsz8vOWj44knS3WjvQaS8ztvgFnsLK3fuN2EATAL7TXwnd95A3w++z718Z2l9eyv+Byz66w77TWQnH/B6atb7HCT2IW6rWh1pL0GEvN7aYCmrch5aK+B1PyizgHKNOVE8D6018BlfvENQOQSG4BUYwOQamwAUo0NQKqxAUg1pw0wHiXBaaft8i3E014D6fm5B3DMvhpyXqeddm0vi5ae3/k3weNREqDTTpePjjHsDwAAf8Y/AQCtcCU3r7m/+FjrupB1HATa8xtzZ//w1ulyeftJpL0VGPYHucBlWuEKVrfXsml7N1q3gaA5v/TsXn8TPGlXaLYOhh2+qI6HA8rzp2Ecic3u/BAojKM06R0AAKJOG+ZQwA46LbRt2B+g5WxJ3VCePwWApHcgNrvzn0QCALqvc/evbq9h2B/c6P5JzLyujwcfmuL8qRn86cU494C07M52pWblJz++AQCiZy9yj//u7gMlJ0NFq9trKH6MVodDAOX509zAP/yEqLefTUrK7rQBzMqHNQAu3+8BAM67B2a+O71eDVZ6jvL8uQYIFkOEcSQyu/NzgOKWz3h8eLUVuLzl+dfFqtPKz9GaP1gMc5PmkAjCsjttALPyTQeHcZQ+33p5p+eebL0BAJzXcOUbivOXLrPE7M4a4D67LVOAmu32c7Tnn5fv7F4LPOWfotrzNHbFa84vNXslhc59Nt7bh7kNAMHeXmXL5Yvm/JqzZ8I4StOLcfZnT2v48bfy/Lns9rR9ouwLrwYl1dgAJELhY1Nv2AAVsE/8ZnlMAe/H/2yAilW15aMrlTXApG9INbIvmWg4cSf4lTRAEz/nfgga9gbFa4SKV4v6xkMgebhx8IgNIISGrb/Nznt9u5LGF9MAys4JgmAxzAaBNRgav/W3cgcQ0PiVFtx86zkeJYH9DSjPEYiIiIiIiIiIHth/rvWM7CdWvZYAAAAASUVORK5CYII="

BOSS_ATTACK_SHEET_B64 = "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"

ENEMY_ATTACK_SHEET_B64 = "iVBORw0KGgoAAAANSUhEUgAAAUAAAABACAYAAABr564eAAAAAXNSR0IArs4c6QAACKtJREFUeJztnTFy3DoMhqE37wAZu4hLV3sMH8J1JsV2sa/g2WJnr2Cnc/Hm1TmEj+EqpV0k827AV3jBQBBJURJFgSS+mZ3ZXUuyfhAEQVDSAiiKoiiKoiiKoiiKoiiKoiiKoiiKoiiKoiiKoiiKoiiKohRGt/H/N47vtj4nRclF6/6/uf4tjO0S/eePxkDXddCII2zuABvTov7W/V+U/txGDop3UKMTiHKADWhZf+v+L05/TgNPFY/U5ATiHCAzLetv3f9F6v9rzYMT5oqviTk2qMluLeuvRcdcxOrPFQBbR6wDZKJ1/YpQcgRA6/zGxPeDKdsqimBa93/R+nPUF1IoKbkO0nOAc4F/fKd6FgNU/3JKtoFo/RoA10f1L0f1l4to/TmmwCU3nqIspXX/F61fF0HWR7QDZKB1/YpgNguAviKn43vtQEp1tO7/CfSbFNNr6RdC19L4A+2+BQHH9zXYoHX9sIL/m4htJJFCv+8Ys22wSQCcsBpYSuPG0PIAAKofAG0wZTX8DG6cPABkZNbVAJxvNze9z99fXvDtrAOKzABvdzv48fqKH0to3Bh0AMA3bemfHPhvd7veZ9IXfAFAop1mT0+5fh/ULtIDoEFR7KQBAGB/PAEAwPPhwX7HgiAisaFjMR5NA8h2JevltKbfwDlgvb+92S9D+vfHk+0DMUFAWJIwCHgYrFPo9+y3WPffSw8QgTUMijg+PsHPX797G11fXsDx8QkO93f2u9vdDj5fXdnP319eSqt7IAPnwKAPZ+0AYLX/eH3FIGAK1OoiVn8HH/pNgfqdAQA7P+/AVL+LT1++AgDAf//+49xfmF1ssAcS8EKBb6r+M8k1rxkArUO4RrPry4tesDs+PvXeH+7v4Ha3g/e3NxsEv93c0Dl/KRggWQ2Oclw/QkdBur8wh5+C1f/py1eAszaH/s4zbSpB/2gAANa2fNAD1geeDw+wP57g05evNAhItIHBQM/1cubqv768gB8f2yX3hTUM6nQGGEl/KTQAcoSl/SEGAwANgC4wM34+PPSy36WF3o3o6R/TjuA2Bek3fJpLQX91lXkIvuDvspkkG0TX+ZboBxIwgQVNdozJpDZmMPjxKa7diRXFQ8YiWaAkR+AM6j8YAIBlP1Q71e2Y/oNwzZSBfpzS8MyP6vcNACBbfzAI8HKPy6dDi0L742m1zp8AV4nC2iNGO/j126DIp8vUHtC3yWQ7pJwCG7pCNSXz4+KvLy+o4egfTSlTYL5a58MV/BDH9L+Umph13s9XV/D+9manNIMNSdtjm8euAgrCGwRiAsDYijg9Bp0mgj8g5mKQudE2jtEOfv3o6wb3xWPz9YOYmYWPVWqArsLv/njqnXho1Dvc38H+eMKMkXb6seuhJGDPjU+LfEHAQYcLAXgMmg0VgNcG8KfE0es8bADobnc7U4j2YBCAGVkfPfbz4aGXBfHOj4fb8vd9aFDm50e09+w041KoQSBMURpIFQAN9Gs1lA4ADMvqpl4IyRtYdBYUc+kDLwdw+9D9MBCWlAWG6mLwod+EspeCtI8GgTO9wXuC/zuzIPp5bvaTggnBD2gQnHEhtN0BBwX+/RxSOVNodcY6CBootsGw/rFkjr8Boav1DdqB18Ico1pv6s+uo5RuB2+G7tJPan+dw5ekazcRQaDXlhOPH7odrNsw+wPUHhjIvPFgAtLa24lPlDkbyeyPJ7M/nvAG5qgX7nN8fKLfS2bsPK0upsllm6nHlkRQA9fq8Q3X8SRqH7TlhHaMfUllzjmK0p/qaTDeKD0n80Po9mSUle4YXczIFypsu7YPHFcaxnOuzvZC7Q7f4JmOWO1shsJfyBKfle7rMW0jUv+aj8MyQDp6TPBzPSIHa2M/f/2G4+OTfQnF5wg9YXwZ31Mzmvo/JDPQj21YgfZQEJg1WHseFSV50PfRrP7Q1GbWC6eNBU2HkaCegqc/sYR0+ab/petP4vP0ZT6iQik2KUb/WiOqCU19pz4OJ3ChpHSCjTVSQEZK0OljzFm9dwCwbUoDNXXGGEN9d8mjoPCYS08uA8XoXy0ArnDMEhqek8oOJWqHxvW33geK0L9WDVB00VpRMpDS/0vsT0Xoz/abIBX90PMiWrdDY/pTdNzSAh9FvP61jTvZ2wM1glIdIcoGI7WRUrWD6u8RtIXnFrpatEOsL/DbItc8obUfiBpT5O7vUFfwi6ZV3Ugr+mmQYx3c109MTXYI6ffcJ7+q/lw/jD43FS6x9sGZq7903Ujr+pHRRGDLe3ozMHk2SALianWT3E5mPCPAIPpXmP4D1em6y+V8SUxtmikt6zf84m/XfcKBZ+iVbpcx/QaIL+SywWY/jN4q/KkecG7siXdEFEuj+m0GE3Nn1PXlhb1bKEcWlIEY/R2Q2wpz2SBnAAyePP5OxpR9CiQ4gp1Hv9o0U5rVz3/v4gy3R8cfkQaVBMFY/cAe8rq2DXIFwF56CxEPM4x8cKiiiMdz37N3MBgJAKUxmPqe8enPGgSzZYCeBxj0jHC4v2shC3Ti0N0UFes3MO2hIB1mgp7bJEvqD5Om/gSvDVIPBJvUAD0LHDbyVzDq+TC+xz+x0bEkJ59Ca/p7OkiQjynm9/rD9eVFaf1hMOubqB9cNkiNtEUQaxgmtpYOwemAaRX8qK81qFm/DQAY3Gescg+mg4XgXNGducrvs0GSmJA1AMau9LkeFV8Bxte5C3TwObSkf5D9LKDIy18SD2S9xCjlsbNngJE1kGpxDAJd4G/V0Yj+VXy4xDpp4JrHyawxUG41BR41xJrz/q1xDQKV3wXQo0X9S/245Cw5UR+2U+GUtpBWA0RsgCy54UfoPO9boSn9C+9ysauiJZLwDp+OvZIcMAe8YBnzf+k+NXSQGBvUppnSmn7DbvGDCjTF4lqgEKld5Ek1jH2U+MbnsRU16a8pmCuKoiiKoiiKoiiKoiiKoiiKoiiKoiiKoiiKIpf/AVysq/Cy7ZiHAAAAAElFTkSuQmCC"


pygame.init()


def get_korean_font(size):
    candidates = ["malgungothic", "applegothic", "nanumgothic", "notosanscjk"]
    for name in candidates:
        font = pygame.font.SysFont(name, size)
        if font.get_ascent() > 0:
            return font
    return pygame.font.SysFont(None, size)


WIDTH, HEIGHT = 800, 600
FPS = 60

WHITE   = (255, 255, 255)
BLACK   = (0,   0,   0)
GRAY    = (20,  20,  40)
BLUE    = (50,  150, 255)
RED     = (220, 50,  50)
YELLOW  = (240, 220, 0)
GREEN   = (50,  220, 80)
ORANGE  = (240, 140, 0)
PINK = (255, 120, 200)


screen = pygame.display.set_mode(
    (WIDTH, HEIGHT),
    pygame.FULLSCREEN | pygame.SCALED
)
# idle 시트 로드
sheet_bytes = base64.b64decode(IDLE_SHEET_B64)
player_sheet = pygame.image.load(io.BytesIO(sheet_bytes)).convert_alpha()

FRAME_W, FRAME_H = 64, 64

idle_frames = []
for i in range(4):
    rect = pygame.Rect(i * FRAME_W, 0, FRAME_W, FRAME_H)
    idle_frames.append(player_sheet.subsurface(rect))


pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()
font = get_korean_font(20)
font_big = get_korean_font(72)
font.set_bold(True)
font_big.set_bold(True)
menu_font = get_korean_font(24)
menu_font.set_bold(True)

# left 시트 로드
left_bytes = base64.b64decode(LEFT_SHEET_B64)
left_sheet = pygame.image.load(io.BytesIO(left_bytes)).convert_alpha()

left_frames = []
for i in range(3):
    rect = pygame.Rect(i * FRAME_W, 0, FRAME_W, FRAME_H)
    left_frames.append(left_sheet.subsurface(rect))

left_stand_img = left_frames[-1]

#오른쪽
right_bytes = base64.b64decode(RIGHT_SHEET_B64)
right_sheet = pygame.image.load(io.BytesIO(right_bytes)).convert_alpha()

right_frames = []

for i in range(3):
    rect = pygame.Rect(i * FRAME_W, 0, FRAME_W, FRAME_H)
    right_frames.append(right_sheet.subsurface(rect))

right_stand_img = right_frames[-1]

dialogue_img = pygame.image.load("assets/player.png").convert_alpha()
dialogue_img = pygame.transform.scale(dialogue_img, (220, 220))

boss1_img = pygame.image.load("assets/boss1.png").convert_alpha()
boss1_dialogue_img = pygame.transform.scale(boss1_img, (220, 220))

boss1_battle_img = pygame.image.load("assets/boss1(1).png").convert_alpha()
boss1_battle_img = pygame.transform.scale(boss1_battle_img, (80, 80))

enemy_img = pygame.image.load("assets/enemy.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (70, 70))

boss_attack_bytes = base64.b64decode(BOSS_ATTACK_SHEET_B64)
boss_attack_sheet = pygame.image.load(io.BytesIO(boss_attack_bytes)).convert_alpha()

boss_attack_frames = []

for i in range(5):
    rect = pygame.Rect(i * 64, 0, 64, 64)
    frame = boss_attack_sheet.subsurface(rect)
    frame = pygame.transform.scale(frame, (80, 80))
    boss_attack_frames.append(frame)
    
enemy_attack_bytes = base64.b64decode(ENEMY_ATTACK_SHEET_B64)
enemy_attack_sheet = pygame.image.load(io.BytesIO(enemy_attack_bytes)).convert_alpha()

enemy_attack_frames = []

for i in range(5):
    rect = pygame.Rect(i * 64, 0, 64, 64)
    frame = enemy_attack_sheet.subsurface(rect)
    frame = pygame.transform.scale(frame, (80, 80))
    enemy_attack_frames.append(frame)

enemy_idle_img = enemy_attack_frames[0]

enemy_attack_frames = [
    enemy_attack_frames[i] for i in [3, 4, 2, 3, 0]
]

red_bullet_img = pygame.image.load(
    "assets/bullet1.png"
).convert_alpha()


red_bullet_img = pygame.transform.scale(
    red_bullet_img,
    (24, 24)
)


blue_bullet_img = pygame.image.load(
    "assets/bullet2.png"
).convert_alpha()

blue_bullet_img = pygame.transform.scale(
    blue_bullet_img,
    (24, 24)
)



score_bullet_img = pygame.image.load(
    "assets/score.png"
).convert_alpha()

score_bullet_img = pygame.transform.scale(
    score_bullet_img,
    (30, 30)
)

reflect_bullet_img = pygame.image.load(
    "assets/reflect.png"
).convert_alpha()

reflect_bullet_img = pygame.transform.scale(
    reflect_bullet_img,
    (25, 25)
)

item_img = pygame.image.load(
    "assets/item.png"
).convert_alpha()

item_img = pygame.transform.scale(
    item_img,
    (28, 28)
)

ending_img = pygame.image.load("assets/ending.png").convert_alpha()
ending_img = pygame.transform.scale(ending_img, (WIDTH, HEIGHT))

over_img = pygame.image.load("assets/over.png").convert_alpha()
over_img = pygame.transform.scale(over_img, (WIDTH, HEIGHT))

# --- 레벨 설정 ---
LEVELS = [
    {"enemy_speed": 2, "spawn": 60, "label": "Lv.1"},
    {"enemy_speed": 3, "spawn": 40, "label": "Lv.2"},
    {"enemy_speed": 5, "spawn": 25, "label": "Lv.3"},
]

# --- 사운드 자리 ---
# shoot_sound    = pygame.mixer.Sound("shoot.wav")
# explosion_sound= pygame.mixer.Sound("explosion.wav")
# hit_sound      = pygame.mixer.Sound("hit.wav")
reflect_sound = pygame.mixer.Sound("assets/sound effect/bullet.wav")
reflect_sound.set_volume(0.6)
pygame.mixer.music.load("assets/music/stage1.wav")
pygame.mixer.music.set_volume(0.5)
menu_move_sound = pygame.mixer.Sound("assets/sound effect/MENU move.wav")
menu_select_sound = pygame.mixer.Sound("assets/sound effect/MENU Select.wav")

menu_move_sound.set_volume(0.5)
menu_select_sound.set_volume(0.6)

item_sound = pygame.mixer.Sound("assets/sound effect/item.wav")
item_sound.set_volume(0.6)

enemy_shoot_sound = pygame.mixer.Sound("assets/sound effect/shoot.wav")
enemy_shoot_sound.set_volume(0.5)

gameover_sound = pygame.mixer.Sound(
    "assets/music/8bit/gameover.mp3"
)

gameclear_sound = pygame.mixer.Sound(
    "assets/music/8bit/gameclear.mp3"
)

bgm_volume = 0.5
sfx_volume = 0.6

PLAYER_W, PLAYER_H = 40, 40
ENEMY_W,  ENEMY_H  = 36, 36
BULLET_W, BULLET_H = 6,  14
ENEMY_BULLET_SPEED = 4

def draw_enemy(surf, enemy):
    rect = enemy["rect"]

    if enemy.get("attack_anim", False):
        enemy["attack_timer"] = enemy.get("attack_timer", 0) + 1

        frame_index = enemy["attack_timer"] // 4

        if frame_index >= len(enemy_attack_frames):
            enemy["attack_anim"] = False
            enemy["attack_timer"] = 0
            img = enemy_idle_img
        else:
            img = enemy_attack_frames[frame_index]
    else:
        img = enemy_idle_img

    surf.blit(
        img,
        (
            rect.centerx - img.get_width() // 2,
            rect.centery - img.get_height() // 2
        )
    )

def spawn_first_wave():
    enemies = []

    start_y = -80

    start_positions = [
        WIDTH // 2 - 60,
        WIDTH // 2 - 20,
        WIDTH // 2 + 20,
        WIDTH // 2 + 60,
    ]

    velocities = [
        (-1.6, 0.9),
        (-0.8, 0.9),
        (0.8, 0.9),
        (1.6, 0.9),
    ]

    for i in range(4):
        spawn_delay = 90 if i in [1, 2] else 210
        
        shot_times = [
            spawn_delay + 160,
            spawn_delay + 170,
            spawn_delay + 180,
            spawn_delay + 200,
            spawn_delay + 210,
            spawn_delay + 220,
            spawn_delay + 240,
            spawn_delay + 250,
            spawn_delay + 260
        ]
        
        enemies.append({
            "rect": pygame.Rect(start_positions[i] - ENEMY_W // 2, start_y, ENEMY_W, ENEMY_H),
            "vx": velocities[i][0],
            "vy": velocities[i][1],
            "stop_timer": 0,
            "hp": 2,
            "shot_index": 0,
            "shot_times": shot_times,
            "spawn_delay": spawn_delay,
            "active": False
        })

    return enemies

def spawn_second_wave():
    enemies = []

    for i in range(4):
        side = i % 2  # 0: 왼쪽, 1: 오른쪽

        if side == 0:
            x = -60
            vx = 3.2
            stop_x = 260
        else:
            x = WIDTH + 60
            vx = -3.2
            stop_x = WIDTH - 260

        y = 80 + i * 55

        enemies.append({
            "rect": pygame.Rect(x, y, ENEMY_W, ENEMY_H),
            "vx": vx,
            "vy": 1.2,
            "stop_x": stop_x,
            "spawn_delay": i * 60,  # 1초 간격
            "active": False,
            "phase": "enter",
            "timer": 0,
            "stop_timer": 0,
            "hp": 2,
            "shot_count": 0,
            "shot_timer": 0,
            "side": side,
        })

    return enemies

def update_second_wave_enemy(en, wave_timer, enemy_bullets):
    if wave_timer < en["spawn_delay"]:
        return

    en["active"] = True

    # 1. 대각선으로 등장
    if en["phase"] == "enter":
        en["rect"].x += en["vx"]
        en["rect"].y += en["vy"]

        if (en["side"] == 0 and en["rect"].centerx >= en["stop_x"]) or \
           (en["side"] == 1 and en["rect"].centerx <= en["stop_x"]):
            en["phase"] = "attack"
            en["stop_timer"] = 0
            en["shot_timer"] = 0
            en["shot_count"] = 0

    # 2. 멈춰서 3번 공격
    elif en["phase"] == "attack":
        en["stop_timer"] += 1
        en["shot_timer"] += 1

        if en["shot_timer"] >= 25 and en["shot_count"] < 3:
            en["attack_anim"] = True
            en["attack_timer"] = 0
            spawn_circle_enemy_bullets(en, enemy_bullets)
            en["shot_count"] += 1
            en["shot_timer"] = 0

        if en["shot_count"] >= 3 and en["shot_timer"] >= 25:
            en["phase"] = "exit"

    # 3. 앞으로 쭉 나가서 퇴장
    elif en["phase"] == "exit":
        en["rect"].x += en["vx"] * 2.2
        en["rect"].y += en["vy"] * 2.2
        
        
def spawn_third_wave():
    enemies = []

    configs = [
        # 왼쪽 팀
        {"side": "left", "spawn_delay": 0,   "y": 120, "shoot_delay": 0},
        {"side": "left", "spawn_delay": 0,   "y": 180, "shoot_delay": 60},

        # 오른쪽 팀
        {"side": "right", "spawn_delay": 180, "y": 120, "shoot_delay": 0},
        {"side": "right", "spawn_delay": 180, "y": 180, "shoot_delay": 60},
    ]

    for cfg in configs:

        if cfg["side"] == "left":
            x = -80
            vx = 4
            stop_x = 240
            exit_vx = -3
        else:
            x = WIDTH + 80
            vx = -4
            stop_x = WIDTH - 240
            exit_vx = 3

        enemies.append({
            "rect": pygame.Rect(x, cfg["y"], ENEMY_W, ENEMY_H),

            "side": cfg["side"],

            "vx": vx,
            "vy": 0,

            "exit_vx": exit_vx,
            "exit_vy": 3,

            "stop_x": stop_x,

            "spawn_delay": cfg["spawn_delay"],

            "phase": "enter",

            "shot_done": False,

            "timer": 0,

            "hp": 2,

            "wave": 3
        })

    return enemies

def update_third_wave_enemy(en, wave_timer, enemy_bullets):

    if wave_timer < en["spawn_delay"]:
        return

    # 등장
    if en["phase"] == "enter":

        en["rect"].x += en["vx"]

        if (
            en["side"] == "left" and en["rect"].x >= en["stop_x"]
        ) or (
            en["side"] == "right" and en["rect"].x <= en["stop_x"]
        ):

            en["phase"] = "shoot"
            en["timer"] = 0

    # 정지 후 발사
    elif en["phase"] == "shoot":

        en["timer"] += 1

        if en["timer"] == 1:
            en["attack_anim"] = True
            en["attack_timer"] = 0
            spawn_circle_enemy_bullets(en, enemy_bullets)

        if en["timer"] >= 60:
            en["phase"] = "exit"

    # 대각선 퇴장
    elif en["phase"] == "exit":

        en["rect"].x += en["exit_vx"]
        en["rect"].y += en["exit_vy"]
        
        
def spawn_fourth_wave():
    enemies = []

    enemies.append({
        "rect": pygame.Rect(WIDTH // 2 - ENEMY_W // 2, -80, ENEMY_W, ENEMY_H),
        "vx": 0,
        "vy": 2.5,
        "stop_y": 150,
        "phase": "enter",
        "timer": 0,
        "hp": 6,
        "wave": 4,
        "shot_index": 0,
        "shot_times": [60, 70, 90, 100],
        "green_side": 0,
    })

    return enemies


def update_fourth_wave_enemy(en, wave_timer, enemy_bullets):
    if en["phase"] == "enter":
        en["rect"].y += en["vy"]

        if en["rect"].centery >= en["stop_y"]:
            en["phase"] = "attack"
            en["timer"] = 0

    elif en["phase"] == "attack":
        en["timer"] += 1

        if en["shot_index"] < len(en["shot_times"]):
            if en["timer"] >= en["shot_times"][en["shot_index"]]:
                en["attack_anim"] = True
                en["attack_timer"] = 0
                spawn_circle_enemy_bullets(en, enemy_bullets)
                en["shot_index"] += 1

        if en["shot_index"] >= 4 and en["timer"] >= 360:
            en["phase"] = "exit"

    elif en["phase"] == "exit":
        en["rect"].y += 4
            
def spawn_circle_enemy_bullets(enemy, enemy_bullets):
    enemy_shoot_sound.play()
      
    cx = enemy["rect"].centerx
    cy = enemy["rect"].centery
    
    base_angle = enemy.get("angle_offset", 0)

    for i in range(16):
        angle = base_angle + i * (360 / 16)
        rad = math.radians(angle)

        bullet_color = RED
        bullet_type = "normal"
        
        
        if enemy.get("wave") == 4:
            if enemy["shot_index"] in [1, 2]:
                green_i = 3
            else:
                green_i = 4

            if i == green_i:
                bullet_color = GREEN
                bullet_type = "reflect"
                angle = 90 + random.randint(-20, 20)
                rad = math.radians(angle)

        elif enemy.get("vx", 0) < -1:
            if i == 5:
                bullet_color = GREEN
                bullet_type = "reflect"

        elif enemy.get("vx", 0) > 1:
            if i == 3:
                bullet_color = GREEN
                bullet_type = "reflect"

        else:
            if i == 4:
                bullet_color = GREEN
                bullet_type = "reflect"

        enemy_bullets.append({
            "x": cx,
            "y": cy,

            "vx": math.cos(rad) * 8,
            "vy": math.sin(rad) * 8,

            "friction": 0.985,
            "min_speed": 1.0,

            "size": 9,
            "color": bullet_color,
            "type": bullet_type,
            
            "angle": angle
        })
    enemy["angle_offset"] = enemy.get("angle_offset", 0) + 12

def spawn_power_items(enemy, items, count=None):
    if count is None:
        count = random.randint(3, 5)

    for i in range(count):
        angle = random.uniform(-1.8, -1.3)
        speed = random.uniform(0.8, 1.6)

        items.append({
            "x": enemy["rect"].centerx,
            "y": enemy["rect"].centery,
            "vx": math.cos(angle) * speed * random.choice([-1, 1]),
            "vy": math.sin(angle) * speed,
            "gravity": 0.025,
            "size": 8,
            "type": "power",
            "timer": 0
        })
        
def draw_stars(stars):
    for s in stars:
        pygame.draw.circle(screen, WHITE, (s[0], s[1]), s[2])

def draw_hud(score, lives, item_count, level_cfg):
    box_w = 230
    box_h = 120
    box_x = WIDTH - box_w - 20
    box_y = 20

    pygame.draw.rect(screen, (5, 5, 20), (box_x, box_y, box_w, box_h))
    pygame.draw.rect(screen, WHITE, (box_x, box_y, box_w, box_h), 2)

    screen.blit(font.render(f"Score: {score}", True, WHITE), (box_x + 15, box_y + 15))
    screen.blit(font.render(f"Life: {'♥ ' * lives}", True, RED), (box_x + 15, box_y + 50))
    screen.blit(font.render(f"Power: Lv.{item_count}", True, YELLOW), (box_x + 15, box_y + 85))


def draw_stage_text(stage_num, frame):
    if frame > 120:
        return

    text = font_big.render(f"STAGE {stage_num}", True, WHITE)
    temp = text.copy()

    if frame < 40:
        alpha = frame * 6
    elif frame < 80:
        alpha = 255
    else:
        alpha = max(0, 255 - (frame - 80) * 6)

    temp.set_alpha(alpha)

    screen.blit(
        temp,
        (
            WIDTH // 2 - temp.get_width() // 2,
            HEIGHT // 2 - temp.get_height() // 2
        )
    )

def game_over_screen(score):
    pygame.mixer.music.stop()
    gameover_sound.play()

    selected = 0
    menu = ["처음화면", "종료"]

    while True:
        screen.blit(over_img, (0, 0))

        for i, text in enumerate(menu):
            outline = menu_font.render(text, True, BLACK)
            item = menu_font.render(text, True, WHITE)

            x = WIDTH // 2 - item.get_width() // 2
            y = 420 + i * 45

            screen.blit(outline, (x - 2, y))
            screen.blit(outline, (x + 2, y))
            screen.blit(outline, (x, y - 2))
            screen.blit(outline, (x, y + 2))

            screen.blit(item, (x, y))

            if selected == i:
                pygame.draw.polygon(screen, YELLOW, [
                    (x - 15, y + 12),
                    (x - 35, y),
                    (x - 35, y + 24),
                ])

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key in [pygame.K_UP, pygame.K_DOWN]:
                    selected = 1 - selected
                    menu_move_sound.play()

                if e.key == pygame.K_RETURN:
                    menu_select_sound.play()

                    if selected == 0:
                        return "title"

                    if selected == 1:
                        pygame.quit()
                        sys.exit()
                        
def confirm_exit_screen():
    selected = 1  # 0: 예, 1: 아니오

    while True:
        screen.fill((10, 10, 30))

        msg = font.render("나가시겠습니까?", True, WHITE)
        yes = font.render("예", True, WHITE)
        no = font.render("아니오", True, WHITE)

        screen.blit(msg, (WIDTH // 2 - 120, HEIGHT // 2 - 80))

        options = [yes, no]
        positions = [
            (WIDTH // 2 - 80, HEIGHT // 2),
            (WIDTH // 2 + 40, HEIGHT // 2),
        ]

        for i, option in enumerate(options):
            screen.blit(option, positions[i])
            if selected == i:
                x, y = positions[i]
                pygame.draw.polygon(screen, YELLOW, [
                    (x - 10, y + 8),
                    (x - 25, y),
                    (x - 25, y + 16),
                ])

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
            
                if e.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    selected = 1 - selected

                if e.key == pygame.K_RETURN:
                    if selected == 0:
                        pygame.quit()
                        sys.exit()
                    else:
                        return

                if e.key == pygame.K_ESCAPE:
                    selected = 1

def dialogue_screen(lines):
    line_index = 0
    char_index = 0
    text_timer = 0

    while line_index < len(lines):
        clock.tick(FPS)

        for e in pygame.event.get():
            
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    enemies = []
                    enemy_bullets = []
                    items = []

                    wave_id = 4
                    wave_timer = 0
                    wave_clear_timer = 0

                    dialogue_active = True
                    dialogue_done = True
                    dialogue_line_index = 0
                    dialogue_char_index = 0
                    dialogue_timer = 0

                    boss_intro_started = False
                    boss_enemy = None
                    boss_attack_anim = False
                    boss_attack_frame = 0
                    boss_attack_timer = 0
                    boss1_x = WIDTH + 200
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_z or e.key == pygame.K_RETURN:
                    if char_index < len(lines[line_index]):
                        char_index = len(lines[line_index])
                    else:
                        line_index += 1
                        char_index = 0
                        text_timer = 0

        screen.fill(GRAY)
        draw_stars([(random.randint(0, WIDTH), random.randint(0, HEIGHT), 1) for _ in range(40)])

        screen.blit(dialogue_img, (40, 260))

        pygame.draw.rect(screen, (5, 5, 25), (40, 430, 720, 130))
        pygame.draw.rect(screen, WHITE, (40, 430, 720, 130), 3)

        if line_index < len(lines):
            text_timer += 1
            if text_timer >= 3 and char_index < len(lines[line_index]):
                char_index += 1
                text_timer = 0

            shown_text = lines[line_index][:char_index]
            text = font.render(shown_text, True, WHITE)
            screen.blit(text, (70, 470))

        pygame.display.flip()
        
        
def ending_screen():
    selected = 0
    menu = ["처음화면", "종료"]

    while True:
        screen.blit(ending_img, (0, 0))

        for i, text in enumerate(menu):
            item = font.render(text, True, WHITE)
            x = WIDTH // 2 - item.get_width() // 2
            y = 420 + i * 45
            screen.blit(item, (x, y))

            if selected == i:
                pygame.draw.polygon(screen, YELLOW, [
                    (x - 15, y + 12),
                    (x - 35, y),
                    (x - 35, y + 24),
                ])

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key in [pygame.K_UP, pygame.K_DOWN]:
                    selected = 1 - selected
                    menu_move_sound.play()

                if e.key == pygame.K_RETURN:
                    menu_select_sound.play()

                    if selected == 0:
                        return "title"

                    if selected == 1:
                        pygame.quit()
                        sys.exit()

def apply_sfx_volume():
    menu_move_sound.set_volume(sfx_volume)
    menu_select_sound.set_volume(sfx_volume)
    item_sound.set_volume(sfx_volume)
    enemy_shoot_sound.set_volume(sfx_volume)
    reflect_sound.set_volume(sfx_volume)
    gameover_sound.set_volume(sfx_volume)
    gameclear_sound.set_volume(sfx_volume)
    
    
def pause_screen():
    global bgm_volume, sfx_volume

    selected = 0
    menu = ["BGM 볼륨", "효과음 볼륨", "계속하기", "처음화면", "종료"]

    while True:
        screen.fill((10, 10, 30))

        title = font_big.render("PAUSE", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 80))

        for i, text in enumerate(menu):
            if i == 0:
                label = f"{text}: {int(bgm_volume * 10)}"
            elif i == 1:
                label = f"{text}: {int(sfx_volume * 10)}"
            else:
                label = text

            outline = menu_font.render(label, True, BLACK)
            item = menu_font.render(label, True, WHITE)

            x = WIDTH // 2 - item.get_width() // 2
            y = 210 + i * 50

            for ox, oy in [
                (-2, -2), (-2, 0), (-2, 2),
                (0, -2),           (0, 2),
                (2, -2),  (2, 0),  (2, 2)
            ]:
                screen.blit(outline, (x + ox, y + oy))

            screen.blit(item, (x, y))

            if selected == i:
                pygame.draw.polygon(screen, YELLOW, [
                    (x - 15, y + 12),
                    (x - 35, y),
                    (x - 35, y + 24),
                ])

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    selected = (selected - 1) % len(menu)
                    menu_move_sound.play()

                if e.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(menu)
                    menu_move_sound.play()

                if e.key == pygame.K_LEFT:
                    if selected == 0:
                        bgm_volume = max(0, bgm_volume - 0.1)
                        pygame.mixer.music.set_volume(bgm_volume)
                    elif selected == 1:
                        sfx_volume = max(0, sfx_volume - 0.1)
                        apply_sfx_volume()

                if e.key == pygame.K_RIGHT:
                    if selected == 0:
                        bgm_volume = min(1, bgm_volume + 0.1)
                        pygame.mixer.music.set_volume(bgm_volume)
                    elif selected == 1:
                        sfx_volume = min(1, sfx_volume + 0.1)
                        apply_sfx_volume()

                if e.key == pygame.K_ESCAPE:
                    return "continue"

                if e.key == pygame.K_RETURN:
                    menu_select_sound.play()

                    if selected == 2:
                        return "continue"

                    if selected == 3:
                        return "title"

                    if selected == 4:
                        pygame.quit()
                        sys.exit()

def option_screen():
    global bgm_volume, sfx_volume

    selected = 0
    menu = ["BGM 볼륨", "효과음 볼륨", "돌아가기"]

    while True:
        screen.fill((10, 10, 30))

        title = font_big.render("OPTION", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

        for i, text in enumerate(menu):
            if i == 0:
                label = f"{text}: {int(bgm_volume * 10)}"
            elif i == 1:
                label = f"{text}: {int(sfx_volume * 10)}"
            else:
                label = text

            item = menu_font.render(label, True, WHITE)
            x = WIDTH // 2 - item.get_width() // 2
            y = 250 + i * 60

            screen.blit(item, (x, y))

            if selected == i:
                pygame.draw.polygon(screen, YELLOW, [
                    (x - 15, y + 12),
                    (x - 35, y),
                    (x - 35, y + 24),
                ])

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                confirm_exit_screen()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    selected = (selected - 1) % len(menu)

                if e.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(menu)

                if e.key == pygame.K_LEFT:
                    if selected == 0:
                        bgm_volume = max(0, bgm_volume - 0.1)
                        pygame.mixer.music.set_volume(bgm_volume)
                    elif selected == 1:
                        sfx_volume = max(0, sfx_volume - 0.1)
                        apply_sfx_volume()

                if e.key == pygame.K_RIGHT:
                    if selected == 0:
                        bgm_volume = min(1, bgm_volume + 0.1)
                        pygame.mixer.music.set_volume(bgm_volume)
                    elif selected == 1:
                        sfx_volume = min(1, sfx_volume + 0.1)
                        apply_sfx_volume()

                if e.key == pygame.K_RETURN:
                    if selected == 2:
                        return

                if e.key == pygame.K_ESCAPE:
                    return

def title_screen():
    menu = ["게임시작", "설정", "종료"]
    selected = 0

    while True:
        screen.fill((10, 10, 30))

        title = font_big.render("HANSHA", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 130))

        for i, text in enumerate(menu):
            item = font.render(text, True, WHITE)
            x = WIDTH // 2 - item.get_width() // 2
            y = 270 + i * 60
            screen.blit(item, (x, y))

            if selected == i:
                pygame.draw.polygon(screen, YELLOW, [
                    (x - 15, y + 12),
                    (x - 35, y),
                    (x - 35, y + 24),
                ])

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                confirm_exit_screen()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    selected = (selected - 1) % len(menu)
                    menu_move_sound.play()

                if e.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(menu)
                    menu_move_sound.play()

                if e.key == pygame.K_ESCAPE:
                    selected = 2

                if e.key == pygame.K_RETURN:
                    menu_select_sound.play()
                    if selected == 0:
                        pygame.mixer.music.play(-1)  # 무한 반복
                        return "start"

                    elif selected == 1:
                        option_screen()
                      

                    elif selected == 2:
                        confirm_exit_screen()
                        
def boss_rotate_pattern(boss_rect, enemy_bullets, timer):
    enemy_shoot_sound.play()
    
    cx = boss_rect.centerx
    cy = boss_rect.centery
    

    for i in range(35):
        angle = (timer // 30) * 12 + i * 20

        rad = math.radians(angle)

        bullet_color = RED
        bullet_type = "normal"

        enemy_bullets.append({
            "x": cx,
            "y": cy,
            "vx": math.cos(rad) * 7,
            "vy": math.sin(rad) * 7,

            "friction": 0.985,
            "min_speed": 1.0,

            "size": 9,
            "color": bullet_color,
            "type": bullet_type
        })
        
def boss_expand_contract_gap_pattern(boss_rect, enemy_bullets, timer):
    enemy_shoot_sound.play()

    cx = boss_rect.centerx
    cy = boss_rect.centery

    bullet_count = 36
    angle_gap = 360 / bullet_count

    # 1차: 넓은 간격 원형탄
    for i in range(bullet_count):
        angle = i * angle_gap
        rad = math.radians(angle)

        enemy_bullets.append({
            "x": cx,
            "y": cy,
            "vx": math.cos(rad) * 7,
            "vy": math.sin(rad) * 7,
            "friction": 0.96,
            "min_speed": 0.4,
            "size": 9,
            "color": RED,
            "type": "contract",
            "timer": 0,
            "phase": "expand",
            "repeat": 0
        })

    # 2차: 1차 탄 사이 틈으로 들어가는 탄
    for i in range(bullet_count):
        angle = i * angle_gap + angle_gap / 2
        rad = math.radians(angle)

        enemy_bullets.append({
            "x": cx,
            "y": cy,
            "vx": math.cos(rad) * 6,
            "vy": math.sin(rad) * 6,
            "friction": 0.985,
            "min_speed": 1.0,
            "size": 7,
            "color": BLUE,
            "type": "normal",
            "delay": 100
        })
        
def boss_homing_eight_pattern(boss_rect, enemy_bullets, player):
    enemy_shoot_sound.play()

    cx = boss_rect.centerx
    cy = boss_rect.centery

    bullet_count = 10

    for i in range(bullet_count):
        angle = i * (360 / bullet_count)
        rad = math.radians(angle)

        bullet_color = BLUE
        bullet_type = "eight_homing"

        # 왼쪽/오른쪽 쪽 탄 4개를 반사탄으로
        if i in [2, 3, 7, 8]:
            bullet_color = GREEN
            bullet_type = "eight_reflect"

        enemy_bullets.append({
            "x": cx,
            "y": cy,
            "start_x": cx,
            "start_y": cy,
            "vx": math.cos(rad) * 3,
            "vy": math.sin(rad) * 3,
            "base_angle": angle,
            "timer": 0,
            "size": 9,
            "color": bullet_color,
            "type": bullet_type,
            "last_vx": math.cos(rad) * 5,
            "last_vy": math.sin(rad) * 5
        })
            
def main():
    pygame.mixer.music.load("assets/music/stage1.wav")
    pygame.mixer.music.play(-1)
    
    stage_text_frame = 0
    player = pygame.Rect(WIDTH // 2 - PLAYER_W // 2, HEIGHT - 70, PLAYER_W, PLAYER_H)
    bullets = []
    enemy_bullets = []
    enemies = spawn_first_wave()
    wave_id = 1
    wave_clear_timer = 0
    wave_timer = 0
    score    = 0
    lives    = 3
    shoot_cd = 0
    spawn_timer = 0
    level_idx = 0
    level_cfg = LEVELS[level_idx]
    invincible = 0
    item_count = 0
    items = []
    power_items = 0
    power_level = 1
    player_anim_timer = 0
    player_frame_index = 0
    boss_attack_delay = -1
    boss_attack_timer = 0
    boss1_hp = 40
    boss_dead_effect = False
    boss_dead_timer = 0
    boss_score_popup = False
    boss_defeated = False
    boss1_max_hp = 40
    boss1_timer = 0
    boss1_shot_index = 0
    boss1_shot_times = [120, 130, 140, 160, 170, 180, 200, 210, 220]
    
    player_state = "idle"

    player_anim_timer = 0
    player_frame_index = 0

    move_anim_timer = 0
    move_anim_index = 0
    
    boss_intro_started = False
    boss_enemy = None
    boss_attack_anim = False
    boss_attack_frame = 0
    boss_attack_timer = 0
        
    dialogue_active = False
    
    dialogue_lines = [
        {"speaker": "left", "text": "별거없네"},
        {"speaker": "left", "text": "꽤 유명해서 기대했는데 말이야."},
        {"speaker": "left", "text": "설마, 이게 끝?"},
        {"speaker": "right", "text": "그렇게 무시하면 섭하지"},
        {"speaker": "right", "text": "조금 혼날 필요가 있어보이는데"},
        {"speaker": "left", "text": "흠"},
        {"speaker": "left", "text": "역시 이렇게 쉬울리 없지"},
        {"speaker": "right", "text": "거만하긴"},
    ]
    
    
    dialogue_line_index = 0
    dialogue_char_index = 0
    dialogue_timer = 0
    dialogue_img_x = -360
    boss1_x = WIDTH + 200
    dialogue_done = False

    stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 2))
             for _ in range(80)]

    while True:
        clock.tick(FPS)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE and not dialogue_active:
                    result = pause_screen()

                    if result == "continue":
                        pass

                    elif result == "title":
                        return
                
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_1:
                        enemies = []
                        enemy_bullets = []
                        items = []

                        wave_id = 4
                        wave_timer = 0
                        wave_clear_timer = 0

                        dialogue_active = True
                        dialogue_done = True
                        dialogue_line_index = 0
                        dialogue_char_index = 0
                        dialogue_timer = 0

                        boss_intro_started = False
                        boss_enemy = None
                        boss1_x = WIDTH + 200
                        
                if e.key == pygame.K_2:
                    boss_attack_anim = True
                    boss_attack_frame = 0
                    boss_attack_timer = 0
                        
                if dialogue_active and (e.key == pygame.K_z or e.key == pygame.K_RETURN):
                    if dialogue_char_index < len(dialogue_lines[dialogue_line_index]["text"]):
                        dialogue_char_index = len(dialogue_lines[dialogue_line_index]["text"])
                    else:
                        dialogue_line_index += 1
                        dialogue_char_index = 0
                        dialogue_timer = 0

                        if dialogue_line_index >= len(dialogue_lines):
                            dialogue_active = False

                            if boss_defeated:
                                boss_enemy = None
                                
                                pygame.mixer.music.stop()
                                gameclear_sound.play()
                                
                                result = ending_screen()

                                if result == "title":
                                    return

                            boss1_timer = 0
                            boss1_shot_index = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= 6
            player_state = "left"

        elif keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += 6
            player_state = "right"

        else:
            player_state = "idle"

        if keys[pygame.K_UP] and player.top > 0:
            player.y -= 6

        if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
            player.y += 6


        # idle 숨쉬기 애니메이션
        if player_state == "idle":
            player_anim_timer += 1

            if player_anim_timer >= 12:
                player_anim_timer = 0
                player_frame_index = (player_frame_index + 1) % len(idle_frames)

        # 좌우 이동 애니메이션
        else:
            move_anim_timer += 1

            if move_anim_timer >= 6:
                move_anim_timer = 0

                if player_state == "left":
                    move_anim_index = min(move_anim_index + 1, len(left_frames) - 1)

                elif player_state == "right":
                    move_anim_index = min(move_anim_index + 1, len(right_frames) - 1)

        bullets = [b for b in bullets if b.bottom > 0]
        for b in bullets:
            b.y -= 10

        wave_timer += 1

        alive_enemies = []
        
        if boss_enemy is not None and not dialogue_active:
            boss1_timer += 1

            if boss1_shot_index < len(boss1_shot_times):
                shot_time = boss1_shot_times[boss1_shot_index]

                if boss1_timer >= shot_time:
                    boss_attack_anim = True
                    boss_attack_frame = 0
                    boss_attack_timer = 0

                    spawn_circle_enemy_bullets(
                        {
                            "rect": boss_enemy,
                            "vx": 0,
                            "wave": 4,
                            "shot_index": boss1_shot_index,
                            "angle_offset": boss1_shot_index * 12
                        },
                        enemy_bullets
                    )

                    boss1_shot_index += 1
                    
            if 180 < boss1_timer < 750:
                if boss1_timer % 20 == 0:
                    boss_attack_anim = True
                    boss_attack_frame = 0
                    boss_attack_timer = 0

                    boss_rotate_pattern(boss_enemy, enemy_bullets, boss1_timer)

            if boss1_timer in [780, 980]:
                boss_attack_anim = True
                boss_attack_frame = 0
                boss_attack_timer = 0

                boss_expand_contract_gap_pattern(boss_enemy, enemy_bullets, boss1_timer)

            if boss1_timer in [1300, 1450, 1600, 1750, 1900]:
                boss_attack_anim = True
                boss_attack_frame = 0
                boss_attack_timer = 0

                boss_homing_eight_pattern(boss_enemy, enemy_bullets, player)
    
            if boss1_timer >= 2100:
                boss1_timer = 180
                boss1_shot_index = 0
            
        for en in enemies:
            if wave_id == 1:
                if wave_timer < en["spawn_delay"]:
                    alive_enemies.append(en)
                    continue

                en["active"] = True

                if en["stop_timer"] > 0:
                    en["stop_timer"] -= 1
                else:
                    en["rect"].x += en["vx"]
                    en["rect"].y += en["vy"]

                if en["shot_index"] < len(en["shot_times"]):
                    shot_time = en["shot_times"][en["shot_index"]]

                    if wave_timer >= shot_time - 10 and en["stop_timer"] <= 0:
                        en["stop_timer"] = 10

                    if wave_timer >= shot_time:
                        en["attack_anim"] = True
                        en["attack_timer"] = 0
                        spawn_circle_enemy_bullets(en, enemy_bullets)
                        en["shot_index"] += 1

            elif wave_id == 2:
                update_second_wave_enemy(en, wave_timer, enemy_bullets)
            
            elif wave_id == 3:
                update_third_wave_enemy(en, wave_timer, enemy_bullets)
                
            elif wave_id == 4:
                update_fourth_wave_enemy(en, wave_timer, enemy_bullets)

            if -150 < en["rect"].x < WIDTH + 150 and en["rect"].y < HEIGHT + 700:
                alive_enemies.append(en)

        enemies = alive_enemies
        
        if len(enemies) == 0:
            wave_clear_timer += 1
        else:
            wave_clear_timer = 0
            
        if wave_id == 1 and wave_clear_timer > 60:
            enemies = spawn_second_wave()
            wave_id = 2
            wave_timer = 0
            wave_clear_timer = 0

        if wave_id == 2 and wave_clear_timer > 60:
            enemies = spawn_third_wave()
            wave_id = 3
            wave_timer = 0
            wave_clear_timer = 0

        if wave_id == 3 and wave_clear_timer > 60:
            enemies = spawn_fourth_wave()
            wave_id = 4
            wave_timer = 0
            wave_clear_timer = 0
            
        if wave_id == 4 and wave_clear_timer > 60 and not dialogue_done:
            dialogue_active = True
            dialogue_img_x = -360
            dialogue_line_index = 0
            dialogue_char_index = 0
            dialogue_timer = 0
            dialogue_done = True
            wave_clear_timer = 0
            

        for b in enemy_bullets:
            if b["type"] in ["eight_homing", "eight_reflect"]:
                b["timer"] += 1

                t = b["timer"]
                angle = math.radians(b["base_angle"])

                # 1단계: 작은 원 확산
                if t < 35:
                    b["x"] += math.cos(angle) * 3
                    b["y"] += math.sin(angle) * 3

                # 2단계: 잠깐 멈춤
                elif t < 55:
                    pass

                # 3단계: 8자 모양
                elif t < 115:
                    local_t = (t - 55) * 0.12

                    b["x"] += math.sin(local_t) * 3
                    b["y"] += math.sin(local_t * 2) * 2

                # 4단계: 다시 원형으로 풀림
                elif t < 145:
                    b["x"] += math.cos(angle) * 2
                    b["y"] += math.sin(angle) * 2

                # 5단계: 2초 정도 플레이어 유도
                elif t < 205:
                    dx = player.centerx - b["x"]
                    dy = player.centery - b["y"]
                    dist = math.hypot(dx, dy)

                    if dist != 0:
                        speed = 4.5
                        b["vx"] = dx / dist * speed
                        b["vy"] = dy / dist * speed

                        b["last_vx"] = b["vx"]
                        b["last_vy"] = b["vy"]

                    b["x"] += b["vx"]
                    b["y"] += b["vy"]

                # 6단계: 마지막 유도 방향 그대로 직진
                else:
                    b["x"] += b["last_vx"] * 1.4
                    b["y"] += b["last_vy"] * 1.4

                continue
                        
            
            if b["type"] == "reflected" and len(enemies) > 0:
                target = min(
                    enemies,
                    key=lambda en: (en["rect"].centerx - b["x"]) ** 2 + (en["rect"].centery - b["y"]) ** 2
                )

                dx = target["rect"].centerx - b["x"]
                dy = target["rect"].centery - b["y"]
                dist = math.hypot(dx, dy)

                if dist == 0:
                    dist = 1

                speed = 15
                b["vx"] = dx / dist * speed
                b["vy"] = dy / dist * speed

            b["x"] += b["vx"]
            b["y"] += b["vy"]
            
            if b["type"] in ["normal", "reflect", "contract"]:
                if b["type"] == "contract":
                    b["timer"] += 1

                    # 처음엔 퍼짐
                    if b["timer"] < 90:
                        pass

                    # 이후 보스 쪽으로 다시 수축
                    elif b["timer"] < 110:
                        dx = boss_enemy.centerx - b["x"]
                        dy = boss_enemy.centery - b["y"]
                        dist = math.hypot(dx, dy)

                        if dist != 0:
                            speed = 4
                            b["vx"] = dx / dist * speed
                            b["vy"] = dy / dist * speed

                    # 수축 후 다시 밖으로 퍼짐
                    else:
                        dx = b["x"] - boss_enemy.centerx
                        dy = b["y"] - boss_enemy.centery
                        dist = math.hypot(dx, dy)

                        if dist != 0:
                            speed = 17
                            b["vx"] = dx / dist * speed
                            b["vy"] = dy / dist * speed

                        b["repeat"] += 1

                        if b["repeat"] < 2:
                            b["timer"] = 0
                        else:
                            b["type"] = "normal"
                
                                
                
                b["vx"] *= b.get("friction", 1)
                b["vy"] *= b.get("friction", 1)

                speed = math.hypot(b["vx"], b["vy"])
                min_speed = b.get("min_speed", 2.5)

                if speed < min_speed:
                    if speed == 0:
                        speed = 1
                    b["vx"] = b["vx"] / speed * min_speed
                    b["vy"] = b["vy"] / speed * min_speed
            
            # 흡수 탄환
            if b["type"] == "absorb":
                dx = player.centerx - b["x"]
                dy = player.centery - b["y"]

                dist = math.hypot(dx, dy)

                if dist != 0:
                    speed = 8

                    b["vx"] = dx / dist * speed
                    b["vy"] = dy / dist * speed
            
        for b in enemy_bullets[:]:
            if b["type"] == "reflected":
                bullet_rect = pygame.Rect(
                    int(b["x"] - b["size"]),
                    int(b["y"] - b["size"]),
                    b["size"] * 2,
                    b["size"] * 2
                )

                # 보스 맞았을 때
                if boss_enemy is not None and boss_enemy.colliderect(bullet_rect):
                    boss1_hp -= 1
                    enemy_bullets.remove(b)

                    if boss1_hp <= 0:
                        pygame.mixer.music.fadeout(1500)
                        score += 2000
                        boss_defeated = True
                        boss_dead_effect = True
                        boss_dead_timer = 0
                        
                        # 남은 탄환 전부 흡수탄으로 변경
                        for eb in enemy_bullets:
                            if eb["type"] not in ["reflected", "absorb"]:
                                eb["type"] = "absorb"
                                eb["color"] = WHITE

                        dialogue_lines = [
                            {"speaker": "right", "text": "생각보다 강하네..."},
                            {"speaker": "left", "text": "이 정도였어?"},
                            {"speaker": "right", "text": "이번엔 내가 졌군."},
                            {"speaker": "left", "text": "다음엔 조금 더 기대할게."}
                        ]

                        dialogue_line_index = 0
                        dialogue_char_index = 0
                        dialogue_timer = 0

                    continue

                # 일반 적 맞았을 때
                for en in enemies[:]:
                    if en["rect"].colliderect(bullet_rect):
                        reflect_damage = power_level
                        en["hp"] -= reflect_damage
                        enemy_bullets.remove(b)

                        if en["hp"] <= 0:
                            if en.get("wave") == 4:
                                spawn_power_items(en, items, count=16)
                            else:
                                spawn_power_items(en, items)

                            for eb in enemy_bullets:
                                if eb["type"] == "normal":
                                    eb["type"] = "absorb"
                                    eb["color"] = WHITE

                            enemies.remove(en)
                            score += 100

                        break

        enemy_bullets = [
            b for b in enemy_bullets
            if -80 < b["x"] < WIDTH + 80 and -80 < b["y"] < HEIGHT + 150
        ]
        
                # 파워업 아이템 이동
        for item in items:
            item["timer"] += 1

            dx = player.centerx - item["x"]
            dy = player.centery - item["y"]
            dist = math.hypot(dx, dy)

            if dist < 90 and dist != 0:
                item["vx"] += dx / dist * 0.25
                item["vy"] += dy / dist * 0.25

                item["vx"] *= 0.92
                item["vy"] *= 0.92
            else:
                item["vy"] += item["gravity"]

            item["x"] += item["vx"]
            item["y"] += item["vy"]

            # 동방 느낌 살짝 흔들림
            item["x"] += math.sin(item["timer"] * 0.08) * 0.4

        # 파워업 아이템 획득
        for item in items[:]:
            item_rect = pygame.Rect(
                int(item["x"] - item["size"]),
                int(item["y"] - item["size"]),
                item["size"] * 2,
                item["size"] * 2
            )

            if player.colliderect(item_rect):
                item_sound.play()
                if item["type"] == "power":
                    
                    power_items += 1

                    if power_level < 3:
                        need_items = 5
                    elif power_level < 7:
                        need_items = 10
                    else:
                        need_items = 15

                    if power_items >= need_items:
                        power_items = 0
                        power_level = min(10, power_level + 1)

                items.remove(item)

        # 화면 밖 아이템 제거
        items = [
            item for item in items
            if item["y"] < HEIGHT + 30
        ]

        hit_bullets = set()
        hit_enemies = set()
        for bi, b in enumerate(bullets):
            for ei, en in enumerate(enemies):
                if b.colliderect(en["rect"]):
                    # explosion_sound.play()
                    hit_bullets.add(bi)
                    hit_enemies.add(ei)
                    score += 10
        bullets  = [b  for i, b  in enumerate(bullets)  if i not in hit_bullets]
        enemies  = [en for i, en in enumerate(enemies)   if i not in hit_enemies]

        level_idx = min(score // 50, len(LEVELS) - 1)
        level_cfg = LEVELS[level_idx]

        if invincible > 0:
            invincible -= 1

        hit_player = False

        # 몸통 충돌은 무적 아닐 때만 데미지
        if invincible <= 0:
            for en in enemies:
                if player.colliderect(en["rect"]):
                    lives -= 1
                    invincible = 90
                    enemies.clear()
                    hit_player = True

                    if lives <= 0:
                        result = game_over_screen(score)

                        if result == "title":
                            return
                    break

        # 탄환 충돌은 항상 검사
        if not hit_player:
            
            for b in sorted(enemy_bullets[:], key=lambda b: b["type"] != "reflect"):

                bullet_rect = pygame.Rect(
                    int(b["x"] - b["size"]),
                    int(b["y"] - b["size"]),
                    b["size"] * 2,
                    b["size"] * 2
                )
                
                player_hitbox = pygame.Rect(
                    player.centerx - 3,
                    player.centery - 3,
                    6,
                    6
                )

                if player_hitbox.colliderect(bullet_rect):

                    if b["type"] in ["reflect", "eight_reflect"]:

                        if boss_enemy is not None:
                            target_rect = boss_enemy

                        elif len(enemies) > 0:
                            target = min(
                                enemies,
                                key=lambda en:
                                (en["rect"].centerx - b["x"]) ** 2 +
                                (en["rect"].centery - b["y"]) ** 2
                            )

                            target_rect = target["rect"]

                        else:
                            continue

                        dx = target_rect.centerx - b["x"]
                        dy = target_rect.centery - b["y"]

                        dist = math.hypot(dx, dy)
                        if dist == 0:
                            dist = 1

                        speed = 15
                        b["vx"] = dx / dist * speed
                        b["vy"] = dy / dist * speed
                        b["color"] = GREEN
                        b["type"] = "reflected"
                        reflect_sound.play()
                        
                        if power_level >= 7:
                            extra = b.copy()
                            extra["vx"] *= 0.9
                            extra["vy"] *= 0.9
                            extra["x"] += 8
                            extra["y"] += 8
                            enemy_bullets.append(extra)
                                                
                        
                    elif b["type"] == "absorb":
                        item_sound.play()
                        score += 10
                        enemy_bullets.remove(b)
                        continue

                    elif b["type"] in ["normal", "eight_homing"]:
                        if invincible <= 0:
                            lives -= 1
                            invincible = 90
                            enemy_bullets.remove(b)

                            if lives <= 0:
                                result = game_over_screen(score)

                                if result == "title":
                                    return

                        else:
                            continue

                    break
                    
        for s in stars:
            s = list(s)

        screen.fill(GRAY)
        draw_stars(stars)

        for b in bullets:
            pygame.draw.rect(screen, YELLOW, b)

        for en in enemies:
            draw_enemy(screen, en)
            
        if boss_enemy is not None:
            if boss_enemy.y < 30:
                boss_enemy.y += 1

            if boss_attack_anim:
                boss_attack_timer += 1

                if boss_attack_timer >= 4:
                    boss_attack_timer = 0
                    boss_attack_frame += 1

                    if boss_attack_frame >= len(boss_attack_frames):
                        boss_attack_anim = False
                        boss_attack_frame = 0

                img = boss_attack_frames[boss_attack_frame]
            else:
                img = boss1_battle_img

            if boss_dead_effect:
                boss_dead_timer += 1

                fade_alpha = max(0, 255 - boss_dead_timer * 5)

                fade_img = img.copy()
                fade_img.set_alpha(fade_alpha)

                screen.blit(
                    fade_img,
                    (
                        boss_enemy.centerx - fade_img.get_width() // 2,
                        boss_enemy.centery - fade_img.get_height() // 2
                    )
                )

                popup_text = font_big.render("+2000", True, YELLOW)
                popup_text.set_alpha(fade_alpha)

                screen.blit(
                    popup_text,
                    (
                        boss_enemy.centerx - popup_text.get_width() // 2,
                        boss_enemy.centery - 90 - boss_dead_timer // 2
                    )
                )

                if boss_dead_timer >= 60:
                    boss_dead_effect = False
                    boss_enemy = None
                    dialogue_active = True

            else:
                screen.blit(
                    img,
                    (
                        boss_enemy.centerx - img.get_width() // 2,
                        boss_enemy.centery - img.get_height() // 2
                    )
                )
            
        for b in enemy_bullets:

            if b["color"] == RED:
                screen.blit(
                    red_bullet_img,
                    (
                        int(b["x"] - red_bullet_img.get_width() // 2),
                        int(b["y"] - red_bullet_img.get_height() // 2)
                    )
                )

            elif b["color"] == BLUE:
                screen.blit(
                    blue_bullet_img,
                    (
                        int(b["x"] - blue_bullet_img.get_width() // 2),
                        int(b["y"] - blue_bullet_img.get_height() // 2)
                    )
                )
                
            elif b["color"] == GREEN:
                screen.blit(
                    reflect_bullet_img,
                    (
                        int(b["x"] - reflect_bullet_img.get_width() // 2),
                        int(b["y"] - reflect_bullet_img.get_height() // 2)
                    )
                )
                
            elif b["type"] == "absorb":
                screen.blit(
                    score_bullet_img,
                    (
                        int(b["x"] - score_bullet_img.get_width() // 2),
                        int(b["y"] - score_bullet_img.get_height() // 2)
                    )
                )

            else:
                pygame.draw.circle(
                    screen,
                    b["color"],
                    (int(b["x"]), int(b["y"])),
                    b["size"]
                )
            
        for item in items:
            screen.blit(
                item_img,
                (
                    int(item["x"] - item_img.get_width() // 2),
                    int(item["y"] - item_img.get_height() // 2)
                )
            )

        blink = (invincible // 10) % 2 == 0
        if blink:
            if player_state == "idle":
                img = idle_frames[player_frame_index]

            elif player_state == "left":
                img = left_frames[move_anim_index]

            elif player_state == "right":
                img = right_frames[move_anim_index]

            screen.blit(
                img,
                (
                    player.centerx - img.get_width() // 2,
                    player.centery - img.get_height() // 2
                )
            )

        draw_hud(score, lives, power_level, level_cfg)
        
        if dialogue_active:
            

            current = dialogue_lines[dialogue_line_index]
            speaker = current["speaker"]

            left_target_x = 30
            right_target_x = WIDTH - 370

            if speaker == "left":
                left_x = left_target_x
                right_x = right_target_x + 40

                left_alpha = 255
                right_alpha = 120

            else:
                left_x = left_target_x - 40
                right_x = right_target_x

                left_alpha = 120
                right_alpha = 255
            
            boss1_x += (right_x - boss1_x) * 0.12

            dialogue_img_x += (left_x - dialogue_img_x) * 0.12

            left_img = pygame.transform.scale(dialogue_img, (340, 340))
            right_img = pygame.transform.scale(boss1_img, (340, 340))

            left_img.set_alpha(left_alpha)
            right_img.set_alpha(right_alpha)

            screen.blit(left_img, (int(dialogue_img_x), HEIGHT - 370))
            
            if dialogue_line_index >= 3 and not boss_intro_started:
                boss_intro_started = True

                pygame.mixer.music.load("assets/music/stage1_boss(1).wav")
                pygame.mixer.music.play(-1)

                boss_enemy = pygame.Rect(WIDTH // 2 - 60, -160, 120, 120)

            # 3번째 대사 이후에 보스 등장
            if dialogue_line_index >= 3:
                screen.blit(right_img, (int(boss1_x), HEIGHT - 370))

            box = pygame.Surface((560, 90), pygame.SRCALPHA)
            box.fill((5, 5, 25, 170))
            screen.blit(box, (120, 480))

            pygame.draw.rect(screen, WHITE, (120, 480, 560, 90), 2)

            dialogue_timer += 1

            if dialogue_timer >= 3:
                dialogue_timer = 0

                if dialogue_char_index < len(current["text"]):
                    dialogue_char_index += 1

            shown_text = current["text"][:dialogue_char_index]

            text = font.render(shown_text, True, WHITE)
            screen.blit(text, (145, 510))

        draw_stage_text(1, stage_text_frame)
        if stage_text_frame <= 120:
            stage_text_frame += 1
            
            
        if boss_enemy is not None and not dialogue_active:
            bar_x = 80
            bar_y = 15

            bar_w = WIDTH - 160
            bar_h = 18

            # 테두리
            pygame.draw.rect(
                screen,
                WHITE,
                (bar_x, bar_y, bar_w, bar_h),
                2
            )

            # 현재 체력
            hp_width = int(bar_w * (boss1_hp / boss1_max_hp))

            pygame.draw.rect(
                screen,
                RED,
                (bar_x + 2, bar_y + 2, hp_width - 4, bar_h - 4)
            )

        pygame.display.flip()
while True:
    title_screen()
    main()

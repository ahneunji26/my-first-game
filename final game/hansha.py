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

screen = pygame.display.set_mode((WIDTH, HEIGHT))

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
font = get_korean_font(36)
font_big = get_korean_font(72)

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

PLAYER_W, PLAYER_H = 40, 40
ENEMY_W,  ENEMY_H  = 36, 36
BULLET_W, BULLET_H = 6,  14
ENEMY_BULLET_SPEED = 4

def draw_enemy(surf, rect):
    cx = rect.centerx
    pygame.draw.polygon(surf, RED, [
        (cx, rect.bottom),
        (rect.left, rect.top),
        (cx, rect.top + 8),
        (rect.right, rect.top),
    ])

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
                spawn_circle_enemy_bullets(en, enemy_bullets)
                en["shot_index"] += 1

        if en["shot_index"] >= 4 and en["timer"] >= 360:
            en["phase"] = "exit"

    elif en["phase"] == "exit":
        en["rect"].y += 4
            
def spawn_circle_enemy_bullets(enemy, enemy_bullets):
    cx = enemy["rect"].centerx
    cy = enemy["rect"].centery

    for i in range(16):
        angle = i * (360 / 16)
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

            "friction": 0.995,
            "min_speed": 2.0,

            "size": 6,
            "color": bullet_color,
            "type": bullet_type
        })

def spawn_power_items(enemy, items):
    count = 2 if random.random() < 0.3 else 1

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
    screen.fill((10, 10, 30))
    screen.blit(font_big.render("GAME OVER", True, RED), (220, 220))
    screen.blit(font.render(f"Score: {score}", True, WHITE), (350, 310))
    screen.blit(font.render("R: Restart   Q: Quit", True, WHITE), (270, 360))
    pygame.display.flip()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r: return True
                if e.key == pygame.K_q: pygame.quit(); sys.exit()

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


def title_screen():
    menu = ["START", "OPTION", "EXIT"]
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
                        # 옵션 화면은 나중에 구현
                        pass

                    elif selected == 2:
                        confirm_exit_screen()


def main():
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
    
    player_state = "idle"

    player_anim_timer = 0
    player_frame_index = 0

    move_anim_timer = 0
    move_anim_index = 0

    stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 2))
             for _ in range(80)]

    while True:
        clock.tick(FPS)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()

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
        
        if len(enemies) == 0 and len(enemy_bullets) == 0:
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

        for b in enemy_bullets:
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
            
            if b["type"] in ["normal", "reflect"]:
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
                for en in enemies:
                    bullet_rect = pygame.Rect(
                        int(b["x"] - b["size"]),
                        int(b["y"] - b["size"]),
                        b["size"] * 2,
                        b["size"] * 2
                    )

                    if en["rect"].colliderect(bullet_rect):
                        reflect_damage = 2 ** (power_level - 1)
                        en["hp"] -= reflect_damage
                        enemy_bullets.remove(b)

                        if en["hp"] <= 0:

                            if en.get("wave") == 4:
                                for _ in range(4):
                                    spawn_power_items(en, items)
                            else:
                                spawn_power_items(en, items)

                            # 화면 탄환 흡수 상태로 변경
                            for eb in enemy_bullets:
                                if eb["type"] == "normal":
                                    eb["type"] = "absorb"
                                    eb["color"] = WHITE

                            enemies.remove(en)
                            score += 100

                        break

        enemy_bullets = [
            b for b in enemy_bullets
            if -50 < b["x"] < WIDTH + 50 and -50 < b["y"] < HEIGHT + 50
        ]
        
                # 파워업 아이템 이동
        for item in items:
            item["timer"] += 1

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
                if item["type"] == "power":
                    power_items += 1
                    power_level = min(5, 1 + power_items // 5)

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
                        if game_over_screen(score):
                            main()
                        return
                    break

        # 탄환 충돌은 항상 검사
        if not hit_player:
            for b in enemy_bullets[:]:
                bullet_rect = pygame.Rect(
                    int(b["x"] - b["size"]),
                    int(b["y"] - b["size"]),
                    b["size"] * 2,
                    b["size"] * 2
                )

                if player.colliderect(bullet_rect):

                    if b["type"] == "reflect":
                        if len(enemies) == 0:
                            enemy_bullets.remove(b)
                            break

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
                        b["color"] = GREEN
                        b["type"] = "reflected"
                        reflect_sound.play()
                        
                        
                    elif b["type"] == "absorb":
                        score += 10
                        enemy_bullets.remove(b)
                        continue

                    elif b["type"] == "normal" and invincible <= 0:
                        lives -= 1
                        invincible = 90
                        enemy_bullets.remove(b)

                        if lives <= 0:
                            if game_over_screen(score):
                                main()
                            return

                    break
                    
        for s in stars:
            s = list(s)

        screen.fill(GRAY)
        draw_stars(stars)

        for b in bullets:
            pygame.draw.rect(screen, YELLOW, b)

        for en in enemies:
            draw_enemy(screen, en["rect"])
            
        for b in enemy_bullets:
            pygame.draw.circle(
                screen,
                b["color"],
                (int(b["x"]), int(b["y"])),
                b["size"]
            )
            
        for item in items:
            pygame.draw.circle(
                screen,
                PINK,
                (int(item["x"]), int(item["y"])),
                item["size"]
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

        draw_stage_text(1, stage_text_frame)
        if stage_text_frame <= 120:
            stage_text_frame += 1

        pygame.display.flip()

title_screen()
main()
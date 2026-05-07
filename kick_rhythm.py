import pygame
import random
import sys
import os

pygame.init()
pygame.mixer.init()

BASE_DIR = os.getcwd()

OPENING_BGM = os.path.join(BASE_DIR, "assets", "sound", "tempo.mp3")
STAGE_BGM = os.path.join(BASE_DIR, "assets", "sound", "four_loop.mp3")
BOSS_BGM = os.path.join(BASE_DIR, "assets", "sound", "spyloop.flac")

# -------------------
# BGM 함수
# -------------------

current_bgm = None

def play_bgm(path, loop=-1, volume=0.5):
    global current_bgm
    
    
    print("BGM 재생 시도:", path)
    print("파일 존재:", os.path.exists(path))

    if current_bgm == path:
        print("이미 재생 중인 BGM")
        return

    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loop)
        current_bgm = path
        print("BGM 재생 성공")
        print("mixer busy:", pygame.mixer.music.get_busy())

    except pygame.error as e:
        print("BGM 재생 실패:", path, e)


def get_korean_font(size):
    candidates = ["malgungothic", "applegothic", "nanumgothic", "notosanscjk"]
    for name in candidates:
        font = pygame.font.SysFont(name, size)
        if font.get_ascent() > 0:
            return font
    return pygame.font.SysFont(None, size)

WIDTH, HEIGHT = 900, 500
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (15, 15, 30)
RED = (230, 60, 70)
YELLOW = (250, 220, 80)
BLUE = (80, 170, 255)
PURPLE = (190, 80, 255)
GREEN = (70, 230, 120)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rhythm Sky Kicker")
clock = pygame.time.Clock()

font = get_korean_font(28)
font_big = get_korean_font(58)

# -----------------------------
# 리듬 설정
# -----------------------------
OFFSET = 0          # 노래/공격 타이밍 보정값(ms)
PERFECT_RANGE = 60
GOOD_RANGE = 110

# 음악 기준 공격 시간표(ms)
NOTE_TIMES = [
    8000, 8430, 8860, 9290,
    9720, 10150, 10580, 11010, 11440, 11870,
    12300, 12730, 13160, 13590, 14020, 14450,
    14880, 15310, 15740, 16170, 16600, 17030,
    17460, 17890, 18320, 18750, 19180, 19610,
    20040, 20470, 20900, 21330, 21560, 21890,
    22390, 22620, 22850, 23350, 23580, 23810
]

BOSS_NOTES = [
    800, 1200, 1600, 2000
]

BULLET_SPEED = 6
JUDGE_LINE_X = 170

PLAYER_W, PLAYER_H = 70, 90
SHIP_W, SHIP_H = 150, 45
BULLET_W, BULLET_H = 22, 22
ENEMY_W, ENEMY_H = 70, 70

def draw_text_center(text, y, color=WHITE, size_font=None):
    f = size_font if size_font else font
    img = f.render(text, True, color)
    screen.blit(img, (WIDTH // 2 - img.get_width() // 2, y))

def opening_screen():
    
    play_bgm(OPENING_BGM)
    page = 0
    lines = [
        "공중 전투 중, 주인공은 실수로 총을 떨어뜨렸다.",
        "무기도 없이 날아오는 적의 총알.",
        "놀란 주인공은 그대로 발로 총알을 차버렸다.",
        "그런데... 총알은 오히려 적에게 되돌아갔다."
    ]

    while True:
        screen.fill(BLACK)
        draw_text_center("Rhythm Sky Kicker", 90, PURPLE, font_big)

        if page < len(lines):
            draw_text_center(lines[page], 220, WHITE)
            draw_text_center("SPACE : 다음     S : 스킵", 360, YELLOW)
        else:
            draw_text_center("리듬에 맞춰 SPACE로 총알을 차서 반사하세요.", 220, WHITE)
            draw_text_center("SPACE : 게임 시작     S : 스킵", 360, GREEN)

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    page += 1
                    if page > len(lines):
                        return
                    
                if e.key == pygame.K_s:
                        return
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def game_over_screen(score):
    while True:
        screen.fill(BLACK)
        draw_text_center("GAME OVER", 150, RED, font_big)
        draw_text_center(f"Score: {score}", 240, WHITE)
        draw_text_center("R : Restart    Q : Quit", 320, YELLOW)
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    return True
                if e.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def clear_screen(score):
    while True:
        screen.fill(BLACK)
        draw_text_center("CLEAR!", 150, GREEN, font_big)
        draw_text_center(f"Final Score: {score}", 240, WHITE)
        draw_text_center("R : Restart    Q : Quit", 320, YELLOW)
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    return True
                if e.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def draw_ship(x, y):
    # 비행선
    pygame.draw.ellipse(screen, (45, 45, 60), (x, y, SHIP_W, SHIP_H))
    pygame.draw.rect(screen, (70, 70, 90), (x + 35, y - 8, 60, 15))
    pygame.draw.circle(screen, PURPLE, (x + 15, y + 25), 8)
    pygame.draw.polygon(screen, PURPLE, [
        (x - 25, y + 20),
        (x, y + 10),
        (x, y + 35)
    ])

def draw_player(player_rect, kick_timer):
    # 몸
    x, y = player_rect.x, player_rect.y

    # 머리
    pygame.draw.circle(screen, (220, 220, 235), (x + 35, y + 15), 18)

    # 가죽자켓 몸통
    pygame.draw.rect(screen, (20, 20, 25), (x + 18, y + 35, 34, 30))

    # 다리
    if kick_timer > 0:
        # 발차기 중
        pygame.draw.line(screen, (245, 210, 190), (x + 35, y + 65), (x + 78, y + 45), 10)
        pygame.draw.rect(screen, BLACK, (x + 70, y + 38, 28, 14))
        pygame.draw.line(screen, (245, 210, 190), (x + 30, y + 65), (x + 18, y + 95), 10)
        pygame.draw.rect(screen, BLACK, (x + 9, y + 87, 18, 25))
    else:
        pygame.draw.line(screen, (245, 210, 190), (x + 25, y + 65), (x + 20, y + 100), 10)
        pygame.draw.line(screen, (245, 210, 190), (x + 45, y + 65), (x + 52, y + 100), 10)
        pygame.draw.rect(screen, BLACK, (x + 10, y + 95, 18, 25))
        pygame.draw.rect(screen, BLACK, (x + 45, y + 95, 18, 25))

def draw_enemy(enemy_rect):
    pygame.draw.rect(screen, RED, enemy_rect)
    pygame.draw.circle(screen, BLACK, enemy_rect.center, 18)
    pygame.draw_text if False else None

def draw_bullet(bullet):
    pygame.draw.circle(screen, YELLOW, bullet.center, bullet.width // 2)
    pygame.draw.circle(screen, ORANGE if False else RED, bullet.center, 5)

def draw_reflected_bullet(bullet):
    pygame.draw.circle(screen, GREEN, bullet.center, bullet.width // 2)
    pygame.draw.circle(screen, WHITE, bullet.center, 5)

def draw_hud(score, lives, combo, result_text, game_time):
    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
    screen.blit(font.render(f"Lives: {'♥ ' * lives}", True, RED), (10, 45))
    screen.blit(font.render(f"Combo: {combo}", True, YELLOW), (10, 80))
    screen.blit(font.render(f"OFFSET: {OFFSET}ms", True, WHITE), (WIDTH - 190, 10))

    if result_text:
        draw_text_center(result_text, 110, GREEN if result_text == "PERFECT" else YELLOW)

def main():
    opening_screen()
    
    play_bgm(STAGE_BGM, loop=-1, volume=0.5)

    player = pygame.Rect(90, HEIGHT // 2 - 40, PLAYER_W, PLAYER_H)
    ship_x = 50
    ship_y = player.bottom - 10

    enemies = []
    enemy_count = 5
    enemy_hp = 100

    for i in range(enemy_count):
        x = WIDTH - 120
        y = 60 + i * 80
        enemies.append({
            "rect": pygame.Rect(x, y, ENEMY_W, ENEMY_H),
            "hp": enemy_hp,
            "shake": 0
        })

    current_enemy_index = 0
    boss_started = False
    
    boss_start_ticks = 0
    boss_note_index = 0
    
    boss_intro = False
    boss = pygame.Rect(WIDTH + 120, HEIGHT // 2 - 70, 120, 140)
    boss_hp = 20

    bullets = []
    reflected_bullets = []

    note_index = 0
    score = 0
    lives = 3
    combo = 0

    kick_timer = 0
    result_text = ""
    result_timer = 0

    start_ticks = pygame.time.get_ticks()

    stars = [
        [random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 2)]
        for _ in range(80)
    ]

    while True:
        dt = clock.tick(FPS)
        now = pygame.time.get_ticks()

        if not boss_started:
            game_time = now - start_ticks + OFFSET
        else:
            game_time = now - boss_start_ticks + OFFSET

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if e.key == pygame.K_SPACE:
                    kick_timer = 8

                    closest = None
                    closest_error = 99999

                    for b in bullets:
                        error = abs(b["hit_time"] - game_time)
                        if error < closest_error:
                            closest = b
                            closest_error = error

                    if closest and closest_error <= GOOD_RANGE:
                        if closest_error <= PERFECT_RANGE:
                            result_text = "PERFECT"
                            score += 100
                            combo += 1
                        else:
                            result_text = "GOOD"
                            score += 50
                            combo += 1

                        result_timer = 30

                        rb = {
                            "rect": pygame.Rect(
                                closest["rect"].x,
                                closest["rect"].y,
                                BULLET_W,
                                BULLET_H
                            ),
                            "vx": random.randint(9, 13),
                            "vy": random.choice([-4, -3, -2, 2, 3, 4])
                        }

                        reflected_bullets.append(rb)
                        bullets.remove(closest)

                    else:
                        result_text = "MISS"
                        result_timer = 30
                        combo = 0

        # 노트 생성
        current_notes = BOSS_NOTES if boss_started else NOTE_TIMES
        
        if boss_started and boss_intro:
            current_notes = []

        if not boss_started:
            while note_index < len(current_notes) and current_notes[note_index] <= game_time + 1500:
                hit_time = current_notes[note_index]
                travel_time = 1500
                start_x = WIDTH + 40
                y = player.centery

                bullet_rect = pygame.Rect(start_x, y, BULLET_W, BULLET_H)

                bullets.append({
                    "rect": bullet_rect,
                    "hit_time": hit_time,
                    "spawn_time": hit_time - travel_time,
                    "start_x": start_x,
                    "target_x": JUDGE_LINE_X
                })

                note_index += 1

        else:
            while boss_note_index < len(current_notes) and current_notes[boss_note_index] <= game_time + 1500:
                hit_time = current_notes[boss_note_index]
                travel_time = 1500
                start_x = WIDTH + 40
                y = player.centery

                bullet_rect = pygame.Rect(start_x, y, BULLET_W, BULLET_H)

                bullets.append({
                    "rect": bullet_rect,
                    "hit_time": hit_time,
                    "spawn_time": hit_time - travel_time,
                    "start_x": start_x,
                    "target_x": JUDGE_LINE_X
                })

                boss_note_index += 1

        # 총알 이동
        for b in bullets:
            remain = b["hit_time"] - game_time
            progress = 1 - (remain / 1500)
            progress = max(0, min(1, progress))
            b["rect"].x = int(b["start_x"] + (b["target_x"] - b["start_x"]) * progress)

        # 판정선 지나간 총알 처리
        missed = []
        for b in bullets:
            if game_time - b["hit_time"] > GOOD_RANGE:
                missed.append(b)

        for b in missed:
            bullets.remove(b)
            lives -= 1
            combo = 0
            result_text = "HIT"
            result_timer = 30

            if lives <= 0:
                if game_over_screen(score):
                    main()
                return

        # 반사 총알 이동
        for rb in reflected_bullets:
            rb["rect"].x += rb["vx"]
            rb["rect"].y += rb["vy"]

        reflected_bullets = [
            rb for rb in reflected_bullets
            if rb["rect"].left < WIDTH and rb["rect"].bottom > 0 and rb["rect"].top < HEIGHT
        ]
        
        if boss_started and boss_intro:
            boss.x -= 3

            if boss.x <= WIDTH - 170:
                boss.x = WIDTH - 170
                boss_intro = False
                boss_start_ticks = pygame.time.get_ticks()

        # 반사 총알이 적에게 닿으면 점수
        for rb in reflected_bullets[:]:
            for i, en in enumerate(enemies):
                if i < current_enemy_index:
                    continue

                if rb["rect"].colliderect(en["rect"]):
                    reflected_bullets.remove(rb)  # 맞는 순간 사라짐
                    en["hp"] -= 1
                    en["shake"] = 12
                    score += 30

                    if en["hp"] <= 0:
                        current_enemy_index += 1

                        if current_enemy_index >= len(enemies) and not boss_started:
                            boss_started = True
                            boss_intro = True
                            boss_start_ticks = pygame.time.get_ticks()
                            boss_note_index = 0

                            bullets.clear()
                            reflected_bullets.clear()

                            play_bgm(BOSS_BGM, loop=-1, volume=0.6)
                            result_text = "BOSS!"
                            result_timer = 60

                    break


        if kick_timer > 0:
            kick_timer -= 1

        if result_timer > 0:
            result_timer -= 1
        else:
            result_text = ""

        # 클리어
        #if note_index >= len(NOTE_TIMES) and len(bullets) == 0:
           # if clear_screen(score):
                #main()
           # return

        # 배경
        screen.fill(GRAY)

        for s in stars:
            s[0] -= s[2]
            if s[0] < 0:
                s[0] = WIDTH
                s[1] = random.randint(0, HEIGHT)
            pygame.draw.circle(screen, WHITE, (s[0], s[1]), s[2])

        # 판정선
        pygame.draw.line(screen, PURPLE, (JUDGE_LINE_X, 0), (JUDGE_LINE_X, HEIGHT), 3)
        screen.blit(font.render("KICK LINE", True, PURPLE), (JUDGE_LINE_X - 55, HEIGHT - 40))

        # 비행선/플레이어
        ship_y = player.bottom - 10
        draw_ship(ship_x, ship_y)
        draw_player(player, kick_timer)
        
                # 총알
        for b in bullets:
            draw_bullet(b["rect"])

        for rb in reflected_bullets:
            draw_reflected_bullet(rb["rect"])

        draw_hud(score, lives, combo, result_text, game_time)

        # 적
        for i, en in enumerate(enemies):
            if i < current_enemy_index:
                continue

            rect = en["rect"].copy()

            if en["shake"] > 0:
                rect.x += random.randint(-5, 5)
                rect.y += random.randint(-3, 3)
                en["shake"] -= 1

            draw_enemy(rect)

            hp_text = font.render(f"HP:{en['hp']}", True, WHITE)
            screen.blit(hp_text, (rect.x - 5, rect.y - 30))
            
        #보스
        if boss_started:
            pygame.draw.rect(screen, PURPLE, boss)
            pygame.draw.circle(screen, BLACK, boss.center, 35)

            hp_text = font.render(f"BOSS HP:{boss_hp}", True, WHITE)
            screen.blit(hp_text, (boss.x - 20, boss.y - 35))

        pygame.display.flip()

main()
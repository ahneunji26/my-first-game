import pygame
import random
import sys
import math

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
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()
font = get_korean_font(36)
font_big = get_korean_font(72)

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

PLAYER_W, PLAYER_H = 40, 40
ENEMY_W,  ENEMY_H  = 36, 36
BULLET_W, BULLET_H = 6,  14
ENEMY_BULLET_SPEED = 3

def draw_player(surf, rect):
    cx = rect.centerx
    pygame.draw.polygon(surf, BLUE, [
        (cx, rect.top),
        (rect.left, rect.bottom),
        (cx, rect.bottom - 8),
        (rect.right, rect.bottom),
    ])
    pygame.draw.rect(surf, YELLOW, (cx - 4, rect.bottom - 10, 8, 10))

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
            spawn_delay + 110,
            spawn_delay + 120,
            spawn_delay + 130,
            spawn_delay + 150,
            spawn_delay + 160,
            spawn_delay + 170,
            spawn_delay + 190,
            spawn_delay + 200,
            spawn_delay + 210
        ]
        
        enemies.append({
            "rect": pygame.Rect(start_positions[i] - ENEMY_W // 2, start_y, ENEMY_W, ENEMY_H),
            "vx": velocities[i][0],
            "vy": velocities[i][1],
            "stop_timer": 0,
            "hp": 3,
            "shot_index": 0,
            "shot_times": shot_times,
            "spawn_delay": spawn_delay,
            "active": False
        })

    return enemies

def update_second_wave_enemy(en, wave_timer, enemy_bullets):
    if wave_timer < en["spawn_delay"]:
        return

    en["active"] = True
    en["timer"] += 1
    t = en["timer"]

    direction = en["direction"]

    base_x = en["base_x"]
    start_y = en["start_y"]

    spread = 120 + t * 0.9

    en["rect"].centerx = (
        base_x
        + math.sin(t * 0.022) * spread * direction
    )
    
    # 아래로 더 강하게 내려감
    en["rect"].centery = start_y + t * 1.45

    # 후반에는 화면 아래로 급강하하며 빠짐
    if t > 170:
        en["rect"].centerx += direction * (t - 170) * 2.5
        en["rect"].centery += (t - 170) * 2.4

    if en["shot_index"] < len(en["shot_times"]):
        shot_time = en["shot_times"][en["shot_index"]]

        if wave_timer >= shot_time:
            spawn_circle_enemy_bullets(en, enemy_bullets)
            en["shot_index"] += 1
            
def spawn_circle_enemy_bullets(enemy, enemy_bullets):
    cx = enemy["rect"].centerx
    cy = enemy["rect"].centery

    for i in range(16):
        angle = i * (360 / 16)
        rad = math.radians(angle)

        bullet_color = RED
        bullet_type = "normal"

        # 왼쪽 바깥 적
        if enemy.get("vx", 0) < -1:
            if i == 2:
                bullet_color = GREEN
                bullet_type = "reflect"

        # 오른쪽 바깥 적
        elif enemy.get("vx", 0) > 1:
            if i == 10:
                bullet_color = GREEN
                bullet_type = "reflect"

        # 가운데 적들
        else:
            if i == 4:
                bullet_color = GREEN
                bullet_type = "reflect"

        enemy_bullets.append({
            "x": cx,
            "y": cy,
            "vx": math.cos(rad) * ENEMY_BULLET_SPEED,
            "vy": math.sin(rad) * ENEMY_BULLET_SPEED,
            "size": 6,
            "color": bullet_color,
            "type": bullet_type
        })


def spawn_second_wave():
    enemies = []

    x_positions = [WIDTH // 2 - 45, WIDTH // 2 + 45]

    for side in range(2):
        for row in range(6):
            direction = -1 if side == 0 else 1
            x = x_positions[side]
            y = -80

            spawn_delay = row * 14 + side * 4
            
            order = row

            enemies.append({
                "rect": pygame.Rect(x - ENEMY_W // 2, y, ENEMY_W, ENEMY_H),
                "base_x": x,
                "start_y": y,
                "side": side,
                "row": row,
                "direction": direction,
                "spawn_delay": spawn_delay,
                "hp": 3,
                "active": False,
                "phase": "enter",
                "timer": 0,
                "angle": -math.pi / 2,
                "turn_center_x": WIDTH // 2 + direction * 70,
                "turn_center_y": 210 + row * 4,
                "shot_index": 0,
                "shot_times": [80 + order * 60, 100 + order * 60],
                "stop_timer": 0,
                "vx": 0,
                "vy": 1.25,
            })

    return enemies

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

                if e.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(menu)

                if e.key == pygame.K_ESCAPE:
                    selected = 2

                if e.key == pygame.K_RETURN:
                    if selected == 0:
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

    stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 2))
             for _ in range(80)]

    while True:
        clock.tick(FPS)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]  and player.left  > 0:      player.x -= 6
        if keys[pygame.K_RIGHT] and player.right < WIDTH:   player.x += 6
        if keys[pygame.K_UP]    and player.top   > 0:      player.y -= 6
        if keys[pygame.K_DOWN]  and player.bottom < HEIGHT: player.y += 6

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
                            spawn_power_items(en, items)
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
            draw_player(screen, player)

        draw_hud(score, lives, power_level, level_cfg)

        draw_stage_text(1, stage_text_frame)
        if stage_text_frame <= 120:
            stage_text_frame += 1

        pygame.display.flip()

title_screen()
main()
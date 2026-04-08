import pygame
import random
import sys
import base64, io   # ✅ 추가

pygame.init()

def get_korean_font(size):
    candidates = ["malgungothic", "applegothic", "nanumgothic", "notosanscjk"]
    for name in candidates:
        font = pygame.font.SysFont(name, size)
        if font.get_ascent() > 0:
            return font
    return pygame.font.SysFont(None, size)

WIDTH, HEIGHT = 800, 600
CELL = 60
FPS = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 200, 50)
DARK = (30, 150, 30)
RED = (220, 50, 50)
GRAY = (40, 40, 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = get_korean_font(36)
font_big = get_korean_font(72)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ✅ 이미지 준비 코드 (여기 추가)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SHEET_B64 = "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"

FRAME_W = 49
FRAME_H = 43
COLS = 4

sheet_bytes = base64.b64decode(SHEET_B64)
player_sheet = pygame.image.load(io.BytesIO(sheet_bytes)).convert_alpha()

player_frames = []
for i in range(12):
    row, col = divmod(i, COLS)
    rect = pygame.Rect(col * FRAME_W, row * FRAME_H, FRAME_W, FRAME_H)
    player_frames.append(player_sheet.subsurface(rect))

walk_frames = [player_frames[i] for i in range(11)]

# --- 레벨 설정 ---
LEVELS = {
    1: {"speed": 8, "label": "Easy"},
    2: {"speed": 12, "label": "Normal"},
    3: {"speed": 18, "label": "Hard"},
}
level = 1

def new_food(snake):
    while True:
        pos = (
            random.randrange(0, WIDTH // CELL) * CELL,
            random.randrange(0, HEIGHT // CELL) * CELL,
        )
        if pos not in snake:
            return pos

def draw_grid():
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, (20, 20, 20), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, (20, 20, 20), (0, y), (WIDTH, y))

# ✅ 이 함수 교체됨
def draw_snake(snake):
    frame_index = (pygame.time.get_ticks() // 150) % len(walk_frames)

    for i, seg in enumerate(snake):
        x, y = seg

        if i == 0:
            frame = walk_frames[frame_index]
        else:
            frame = walk_frames[1]

        frame = pygame.transform.scale(frame, (CELL, CELL))
        screen.blit(frame, (x, y))

def draw_hud(score, level):
    screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
    screen.blit(font.render(f"Level: {LEVELS[level]['label']}", True, WHITE), (10, 40))

def game_over_screen(score):
    screen.fill(GRAY)
    screen.blit(font_big.render("GAME OVER", True, RED), (220, 220))
    screen.blit(font.render(f"Score: {score}", True, WHITE), (350, 310))
    screen.blit(font.render("R: Restart   Q: Quit", True, WHITE), (270, 360))
    pygame.display.flip()
    while True:
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

def level_select_screen():
    screen.fill(GRAY)
    screen.blit(font_big.render("SNAKE", True, GREEN), (310, 160))
    for lv, info in LEVELS.items():
        screen.blit(
            font.render(f"{lv}: {info['label']}", True, WHITE), (340, 250 + lv * 40)
        )
    pygame.display.flip()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key in (pygame.K_1, pygame.K_2, pygame.K_3):
                    return int(e.unicode)

def main():
    global level
    level = level_select_screen()

    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = (CELL, 0)
    food = new_food(snake)
    score = 0
    speed = LEVELS[level]["speed"]

    while True:
        clock.tick(speed)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP and direction != (0, CELL):
                    direction = (0, -CELL)
                if e.key == pygame.K_DOWN and direction != (0, -CELL):
                    direction = (0, CELL)
                if e.key == pygame.K_LEFT and direction != (CELL, 0):
                    direction = (-CELL, 0)
                if e.key == pygame.K_RIGHT and direction != (-CELL, 0):
                    direction = (CELL, 0)

        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if (
            head[0] < 0
            or head[0] >= WIDTH
            or head[1] < 0
            or head[1] >= HEIGHT
            or head in snake
        ):
            if game_over_screen(score):
                main()
            return

        snake.insert(0, head)

        if head == food:
            score += 10
            food = new_food(snake)
            if score % 50 == 0 and level < 3:
                level = min(level + 1, 3)
                speed = LEVELS[level]["speed"]
        else:
            snake.pop()

        screen.fill(GRAY)
        draw_grid()
        pygame.draw.rect(screen, RED, (*food, CELL, CELL))
        draw_snake(snake)
        draw_hud(score, level)
        pygame.display.flip()

main()
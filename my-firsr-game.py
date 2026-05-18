import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AABB Example")

clock = pygame.time.Clock()

# 색상
WHITE = (255, 255, 255)
GRAY = (120, 120, 120)
RED = (255, 0, 0)

# 이동 가능한 사각형
player = pygame.Rect(100, 100, 80, 80)

# 중앙 고정 사각형
fixed = pygame.Rect(0, 0, 120, 120)
fixed.center = (WIDTH // 2, HEIGHT // 2)

# 이동 속도
speed = 5

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리 (대각선 속도 보정 포함)
    keys = pygame.key.get_pressed()

    dx, dy = 0, 0

    if keys[pygame.K_LEFT]:
        dx -= 1
    if keys[pygame.K_RIGHT]:
        dx += 1
    if keys[pygame.K_UP]:
        dy -= 1
    if keys[pygame.K_DOWN]:
        dy += 1

    # 벡터 길이 계산
    length = (dx**2 + dy**2) ** 0.5

    # 정규화
    if length != 0:
        dx /= length
        dy /= length

    # 이동 적용
    player.x += dx * speed
    player.y += dy * speed

    # 화면 밖으로 안 나가게 제한
    player.x = max(0, min(player.x, WIDTH - player.width))
    player.y = max(0, min(player.y, HEIGHT - player.height))

    # 화면 배경
    screen.fill(WHITE)

    # 회색 사각형 2개 그리기
    pygame.draw.rect(screen, GRAY, player)
    pygame.draw.rect(screen, GRAY, fixed)

    # 각 오브젝트의 AABB 표시
    pygame.draw.rect(screen, RED, player, 2)
    pygame.draw.rect(screen, RED, fixed, 2)

    pygame.display.flip()

pygame.quit()
sys.exit()
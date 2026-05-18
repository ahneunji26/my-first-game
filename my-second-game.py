import pygame
import sys
import math

from sprites import load_sprite

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle + AABB + OBB Collision")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

# 색상
WHITE = (255, 255, 255)
RED_BG = (255, 220, 220)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 180, 0)
BLACK = (0, 0, 0)

# -------------------------
# 오브젝트 설정
# -------------------------
player = pygame.Rect(100, 100, 80, 110)
fixed = pygame.Rect(0, 0, 120, 120)
fixed.center = (WIDTH // 2, HEIGHT // 2)

player_x = float(player.x)
player_y = float(player.y)

move_speed = 5

# -------------------------
# 스프라이트
# -------------------------
player_image = load_sprite("adventurer", (player.width, player.height))
fixed_image_original = load_sprite("stone", (fixed.width, fixed.height))

# 회전
angle = 0
base_rotation_speed = 1
fast_rotation_speed = 4


def rotate_point(px, py, cx, cy, angle_degrees):
    rad = math.radians(angle_degrees)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)

    tx = px - cx
    ty = py - cy

    rx = tx * cos_a - ty * sin_a
    ry = tx * sin_a + ty * cos_a

    return (cx + rx, cy + ry)


def subtract(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])


def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def normalize(v):
    length = math.sqrt(v[0] * v[0] + v[1] * v[1])
    if length == 0:
        return (0, 0)
    return (v[0] / length, v[1] / length)


def get_axes(points):
    axes = []
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]

        edge = subtract(p2, p1)
        normal = (-edge[1], edge[0])
        axis = normalize(normal)
        axes.append(axis)
    return axes


def project_polygon(points, axis):
    projections = [dot(point, axis) for point in points]
    return min(projections), max(projections)


def overlap_on_axis(points1, points2, axis):
    min1, max1 = project_polygon(points1, axis)
    min2, max2 = project_polygon(points2, axis)
    return not (max1 < min2 or max2 < min1)


def sat_collision(points1, points2):
    axes = get_axes(points1) + get_axes(points2)
    for axis in axes:
        if not overlap_on_axis(points1, points2, axis):
            return False
    return True


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------------------------
    # 입력
    # -------------------------
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

    length = (dx ** 2 + dy ** 2) ** 0.5
    if length != 0:
        dx /= length
        dy /= length

    player_x += dx * move_speed
    player_y += dy * move_speed

    player_x = max(0, min(player_x, WIDTH - player.width))
    player_y = max(0, min(player_y, HEIGHT - player.height))

    player.x = int(player_x)
    player.y = int(player_y)

    # -------------------------
    # 회전
    # -------------------------
    if keys[pygame.K_z]:
        angle += fast_rotation_speed
    else:
        angle += base_rotation_speed

    angle %= 360

    # -------------------------
    # 회전된 스프라이트
    # -------------------------
    rotated_fixed_image = pygame.transform.rotate(fixed_image_original, angle)
    rotated_fixed_rect = rotated_fixed_image.get_rect(center=fixed.center)

    # -------------------------
    # 스프라이트 실제 픽셀 기준 AABB
    # -------------------------
    fixed_mask = pygame.mask.from_surface(rotated_fixed_image)
    fixed_aabb_list = fixed_mask.get_bounding_rects()

    if fixed_aabb_list:
        local_aabb = fixed_aabb_list[0]
        fixed_sprite_aabb = pygame.Rect(
            rotated_fixed_rect.left + local_aabb.left,
            rotated_fixed_rect.top + local_aabb.top,
            local_aabb.width,
            local_aabb.height
        )
    else:
        fixed_sprite_aabb = pygame.Rect(rotated_fixed_rect.centerx, rotated_fixed_rect.centery, 0, 0)

    # -------------------------
    # Circle 충돌
    # -------------------------
    player_center = player.center
    fixed_center = fixed.center

    player_radius = player.width // 2
    fixed_radius = fixed.width // 2

    diff_x = player_center[0] - fixed_center[0]
    diff_y = player_center[1] - fixed_center[1]

    circle_hit = (diff_x * diff_x + diff_y * diff_y) <= (player_radius + fixed_radius) ** 2

    # -------------------------
    # AABB 충돌
    # 이제 회전 Surface 전체가 아니라
    # 실제 스프라이트 픽셀 기준 AABB와 충돌 검사
    # -------------------------
    aabb_hit = player.colliderect(fixed_sprite_aabb)

    # -------------------------
    # OBB 충돌
    # -------------------------
    player_points = [
        player.topleft,
        player.topright,
        player.bottomright,
        player.bottomleft,
    ]

    cx, cy = fixed.center
    half_w = fixed.width / 2
    half_h = fixed.height / 2

    top_left = (cx - half_w, cy - half_h)
    top_right = (cx + half_w, cy - half_h)
    bottom_right = (cx + half_w, cy + half_h)
    bottom_left = (cx - half_w, cy + half_h)

    fixed_obb_points = [
        rotate_point(*top_left, cx, cy, angle),
        rotate_point(*top_right, cx, cy, angle),
        rotate_point(*bottom_right, cx, cy, angle),
        rotate_point(*bottom_left, cx, cy, angle),
    ]

    obb_hit = sat_collision(player_points, fixed_obb_points)

    # -------------------------
    # 배경
    # -------------------------
    if obb_hit:
        screen.fill(RED_BG)
    else:
        screen.fill(WHITE)

    # -------------------------
    # 그리기
    # -------------------------
    screen.blit(player_image, player.topleft)
    screen.blit(rotated_fixed_image, rotated_fixed_rect.topleft)

    # AABB
    pygame.draw.rect(screen, RED, player, 2)
    pygame.draw.rect(screen, RED, fixed_sprite_aabb, 2)

    # Circle
    pygame.draw.circle(screen, BLUE, player_center, player_radius, 2)
    pygame.draw.circle(screen, BLUE, fixed_center, fixed_radius, 2)

    # OBB
    pygame.draw.polygon(screen, GREEN, fixed_obb_points, 2)

    # 텍스트
    circle_text = font.render(
        "Circle: HIT" if circle_hit else "Circle: MISS",
        True,
        BLUE if circle_hit else BLACK
    )
    aabb_text = font.render(
        "AABB: HIT" if aabb_hit else "AABB: MISS",
        True,
        RED if aabb_hit else BLACK
    )
    obb_text = font.render(
        "OBB: HIT" if obb_hit else "OBB: MISS",
        True,
        GREEN if obb_hit else BLACK
    )

    screen.blit(circle_text, (20, 20))
    screen.blit(aabb_text, (20, 55))
    screen.blit(obb_text, (20, 90))

    pygame.display.flip()

pygame.quit()
sys.exit()
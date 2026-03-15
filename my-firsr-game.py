import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fancy Particle Playground - Pretty Version")
clock = pygame.time.Clock()

particles = []

class Particle:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(1.5, 5.5)

        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

        self.life = random.randint(50, 90)
        self.max_life = self.life

        self.size = random.uniform(4, 9)

        # 더 예쁜 파스텔 느낌 색상
        palette = [
            (255, 170, 210),
            (170, 220, 255),
            (255, 230, 170),
            (200, 255, 200),
            (230, 180, 255),
        ]
        self.color = random.choice(palette)

        # 살짝 흔들리는 움직임용
        self.wobble = random.uniform(0, math.pi * 2)

    def update(self):
        self.x += self.vx
        self.y += self.vy

        # 중력
        self.vy += 0.06

        # 공기저항
        self.vx *= 0.995
        self.vy *= 0.995

        # 살짝 흔들리는 느낌
        self.wobble += 0.15
        self.x += math.sin(self.wobble) * 0.3

        self.life -= 1

    def draw(self, surf):
        if self.life <= 0:
            return

        life_ratio = self.life / self.max_life
        alpha = int(255 * life_ratio)
        radius = max(1, int(self.size * life_ratio + 1))

        # 파티클 전용 투명 Surface
        particle_surf = pygame.Surface((radius * 6, radius * 6), pygame.SRCALPHA)
        cx, cy = particle_surf.get_width() // 2, particle_surf.get_height() // 2

        # 바깥쪽 glow
        glow_color = (*self.color, alpha // 4)
        pygame.draw.circle(particle_surf, glow_color, (cx, cy), radius * 2)

        # 중간 glow
        mid_color = (*self.color, alpha // 2)
        pygame.draw.circle(particle_surf, mid_color, (cx, cy), int(radius * 1.4))

        # 중심
        core_color = (255, 255, 255, alpha)
        pygame.draw.circle(particle_surf, core_color, (cx, cy), radius)

        surf.blit(particle_surf, (self.x - cx, self.y - cy))

    def alive(self):
        return self.life > 0


def draw_background(surface, t):
    # 세로 그라데이션 + 물결 효과
    for y in range(HEIGHT):
        wave = math.sin(y * 0.012 + t) * 20
        r = int(20 + 20 * math.sin(t * 0.7 + y * 0.01))
        g = int(30 + y * 0.12 + wave)
        b = int(70 + y * 0.08 + 30 * math.sin(t + y * 0.008))

        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))

        pygame.draw.line(surface, (r, g, b), (0, y), (WIDTH, y))

    # 배경의 은은한 원형 빛
    glow_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

    glow1_x = WIDTH // 2 + int(math.sin(t * 0.8) * 180)
    glow1_y = HEIGHT // 2 + int(math.cos(t * 0.6) * 100)
    pygame.draw.circle(glow_surf, (255, 180, 220, 35), (glow1_x, glow1_y), 160)

    glow2_x = WIDTH // 2 + int(math.cos(t * 0.5) * 220)
    glow2_y = HEIGHT // 2 + int(math.sin(t * 0.9) * 120)
    pygame.draw.circle(glow_surf, (150, 220, 255, 30), (glow2_x, glow2_y), 200)

    surface.blit(glow_surf, (0, 0))


running = True
time_flow = 0

# 잔상 효과용 surface
fade_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()

    time_flow += 0.03

    draw_background(screen, time_flow)

    # 잔상 효과
    fade_surface.fill((0, 0, 0, 30))
    screen.blit(fade_surface, (0, 0))

    # 마우스 누를 때 파티클 생성
    if buttons[0]:
        for _ in range(10):
            particles.append(Particle(mouse_x, mouse_y))

        # 클릭 지점에 큰 빛 효과
        click_glow = pygame.Surface((180, 180), pygame.SRCALPHA)
        pygame.draw.circle(click_glow, (255, 255, 255, 35), (90, 90), 60)
        pygame.draw.circle(click_glow, (255, 200, 230, 25), (90, 90), 80)
        screen.blit(click_glow, (mouse_x - 90, mouse_y - 90))

    for p in particles:
        p.update()
        p.draw(screen)

    particles = [p for p in particles if p.alive()]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
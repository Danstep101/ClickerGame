import pygame
import sys

# Инициализация PyGame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Мой кликер (как Notcoin)")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)

# Счётчик монет
coins = 0
font = pygame.font.SysFont("Arial", 36)

# Кнопка для кликов
button_rect = pygame.Rect(100, 200, 200, 200)

# Основной цикл игры
running = True
while running:
    screen.fill(WHITE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                coins += 1

    # Рисуем кнопку
    pygame.draw.ellipse(screen, GOLD, button_rect)
    pygame.draw.ellipse(screen, BLACK, button_rect, 3)

    # Выводим счётчик
    text = font.render(f"Монеты: {coins}", True, BLACK)
    screen.blit(text, (100, 100))

    pygame.display.flip()

pygame.quit()
sys.exit()
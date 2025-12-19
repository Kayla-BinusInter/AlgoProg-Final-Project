import pygame
import sys
import level1

#hi:)
pygame.init()

# Window
screen = pygame.display.set_mode((960, 540))
pygame.display.set_caption("Final Project")
clock = pygame.time.Clock()
fps = 30

background_color = (122, 210, 119)
paddle_color = (255, 255, 255)
text = pygame.font.SysFont("Arial", 30)

# Makes sure it only stops running when you close the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quitting detected")
            running = False

# press arrow keys = color cahnge
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                level1.up_pressed_arrow = True
                level1.check_hit("up", "arrow")
            if event.key == pygame.K_DOWN:
                level1.down_pressed_arrow = True
                level1.check_hit("down", "arrow")
            if event.key == pygame.K_LEFT:
                level1.left_pressed_arrow = True
                level1.check_hit("left", "arrow")
            if event.key == pygame.K_RIGHT:
                level1.right_pressed_arrow = True
                level1.check_hit("right", "arrow")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                level1.up_pressed_arrow = False
            if event.key == pygame.K_DOWN:
                level1.down_pressed_arrow = False
            if event.key == pygame.K_LEFT:
                level1.left_pressed_arrow = False
            if event.key == pygame.K_RIGHT:
                level1.right_pressed_arrow = False

# press WASD keys = color change
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                level1.up_pressed_key = True
                level1.check_hit("w", "key")
            if event.key == pygame.K_s:
                level1.down_pressed_key = True
                level1.check_hit("s", "key")
            if event.key == pygame.K_a:
                level1.left_pressed_key = True
                level1.check_hit("a", "key")
            if event.key == pygame.K_d:
                level1.right_pressed_key = True
                level1.check_hit("d", "key")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                level1.up_pressed_key = False
            if event.key == pygame.K_s:
                level1.down_pressed_key = False
            if event.key == pygame.K_a:
                level1.left_pressed_key = False
            if event.key == pygame.K_d:
                level1.right_pressed_key = False

    screen.fill(background_color)

    level1.player1_arrows(screen)
    level1.player2_keys(screen)

    level1.update_notes()
    level1.update_spawning()
    level1.draw_notes(screen)
    level1.draw_judgement(screen)

    pygame.display.update()
    clock.tick(fps)

# Quits
pygame.quit()
sys.exit()
import pygame
import random

pygame.init()

spawn_timer = 0
spawn_delay = random.randint(5, 10)

notes = []
last_judgement = None      # "HIT" or "MISS"
judgement_time = 0        # time in ms
judgement_duration = 500  # duration to display judgement

# arrows
arrow_left_ua = pygame.image.load("gred_left_arrow.png")
arrow_left_ua = pygame.transform.scale(arrow_left_ua, (70, 65))
grarrowx = 590
grarrowy = 50

arrow_up_ua = pygame.image.load("gyellow_up_arrow.png")
arrow_up_ua = pygame.transform.scale(arrow_up_ua, (65, 70))
gyarrowx = 680
gyarrowy = 50

arrow_down_ua = pygame.image.load("ggreen_down_arrow.png")
arrow_down_ua = pygame.transform.scale(arrow_down_ua, (65, 70))
ggarrowx = 770
ggarrowy = 50

arrow_right_ua = pygame.image.load("gblue_right_arrow.png")
arrow_right_ua = pygame.transform.scale(arrow_right_ua, (70, 65))
gbarrowx = 860
gbarrowy = 50

arrow_left = pygame.image.load("red_left_arrow.png")
arrow_left = pygame.transform.scale(arrow_left, (70, 65))
rarrowx = 590
rarrowy = 50

arrow_up = pygame.image.load("yellow_up_arrow.png")
arrow_up = pygame.transform.scale(arrow_up, (65, 70))
yarrowx = 680
yarrowy = 50

arrow_down = pygame.image.load("green_down_arrow.png")
arrow_down = pygame.transform.scale(arrow_down, (65, 70))
garrowx = 770
garrowy = 50

arrow_right = pygame.image.load("blue_right_arrow.png")
arrow_right = pygame.transform.scale(arrow_right, (70, 65))
barrowx = 860
barrowy = 50

# other side arrows
Akey_left_ua = pygame.image.load("gred_left_arrow.png")
Akey_left_ua = pygame.transform.scale(Akey_left_ua, (70, 65))
grAkeyx = 30
grAkeyy = 50

Wkey_up_ua = pygame.image.load("gyellow_up_arrow.png")
Wkey_up_ua = pygame.transform.scale(Wkey_up_ua, (65, 70))
gyWkeyx = 120
gyWkeyy = 50

Skey_down_ua = pygame.image.load("ggreen_down_arrow.png")
Skey_down_ua = pygame.transform.scale(Skey_down_ua, (65, 70))
ggSkeyx = 210
ggSkeyy = 50

Dkey_right_ua = pygame.image.load("gblue_right_arrow.png")
Dkey_right_ua = pygame.transform.scale(Dkey_right_ua, (70, 65))
gbDkeyx = 300
gbDkeyy = 50

Akey_left = pygame.image.load("red_left_arrow.png")
Akey_left = pygame.transform.scale(Akey_left, (70, 65))
rAkeyx = 30
rAkeyy = 50

Wkey_up = pygame.image.load("yellow_up_arrow.png")
Wkey_up = pygame.transform.scale(Wkey_up, (65, 70))
yAkeyx = 120
yAkeyy = 50

Skey_down = pygame.image.load("green_down_arrow.png")
Skey_down = pygame.transform.scale(Skey_down, (65, 70))
gSkeyx = 210
gSkeyy = 50

Dkey_right = pygame.image.load("blue_right_arrow.png")
Dkey_right = pygame.transform.scale(Dkey_right, (70, 65))
bDkeyx = 300
bDkeyy = 50

# they start unpressed
up_pressed_arrow = False
down_pressed_arrow = False
left_pressed_arrow = False
right_pressed_arrow = False

up_pressed_key = False
down_pressed_key = False
left_pressed_key = False
right_pressed_key = False

# player 1 arrow keys
def player1_arrows(screen):
    if left_pressed_arrow:
        screen.blit(arrow_left, (rarrowx, rarrowy))
    else:
        screen.blit(arrow_left_ua, (grarrowx, grarrowy))

    if up_pressed_arrow:
        screen.blit(arrow_up, (yarrowx, yarrowy))
    else:
        screen.blit(arrow_up_ua, (gyarrowx, gyarrowy))

    if down_pressed_arrow:
        screen.blit(arrow_down, (garrowx, garrowy))
    else:
        screen.blit(arrow_down_ua, (ggarrowx, ggarrowy))

    if right_pressed_arrow:
        screen.blit(arrow_right, (barrowx, barrowy))
    else:
        screen.blit(arrow_right_ua, (gbarrowx, gbarrowy))

# player 2 wasd keys
def player2_keys(screen):
    if left_pressed_key:
        screen.blit(Akey_left, (rAkeyx, rAkeyy))
    else:
        screen.blit(Akey_left_ua, (grAkeyx, grAkeyy))

    if up_pressed_key:
        screen.blit(Wkey_up, (yAkeyx, yAkeyy))
    else:
        screen.blit(Wkey_up_ua, (gyWkeyx, gyWkeyy))

    if down_pressed_key:
        screen.blit(Skey_down, (gSkeyx, gSkeyy))
    else:
        screen.blit(Skey_down_ua, (ggSkeyx, ggSkeyy))

    if right_pressed_key:
        screen.blit(Dkey_right, (bDkeyx, bDkeyy))
    else:
        screen.blit(Dkey_right_ua, (gbDkeyx, gbDkeyy))

def spawn_note(direction, lane):
    if lane == "arrow":
        if direction == "left":
            x = rarrowx
        elif direction == "up":
            x = yarrowx
        elif direction == "down":
            x = garrowx
        elif direction == "right":
            x = barrowx

    elif lane == "key":
        if direction == "a":
            x = rAkeyx
        elif direction == "w":
            x = yAkeyx
        elif direction == "s":
            x = gSkeyx
        elif direction == "d":
            x = bDkeyx
    else:
        return

    notes.append({
        "lane": lane,
        "direction": direction,
        "x": x,
        "y": spawn_y,
        "speed": note_speed
    })
    print(notes)

hitline_y = yarrowy + arrow_up.get_height() // 2
hittolerance = 20

note_speed = 10
spawn_y = 540

FPS = 30
travel_time_ms = (spawn_y - hitline_y) / note_speed * (1000 / FPS)
hitwindow = 20
misswindow = 50

# so you can see the note on screen and its position
def draw_notes(screen):
    for note in notes:
        if note["lane"] == "arrow":
            if note["direction"] == "up":
                screen.blit(arrow_up, (note["x"], note["y"]))
            elif note["direction"] == "down":
                screen.blit(arrow_down, (note["x"], note["y"]))
            elif note["direction"] == "left":
                screen.blit(arrow_left, (note["x"], note["y"]))
            elif note["direction"] == "right":
                screen.blit(arrow_right, (note["x"], note["y"]))

        elif note["lane"] == "key":
            if note["direction"] == "w":
                screen.blit(Wkey_up, (note["x"], note["y"]))
            elif note["direction"] == "s":
                screen.blit(Skey_down, (note["x"], note["y"]))
            elif note["direction"] == "a":
                screen.blit(Akey_left, (note["x"], note["y"]))
            elif note["direction"] == "d":
                screen.blit(Dkey_right, (note["x"], note["y"]))

# moves notes
def update_notes():
    global last_judgement, judgement_time

    for note in notes[:]:
        note["y"] -= note["speed"]

        if note["y"] < hitline_y - misswindow:
            last_judgement = "MISS"
            judgement_time = pygame.time.get_ticks()
            notes.remove(note)

def update_spawning():
    global spawn_timer

    spawn_timer += 1

    if spawn_timer >= spawn_delay:
        spawn_timer = 0

        # Random lane
        lane = random.choice(["arrow", "key"])

        # Random direction depending on lane
        if lane == "arrow":
            direction = random.choice(["up", "down", "left", "right"])
        else:
            direction = random.choice(["w", "a", "s", "d"])

        spawn_note(direction, lane)

def check_hit(direction, lane):
    global last_judgement, judgement_time

    closest_note = None
    closest_distance = hittolerance + 1

    for note in notes:
        if note["direction"] == direction and note["lane"] == lane:
            distance = abs(note["y"] - hitline_y)
            if distance < closest_distance:
                closest_distance = distance
                closest_note = note

    if closest_note and closest_distance <= hitwindow:
        notes.remove(closest_note)
        last_judgement = "HIT"
        judgement_time = pygame.time.get_ticks()
        return True

    return False

def draw_judgement(screen):
    if last_judgement is None:
        return

    current_time = pygame.mixer.music.get_pos()
    if current_time - judgement_time > judgement_duration:
        return

    font = pygame.font.SysFont("", 40)

    if last_judgement == "HIT":
        color = (255, 255, 255)
    else:
        color = (255, 80, 80)

    text = font.render(last_judgement, True, color)
    rect = text.get_rect(center=(480, 270))  # center screen
    screen.blit(text, rect)
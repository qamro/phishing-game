import pygame
import random

pygame.init()

# set up the configuration and colors and fonts
WIDTH, HEIGHT = 800, 600
WATER_Y = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 32, True)

COLORS = {
    "orange": (255, 144, 40),
    "green": (90, 180, 70),
    "violet": (150, 80, 200)
}

score = 0
hook = {"x": 560, "y": 190, "state": "idle", "fish": None}


# make a fish 
def make_fish():
    return {
        "x": random.randint(0, WIDTH),
        "y": random.randint(WATER_Y + 60, HEIGHT - 60),
        "speed": random.choice([-3, -2, 2, 3]),
        "color": random.choice(list(COLORS))
    }
    

fishes = [make_fish() for _ in range(6)]


def cast():
    if hook["state"] == "idle":
        hook["state"] = "down"
        


def update():
    global score
    # update the fishes
    for fish in fishes:
        fish["x"] += fish["speed"]
        if fish["x"] < -40 or fish["x"] > WIDTH + 40:
            fish["speed"] = -fish["speed"]
    
    # update the hook
    if hook["state"] == "down":
        hook["y"] += 6
        for fish in fishes:
            near_x = abs(fish["x"] - hook["x"]) < 30
            near_y = abs(fish["y"] - hook["y"]) < 20
            if near_x and near_y:
                hook["state"] = "up"
                hook["fish"] = fish
                score += 1
                break
        if hook["y"] > HEIGHT - 40:
            hook["state"] = "up"
    elif hook["state"] == "up":
        hook["y"] -= 8
        if hook["fish"]:
            hook["fish"]["x"] = hook["x"]
            hook["fish"]["y"] = hook["y"] 
        if hook["y"] <= 190:
            if hook["fish"]:
                fishes.remove(hook["fish"])
                fishes.append(make_fish())
                hook["fish"] = None
            hook["state"] = "idle"



import pygame, sys, json
import tkinter as tk
from tkinter import filedialog
import button

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

pygame.display.set_caption("MuzicPlayz")
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

icons = pygame.Surface((256, 256))
icons.fill((0, 0, 0))
pygame.display.set_icon(icons)

DATA_FILE_PATH = "data.json"
dataObj = {
    "paused": True,
    "directory": ""
}
try:
    with open(DATA_FILE_PATH, "r") as file:
        dataObj = json.load(file)
except:
    with open(DATA_FILE_PATH, "w") as file:
        json.dump(dataObj, file, indent=4)

openFileBtn: button.Button = button.Button(pygame.Rect((400 - 180) / 2, 400 - 30 - 15, 180, 30), 3)

def selectFolder() -> str:
    root = tk.Tk()
    root.withdraw()
    folderPath = filedialog.askdirectory()
    root.destroy()
    return folderPath

running = True
while running:
    screen.fill((20, 20, 20))

    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE: running = False
    
    if openFileBtn.isClicked(events):
        dataObj["directory"] = selectFolder()
        print("[INFO]: Chosen directory '" + dataObj["directory"] + "'")

    openFileBtn.draw(screen, "OPEN FOLDER", pygame.Color(255, 255, 255), pygame.Color(0, 0, 0))

    pygame.display.update()
    clock.tick(60)

with open(DATA_FILE_PATH, "w") as file:
    json.dump(dataObj, file, indent=4)

pygame.quit()
sys.exit()

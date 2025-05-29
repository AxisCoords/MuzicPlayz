import random
import pygame, sys, json
import tkinter as tk
import glob
from tkinter import filedialog
from button import Button

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

pygame.display.set_caption("MuzicPlayz")
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

icons = pygame.Surface((256, 256))
icons.fill((0, 0, 0))
pygame.display.set_icon(icons)

def setMusics():
    global musicFiles, dataObj
    musicFiles = glob.glob(dataObj["directory"] + "/*.mp3")
    musicFiles = [f.replace("\\", "/") for f in musicFiles]

DATA_FILE_PATH = "data.json"
dataObj = {
    "paused": True,
    "directory": "" 
}
try:
    with open(DATA_FILE_PATH, "r") as file:
        dataObj = json.load(file)
        setMusics()
except:
    with open(DATA_FILE_PATH, "w") as file:
        json.dump(dataObj, file, indent=4)

openFileBtn: Button = Button(pygame.Rect((400 - 180) / 2, 400 - 30 - 15, 180, 30), 3)

def selectFolder() -> str:
    root = tk.Tk()
    root.withdraw()
    folderPath = filedialog.askdirectory()
    root.destroy()
    return folderPath

# TODO: Play songs
def playSong():
    if len(musicFiles) > 1:
        rand = random.choice(musicFiles)

        pygame.mixer.music.load(rand)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.2)

        print("Playing: " + rand)
    else:
        print("[WARNING]: No songs found")

running = True
while running:
    screen.fill((20, 20, 20))

    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE: running = False
    
    if openFileBtn.isClicked(events):
        dataObj["directory"] = selectFolder()
        setMusics()
        print("[INFO]: Chosen directory '" + dataObj["directory"] + "'")

        playSong()

        print(musicFiles)

    openFileBtn.draw(screen, "OPEN FOLDER", pygame.Color(255, 255, 255), pygame.Color(0, 0, 0))

    pygame.display.update()
    clock.tick(60)

with open(DATA_FILE_PATH, "w") as file:
    json.dump(dataObj, file, indent=4)

pygame.quit()
sys.exit()

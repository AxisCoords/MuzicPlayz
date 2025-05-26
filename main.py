import pygame, sys
import tkinter as tk
from tkinter import filedialog
import button

pygame.init()
pygame.mixer.init()

pygame.display.set_caption("MuzicPlaiz")
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

icons = pygame.Surface((256, 256))
icons.fill((0, 0, 0))
pygame.display.set_icon(icons)

openFileBtn: button.Button = button.Button(pygame.Rect((400 - 160) / 2, ((400 - 30) / 2) + 60, 160, 30), 4)
playBtn: button.Button = button.Button(pygame.Rect(0, 0, 40, 40), 20)

def selectFolder() -> str:
    root = tk.Tk()
    root.withdraw()
    folderPath = filedialog.askdirectory()
    root.destroy()
    return folderPath

running = True
while running:
    screen.fill((0, 0, 0))

    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            running = False
    
    if openFileBtn.isClicked(events):
        directory = selectFolder()
        if len(directory) > 0: print(directory)
        else: print("[WARNING]: Didn't select any folder")

    openFileBtn.draw(screen, "Hello World!", pygame.Color(255, 255, 255), pygame.Color(0, 0, 0))
    playBtn.draw(screen, "I I", pygame.Color(255, 255, 255), pygame.Color(0, 0, 0))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()

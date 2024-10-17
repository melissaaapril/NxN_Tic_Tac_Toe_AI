import pygame
import os

def init_sounds():
    pygame.mixer.init()

    # gonna use relative path here to make it easier
    sound_folder = os.path.join(os.path.dirname(__file__), "sounds")

    # load sounds from the relative path
    global song, circle_sound, x_sound, win_sound, lose_sound, draw_sound
    try:
        song = pygame.mixer.Sound(os.path.join(sound_folder, 'song.mp3'))
        circle_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'circle.mp3'))
        x_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'x.mp3'))
        win_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'win.mp3'))
        lose_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'lose.mp3'))
        draw_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'draw.mp3'))
        song.set_volume(0.5)
    except pygame.error as e:
        print(f"Error loading sound: {e}")

def play_background_music():
    try:
        song.play(-1)  # Loop indefinitely
    except NameError:
        pass  

def stop_background_music():
    try:
        song.stop()
    except NameError:
        pass  

def play_circle_sound():
    try:
        circle_sound.play()
    except NameError:
        pass  

def play_x_sound():
    try:
        x_sound.play()
    except NameError:
        pass  

def play_win_sound():
    try:
        win_sound.play()
    except NameError:
        pass  

def play_lose_sound():
    try:
        lose_sound.play()
    except NameError:
        pass  

def play_draw_sound():
    try:
        draw_sound.play()
    except NameError:
        pass  

import pygame
import csv
import os
from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw
from config import ROOT

ROOT.mainloop()

if os.path.isfile(os.getcwd()+"/config.csv"):
    with open("config.csv","r") as cf:
        reader = csv.reader(cf)
        for i in reader:
            if i != []:
                R1 = i[0]
                R2 = i[1]
                R3 = i[2]
                KEY = i[3]
                RINGS = eval(i[4])
                PBC = eval(i[5])
                RF = i[6] 


    animating = True

    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Enigma Machine Simulator")

    MONO = pygame.font.SysFont("FreeMono", 22)
    BOLD = pygame.font.SysFont("FreeMono", 22, bold = True)

    WIDTH = 1300
    HEIGHT = 750
    MARGINS = {'top':150, 'bottom':50, 'left': 100, 'right':100}
    GAP = 100

    INPUT = ""
    OUTPUT = ""

    PATH = []

    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

    ROTORS = {
        'I': Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ",'Q'),
        "II" : Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE",'E'),
        "III" : Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO",'V'),
        "IV" : Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB",'J'),
        "V" : Rotor("VZBRGITYUPSDNHLXAWMJQOFECK",'Z')
    }

    REFLECTORS = {
        "A" : Reflector("EJMZALYXVBWFCRQUONTSPIKHGD"),
        "B" : Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT"),
        "C" : Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
    }

    KB = Keyboard()
    PB = Plugboard(PBC)

    ENIGMA = Enigma(REFLECTORS[RF],ROTORS[R1],ROTORS[R2],ROTORS[R3],PB,KB)

    ENIGMA.set_rings(RINGS)
    ENIGMA.set_key(KEY)


    while animating:

        SCREEN.fill("#333333")

        text = BOLD.render(INPUT, True, "white")
        text_box = text.get_rect(center = (WIDTH/2,MARGINS["top"]/3))
        SCREEN.blit(text, text_box)

        text = MONO.render(OUTPUT, True, "white")
        text_box = text.get_rect(center = (WIDTH/2,MARGINS["top"]/3+25))
        SCREEN.blit(text, text_box)

        draw(ENIGMA, PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                animating = False
                os.remove(os.getcwd() + "/config.csv")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    INPUT += " "
                    OUTPUT += " "
                else:
                    key = event.unicode
                    if key in "abcdefghijklmnopqrstuvwxyz":
                        letter = key.upper()
                        INPUT += letter
                        PATH, cipher = ENIGMA.encipher(letter)
                        OUTPUT += cipher
                        
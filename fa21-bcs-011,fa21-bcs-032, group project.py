import pygame
import sys
import random
import time
import re
from pygame.locals import *
background = (238, 197, 145)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (69, 139, 116)
BLUE = (0, 0, 255)
GREY = (200, 200, 200)
LEFT_CLICK = (1, 0, 0)
RIGHT_CLICK = (0, 0, 1)
pygame.init()
pygame.display.set_caption("Hangman")
Display = pygame.display.set_mode((500, 500), 0, 32)
Easy = ["STAR", "PICNIC", "PIE", "HAT", "HEART", "FLAG"]
Medium = ["CARPET", "POPCORN", "SEAFOOD", "DOORBELL", "COWBOY",
          "INSIDE", "OUTSIDE", "RAINBOW", "POSTMAN", "WATERMELON",
          "FOOTBALL", "STRAWBERRY"]
Hard = ["BACKGROUND", "BOOKWORM", "FIREFIGHTER", "SOUNDPROOF", "THUNDERSTORM",
        "CAMPGROUND", "FRIENDSHIP", "SKYSCRAPER", "SUPERHUMAN", "FINGERPRINT",
        "MASTERPIECE", "LOUDSPEAKER"]
Font = pygame.font.Font("freesansbold.ttf", 33)
Font2 = pygame.font.Font("freesansbold.ttf", 20)
Display.fill(background)


def random_num(choice):
    Random_Num = 0
    if choice == 1:
        Random_Num = random.randint(0, len(Easy) - 1)
    elif choice == 2:
        Random_Num = random.randint(0, len(Medium) - 1)
    elif choice == 3:
        Random_Num = random.randint(0, len(Hard) - 1)
    return Random_Num


def list(number, choice):
    if choice == 1:
        Word = Easy[number]
    elif choice == 2:
        Word = Medium[number]
    elif choice == 3:
        Word = Hard[number]
    return Word


def Hangman(condition):
    if condition == 0:
        pygame.draw.line(Display, GREY, (10, 400), (300, 400), 8)
        pygame.draw.line(Display, GREY, (50, 50), (50, 400), 8)
        pygame.draw.line(Display, GREY, (50, 60), (250, 60), 8)
        pygame.draw.line(Display, GREY, (150, 60), (150, 100), 8)
        pygame.draw.circle(Display, GREY, (150, 150), 50, 8)
        pygame.draw.line(Display, GREY, (150, 200), (150, 300), 8)
        pygame.draw.line(Display, GREY, (150, 210), (100, 250), 8)
        pygame.draw.line(Display, GREY, (150, 210), (200, 250), 8)
        pygame.draw.line(Display, GREY, (150, 300), (100, 350), 8)
        pygame.draw.line(Display, GREY, (150, 300), (200, 350), 8)
    elif condition == 1:
        pygame.draw.line(Display, WHITE, (10, 400), (300, 400), 8)
    elif condition == 2:
        pygame.draw.line(Display, WHITE, (50, 50), (50, 400), 8)
    elif condition == 3:
        pygame.draw.line(Display, WHITE, (50, 60), (250, 60), 8)
    elif condition == 4:
        pygame.draw.line(Display, WHITE, (150, 60), (150, 100), 8)
    elif condition == 5:
        pygame.draw.circle(Display, WHITE, (150, 150), 50, 8)
    elif condition == 6:
        pygame.draw.line(Display, WHITE, (150, 200), (150, 300), 8)
    elif condition == 7:
        pygame.draw.line(Display, WHITE, (150, 210), (100, 250), 8)
    elif condition == 8:
        pygame.draw.line(Display, WHITE, (150, 210), (200, 250), 8)
    elif condition == 9:
        pygame.draw.line(Display, WHITE, (150, 300), (100, 350), 8)
    elif condition == 10:
        pygame.draw.line(Display, WHITE, (150, 300), (200, 350), 8)


def PreHangMan():
    pygame.draw.line(Display, GREEN, (10, 400), (190, 400), 8)
    pygame.draw.line(Display, GREEN, (30, 90), (30, 400), 8)
    pygame.draw.line(Display, GREEN, (30, 100), (160, 100), 8)
    pygame.draw.line(Display, GREEN, (100, 100), (100, 120), 8)
    pygame.draw.circle(Display, GREEN, (100, 170), 50, 8)
    pygame.draw.line(Display, GREEN, (100, 220), (100, 320), 8)
    pygame.draw.line(Display, GREEN, (100, 230), (50, 270), 8)
    pygame.draw.line(Display, GREEN, (100, 230), (150, 270), 8)
    pygame.draw.line(Display, GREEN, (100, 320), (50, 360), 8)
    pygame.draw.line(Display, GREEN, (100, 320), (150, 360), 8)


def StartScreen():
    Display.blit(pygame.font.Font("freesansbold.ttf", 40).render("HANGMAN", True, BLACK), (20, 20))
    Display.blit(Font2.render("by FA21-BCS-011, FA21-BCS-032", True, BLACK), (60, 60))
    Display.blit(Font.render("Level Difficulty", True, BLACK), (200, 150))
    Display.blit(Font2.render("1-Easy", True, BLACK), (200, 200))
    Display.blit(Font2.render("2-Medium", True, BLACK), (200, 250))
    Display.blit(Font2.render("3-Hard", True, BLACK), (200, 300))


def main():
    TheChoice = 0
    StartScreen()
    PreHangMan()
    FirstCondition = True
    while FirstCondition:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[1] > 200 and
                    pygame.mouse.get_pos()[0] < 265 and pygame.mouse.get_pos()[1] < 215):
                    TheChoice = 1
                    FirstCondition = False
                    break
                elif (pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[1] > 250 and
                      pygame.mouse.get_pos()[0] < 295 and pygame.mouse.get_pos()[1] < 265):
                    TheChoice = 2
                    FirstCondition = False
                    break
                elif (pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[1] > 300 and
                      pygame.mouse.get_pos()[0] < 265 and pygame.mouse.get_pos()[1] < 315):
                    TheChoice = 3
                    FirstCondition = False
                    break
        if (TheChoice != 0):
            Display.fill(background)
        pygame.display.update()
    TheNum = random_num(TheChoice)
    TheWord = list(TheNum, TheChoice)
    EmptyList = []
    for i in range(len(TheWord)):
        EmptyList.append('_ ')
    Hidden = Font.render("".join(EmptyList), True, BLACK)
    HiddenRect = Hidden.get_rect()
    HiddenRect.center = (350, 250)
    Display.blit(Hidden, HiddenRect)
    Condition = 0
    Off = 0
    LastKeyPressed = ""
    Display.blit(pygame.font.Font("freesansbold.ttf", 15).render("Press 0 to quit game", True, BLACK), (20, 10))
    while True:
        Hangman(Condition)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                LastKeyPressed = event.key
                pygame.draw.rect(Display, background, (220, 200, 280, 100))
                pygame.draw.rect(Display, background, (260, 50, 200, 100))
                UserInput = event.key
                if re.search("[a-z]", chr(event.key)):
                    if ((chr(event.key).upper() in TheWord) or (chr(event.key).lower() in TheWord)):
                        for i in range(len(TheWord)):
                            if ((TheWord[i] == (chr(event.key)).upper()) or (TheWord[i] == (chr(event.key)).lower())):
                                EmptyList[i] = TheWord[i]
                    else:
                        Condition = Condition + 1
                    Hidden = Font.render("".join(EmptyList), True, BLACK)
                    HiddenRect = Hidden.get_rect()
                    HiddenRect.center = (350, 250)
                    Display.blit(Hidden, HiddenRect)
                else:
                    if (event.key == K_0 or event.key == 256):
                        Display.blit(Font.render("EXIT?", True, RED), (340, 220))
                        Display.blit(Font2.render("Yes", True, BLACK), (340, 270))
                        Display.blit(Font2.render("No", True, BLACK), (415, 270))
                    else:
                        Input = Font2.render("INVALID INPUT!!!", True, RED)
                        InputRect = Input.get_rect()
                        InputRect.center = (350, 100)
                        Display.blit(Input, InputRect)
                        Display.blit(Hidden, HiddenRect)
            elif event.type == KEYUP:
                pygame.draw.rect(Display, background, (260, 50, 200, 100))
            elif event.type == MOUSEBUTTONDOWN:
                    if (pygame.mouse.get_pressed() == LEFT_CLICK):
                        if (pygame.mouse.get_pos()[0] > 340 and pygame.mouse.get_pos()[1] > 270 and
                                pygame.mouse.get_pos()[0] < 385 and pygame.mouse.get_pos()[1] < 285):
                            pygame.draw.rect(Display, background, (340, 270, 35, 25))
                            Display.blit(Font2.render("Yes", True, GREEN), (340, 270))
                        elif (pygame.mouse.get_pos()[0] > 415 and pygame.mouse.get_pos()[1] > 270 and
                              pygame.mouse.get_pos()[0] < 450 and pygame.mouse.get_pos()[1] < 285):
                            pygame.draw.rect(Display, background, (415, 270, 35, 25))
                            Display.blit(Font2.render("No", True, GREEN), (415, 270))
            elif event.type == MOUSEBUTTONUP:
                if (LastKeyPressed == K_0 or LastKeyPressed == 256):
                    if (pygame.mouse.get_pos()[0] > 340 and pygame.mouse.get_pos()[1] > 270 and
                            pygame.mouse.get_pos()[0] < 385 and pygame.mouse.get_pos()[1] < 285):
                        pygame.quit()
                        sys.exit()
                    elif (pygame.mouse.get_pos()[0] > 415 and pygame.mouse.get_pos()[1] > 270 and
                          pygame.mouse.get_pos()[0] < 450 and pygame.mouse.get_pos()[1] < 285):
                        pygame.draw.rect(Display, background, (415, 270, 35, 25))
                        Display.blit(Font2.render("No", True, GREEN), (415, 270))
                        pygame.draw.rect(Display, background, (300, 200, 200, 100))
                        Hidden = Font.render("".join(EmptyList), True, BLACK)
                        HiddenRect = Hidden.get_rect()
                        HiddenRect.center = (400, 250)
                        Display.blit(Hidden, HiddenRect)
                        LastKeyPressed = ""
                    else:
                        pygame.draw.rect(Display, background, (340, 270, 35, 25))
                        Display.blit(Font2.render("Yes", True, BLACK), (340, 270))
                        pygame.draw.rect(Display, background, (415, 270, 35, 25))
                        Display.blit(Font2.render("No", True, BLACK), (415, 270))
        if (Condition == 10):
            Display.fill(background)
            Hangman(Condition + 1)
            Over = Font2.render("GAME OVER!!!", True, RED)
            OverRect = Over.get_rect()
            OverRect.center = (250, 220)
            Display.blit(Over, OverRect)
            Off = 1
        elif (TheWord == "".join(EmptyList)):
            Display.fill(background)
            Cong = Font.render("CONGRATS!!!", True, GREEN)
            CongRect = Cong.get_rect()
            CongRect.center = (250, 220)
            Display.blit(Cong, CongRect)
            Word = Font2.render("The word is:", True, BLACK)
            WordRect = Word.get_rect()
            WordRect.center = (250, 250)
            Display.blit(Word, WordRect)
            Word2 = Font.render(TheWord, True, BLACK)
            Word2Rect = Word2.get_rect()
            Word2Rect.center = (250, 285)
            Display.blit(Word2, Word2Rect)
            Off = 1
        pygame.display.update()
        pygame.time.Clock().tick(30)
        if (Off == 1):
            time.sleep(3)
            pygame.quit()
            sys.exit()
main()
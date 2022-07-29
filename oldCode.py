import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (0, 0)
os.environ['SDL_VIDEO_CENTERED'] = '0'
import pygame
from pygame.locals import *
from sys import exit
import time

# game screen settings
pygame.init()
size = 640, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mugic")

# global vars
bg_pos = (0, 0)
highScore = []
last_state = 0
player_score = 0


# read high score
def high_score_read():
    fin = open('score\\score.txt', 'r')
    for line in fin:
        a = line.strip()
        s = a.split(' ')
        for i in range(len(s)):
            highScore.append(s[i])
    fin.close()


def game_intro():
    global bg_pos

    # intro background settings
    background = pygame.image.load("image\\Start.jpg").convert()
    intro_start_bg = pygame.image.load("image\\Start.jpg").convert()
    intro_help_bg = pygame.image.load("image\\Help.jpg").convert()
    intro_quit_bg = pygame.image.load("image\\Quit.jpg").convert()

    # intro settings
    intro = True
    intro_state = 1  # which intro_button should be highlighted

    # intro bg music settings
    pygame.mixer.music.load('song\\UnNOT!CED_FULL.mp3')
    pygame.mixer.music.play(-1)

    # changing intro background
    def intro_change(state):
        if intro_state == 1:
            background.blit(intro_start_bg, bg_pos)
        elif intro_state == 2:
            background.blit(intro_help_bg, bg_pos)
        else:
            background.blit(intro_quit_bg, bg_pos)

    # show help and other stuff
    def game_help():
        # state switches
        intro = False
        help = True

        # help pic settings
        help_pic = pygame.image.load('image\\Help2.jpg').convert()

        while help:
            background.blit(help_pic, bg_pos)  # change background into help page.
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == pygame.K_RETURN:  # if enter pressed, return to main menu.
                        background.blit(intro_help_bg, (0, 0))
                        help = False
                        intro = True
            screen.blit(background, bg_pos)
            pygame.display.update()

    while intro:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_DOWN:  # if "down" key is pressed, change intro_state.
                    if intro_state < 3:
                        intro_state += 1
                if event.key == pygame.K_UP:  # if "up" key is pressed, change intro_state.
                    if intro_state > 1:
                        intro_state -= 1
                if event.key == pygame.K_RETURN:  # if "enter is pressed, do things.
                    if intro_state == 1:  # if intro_state == 1, stop music and continue.
                        pygame.mixer.music.stop()
                        intro = False
                        song_selection()
                    elif intro_state == 2:  # if intro_state == 2,  proceed to game_help.
                        game_help()
                    else:  # intro_state == 3  # if intro_state == 3, quit program.
                        quit()
            intro_change(intro_state)  # update highlighted button by calling intro_function
        screen.blit(background, (0, 0))
... (還剩 466 行)
　收起
mugic.py
20 KB
﻿
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (0, 0)
os.environ['SDL_VIDEO_CENTERED'] = '0'
import pygame
from pygame.locals import *
from sys import exit
import time

# game screen settings
pygame.init()
size = 640, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mugic")

# global vars
bg_pos = (0, 0)
highScore = []
last_state = 0
player_score = 0


# read high score
def high_score_read():
    fin = open('score\\score.txt', 'r')
    for line in fin:
        a = line.strip()
        s = a.split(' ')
        for i in range(len(s)):
            highScore.append(s[i])
    fin.close()


def game_intro():
    global bg_pos

    # intro background settings
    background = pygame.image.load("image\\Start.jpg").convert()
    intro_start_bg = pygame.image.load("image\\Start.jpg").convert()
    intro_help_bg = pygame.image.load("image\\Help.jpg").convert()
    intro_quit_bg = pygame.image.load("image\\Quit.jpg").convert()

    # intro settings
    intro = True
    intro_state = 1  # which intro_button should be highlighted

    # intro bg music settings
    pygame.mixer.music.load('song\\UnNOT!CED_FULL.mp3')
    pygame.mixer.music.play(-1)

    # changing intro background
    def intro_change(state):
        if intro_state == 1:
            background.blit(intro_start_bg, bg_pos)
        elif intro_state == 2:
            background.blit(intro_help_bg, bg_pos)
        else:
            background.blit(intro_quit_bg, bg_pos)

    # show help and other stuff
    def game_help():
        # state switches
        intro = False
        help = True

        # help pic settings
        help_pic = pygame.image.load('image\\Help2.jpg').convert()

        while help:
            background.blit(help_pic, bg_pos)  # change background into help page.
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == pygame.K_RETURN:  # if enter pressed, return to main menu.
                        background.blit(intro_help_bg, (0, 0))
                        help = False
                        intro = True
            screen.blit(background, bg_pos)
            pygame.display.update()

    while intro:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_DOWN:  # if "down" key is pressed, change intro_state.
                    if intro_state < 3:
                        intro_state += 1
                if event.key == pygame.K_UP:  # if "up" key is pressed, change intro_state.
                    if intro_state > 1:
                        intro_state -= 1
                if event.key == pygame.K_RETURN:  # if "enter is pressed, do things.
                    if intro_state == 1:  # if intro_state == 1, stop music and continue.
                        pygame.mixer.music.stop()
                        intro = False
                        song_selection()
                    elif intro_state == 2:  # if intro_state == 2,  proceed to game_help.
                        game_help()
                    else:  # intro_state == 3  # if intro_state == 3, quit program.
                        quit()
            intro_change(intro_state)  # update highlighted button by calling intro_function
        screen.blit(background, (0, 0))
        pygame.display.update()


def song_selection():
    song_select_bg = pygame.image.load('image\\slit_sel.jpg').convert()

    song_sel = True
    song_select_state = 1

    last_state = 0

    # use for setting difficulty
    def difficulty_sel(song):
        global highScore

        # bg settings
        slit_ez_bg = pygame.image.load('image\\SlitEasy.jpg').convert()
        slit_hd_bg = pygame.image.load('image\\SlitHard.jpg').convert()
        '''
        perse_ez_bg = pygame.image.load('image\\perse_easy.png').convert()
        perse_hd_bg = pygame.image.load('image\\perse_hard.png').convert()
        un_ez_bg = pygame.image.load('image\\un_easy.png').convert()
        un_hd_bg = pygame.image.load('image\\un_hard.png').convert()
        '''
        difficulty = ['easy', 'hard']
        song_difficulty = 1
        dif = True

        while dif:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == pygame.K_RIGHT:  # if "DOWN" key is pressed, change difficulty_state.
                        if song_difficulty == 1:
                            song_difficulty = 2
                    if event.key == pygame.K_LEFT:  # if "UP" key is pressed, change difficulty_state.
                        if song_difficulty == 2:
                            song_difficulty = 1
                    if event.key == pygame.K_RETURN:  # if "ENTER" is pressed, return state and continue.
                        if song_difficulty == 1:
                            pygame.mixer.music.stop()
                            pygame.time.delay(1500)
                            game(song, difficulty[song_difficulty - 1])
                        else:
                            pygame.mixer.music.stop()
                            pygame.time.delay(1500)
                            game(song, difficulty[song_difficulty - 1])

            if song_difficulty == 1:
                screen.blit(slit_ez_bg, bg_pos)
            else:
                screen.blit(slit_hd_bg, bg_pos)

            pygame.display.update()

    def song_state(state):
        global last_state

        pers_pic = pygame.image.load('image\\PersephoneSel.jpg').convert()
        slit_pic = pygame.image.load('image\\slit_sel.jpg').convert()
        un_pic = pygame.image.load('image\\UnnoticedSel.jpg').convert()

        if state == 1:
            screen.blit(slit_pic, bg_pos)
            if last_state != state:
                pygame.mixer.music.load('song\\slit.mp3')
                pygame.mixer.music.play(-1)
        elif state == 2:
            screen.blit(pers_pic, bg_pos)
            if last_state != state:
                pygame.mixer.music.load('song\\Persephone.mp3')
                pygame.mixer.music.play(-1)
        else:
            screen.blit(un_pic, bg_pos)
            if last_state != state:
                pygame.mixer.music.load('song\\UnNOT!CED.mp3')
                pygame.mixer.music.play(-1)

        last_state = state

    while song_sel:
        screen.blit(song_select_bg, bg_pos)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:  # if "Left" key is pressed, change song preview.
                    pygame.mixer.music.stop()
                    pygame.time.wait(500)
                    song_select_state += 1
                    if song_select_state > 3:
                        song_select_state = 1
                if event.key == pygame.K_RIGHT:  # if "Right" key is pressed, change song preview.
                    pygame.mixer.music.stop()
                    pygame.time.wait(500)
                    song_select_state -= 1
                    if song_select_state < 1:
                        song_select_state = 3
                if event.key == pygame.K_RETURN:
                    if song_select_state == 1:
                        difficulty_sel('slit')

        song_state(song_select_state)
        pygame.display.update()


def game(song, difficulty):
    global highScore, bg_pos, player_score

    game_bg_c = pygame.image.load("image\\Play.jpg").convert()
    game_bg = pygame.image.load("image\\Play.jpg").convert()

    # charts and notes section
    chart = []
    note_process = []
    current_notes = []
    D_NOTE_POS = 140
    F_NOTE_POS = 230
    J_NOTE_POS = 320
    K_NOTE_POS = 410
    note_pic = pygame.image.load('image\\note.png').convert()

    # pressed light related section
    press_light_pic = pygame.image.load('image\\shine.jpg').convert()
    PRESS_LIGHT_TIME = 10
    press_light = []

    # song related section
    SLIT_BPM = 165

    # judgement related section
    PERFECT_ZONE = 50
    GOOD_ZONE = 100
    judge_font = pygame.font.Font('font\\jf-openhuninn-1.0.ttf', 16)
    JUDGE_FONT_Y = 500
    JUDGE_LINE = 624
    judge = []

    # score related section
    score_font = pygame.font.Font('font\\jf-openhuninn-1.0.ttf', 28)
    score_pos = (16.5, 250)
    player_score = 0
    playerMaxScore = 1000000
    note_score = 0

    # speed settings
    clock = pygame.time.Clock()
    clock_adjust = clock.tick(500)
    notes_fall_speed = clock_adjust * 0.9

    # timer settings related
    start_timer = 0
    timing = 0
    timer = 0
    stop_timer = 0

    # convert chart.txt to array
    def chart_input():
        if song == 'slit':
            if difficulty == 'easy':
                chart_txt = open('chart\\slit_ez.txt', 'r')
            else:
                chart_txt = open('chart\\slit_hd.txt', 'r')
        elif song == 'perse':
            if difficulty == 'easy':
                pass
            else:
                pass
        else:
            if difficulty == 'easy':
                pass
            else:
                pass

        for line in chart_txt:
            chart_a = line.strip()
            chart_b = chart_a.split(',')
            chart.append(chart_b)
        chart_txt.close()
    chart_input()

    '''def chart_convert(song):
        for line in chart:
            if song == 'slit':
                line[0] = line[0] * SLIT_BPM
            else:
                pass
    chart_convert(song)'''

    def notes_count():
        count = 0
        for i in chart:
            for j in i:
                if j == '1':
                    count += 1
        return count

    note_count = notes_count()

    def note_score_set():
        return playerMaxScore / note_count

    note_score = note_score_set()

    def bpm_timer(song):
        if song == 'slit':
            return time.perf_counter() / 60 * SLIT_BPM * 2 // 1

    def note_pop(note_coord):
        for i in range(len(current_notes)):
            if current_notes[i] == note_coord:
                current_notes.pop(i)
                break

    def judgement(note_coord):
        global player_score
        if abs(note_coord[1] - JUDGE_LINE) < PERFECT_ZONE:
            judge.append(['Perfect', note_coord[0] + 12, 100])
            player_score += note_score
        else:
            judge.append(['Good', note_coord[0] + 17, 100])
            player_score += note_score * 0.7
        note_pop(note_coord)

    def find_note(note_x):
        note_found = []
        for j in current_notes:  # format:[x, y]
            if note_x == j[0] and abs(j[1] - JUDGE_LINE) < GOOD_ZONE and not note_found:
                note_found.append(j)
        if note_found:
            judgement(*note_found)

    def note_press(pressed_key):
        if current_notes:  # format:[x, y]
            if pressed_key == 'd':
                find_note(D_NOTE_POS + 5)
                press_light.append([D_NOTE_POS, 20])
            if pressed_key == 'f':
                find_note(F_NOTE_POS + 5)
                press_light.append([F_NOTE_POS, 20])
            if pressed_key == 'j':
                find_note(J_NOTE_POS + 5)
                press_light.append([J_NOTE_POS, 20])
            if pressed_key == 'k':
                find_note(K_NOTE_POS + 5)
                press_light.append([K_NOTE_POS, 20])

    def notes_move():
        for i in range(len(current_notes)):  # format: [x, y]
            game_bg.blit(note_pic, current_notes[i])
            current_notes[i][1] += notes_fall_speed
            if current_notes[i][1] >= 720:
                judge.append(['miss', current_notes[i][0] + 22, 100])
                current_notes.pop(i)
                break

    def pressed_light():
        if press_light:
            for i in range(len(press_light)):
                if press_light[i][1] > 0:
                    game_bg.blit(press_light_pic, (press_light[i][0], 624))
                else:
                    press_light.pop()
                    break
                press_light[i][1] -= 1

    def judge_font_set():
        if judge:  # format: (case, x, 250)
            for i in range(len(judge)):
                if judge[i][2] > 0:
                    judge_text = judge_font.render(judge[i][0], True, (153, 217, 234))
                    game_bg.blit(judge_text, (judge[i][1], JUDGE_FONT_Y))
                else:
                    judge.pop(i)
                    break
                judge[i][2] -= 1

    def score_print():
        copy_score = player_score
        if player_score == 0:
            copy_counter = 1
        else:
            copy_counter = 0
        while copy_score > 1:
            copy_score /= 10
            copy_counter += 1
        score_text = score_font.render('0' * (6 - copy_counter) + str(round(player_score)), True, (255, 255, 255))
        game_bg.blit(score_text, score_pos)

    def song_pic_set():
        if song == 'slit':
            song_pic = pygame.image.load('image\\slit.jpg').convert()
        elif song == 'perse':
            pass
        else:
            pass
        game_bg.blit(song_pic, (23, 23))

    def text_set():
        song_font = pygame.font.Font('font\\Bradley-Hand-ITC.ttf', 48)
        score_text_font = pygame.font.Font('font\\Bradley-Hand-ITC.ttf', 32)
        song_text = song_font.render(song, True, (255, 255, 255))
        score_text = score_text_font.render('score', True, (255, 255, 255))
        game_bg.blit(song_text, (33, 115.5))
        game_bg.blit(score_text, (35, 215))

    pygame.mixer.music.load('song\\slit.mp3')
    pygame.mixer.music.play(1)

    game_state = True

    while game_state:
        game_bg.blit(game_bg_c, bg_pos)

        # timer in beats of song
        if timing != bpm_timer(song):
            timer += 1
            timing = bpm_timer(song)

        # process due notes into firing
        if not note_process:
            if chart:
                for i in chart[0]:
                    note_process.append(int(i))
                chart.pop(0)
        else:
            if timer == note_process[0]+1:
                if note_process[1] == 1:
                    current_notes.append([D_NOTE_POS + 5, 0])
                if note_process[2] == 1:
                    current_notes.append([F_NOTE_POS + 5, 0])
                if note_process[3] == 1:
                    current_notes.append([J_NOTE_POS + 5, 0])
                if note_process[4] == 1:
                    current_notes.append([K_NOTE_POS + 5, 0])
                note_process = []

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_d:
                    note_press('d')
                if event.key == pygame.K_f:
                    note_press('f')
                if event.key == pygame.K_j:
                    note_press('j')
                if event.key == pygame.K_k:
                    note_press('k')
                if event.key == pygame.K_t:
                    game_state = False
                    pygame.mixer.music.stop()
                    player_score = playerMaxScore
                    game_score(song, difficulty)

        if not chart and not current_notes:
            stop_timer += (timer/timer)
            if stop_timer > 300:
                game_score(song, difficulty)
                game_state = False

        # screen update
        notes_move()
        pressed_light()
        text_set()
        judge_font_set()
        song_pic_set()
        score_print()
        screen.blit(game_bg, bg_pos)
        pygame.display.update()


def game_score(song, difficulty):
    global highScore, player_score

    background = pygame.image.load('image\\slit_sel.jpg').convert()

    highScore_place = 0
    highScore_counter = False

    if song == 'perse':
        if difficulty == 'easy':
            highScore_place = 1
        else:
            highScore_place = 2
    elif song == 'slit':
        if difficulty == 'easy':
            highScore_place = 4
        else:
            highScore_place = 5
    else:
        if difficulty == 'easy':
            highScore_place = 7
        else:
            highScore_place = 8

    if int(player_score) > int(highScore[highScore_place]):
        highScore[highScore_place] = round(player_score)
        highScore_counter = True

    if highScore_counter:
        score_txt = open('score\\score.txt', 'w')
        score_txt.write('perse ' + str(highScore[1]) + ' ' + str(highScore[2]) + '\n')
        score_txt.write('slit ' + str(highScore[4]) + ' ' + str(highScore[5]) + '\n')
        score_txt.write('un ' + str(highScore[7]) + ' ' + str(highScore[8]) + '\n')
        score_txt.close()

    if highScore_place == 1:
        pass
    elif highScore_place == 2:
        pass
    elif highScore_place == 4:
        game_continue = pygame.image.load("image\\SlitEasyScore_Con.jpg").convert()
        game_quit = pygame.image.load("image\\SlitEasyScore_Quit.jpg").convert()
    elif highScore_place == 5:
        game_continue = pygame.image.load("image\\SlitHardScore_Con.jpg").convert()
        game_quit = pygame.image.load("image\\SlitHardScore_Quit.jpg").convert()
    elif highScore_place == 7:
        pass
    else: pass

    def score_set():
        score_font = pygame.font.Font('font\\Bradley-Hand-ITC.ttf', 100)
        score_text = score_font.render(str(round(player_score)), True, (245, 159, 203))
        background.blit(score_text, (198, 392))

    def high_score_set():
        high_score_font = pygame.font.Font('font\\Bradley-Hand-ITC.ttf', 40)
        high_score_text = high_score_font.render(str(round(int(highScore[highScore_place]))), True, (104, 144, 220))
        background.blit(high_score_text, (379, 504))

    continue_state = 0
    score_state = True

    while score_state:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if continue_state == 0:
                        high_score_read()
                        game_intro()
                    else:
                        quit()
                if event.key == pygame.K_LEFT:
                    if continue_state == 1:
                        continue_state = 0
                if event.key == pygame.K_RIGHT:
                    if continue_state == 0:
                        continue_state = 1

        if continue_state == 0:
            background.blit(game_continue, bg_pos)
        else:
            background.blit(game_quit, bg_pos)

        high_score_set()
        score_set()
        screen.blit(background, bg_pos)
        pygame.display.update()


if __name__ == '__main__':
    pygame.mouse.set_visible(False)
    high_score_read()
    game_intro()

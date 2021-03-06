#!/usr/bin/env python3
import pygame
from game import *
from player import Player
from direction import Direction
from key import Key


pygame.init()
pygame.font.init()

game = Game()

game_display = pygame.display.set_mode(
    (game.get_width(),game.get_height()), pygame.FULLSCREEN)
pygame.display.set_caption('Tank Battalion')
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
show_coordinats = False

player_up_image = pygame.image.load('sprites/PlayerUp.png')
player_right_image = pygame.image.load('sprites/PlayerRight.png')
player_down_image = pygame.image.load('sprites/PlayerDown.png')
player_left_image = pygame.image.load('sprites/PlayerLeft.png')
shell_image = pygame.image.load('sprites/Shell.png')

myfont = pygame.font.SysFont('Comic Sans MS', 16)

def get_player_image(direction):
    if direction == Direction.UP:
        return player_up_image
    elif direction == Direction.RIGHT:
        return player_right_image
    elif direction == Direction.DOWN:
        return player_down_image
    else:
        return player_left_image

background_image = pygame.image.load('sprites/Background.png')

while not game.get_quit():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.set_quit(True)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game.set_quit(True)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                game.set_quit(True)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.add_key(Key.UP)
            elif event.key == pygame.K_RIGHT:
                game.add_key(Key.RIGHT)
            elif event.key == pygame.K_DOWN:
                game.add_key(Key.DOWN)
            elif event.key == pygame.K_LEFT:
                game.add_key(Key.LEFT)
            elif event.key == pygame.K_SPACE:
                game.add_key(Key.SHOOT)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                game.remove_key(Key.UP)
            elif event.key == pygame.K_RIGHT:
                game.remove_key(Key.RIGHT)
            elif event.key == pygame.K_DOWN:
                game.remove_key(Key.DOWN)
            elif event.key == pygame.K_LEFT:
                game.remove_key(Key.LEFT)

    game.tick()
    game_display.blit(background_image, (0,0))
    game_display.blit(
        get_player_image(game.get_player().get_direction()), 
        (game.get_player().get_x(),game.get_player().get_y()))

    if game.get_player().is_shooting():
        game_display.blit(
            shell_image, 
            (game.get_player().get_shell().get_x(),game.get_player().get_shell().get_y()))


    if show_coordinats:
        text_x = myfont.render(str(game.get_player().get_x()), False, (255, 255, 255))
        text_y = myfont.render(str(game.get_player().get_y()), False, (255, 255, 255))
        game_display.blit(text_x, (0,  0))
        game_display.blit(text_y, (0, 20))

    pygame.display.update()
    clock.tick(60)
    

pygame.quit()
quit()

# coding=utf-8
import pygame


class Field:
    '''
    Klasa przechowująca dane pola
    '''
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.rect = pygame.Rect(position[0], position[1], 50, 50)
        self.cords = (position[0] / 60, position[1] / 60)

# coding=utf-8
import pygame


class Player(object):
    '''
    Klasa przechowująca dane gracza
    '''
    def __init__(self, number, color):
        self.number = number
        self.color = color
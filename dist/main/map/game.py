import pyglet
import random, math
import pickle

from map.map import Map
from map.gamewindow import GameWindow



"""
The Game class controls the UI, and acts as a controller
for the game map and window.
"""
class Game():
        
    def __init__(self, map):
        map = map
        
        """
        try:
            map_file = open("save.map", "rb")
            map = pickle.load(map_file)
        except FileNotFoundError:
            map = Map()
        """
            
        window = GameWindow(map)

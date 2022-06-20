import constants
from execution import Executes
from game.shared.point import Point


class Direction(Executes):
   

    def __init__(self, keyboard_service):
        
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self._direction2 = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)

        # left 
        if self._keyboard_service.is_key_down('i'):
            self._direction2 = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('j'):
            self._direction2 = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('k'):
            self._direction2 = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('l'):
            self._direction2 = Point(0, constants.CELL_SIZE)
        
        player1 = cast.get_first_actor("player1")
        player2 = cast.get_first_actor("player2")
        player1.turn_head(self._direction)
        player2.turn_head(self._direction)
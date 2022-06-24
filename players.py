
from tkinter import constants
from constants import GREEN, RED, WHITE, MAX_X, MAX_Y
from point import Point
from scores import Scores
from snake import Snake

class Players:
    score = Scores()
    snake = None
    def __init__(self, initial_segment_list):
        '''makes up the workings of the green and red 
        snakes upon the screen that the video_service 
        displays:'''
        self._up = None
        self._down = None
        self._left = None
        self._right = None
        self.snake = Snake(initial_segment_list)

    def set_movement_keys(self, up, down, left, right):
        self._up = up
        self._down = down
        self._right = right
        self._left = left

    def get_movement_keys(self):
        return self._up, self._down, self._left, self._right

    def get_color(self):
        """Gets the actor's color as a tuple of three ints (r, g, b).
        
        Returns:
            Color: The actor's text color.
        """
        return self._color

    def get_players_position(self):
        #Class contestants they have a move or execution, 
        # and then they will add this location to the players
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
        
    def get_text(self):
        """Gets the actor's textual representation.
        
        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity

    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        # Move all your snake segments
        # x = (self..get_x() + self._velocity.get_x()) % constants.MAX_X
        # y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_Y
        # self._position = Point(x, y)

    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._color = color

    def set_position(self,position):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position

    def set_text(self,text):
        """Updates the text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self,velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity

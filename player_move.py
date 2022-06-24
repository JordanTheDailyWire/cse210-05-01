from direction import Direction
from point import Point
class player_move(Direction):
    """
    An update action that moves all the actors.
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """
    def __init__(self):
        """Constructs a new Actor."""
        self._text = ""
        self._font_size = 15
        self._color = (255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
    def execute(self, cast, script):
        """Executes the player's move
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()
    def set_position(self, position):
        """Updates the position to the given one.
        Args:
            position (Point): The given position.
        """
        self._position = position

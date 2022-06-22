import constants
from scores import Scores
from snake import Snake
from collision import Collision
from collision_detecotr import Collision_Detection
from draw_players_action import DrawPlayersAction
from director import Director
from direction import Direction
from keyboard_service import KeyboardService
from move_actors_action import MoveActorsAction
from video_service import VideoService
from execution import Execution
from contestants import Contestants
from players import Players
from colors import Colors
from point import Point


def main():
    # create the cast
    cast = Cast()
    cast.add_actor("snakes", Snake())
    cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", Direction(keyboard_service))
    script.add_action("update",MoveActorsAction())
    script.add_action("update", Collision_Detection())
    script.add_action("output", DrawPlayersAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()

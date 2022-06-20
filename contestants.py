from point import Point
#from direction import Direction
#from execution import Execution
#from keyboard_service import KeyboardService

class contestants('''Execution, KeyboardService'''):
    def __init__(self):
        super().__init__()
        #Begins the instance of two players
        '''Attributes:'''
        ks=self.Keyboard_service
        direct=self.direction
        self.a = (-1,0)
        self.s = (0,-1)
        self.d = (+1,0)
        self.w = (0,+1)
        self.j = (-1,0)
        self.k = (0,-1)
        self.l = (+1,0)
        self.i = (0,+1)
        self.x = Point.get_x()
        self.y = Point.get_y()
        

    def execute(self,point):
        if self.direct == self.a: 
            self.execute == (-1,0) + point(self.x,self.y) 
            return sum()

        elif self.direct == self.s:
            self.execute == (0,-1) + point(self.x,self.y)
            return sum()

        elif self.direct == self.d:
            self.execute == (+1,0) + point(self.x,self.y)
            return sum()

        elif self.direct == self.w:
            self.execute == (0,+1) + point(self.x,self.y)
            return sum()

        elif self.direct == self.k:
            self.execute == (0,-1) + point(self.x,self.y)
            return sum()

        elif self.direct == self.l:
            self.execute == (+1,0) + point(self.x,self.y)
            return sum()

        elif self.direct == self.i:
            self.execute == (0,+1) + point(self.x,self.y)
            return sum()

        elif self.direct == self.j:
            self.execute == (-1,0) + point(self.x,self.y)
            return sum()  

from tkinter import *
from snake import *
import random

class Interface(object):

    """Docstring for Interface. """

    def __init__(self):
        """Initialise interface"""

        self.root = Tk()
        self.root.title("snake")

        self.canvas = Canvas(self.root, width=600, height=600, bg='grey')
        self.canvas.grid(row=0, column=0)

        self.direction = None

        self.game_is_start = False

        self.size = 15
        
        self.snake = Snake(20, 20)
        self.snake.plot(self.canvas, self.size, first=True)
        self.case_occupe = [[20, 20]]

        self.id_apple = None
        self.pos_apple = self.create_apple()

        self.game_over = False
        
        self.root.bind('<d>', self.right)
        self.root.bind('<q>', self.left)
        self.root.bind('<z>', self.up)
        self.root.bind('<s>', self.down)
        self.root.bind('<g>', self.get_info)

        self.root.bind('<Down>', self.down)
        self.root.bind('<Up>', self.up)
        self.root.bind('<Left>', self.left)
        self.root.bind('<Right>', self.right)

        self.root.mainloop()

    def actualise(self):
        if self.game_over:
            pass
        elif self.direction == 'R':
            self.check_game_over(self.snake.x+1, self.snake.y)
            self.snake.actualise(self.snake.x+1, self.snake.y)
            self.snake.move(self.canvas, self.size)
            del self.case_occupe[-1]
            self.case_occupe.insert(0, (self.snake.x, self.snake.y))
            self.get_apple()
        elif self.direction == 'L':
            self.check_game_over(self.snake.x-1, self.snake.y)
            self.snake.actualise(self.snake.x-1, self.snake.y)
            self.snake.move(self.canvas, self.size)
            del self.case_occupe[-1]
            self.case_occupe.insert(0, (self.snake.x, self.snake.y))
            self.get_apple()
        elif self.direction == 'U':
            self.check_game_over(self.snake.x, self.snake.y-1)
            self.snake.actualise(self.snake.x, self.snake.y-1)
            self.snake.move(self.canvas, self.size)
            del self.case_occupe[-1]
            self.case_occupe.insert(0, (self.snake.x, self.snake.y))
            self.get_apple()
        elif self.direction == 'D':
            self.check_game_over(self.snake.x, self.snake.y+1)
            self.snake.actualise(self.snake.x, self.snake.y+1)
            self.snake.move(self.canvas, self.size)
            del self.case_occupe[-1]
            self.case_occupe.insert(0, (self.snake.x, self.snake.y))
            self.get_apple()

        self.canvas.after(150, self.actualise)


    def right(self, r):
        if self.game_is_start:
            self.direction = 'R'
        else:
            self.game_is_start = True
            self.direction = 'R'
            self.actualise()

    def left(self, l):
        if self.game_is_start:
            self.direction = 'L'
        else:
            self.game_is_start = True
            self.direction = 'L'
            self.actualise()
    
    def up(self, u):
        if self.game_is_start:
            self.direction = 'U'
        else:
            self.game_is_start = True
            self.direction = 'U'
            self.actualise()


    def down(self, d):
        if self.game_is_start:
            self.direction = 'D'
        else:
            self.game_is_start = True
            self.direction = 'D'
            self.actualise()
            

    def create_apple(self):
        continuer = True
        while continuer:
            pos_x, pos_y = self.size*random.randint(1, 39), self.size*random.randint(1, 39)
            if (pos_x, pos_y) not in self.case_occupe:
                continuer = False
        x, y = pos_x+self.size/2, pos_y+self.size/2
        r = self.size/2
        self.id_apple = self.canvas.create_oval(x+r, y+r, x-r, y-r, fill='red')
        return pos_x, pos_y

    def get_apple(self):
        if self.size*self.snake.x == self.pos_apple[0] and self.size*self.snake.y == self.pos_apple[1]:
            self.snake.add_element(self.canvas, self.size)
            self.canvas.delete(self.id_apple)
            self.case_occupe = []
            self.snake.act_case_occupe(self.case_occupe)
            self.pos_apple = self.create_apple()

    

    def check_game_over(self, x, y):
        if (x, y) in self.case_occupe:
            self.game_over = True
        if (0 > x) or (x > 39) or (0 > y) or (y > 39):
            self.game_over = True

        if self.game_over:
            self.canvas.create_text(300, 300, text="Game Over", font=("Arial", 50), fill='red')

    def get_info(self, g):
        self.canvas.delete(2)


if __name__ == "__main__":
    interface = Interface()



    
        

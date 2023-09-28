

class Snake:

    def __init__(self, x, y, next=None):
        self.x = x 
        self.y = y
        self.previous = None #tail is the first previous
        self.next = next #head is the first next 
        self.previous_x = None #the previous position and the position of the previous
        self.previous_y = None

        self.id_element = None

    def add_element(self, canvas, size):
        if self.previous == None:
            self.previous = Snake(self.previous_x, self.previous_y, next=self)
            self.previous.plot(canvas, size)

        else:
            self.previous.add_element(canvas, size)


    def actualise(self, new_x, new_y):
        if self.previous == None:
            self.previous_x, self.previous_y = self.x, self.y
            self.x, self.y = new_x, new_y

        else :
            self.previous_x, self.previous_y = self.x, self.y
            self.x, self.y = new_x, new_y
            self.previous.actualise(self.previous_x, self.previous_y)

    def plot(self, canvas, size, first = False):
        if first:
            self.id_element = canvas.create_rectangle(size*self.x, size*self.y, size*self.x+size, size*self.y+size, fill='#006600')
        else :
            self.id_element = canvas.create_rectangle(size*self.x, size*self.y, size*self.x+size, size*self.y+size, fill='#009900')
            #self.next.plot(canvas, size)


    def move(self, canvas, size):
        if self.next == None and self.previous == None:
            canvas.delete(self.id_element)
            self.id_element = canvas.create_rectangle(size*self.x, size*self.y, size*self.x+size, size*self.y+size, fill='#006600')

        elif self.next == None:
            canvas.delete(self.id_element)
            self.id_element = canvas.create_rectangle(size*self.x, size*self.y, size*self.x+size, size*self.y+size, fill='#006600')
            self.previous.move(canvas, size) 

        elif self.previous == None:
            canvas.delete(self.id_element)
            self.id_element = canvas.create_rectangle(size*self.x, size*self.y, size*self.x+size, size*self.y+size, fill='#009900')
        else :
            canvas.delete(self.id_element)
            self.id_element = canvas.create_rectangle(size*self.x, size*self.y, size*self.x+size, size*self.y+size, fill='#009900')
            self.previous.move(canvas, size) 

    
    def act_case_occupe(self, case_occupe):
        if self.previous == None:
            case_occupe.append((self.x, self.y))
        else :
            case_occupe.append((self.x, self.y))
            self.previous.act_case_occupe(case_occupe)
        

    def get_info(self):
        if self.previous == None:
            print(self.x, self.y, "previous", self.previous_x, self.previous_y)
        else:
            print(self.x, self.y, "previous", self.previous_x, self.previous_y)
            self.previous.get_info()

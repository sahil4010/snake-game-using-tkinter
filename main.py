#  Snake game with Python Tkinter

from tkinter import *
from random import randint

tiles = 20
lb_config = {'font': 'joystix\ Monospace 10', 'bg':'#253434', 'fg': 'white'}
 
class App():
    def __init__(self, master): 

          

        self.master = master
        self.master.state('zoomed')  
        self.master.resizable(0, 0)
        self.master.title('Snake Game')
        self.master['bg'] = '#253434'

        #  Frames

        self.gameFrame = Frame(self.master, width=600, height=600, highlightbackground='white', highlightthickness=1)
        self.labelFrame = Frame(self.master, bg='#253434')

        self.labelFrame.place(x=0, y=0)
        self.gameFrame.place(anchor="c", relx=.5, rely=.5)

        #  Labels
        self.points = IntVar()
        self.points.set(0)
        
        self.lb_points = Label(self.labelFrame, lb_config, text=f'Points:')
        self.lb_npoints = Label(self.labelFrame, lb_config, textvariable=self.points)

        self.lb_points.grid(row=1, column=0,padx=5, pady=20)
        self.lb_npoints.grid(row=1, column=1)


        #  Canvas

        self.canvas = Canvas(self.gameFrame, width=600, height=600, bg='#264D4D')
        self.text = self.draw_text(300, 300, 'space to start')
        self.canvas.pack()

        #  Cobra

        self.snakeX = [20, 20, 20]  
        self.snakeY = [20, 21, 22]  
        self.snakeLength = 3  
        self.key = 'Up'

        
        self.appleX = randint(1, 28)
        self.appleY = randint(1, 28)

       
        self.master.bind('<space>', lambda _: self.startGame())
        self.master.bind('<KeyPress>', self.getKey)
 

    
    def startGame(self): 
        self.master.unbind('<space>')  
        self.canvas.delete(self.text)
        self.gameLoop()
   

    
    def getKey(self, event):
        keys = ['Up', 'Down', 'Left', 'Right', ' ']
        for v in keys: 
            if event.keysym == v: self.key = event.keysym


    
    def snakeMove(self):
        for i in range(self.snakeLength-1, 0, -1):
            self.snakeX[i] = self.snakeX[i-1]
            self.snakeY[i] = self.snakeY[i-1]
        
        
        if self.key == 'Up': self.snakeY[0] -= 1  
        elif self.key == 'Down': self.snakeY[0] += 1  
        elif self.key == 'Left': self.snakeX[0] -= 1  
        elif self.key == 'Right': self.snakeX[0] += 1  

        self.eatApple()


                      
    def eatApple(self):
        if self.snakeX[0] == self.appleX and self.snakeY[0] == self.appleY:
            self.snakeLength += 1

            x = self.snakeX[len(self.snakeX)-1] 
            y = self.snakeY[len(self.snakeY) - 1]
            self.snakeX.append(x+1)  
            self.snakeY.append(y)
            self.createNewApple()
            self.points.set(self.points.get() + 1)


    
    def createNewApple(self):
        self.appleX = randint(1, 28)
        self.appleY = randint(1, 28)


    
    def draw_text(self, x, y, text, size=25, fg='white'):
        font = (f'joystix\ Monospace {size}')
        return self.canvas.create_text(x, y, text=text, font=font, fill=fg)
   
  
    
    def gameOver(self):
       
        if self.snakeX[0] < 0 or self.snakeX[0] > 29 or self.snakeY[0] < 0 or self.snakeY[0] > 29:
            return True

        
        for i in range(1, self.snakeLength):
            if self.snakeX[0] == self.snakeX[i] and self.snakeY[0] == self.snakeY[i]:
                return True

        return False  
   

    
    def gameLoop(self):
        self.canvas.after(100, self.gameLoop)  
        self.canvas.delete('all')  

        if self.gameOver() == False:
            self.snakeMove()

            
            self.canvas.create_rectangle(self.snakeX[0]*tiles, self.snakeY[0]*tiles, self.snakeX[0]*tiles+tiles, self.snakeY[0]*tiles+tiles, fill='white')

        
            for i in range(1, self.snakeLength):
                self.canvas.create_rectangle(self.snakeX[i]*tiles, self.snakeY[i]*tiles, self.snakeX[i]*tiles+tiles, self.snakeY[i]*tiles+tiles, fill='white')
        
            
            self.canvas.create_rectangle(self.appleX*tiles, self.appleY*tiles, self.appleX*tiles+tiles, self.appleY*tiles+tiles, fill='red')


        else: 
            self.draw_text(300, 300, 'GameOver!', 40)
            self.draw_text(300, 340,  f'Your Points:{self.points.get()}', 10)
            self.draw_text(300, 380,  f'Press r to restart', 10)
            self.master.bind('<r>', lambda _: self.replayGame())


    def replayGame(self):
        self.__init__(self.master)


if __name__ == "__main__":
    root = Tk()
    App(root)
    root.mainloop()
    
class Ball:
    def __init__(self,r,start,color,speed):
        self.r = r
        self.start = start
        self.color = color
        self.speed = speed
        self.direction = [-speed[0],-speed[1]]

    def move(self):
        self.start[0] += self.direction[0]
        self.start[1] += self.direction[1]


class Rect:
    def __init__(self,len,start,color,speed,direction):
        self.len = [len,len]
        self.start = start
        self.color = color
        self.speed = speed
        self.direction = direction


    def move(self):
        if self.direction == 'r':
            self.start[0] += self.speed 
        elif self.direction == 'l':
            self.start[0] -= self.speed 
        elif self.direction == 'u':
            self.start[1] -= self.speed 
        elif self.direction == 'd':
            self.start[1] += self.speed
    


import random


class Racers:

    def __init__(self, color, position, shape, name):
        self.color = color
        self.shape = shape
        self.name = name
        self.position = position
        """this function places the racers at their finish line and gives them their color shape and
        position and start races """
        from turtle import Turtle
        self.name = Turtle()
        self.name.shape(self.shape)
        self.name.goto(self.position)
        self.name.color(self.color)
        self.name.forward(random.randint(1, 10))


turtle_1 = Racers(color='green', position=23, shape='turtle', name='frank')
turtle_1.set_state()
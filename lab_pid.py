import matplotlib.pyplot as plt
import math

dt = 0.01

def norm2(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def draw(robot):
    pass        

class Robot:
    v = 0
    w = 0
    vel_left = 0
    vel_right = 0
    wheel_radius = 0
    body_radius = 0
    pos = [0.0,0.0]
    angle = 0.0
    goal = [0.0,0.0]

    def __init__(self, wheel_radius, body_radius):
        self.wheel_radius = wheel_radius
        self.body_radius = body_radius

    def step(self):
        pass

    def control(self):
        pass


myRobot = Robot(0.04, 0.12)

myRobot.pos = [3.0,7.0]
myRobot.angle = math.pi / 6
myRobot.goal = [10,2]

while norm2(myRobot.pos, myRobot.goal) > 0.06:
    myRobot.control()
    myRobot.step()
    draw(myRobot)

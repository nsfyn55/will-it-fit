import pygame
from math import sin,sqrt,atan

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
#TODO
# -Take a single point and calculate a rotated pair
# -Take list of points and return rotated list
# -cacluate current angle and find new point
#  as a function of current angle + desired rotation

def rotate_a_point(point, rotation, pivot):
    #calculate new y from angle and old
    total_rotation = current_angle_in_rad(point,pivot) + rotation
    radius = calculate_radius_from_center(point,pivot)

    new_y = calc_y_component_from_angle_and_radius(radius,total_rotation)  
    new_x = x_component_from_y(pivot,new_y,radius)
    
    return Point(new_x,new_y)
        
def current_angle_in_rad(p,c):
    adj = p.x -c.x
    opp = p.y -c.y
    
    if(opp == 0 and adj ==0):
        return atan(0)
    return atan(opp/adj)    

def calculate_radius_from_center(p,c):
    return sqrt(pow(c.x + p.x,2) + pow(c.y+p.y,2))

def x_component_from_y(center_point, y, radius):
    return sqrt(pow(radius,2) - pow((y-center_point.y),2)) + center_point.x

def calc_y_component_from_angle_and_radius(radius, angle):
    return sin(angle) * radius

def get_center_of_canvas(x,y):
    x = x/2
    y = y/2
    return Point(x,y)

#screen = pygame.display.set_mode((640, 480))
#running = 1 
#while running:
#    event = pygame.event.poll()
#    if event.type == pygame.QUIT:
#        running = 0
#    screen.fill((0, 0, 0))
#        
#    p1 = Point(600,240)
#    p2 = Point(40,240)
#    
#    
#    #Draw a horizontal line
#    pygame.draw.line(screen, (0, 0, 255), (p1.x, p1.y), (p2.x, p2.y))
#    
#    #draw to screen
#    pygame.display.flip()

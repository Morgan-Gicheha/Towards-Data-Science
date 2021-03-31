from random import choice

class Random_walk():
    """ This clas generates rndon x and y coordinates"""
    def __init__(self,number_of_points = 5000):
        self.number_of_points = number_of_points

        # initalize x and y values
        self.x_values = [0]
        self.y_values = [0]

    def point_filler(self):
        """generation the random points"""
        while len(self.x_values) < self.number_of_points:
        # decide which direction to go and by how far
        # for this we will need the direction and distance

        # generating a single x-coordinate
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            
        # generating a single y-coordinate
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
             
            #  rejecting moves that go nowhere.. that is (0,0)
            if x_step == 0 and y_step == 0:
                continue
            # calculatin the next move
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # appending
            self.x_values.append(next_x)
            self.y_values.append(next_y)

            

x = Random_walk()
x.point_filler()
print(len(x.x_values + x.y_values))
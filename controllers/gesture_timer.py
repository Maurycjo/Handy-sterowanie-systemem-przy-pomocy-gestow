
class GestureTimer():
    def __init__(self):
        self.times = [3.76 , 3.39 , 3.87, 4.02, 3.62, 4.06, 4.06, 3.63, 2.90, 3.24, 3.67, 3.90, 3.65, 3.74, 3.20, 3.27, 4.10, 3.72, 3.39, 3.17
                      , 3.57, 3.96, 3.38, 3.69, 3.72] #not less than 2.0

    def get_time(self,number:int):
        return self.times[number-1]


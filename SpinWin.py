from random import *
class SpinWin:
    #Empty constructor method
    def __init__(self):
        pass
    #Determine the prize number. As there are 8 elements on the Spin Wheel, 
    #we can randomly choose a value between 0 & 7.
    def GetPrizeNumber(self):
        self.prizeNumber = randint(0,7)
        return self.prizeNumber
    #Determine the number of rotations for the wheel should spin for. 10 rotations is the maximum number of times a wheel should spin.  
    def GetWheelRotation(self):
        numberOfElementsInWheel = 8
        #Number of degrees between the centre of one segment, and the centre of the next element. 
        degreeDifferenceBetweenEachSegment = 45
        maxNumberOfRotations = 10
        currentElement = self.prizeNumber
        totalRotation = ((numberOfElementsInWheel - currentElement) * degreeDifferenceBetweenEachSegment) + (maxNumberOfRotations * 360)
        return totalRotation
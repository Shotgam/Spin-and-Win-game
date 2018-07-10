class Spin&Win:
    numberOfElementsInWheel = 8
    degreeDifferenceBetweenEachSegment = 45
    maxNumberOfRotations = 10

    def __init__(self):
        self.prizeNumber
    
    def GetPrizeNumber(self):
        self.prizeNumber = randint(0,7)
        return self.prizeNumber

    def GetWheelRotation(self):
        currentElement = self.prizeNumber
        totalRotation = ((numberOfElementsInWheel - currentElement) * degreeDifferenceOfOneSegment) + (numberOfRotations * 360)
        return totalRotation
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.lots = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.lots[carType] > 0:
            self.lots[carType] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **balls):
        print(balls)
        self.contents = []
        for type, times in balls.items():
            for i in range(times):
                self.contents.append(type)
        self.backUp = copy.copy(self.contents)

    def draw(self, amount):
        if amount >= len(self.contents):
            return self.contents
        drawnLst = []
        for i in range(amount):
            drawPos = random.randint(0, len(self.contents) - 1)
            drawnLst.append(self.contents.pop(drawPos))
        return drawnLst

    def reset(self):
        self.contents = copy.copy(self.backUp)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    countSuccess = 0

    for i in range(num_experiments):
        drawnBalls = hat.draw(num_balls_drawn)
        successFlag = True
        for type, times in expected_balls.items():

            if drawnBalls.count(type) < times:
                successFlag = False

        if successFlag == True:
            countSuccess += 1
        hat.reset()
    return countSuccess / num_experiments

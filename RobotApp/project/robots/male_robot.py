from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    INITIAL_WEIGHT = 9

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.INITIAL_WEIGHT)

    @property
    def weight_gain_after_eating(self):
        return 3


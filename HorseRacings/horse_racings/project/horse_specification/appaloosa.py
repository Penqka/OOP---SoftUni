from project.horse_specification.horse import Horse


class Appaloosa(Horse):

    @property
    def maximum_speed(self):
        return 120

    @property
    def speed_increase_in_training(self):
        return 2



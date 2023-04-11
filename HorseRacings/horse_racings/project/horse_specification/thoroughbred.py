from project.horse_specification.horse import Horse


class Thoroughbred(Horse):

    @property
    def maximum_speed(self):
        return 140

    @property
    def speed_increase_in_training(self):
        return 3


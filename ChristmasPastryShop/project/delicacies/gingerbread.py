from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    PORTION_SIZE = 200

    def __init__(self, name, price):
        super().__init__(name, self.PORTION_SIZE, price)

    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."



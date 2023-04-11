from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name):
        super().__init__(name, self.CAPACITY)

    def details(self):
        robots = ['none']

        if self.robots:
            robots = [r.name for r in self.robots]

        return f"{self.name} Main Service:\n" \
               f"Robots: {' '.join(robots)}"

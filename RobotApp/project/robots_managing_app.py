from typing import List

from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }

    VALID_ROBOTS = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }

    def __init__(self):
        self.robots: List[MaleRobot, FemaleRobot] = []
        self.services: List[MainService, SecondaryService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")

        service = self.VALID_SERVICES[service_type](name)
        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    @staticmethod
    def __get_robot_or_service(obj_name, iter_list):
        return [i for i in iter_list if i.name == obj_name][0]

    @staticmethod
    def __check_robot_compatibility(robot_type, service_type):
        if robot_type == "MaleRobot" and service_type == "MainService":
            return True

        if robot_type == "FemaleRobot" and service_type == "SecondaryService":
            return True

        return False

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.__get_robot_or_service(robot_name, self.robots)
        service = self.__get_robot_or_service(service_name, self.services)

        robot_type = robot.__class__.__name__
        service_type = service.__class__.__name__

        if not self.__check_robot_compatibility(robot_type, service_type):
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.__get_robot_or_service(service_name, self.services)

        try:
            robot = [r for r in service.robots if r.name == robot_name][0]
        except IndexError:
            raise Exception("No such robot in this service!")

        self.robots.append(robot)
        service.robots.remove(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.__get_robot_or_service(service_name, self.services)

        [r.eating() for r in service.robots]

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.__get_robot_or_service(service_name, self.services)
        total_price_of_robots = 0

        for r in service.robots:
            total_price_of_robots += r.price

        return f"The value of service {service_name} is {total_price_of_robots:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())

        return '\n'.join(result)







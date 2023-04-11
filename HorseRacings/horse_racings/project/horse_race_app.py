from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if [h for h in self.horses if h.name == horse_name]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_HORSES:
            horse = self.VALID_HORSES[horse_type](horse_name, horse_speed)
            self.horses.append(horse)

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if [j for j in self.jockeys if j.name == jockey_name]:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if [r for r in self.horse_races if r.race_type == race_type]:
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey = [j for j in self.jockeys if j.name == jockey_name][0]
        except IndexError:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        free_horse = None

        for horse in self.horses[::-1]:
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                free_horse = horse
                break

        if free_horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = free_horse
        free_horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {free_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        try:
            race = [r for r in self.horse_races if r.race_type == race_type][0]
        except IndexError:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = [j for j in self.jockeys if j.name == jockey_name][0]
        except IndexError:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        try:
            race = [r for r in self.horse_races if r.race_type == race_type][0]
        except IndexError:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = None
        max_speed = 0

        for jockey in race.jockeys:
            if jockey.horse.speed > max_speed:
                winner = jockey
                max_speed = jockey.horse.speed

        return f"The winner of the {race_type} race, with a speed of {max_speed}km/h is " \
               f"{winner.name}! Winner's horse: {winner.horse.name}."
























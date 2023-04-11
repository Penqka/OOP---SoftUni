from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    @property
    def is_band_valid_for_concert(self):
        return {
            'Rock': {
                'Drummer': ['play the drums with drumsticks'],
                'Singer': ['sing high pitch notes'],
                'Guitarist': ['play rock']
            },
            'Metal': {
                'Drummer': ['play the drums with drumsticks'],
                'Singer': ['sing low pitch notes'],
                'Guitarist': ['play metal']
            },
            'Jazz': {
                'Drummer': ['play the drums with drum brushes'],
                'Singer': ['sing high pitch notes', 'sing low pitch notes'],
                'Guitarist': ['play jazz']
            },
        }

    @property
    def valid_musicians(self):
        return {
            "Guitarist": Guitarist,
            "Drummer": Drummer,
            "Singer": Singer
        }

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.valid_musicians:
            raise ValueError("Invalid musician type!")

        if [m for m in self.musicians if m.name == name]:
            raise Exception(f"{name} is already a musician!")

        musician = self.valid_musicians[musician_type](name, age)
        self.musicians.append(musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if [b for b in self.bands if b.name == name]:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        found_concert = [c for c in self.concerts if c.place == place]
        if found_concert:
            raise Exception(f"{found_concert[0].place} is already registered for {found_concert[0].genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)

        return f"{concert.genre} concert in {concert.place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = [m for m in self.musicians if m.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = [m for m in band.members if m.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def validate_musicians(self, musicians, genre, musician_type, band_name):
        for musician in musicians:
            for skill in self.is_band_valid_for_concert[genre][musician_type]:
                if skill not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]

        required_members = {m.__class__.__name__ for m in band.members}
        if len(required_members) < 3:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        drummers = [m for m in band.members if m.__class__.__name__ == 'Drummer']
        singers = [m for m in band.members if m.__class__.__name__ == 'Singer']
        guitarists = [m for m in band.members if m.__class__.__name__ == 'Guitarist']

        concert = [c for c in self.concerts if c.place == concert_place][0]
        genre = concert.genre
        band_name = band.name

        self.validate_musicians(drummers, genre, 'Drummer', band_name)
        self.validate_musicians(singers, genre, 'Singer', band_name)
        self.validate_musicians(guitarists, genre, 'Guitarist', band_name)

        profit = concert.audience * concert.ticket_price - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."




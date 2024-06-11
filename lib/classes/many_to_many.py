class Band:
    all = []

    def __init__(self, name, hometown):
        self._name = name
        self._hometown = hometown
        self.name = name
        self.hometown = hometown
        Band.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if (
            isinstance(value, str)
            and len(value) > 0
            and not hasattr(self, "value")
        ):
            self._name = value
        else:
            return ValueError("Name must be a non-empty string")

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, hometown):
        if (
            isinstance(hometown, str)
            and len(hometown) > 0
            and not hasattr(self, "hometown")
        ):
            self._name = hometown
        else:
            return ValueError("Name must be a non-empty str")

    def concerts(self):
        concerts = [concert for concert in Concert.all if concert.band == self]
        return concerts if concerts else None

    def venues(self):
        venues = list(set(concert.venue for concert in self.concerts()))
        return venues if venues else None

    def play_in_venue(self, venue, date):
        concert = Concert(date, self, venue)
        self._concerts.append(concert)
        return concert

    def all_introductions(self):
        return [
            f"Hello {concert.venue.city}!!!!! We are {self._name} and we're from {self._hometown}"
            for concert in self._concerts
        ]


class Concert:
    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if (
            isinstance(date, str)
            and len(date) > 0
            and not hasattr(self, "date")
        ):
            self._date = date
        else:
            return ValueError("Date must be a non-empty str")

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, band):
        if isinstance(band, Band):
            self._band = band
        else:
            return ValueError("Band must be a Band instance")

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, venue):
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be of type Venue")
        self._venue = venue

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    all = []

    def __init__(self, name, city):
        self.name = name
        self.city = city
        Venue.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (
            isinstance(name, str)
            and len(name) > 0
            and not hasattr(self, "name")
        ):
            self._name = name
        else:
            return ValueError("Name must be a non-empty str")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if (
            isinstance(city, str)
            and len(city) > 0
            and not hasattr(self, "city")
        ):
            self._city = city
        else:
            return ValueError("City must be a non-empty str")

    def concerts(self):
        result = [concert for concert in Concert.all if concert.venue == self]
        return result if result else None

    def bands(self):
        result = list(set(concert.band for concert in self.concerts()))
        return result if result else None

    def concert_on(self, date):
        for concert in self.concerts():
            if concert.date == date:
                return concert
        return None


# Example usage:

# Create instances of Band
metallica = Band("Metallica", "Los Angeles")
linkin_park = Band("Linkin Park", "Los Angeles")

# Create instances of Venue
stadium_a = Venue("Stadium A", "Los Angeles")
stadium_b = Venue("Stadium B", "San Francisco")

# Create instances of Concert
concert1 = Concert("2024-07-15", metallica, stadium_a)
concert2 = Concert("2024-08-20", linkin_park, stadium_b)

# Accessing properties and methods
print(metallica.name)  
print(linkin_park.name)
print(concert1.band)  
print(stadium_a.city)
print(stadium_b.city)  
print(stadium_a.concerts())  
print(concert1.introduction())  



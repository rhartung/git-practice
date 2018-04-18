"""Gonna put a whole lot of code in here - develop on a-remote-branch."""


class Doggo(object):
    """A friendly, happy doggo."""

    def __init__(self, breed, color, goodness_rating):
        """Params: breed, and color are strings, goodness_rating is int from 1-10.
        """
        
        self.breed = breed
        self.color = color
        self.goodness_rating = goodness_rating

    def do_good(self):
        """Add +1 to goodness_rating for good doggo deeds."""

        self.goodness_rating += 1

    def do_bad(self):
        """Subtract 1 from goodness_rating for bad doggo deeds."""

        self.goodness_rating -= 1

    def dye_hair(self, color):
        """Change doggo color."""

        self.color = color

"""Gonna put a whole lot of code in here - develop on a-remote-branch."""


GOOD_DOGGO_DEEDS = {"wag tail", "sit", "stay", "lie down", "roll over", "shake",
                    "save Timmy from well"}

BAD_DOGGO_DEEDS = {"poop on carpet", "bark", "bite", "eat garbage", "attack mailman",
                   "chew couch"}

class Doggo(object):
    """A friendly, happy doggo."""

    def __init__(self, name, breed, color, goodness_rating):
        """Params: name, breed, and color are strings, goodness_rating starts as int from 1-10.
        """
        
        self.name = name
        self.breed = breed
        self.color = color
        self.goodness_rating = goodness_rating
        self.friends = set()

    def do_good(self):
        """Add +1 to goodness_rating for good doggo deeds."""

        self.goodness_rating += 1

    def do_bad(self):
        """Subtract 1 from goodness_rating for bad doggo deeds."""

        self.goodness_rating -= 1

    def dye_hair(self, color):
        """Change doggo color."""

        self.color = color

    def add_friends(self, dog_friends):
        """Add list of friends to Doggo's set of friends."""

        if type(dog_friends) != list:
            return "dog_friends parameter must be in list format."

        for friend in dog_friends:
            if friend not in self.friends:
                self.friends.add(friend)

            else:
                return "{} is already friends with {}!".format(self.name, friend.name)

        return "{} has new friends!".format(self.name)


import random
import datetime
import logging
from mmgen.data import names
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Person:
    """
    Represents an individual and their visible and hidden traits
    """
    first_name = None
    last_name = None
    gender = None
    birth_date = None

    # Personal attributes
    # Each attribute uses 0.0 as an average
    attributes = {
        # High number represents a physically stronger character
        "strength": 0.0,

        # A high number means the person is nimble and agile, a lower number represents a clumsy character
        "dexterity": 0.0,

        # Higher numbers represents a higher level of raw intelligence (IQ)
        "intelligence": 0.0,

        # Higher number represents a stable person, lower number means the person is hotheaded
        "temper": 0.0,

        # Higher number means the person is highly committed to their own moral code. Lower number means the person is more pragmatic
        "idealism": 0.0,

        # Higher number means the person is more well educated
        "education": 0.0,
    }

    def __init__(self):
        self.gender = random.randint(0,1)

        # Random last name
        self.last_name = random.choice(names.LAST_NAME)

        # Random first name, based on gender
        if self.gender == 0:
            self.first_name = random.choice(names.FIRST_NAME_MALE)
        else:
            self.first_name = random.choice(names.FIRST_NAME_FEMALE)

    def encode(self):
        """
        Encodes the object as a pure datastructure
        Useful for writing output
        """
        out = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": datetime.datetime.fromtimestamp(self.birth_date).strftime("%Y-%m-%d"),
            "attributes": {}
        }
        for att in self.attributes.keys():
            out["attributes"][att] = self.attributes[att]
        return out

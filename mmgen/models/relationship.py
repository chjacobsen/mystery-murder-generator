import random
import logging
from mmgen.util.randomize import weighted_roll
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate (person_a, person_b):
    """
    Generates a relationship between two people
    """
    roll_table = {}
    for rel_type in RELATION_TYPES:
        relobj = rel_type(person_a, person_b)
        odds = int(round(relobj.base_odds * relobj.get_chance_modifier()))
        if odds > 0:
            roll_table[relobj] = odds
    logger.info("Relation roll table: " + str(roll_table))

    relobj = weighted_roll(roll_table)
    person_a.relations.append(relobj)
    person_b.relations.append(relobj)

class Relationship:

    base_odds = 100
    type_name = "RELATION"

    rel_subject = None
    rel_object = None

    def get_chance_modifier (self):
        """
        Returns a single float determining the relative probability of this relationship

        Returning 2.0 will mean there is a twice as high as normal chance for the relationship to exist

        Returning 1.0 will mean there is no change to the modifier

        Returning 0.0 will mean that there is no chance for the relationship to exist
        """
        return 1.0

    def pick_subject(self, person_a, person_b):
        """
        Some relationships, like friendships, don't care about subject and object, so it can be randomized.
        For others, like parent-child and boss-employee, it matters.
        """
        return random.choice([person_a, person_b])

    def __init__(self, person_a, person_b):
        self.rel_subject = self.pick_subject(person_a, person_b)
        if self.rel_subject is person_a:
            self.rel_object = person_b
        else:
            self.rel_object = person_a

    def encode(self):
        return [self.type_name, self.rel_subject.full_name(), self.rel_object.full_name()]

class Parent(Relationship):

    base_odds = 40
    type_name = "PARENT_CHILD"

    def get_chance_modifier(self):
        if self.rel_object.birth_date - self.rel_subject.birth_date < 3600 * 24 * 365 * 18:
            return 0.0
        return 1.0

    def pick_subject(self, person_a, person_b):
        if person_a.birth_date < person_b.birth_date:
            return person_a
        return person_b

class Friend(Relationship):
    base_odds = 100
    type_name = "FRIEND"



# Weighted list for rolling relationships
RELATION_TYPES = [
    Friend,
    Parent,
]

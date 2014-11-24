import random
import logging
from mmgen.util.randomize import weighted_roll
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_PROBABILITY = 100

def generate (person_a, person_b):
    """
    Generates a relationship between two people
    """
    roll_table = {}
    for rel_type in RELATION_TYPES:
        relobj = rel_type(person_a, person_b)
        odds = int(round(relobj.get_chance()))
        if odds > 0:
            roll_table[relobj] = odds
    logger.info("Relation roll table: " + str(roll_table))

    relobj = weighted_roll(roll_table)
    person_a.relations.append(relobj)
    person_b.relations.append(relobj)

class Relationship:

    type_name = "RELATION"

    rel_subject = None
    rel_object = None

    def get_chance (self):
        """
        Returns the odds of a particular relationship existing

        Higher numbers mean higher probability

        A probability of 0 means the relationship cannot exist under the given conditions
        """
        return BASE_PROBABILITY

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
    """
    The subject is the biological parent of the object
    """

    type_name = "PARENT_CHILD"

    def get_chance(self):
        # Check that there is a reasonable minimum age difference
        if self.rel_object.birth_date - self.rel_subject.birth_date < 3600 * 24 * 365 * 18:
            return 0.0

        # Since we're dealing with biological parents, ensure there's a maximum of one for each gender
        for rel in self.rel_object.relations:
            if rel.type_name == self.type_name and rel.rel_subject.gender == self.rel_subject.gender:
                return 0.0

        return BASE_PROBABILITY * 0.4

    def pick_subject(self, person_a, person_b):
        if person_a.birth_date < person_b.birth_date:
            return person_a
        return person_b

class Friend(Relationship):
    """
    A generic friendship, a relationship type without many prerequisites
    """

    type_name = "FRIEND"



# Weighted list for rolling relationships
RELATION_TYPES = [
    Friend,
    Parent,
]

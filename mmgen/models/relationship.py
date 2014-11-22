import random


def generate (person_a, person_b):
    """
    Generates a relationship between two people
    """

class Relationship:

    type_name = "RELATION"

    rel_subject = None
    rel_object = None

    def is_sane (self):
        """
        Determines whether the relationship, as currently set, makes sense
        """
        return True

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

    type_name = "PARENT_CHILD"

    def is_sane(self):
        if self.rel_object.birth_date - self.rel_subject.birth_date < 3600 * 24 * 365 * 18:
            return False
        return True

    def pick_subject(self, person_a, person_b):
        if person_a.birth_date < person_b.birth_date:
            return person_a
        return person_b

class Friend(Relationship):

    type_name = "FRIEND"

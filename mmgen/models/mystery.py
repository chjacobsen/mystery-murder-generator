from __future__ import absolute_import
import random
import datetime
import logging
from mmgen.data import murder
from mmgen.models import person
from mmgen.models import relationship
from mmgen.util.randomize import weighted_roll
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Mystery:
    """
    A full mystery
    """
    timeline = None
    people = []
    num_characters = 0
    start_date = None
    current_date = None

    def populate(self):
        logger.info("Generating {0} characters".format(self.num_characters))

        # Generate some basic information for each person
        for n in range(self.num_characters):
            pers = person.Person()
            logger.info("Created person: {0} {1}".format(pers.first_name, pers.last_name))

            # Generate a birth date. Each person has to be at least 18 years old
            pers.birth_date = random.randint(self.start_date, self.current_date - (3600 * 24 * 365 * 18))
            logger.info("Born: {0}".format(datetime.datetime.fromtimestamp(pers.birth_date).strftime("%Y-%m-%d")))
            self.people.append(pers)
        self.method = weighted_roll(murder.MURDER_METHOD)
        self.motive = weighted_roll(murder.MURDER_MOTIVE)
        self.people[0].is_victim = True
        self.people[1].is_murderer = True
        for pa in range(len(self.people)):
            pers_a = self.people[pa]
            for pb in range(pa + 1, len(self.people)):
                pers_b = self.people[pb]
                relationship.generate(pers_a, pers_b)


    def encode(self):
        """
        Encodes the object as a data structure
        Useful when writing output
        """
        out = {
            "mystery_name": "Notorious crime",
            "start_date": datetime.datetime.fromtimestamp(self.start_date).strftime("%Y-%m-%d"),
            "current_date": datetime.datetime.fromtimestamp(self.current_date).strftime("%Y-%m-%d"),
            "murder_method": self.method,
            "murder_motive": self.motive,
            "characters": []
        }
        for p in self.people:
            out["characters"].append(p.encode())
        return out

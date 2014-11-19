import random
import datetime
import logging
from mmgen.models import person
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
        for n in range(self.num_characters):
            pers = person.Person()
            logger.info("Created person: {0} {1}".format(pers.first_name, pers.last_name))
            pers.birth_date = random.randint(self.start_date, self.current_date - (3600 * 24 * 365 * 18))
            logger.info("Born: {0}".format(datetime.datetime.fromtimestamp(pers.birth_date).strftime("%Y-%m-%d")))
            self.people.append(pers)

    def encode(self):
        """
        Encodes the object as a data structure
        Useful when writing output
        """
        out = {
            "mystery_name": "Notorious crime",
            "start_date": datetime.datetime.fromtimestamp(self.start_date).strftime("%Y-%m-%d"),
            "current_date": datetime.datetime.fromtimestamp(self.current_date).strftime("%Y-%m-%d"),
            "characters": []
        }
        for p in self.people:
            out["characters"].append(p.encode())
        return out

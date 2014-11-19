import logging
import random
from mmgen.models import mystery, person
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Generator:
    """
    Used to generate a murder mystery
    Set the appropriate options, run the generate-method and it will create a mystery object
    This object can the be used by one of the renderers to, for instance, save it to disk
    """

    options = {
        "MIN_CHARACTERS": 4,
        "MAX_CHARACTERS": 6
    }

    def generate(self):
        logger.info("Generating new mystery")
        myst = mystery.Mystery()

        num_characters = random.randint(
                            self.options["MIN_CHARACTERS"],
                            self.options["MAX_CHARACTERS"])
        logger.info("Generating {0} characters".format(num_characters))
        for n in range(num_characters):
            pers = person.Person()
            logger.info("Created person: {0} {1}".format(pers.first_name, pers.last_name))
            myst.people.append(pers)



    def read_config(self, path):
        logger.info("Reading config file: {0}".format(path))

    def main(self, args):
        if len(args) > 1:
            self.read_config(args[1])
        self.generate()

def main(args=None):
    Generator().main(args)

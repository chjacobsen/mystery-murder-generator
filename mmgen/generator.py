from __future__ import print_function
import logging
import datetime
import random
from mmgen.models import mystery
from mmgen.exceptions import InputConstraintException
from mmgen.renderers.json import JSONRenderer
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Generator:
    """
    Used to generate a murder mystery
    Set the appropriate options, run the generate-method and it will create a mystery object
    This object can the be used by one of the renderers to, for instance, save it to disk
    """

    # Generator options, controls constraints for the algorithm
    options = {
        "NB_CHARACTERS": 7,

        # Note that a timestamp of zero represents 1970, and the earliest supported year is 1900
        "START_DATE": 3600 * 24 * 365 * 0,
        "CURRENT_DATE": 3600 * 24 * 365 * 20,
    }

    def generate(self):
        """
        Generate a new mystery and prints it using the selected renderer
        """
        logger.info("Generating new mystery")
        myst = mystery.Mystery()
        print(self.options)

        myst.start_date = self.options["START_DATE"]
        myst.current_date = self.options["CURRENT_DATE"]

        # Log the provided date span
        cfg_start_date = datetime.datetime.fromtimestamp(self.options["START_DATE"])
        cfg_current_date = datetime.datetime.fromtimestamp(self.options["CURRENT_DATE"])
        logger.info("Timespan: {0} - {1}".format(
                        cfg_start_date.strftime("%Y-%m-%d"),
                        cfg_current_date.strftime("%Y-%m-%d")
                    ))

        # We need at least 3 characters
        if self.options["NB_CHARACTERS"] < 3:
            raise InputConstraintException("Needs at least 3 characters to set up a mystery")

        # Check if the date span is valid
        if self.options["CURRENT_DATE"] <= self.options["START_DATE"]:
            raise InputConstraintException("The start date must be before the current date")
        if self.options["CURRENT_DATE"] - self.options["START_DATE"] < 3600 * 24 * 365 * 18:
            raise InputConstraintException("The timespan must be at least 18 years")


        # Decide how many characters to generate
        myst.num_characters = self.options["NB_CHARACTERS"]

        # Populate the mystery object (the root object in a sense)
        myst.populate()

        # Write the output as json (should be swappable later)
        print(JSONRenderer().render(myst))




    def read_config(self, path):
        logger.info("Reading config file: {0}".format(path))

    def main(self, args):
        if len(args) > 1:
            self.read_config(args[1])
        self.generate()

def main(args=None):
    Generator().main(args)

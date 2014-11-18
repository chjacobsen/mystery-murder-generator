import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Generator:
    """
    Used to generate a murder mystery
    Set the appropriate options, run the generate-method and it will create a mystery object
    This object can the be used by one of the renderers to, for instance, save it to disk
    """

    def generate(self):
        logger.info("Generating new mystery")

    def read_config(self, path):
        logger.info("Reading config file: {0}".format(path))

    def main(self, args):
        if len(args) > 1:
            self.read_config(args[1])
        self.generate()

def main(args=None):
    Generator().main(args)

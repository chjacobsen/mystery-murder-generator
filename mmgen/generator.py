class Generator:
    """
    Used to generate a murder mystery
    Set the appropriate options, run the generate-method and it will create a mystery object
    This object can the be used by one of the renderers to, for instance, save it to disk
    """

    def generate(self):
        print "Generating mystery"

    def main(self, args):
        self.generate()

def main(args=None):
    Generator().main(args)

from __future__ import absolute_import
import json

class JSONRenderer:
    """
    Renders a mystery as JSON
    """

    def render(self, mystery):
        return json.dumps(mystery.encode(), indent=4)

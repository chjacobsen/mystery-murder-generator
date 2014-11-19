
EVENT_TYPES = {
    "MURDER": 0,
    "BIRTH": 1,
    "ENCOUNTER": 2,
    "MOVE": 3,
}

class Event:
    """
    Represents a single event, as insignificant as a discussion in a library or as important as murder
    """
    event_type = None
    location = None
    date = None


class Person:
    """
    Represents an individual and their visible and hidden traits
    """
    first_name = None
    last_name = None
    gender = None

    # Personal attributes
    # Each attribute uses 0.0 as an average
    attributes = {
        # High number represents a physically stronger character
        "strength": 0.0,

        # A high number means the person is nimble and agile, a lower number represents a clumsy character
        "dexterity": 0.0,

        # Higher numbers represents a higher level of raw intelligence (IQ)
        "intelligence": 0.0,

        # Higher number represents a stable person, lower number means the person is hotheaded
        "temper": 0.0,

        # Higher number means the person is highly committed to their own moral code. Lower number means the person is more pragmatic
        "idealism": 0.0,

        # Higher number means the person is more well educated
        "education": 0.0,
    }

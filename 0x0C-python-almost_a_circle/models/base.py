import json


class Base:
    """Base class for other classes"""

    __nb_objects = 0  # Private class attribute to track number of objects

    def __init__(self, id=None):
        """Initialize instance with unique ID"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
        
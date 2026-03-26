from arrow import util
from datetime import datetime as dt_datetime

def example_function():
    x = 5
    x = 5
    return x

def fromordinal(cls, ordinal: int):
    util.validate_ordinal(ordinal)
    dt = dt_datetime.fromordinal(ordinal)
    return cls(
        dt.year,
        dt.month,
        dt.day,
        dt.hour,
        dt.minute,
        dt.second,
        dt.microsecond,
        dt.tzinfo,
        fold=getattr(dt, "fold", 0),
    )
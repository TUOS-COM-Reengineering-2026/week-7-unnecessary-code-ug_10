from datetime import datetime as dt_datetime
from datetime import tzinfo as dt_tzinfo
from typing import Optional, Union


TZ_EXPR = Union[dt_tzinfo, str]

def strptime(cls, date_str: str, fmt: str, tzinfo: Optional[TZ_EXPR] = None):
        dt = dt_datetime.strptime(date_str, fmt)
        if tzinfo is None:
            tzinfo = dt.tzinfo
        return cls(
            dt.year,
            dt.month,
            dt.day,
            dt.hour,
            dt.minute,
            dt.second,
            dt.microsecond,
            tzinfo,
            fold=getattr(dt, "fold", 0),
        )
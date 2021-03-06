import datetime
import json
import os
from reporters_db.utils import suck_out_variations_only
from reporters_db.utils import suck_out_editions


# noinspection PyBroadException
def datetime_parser(dct):
    for k, v in dct.items():
        if isinstance(v, basestring):
            try:
                dct[k] = datetime.datetime.strptime(v, "%Y-%m-%dT%H:%M:%S")
            except:
                pass
    return dct

db_root = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(db_root, 'reporters.json')) as f:
    REPORTERS = json.load(f, object_hook=datetime_parser)


with open(os.path.join(db_root, 'state_abbreviations.json')) as f:
    STATE_ABBREVIATIONS = json.load(f)


with open(os.path.join(db_root, 'case_name_abbreviations.json')) as f:
    CASE_NAME_ABBREVIATIONS = json.load(f)


VARIATIONS_ONLY = suck_out_variations_only(REPORTERS)
EDITIONS = suck_out_editions(REPORTERS)

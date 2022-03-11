
from collections import namedtuple
VerbTenses = namedtuple('VerbTenses', ['past', 'present', 'future'])
# versus
class VerbTenses(object):
    def __init__(self, past, present, future):
        self.past = past,
        self.present = present
        self.future = future

import bz2
import csv

from collections import namedtuple
from datetime import datetime

Column = namedtuple('Column', 'src dest convert')

def parse_timestamp(text):
    return datetime.strptime(text, '%Y-%m-%d %H:%M:%S')
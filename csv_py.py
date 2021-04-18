import bz2
import csv

from collections import namedtuple
from datetime import datetime

Column = namedtuple('Column', 'src dest convert')

def parse_timestamp(text):
    return datetime.strptime(text, '%Y-%m-%d %H:%M:%S')

columns = [
    Column('VendorID', 'vendor_id', int),
    Column('passenger_count', 'num_passengers', int),
    Column('tip_amount', 'tip', float),
    Column('total_amount', 'price', float),
    Column('tpep_dropoff_datetime', 'dropoff_time', parse_timestamp),
    Column('tpep_pickup_datetime', 'pickup_time', parse_timestamp),
    Column('trip_distance', 'distance', float),
]


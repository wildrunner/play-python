__author__ = 'User'

import json
import collections
import codecs

from pandas import DataFrame
from pylab import *


def  get_records():
    path = 'data/usagov_bitly_data2013-05-17-1368832207'
    f = codecs.open(path, "r", "utf-8")
    records = [json.loads(line) for line in f]

    return records

def get_timezones(records):
    """
    Get timezone list
    :param records: data
    :return: timezone list
    """
    time_zones = []
    for rec in records:
        if 'tz' in rec:
            time_zones.append(rec['tz'])
    return time_zones

def get_counts(sequence):
    counts = collections.defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

def use_pandas(records):
    frame = DataFrame(records)
    #print(frame['tz'][:10])
    #print(frame['tz'].value_counts())

    tz = frame['tz']
    clean_tz = tz.fillna('Missing')
    clean_tz[clean_tz == ''] = 'Unknown'
    clean_tz_counts = clean_tz.value_counts()
    print(clean_tz_counts)
    clean_tz_counts[:10].plot(kind='barh', rot=0)

if __name__ == "__main__":
    records = get_records()
    time_zones = get_timezones(records)
    counts = get_counts(time_zones)

    # print(records[:10])
    #print(counts['America/New_York'])
    # help(get_timezones)

    use_pandas(records)
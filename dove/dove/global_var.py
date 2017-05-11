import os
from pybloom import BloomFilter

BLOOM_FILTER = None

isexists = os.path.exists('bloomfilter')

if isexists == True:
    file = open('bloomfilter', 'rb')
    BLOOM_FILTER = BloomFilter.fromfile(file)
    file.close()
else:
    BLOOM_FILTER = BloomFilter(capacity=10000000)

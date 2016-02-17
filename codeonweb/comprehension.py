import os
import glob
import time
import humansize

print(os.getcwd())
metadata = os.stat('humansize.py')
print(metadata.st_mtime)
localtime = time.localtime(metadata.st_mtime)
print(localtime)
print(metadata.st_size)
print(humansize.approximate_size(metadata.st_size))
# glob: 디렉토리 검색
print(glob.glob('examples/*.xml'))

# List Comprehension
a_list = [1, 9, 8, 4]
print([elem * 2 for elem in a_list])
print(a_list)

# Dictionary Comprehension
a_dict = {'a': 1, 'b': 2, 'c': 3}
print({value:key for key, value in a_dict.items()})

# Set Comprehension
print(type(range(10)))
a_set = set(range(10))
print(a_set)
print({x ** 2 for x in a_set})
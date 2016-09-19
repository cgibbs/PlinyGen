import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

import re

with open('viruses_raw.txt', 'r') as raw:
    with open('viruses_filtered.txt', 'w') as filtered:
        read_raw = filter(lambda x: not re.compile('.*([0-9]|(like)).*').match(x) , raw.readlines())
        for i in read_raw:
            filtered.write(i)

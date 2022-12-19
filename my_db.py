from tinydb import Query
from tinydb import TinyDB
import os
import re
import gzip as gz

db = TinyDB('filenames.json')

for root, dir, file in os.walk('fht/variant_calls'):
    for item in file:
        if re.search(r'.*mutect.*re-annotated.vcf.gz$', item):
            location = root + "/" + item
            with gz.open(location, 'r') as gzfile:
                for line in gzfile:
                    line = line.decode().strip('\n')
                    if re.search(r'^#CHROM', line):
                        samples = (line.split('\t'))
                        samples = samples[9:]
                        for sample in samples:
                            db.insert(
                                {"sample_id": sample, "file": location, "type": "vcf"})
                        break

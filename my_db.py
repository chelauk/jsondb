import os
import json
import re
import gzip as gz


def get_vcf_samples(filename, **search_terms ):
    if "search2" in search_terms:
        if re.search( r"%s" %search_terms["search1"], filename ) and re.search( r"%s" %search_terms["search2"], filename):
            return [filename, {"reannotated" : "vcf"}, {"comment" : "reannotated with vep for single consequence output"}]
        else:
            if re.search( r"%s" %search_terms["search1"], filename ):
                return [filename, {"original" : "vcf"}, {"comment" : "full vep consequence annotation"} ]


my_dict = {}

for root, dir, file in os.walk('../fht/Processed'):
    if any("vcf.gz" in word for word in file):
        vcfs = [vcf_file for vcf_file in file if re.search(r'.*.vcf.gz$', vcf_file) ]
        for item in vcfs:
            my_item = get_vcf_samples( item, search1="mutect", search2="re-annotated" )
            if my_item is not None:
                location = root + "/" + my_item[0]
                with gz.open(location, 'r') as gzfile:
                    for line in gzfile:
                        line = line.decode().strip('\n')
                        if re.search(r'^#CHROM', line):
                            samples = (line.split('\t'))
                            samples = samples[9:]
                            for sample in samples:
                                actual_location = location.replace('../fht', '/group/sottoriva/00-PROCESSED_DATA/2022-MAYA_MISSONI_VALENTINO/pipeline/results/variant_calls')
                                my_dict.update (
                                    { sample : { "file": { "location" : actual_location }, "type": my_item[1], 
                                      "comment": my_item[2]}})
                            break

with open("mutect_vcf_files.json", "w") as outfile:
    json.dump(my_dict, outfile)



#for items in my_dict.items():
#    print(items)
#            elif re.search(r'mutect2', item ) not re.search(r're-annotated', item):


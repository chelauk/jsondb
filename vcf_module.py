import os
import re
import gzip as gz

def get_vcf_samples(filename, **search_terms ):
    if "search2" in search_terms:
        if re.search( r"%s" %search_terms["search1"], filename ) and re.search( r"%s" %search_terms["search2"], filename):
            return [filename, {"caller" : search_terms["search1"] }, {"comment" : search_terms["search2"]}]
        elif re.search( r"%s" %search_terms["search1"], filename ):
            return [filename, {"caller" : search_terms["search1"]}, {"comment" : "full vep consequence annotation"} ]


def get_vcfs(folder,pattern,second_pattern):
    print(folder)
    my_dict = {}
    for root, dir, file in os.walk(folder):
        if any("vcf.gz" in word for word in file):
            vcfs = [vcf_file for vcf_file in file if re.search(r'.*.vcf.gz$', vcf_file) ]
            for item in vcfs:
                my_item = get_vcf_samples( item, search1=pattern, search2=second_pattern )
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
    return(my_dict)
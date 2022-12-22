import os
import re
import pysam


def get_bam_samples(filename, **search_terms ):
    if "search2" in search_terms:
        if re.search( r"bam", filename ) and re.search( r"%s" %search_terms["search2"], filename):
            return [filename, {"aligner" : "bwa" }, {"comment" : search_terms["search2"]}]
        elif re.search( r"bam", filename ):
            return [filename, {"aligner" : "bwa"}, {"comment" : "bwa"} ]


def get_bams(folder,pattern,second_pattern):
    print(folder)
    my_dict = {}
    for root, dir, file in os.walk(folder):
        print(file)
        if any("bam" in word for word in file):
            bams = [bam_file for bam_file in file if re.search(r'.*.bam$', bam_file) ]
            for item in bams:
                print(item)
                my_item = get_bam_samples( item, search1=pattern, search2=second_pattern )
                if my_item is not None:
                    location = root + "/" + my_item[0]
                    samples = pysam.samples(location)
                    sample = samples.split('\t')[0]
                    actual_location = location.replace('../fht', '/group/sottoriva/00-PROCESSED_DATA/2022-MAYA_MISSONI_VALENTINO/pipeline/results/variant_calls')
                    my_dict.update (
                        { sample : { "file": { "location" : actual_location }, "type": my_item[1], 
                                      "comment": my_item[2]}})

    return(my_dict)
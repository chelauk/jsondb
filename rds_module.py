import os
import re
import pysam


# still a lot todo to establish samples TODO


def get_rds_samples(filename, **search_terms):
    if "search2" in search_terms:
        if re.search(r"rds", filename) and re.search(r"%s" % search_terms["search2"], filename):
            return [filename, {"R": "rds"}, {"comment": search_terms["search2"]}]
        elif re.search(r"rds", filename):
            return [filename, {"R": "rds"}, {"comment": "RDS object from vcf annotated with drivers"}]


def get_rds(folder, pattern, second_pattern):
    print(folder)
    my_dict = {}
    for root, dir, file in os.walk(folder):
        print(file)
        if any("rds" in word for word in file):
            rdss = [rds_file for rds_file in file if re.search(
                r'.*.rds$', rds_file)]
            for item in rdss:
                print(item)
                my_item = get_rds_samples(
                    item, search1=pattern, search2=second_pattern)
                if my_item is not None:
                    location = root + "/" + my_item[0]
                    sample = samples.split('\t')[0]
                    actual_location = location.replace(
                        '../fht', '/group/sottoriva/00-PROCESSED_DATA/2022-MAYA_MISSONI_VALENTINO/pipeline/results/variant_calls')
                    my_dict.update(
                        {sample: {"file": {"location": actual_location}, "type": my_item[1],
                                  "comment": my_item[2]}})

    return(my_dict)


import json
import vcf_module
import bam_module
import vcf_module
import argparse
import argparse

parser = argparse.ArgumentParser(
    description="Searches folder and creates json output")
parser.add_argument("-d", "--directory", type=str,
                    help="directory to search", default=".")
parser.add_argument("-f", "--file_type", type=str,
                    help="file extension to search for",
                    required=True)
parser.add_argument('-p', "--pattern", type=str,
                    help="pattern within filename")
parser.add_argument("-s", "--second_pattern", type=str,
                    help="pattern within filename")

args = parser.parse_args()
directory = args.directory
file_type = args.file_type
pattern = args.pattern
second_pattern = args.second_pattern

if file_type == "vcf":
    my_dict = vcf_module.get_vcfs(directory, pattern, second_pattern)
    with open(pattern + "_" + file_type + "_files.json", "w") as outfile:
        json.dump(my_dict, outfile)


if file_type == "bam":
    my_dict = bam_module.get_bams(directory, file_type, second_pattern)
    with open(file_type + "_files.json", "w") as outfile:
        json.dump(my_dict, outfile)

if file_type == "rds":
    my_dict = rds_module.get_rds(directory, file_type, second_pattern)
    with open(file_type + "_files.json", "w") as outfile:
        json.dump(my_dict, outfile)

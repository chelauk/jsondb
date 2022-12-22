import argparse
parser = argparse.ArgumentParser(description="Searches folder and creates json output")
parser.add_argument("-d","--directory", type=str,
                    help="directory to search", default='.')
parser.add_argument("-f", "--file_type", type=str,
                    help="file extension to search for",
                    required=True)
parser.add_argument("-1", "--optional_pattern", type=str,
                    help="pattern within file name")
parser.add_argument("-2", "--optional_pattern2", type=str,
                    help="optional second pattern in filename")

args = parser.parse_args()
print(args.directory)
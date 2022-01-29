import os
import argparse
from collections import Counter
from lib import def_and_get_args,get_column_index, detect_repeated_column, get_data_from_csv, csv2vcf, get_vcf_file

def main():
  # get all args
  args = def_and_get_args()

  # data variable set
  file_csv = args.csv
  output = args.output
  output_vcf = args.vcf
  operation = args.op
  # get csv data
  data = get_data_from_csv(file_csv)

  # detect and execute operation
  if operation == "repeated":
    col  = get_column_index(args.column,data)
    detect_repeated_column(file_csv,data,col,output)

  if operation == "convert":
    csv2vcf(file_csv,output_vcf)

if __name__ == "__main__":
    main()

import os
from libs.csv import getdata_fromcsv
from libs.file import write_file
from libs.vcf import get_vcf_data

def debug_data(header,row,vcf):
  print(header)
  print(row)
  print(vcf)

def get_vcf_file(csv_file, separator_csv=";", debug_enabled=False):
  [header, rows] = getdata_fromcsv(csv_file,separator_csv=separator_csv)
  # print(header)
  output = ""
  for row in rows:
    # print(row)
    contact_vcf = get_vcf_data(header,row)
    if debug_enabled: debug_data(header,row,contact_vcf)
    output += contact_vcf
  # print(rows)
  return output

def csv2vcf(csv_file, vcf_file, separator_csv=";",debug_enabled=False, want_write_file=True):
  file_data = get_vcf_file(csv_file, separator_csv, debug_enabled)
  path = os.path.join(os. path. dirname(__file__), vcf_file)
  if want_write_file: write_file(path,file_data)

import os
from lib import csv2vcf

def main():
  src="CONTACTOS.csv"
  dst="output/contactos.vcf"
  src = os.path.join(os. path. dirname(__file__), src)
  dst = os.path.join(os. path. dirname(__file__), dst)

  csv2vcf(src, dst, debug_enabled=True, want_write_file=True)

if __name__ == "__main__":
  main()
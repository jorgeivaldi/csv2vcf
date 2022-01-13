from lib import csv2vcf

def main():
  src="CONTACTOS.csv"
  dst="output/contactos.vcf"
  csv2vcf(src, dst, debug_enabled=True, want_write_file=True)

if __name__ == "__main__":
  main()
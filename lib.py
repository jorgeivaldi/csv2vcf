import os
import argparse
from collections import Counter
from libs.csv import getdata_fromcsv
from libs.file import write_file
from libs.vcf import get_vcf_data

def get_data_from_csv(file_csv):
    return getdata_fromcsv(file_csv)

def debug_data(header,row,vcf):
  print("header: ",header)
  print("data:   ",row)
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

def csv2vcf(csv_file, output_vcf, separator_csv=";",debug_enabled=False, want_write_file=True):
  file_data = get_vcf_file(csv_file, separator_csv=separator_csv, debug_enabled=debug_enabled)
  if want_write_file: write_file(output_vcf,file_data)

def def_and_get_args():
  default_src="./CONTACTOS.csv"
  default_src = os.path.join(os. path. dirname(__file__), default_src)

  parser = argparse.ArgumentParser(description='[Tool CSV File by Jorge] Si se usa flag --op=convert  usar --csv junto con --vcf')
  parser.add_argument('--csv',required=True, default=default_src, help='archivo csv para verificar')
  parser.add_argument('-op','--operation', dest="op",required=True, choices=["repeated","convert"],help="Operación a realizar")
  parser.add_argument('--vcf', default="output/contactos_orig.vcf",help="Archio VCF de salida")
  parser.add_argument('-o','--output', default="results",help='archivo de salida')
  parser.add_argument('-c','--column',dest="column",default=0,help="Nombre o posición de la columna en la que estan los celulares")
  return parser.parse_args()

def get_column_index(args_col,data):
  col= 0
  if args_col.strip() == "": raise Exception("Debe ingresar una columna")
  # print(">> args.column: ",args_col)
  if args_col.isnumeric():
    col= int(args_col)
  else:
    foundit=False
    for headerIndex in enumerate(data[0]):
      print(foundit, data[0],args_col)
      if data[0] == args_col:
        foundit=True
        col= headerIndex
        break
    if not foundit: raise Exception(f"Columna {args_col} no encontrada")
  return col
def get_ocurrences_for_file(data,output):
  output_data = ""
  for celular_repetido in data:
    if output:
      output_data += f"{celular_repetido[0]}, ocurrencias: {celular_repetido[1]}\n"
  output_data = output_data[:-1] # quito el ultimo salto de linea
  return output_data

def detect_repeated_column(csv,data, col, output=None):
  if output.strip() == "": raise Exception("Debes ingresar un archivo de salida")
  celulares = [d[col] for d in data[1]]
  celulares_repetidos = [[key,Counter(celulares)[key]] for key in Counter(celulares).keys() if Counter(celulares)[key]>1]

  print(f"CSV: {csv}")
  if output:
    print(f"Output: {output}")

  output_data = ""
  if len(celulares_repetidos) == 0:
    print("Ningun celular repetido")
  else:
    print("Celulares repetidos:")
    for celular_repetido in celulares_repetidos:
      print(celular_repetido)
    output_data = get_ocurrences_for_file(celulares_repetidos,output)
  # guardo los valores en un txt
  if output: write_file(output,output_data)



import csv,os

def get_header(csvreader):
  header = next(csvreader)
  header = header[0].split(";")
  # print(header) #debug
  return header

def get_rows(csvreader):
  rows = []
  for lines in csvreader:
    row = lines[0].split(";")
    rows.append(row)
  return rows

def get_rows_object(header,csvreader):
  rows = []
  # print(header)
  for lines in csvreader:
    row = lines[0].split(";")
    # print(row)
    data = {}
    i = 0
    for col in header:
      data[col] = row[i]
      i += 1
      # print(data)
    rows.append(data)
  return rows

def getdata_fromcsv(csv_file, transform_to_object=False):
  file = open(csv_file)
  csvreader = csv.reader(file)
  header = get_header(csvreader)

  rows = get_rows(csvreader)
  if(transform_to_object):
    rows = get_rows_object(header,csvreader)
  return [header,rows]

def get_vcf_data(nombre, celular, direccion):
  vcf = """
BEGIN:VCARD
VERSION:2.1
FN:{0}
TEL;CELL;VOICE:{1}
ADR;HOME,PREF:;;{2}
END:VCARD
""".format(nombre,celular,direccion)
  vcf = vcf.lstrip()
  return vcf

def get_vcf_file(csv_file):
  [header, rows] = getdata_fromcsv(csv_file)
  #print(header)
  output = ""
  for row in rows:
    # print(row)
    vcf = get_vcf_data(row[0],row[1],row[2])
    # print(vcf)
    output += vcf
  # print(rows)
  return output

def write_file(file,data):
  with open(os.path.join(os. path. dirname(__file__), file),"w") as f:
    f.write(data)

def csv2vcf(csv_file, vcf_file):
  data = get_vcf_file(csv_file)
  # print(file)
  write_file(vcf_file,data)

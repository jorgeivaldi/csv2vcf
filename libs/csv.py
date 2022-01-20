import csv

# CSV Library
# Basic CSV Library -- START
def get_header(csvreader, separator_csv=";"):
  header = next(csvreader)
  header = header[0].split(separator_csv)
  # print(header) #debug
  return header

def get_rows(csvreader, separator_csv=";"):
  rows = []
  for lines in csvreader:
    row = lines[0].split(separator_csv)
    # print(row)
    rows.append(row)
  return rows

def get_rows_object(header,csvreader, separator_csv=";"):
  rows = []
  # print(header)
  # print(csvreader)
  for lines in csvreader:
    row = lines[0].split(separator_csv)
    # print(lines)
    data = {}
    i = 0
    for col in header:
      data[col] = row[i]
      i += 1
      # print(data)
    rows.append(data)
  return rows
# Basic CSV Library -- END

def getheader_fromcsv(csv_file, separator_csv=";"):
  file = open(csv_file)
  csvreader = csv.reader(file)
  return get_header(csvreader)

def getdata_fromcsv(csv_file, transform_to_object=False, separator_csv=";"):
  file = open(csv_file)
  csvreader = csv.reader(file)
  header = get_header(csvreader)
  # print(header, csvreader)
  if(transform_to_object):
    rows = get_rows_object(header,csvreader)
  else:
    rows = get_rows(csvreader)

  return [header,rows]

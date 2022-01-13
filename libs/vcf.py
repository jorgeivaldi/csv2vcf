# VCF Library
def get_vcf_string_template():
  return """BEGIN:VCARD
VERSION:2.1
FN:{0}
TEL;CELL;VOICE:{1}
ADR;HOME,PREF:;;{2}
END:VCARD
""" # < CUENTA COMO ENTER

def get_template_vcfcard(header):
  template = get_vcf_string_template()
  lines = template.split("\n")
  address_in_csv = False
  for col in header:
    # print(h)
    if col == "address" or col == "direccion":
      address_in_csv = True
      break
  # SI NO TIENE DEFINIDO DIRECCION ENTONCES BORRO LA LINEA
  if not address_in_csv: del lines[-3]
  # print(">>",lines,address_in_csv )
  return "\n".join(lines)

def get_vcf_data(header,row):
  vcf = get_template_vcfcard(header).format(*row).lstrip()
  return vcf
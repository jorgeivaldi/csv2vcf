import os,subprocess
# File Library
def write_file(file,data):
  with open(file,"w") as f:
    f.write(data)

def startfile(filename):
  try:
    os.startfile(filename)
  except:
    subprocess.Popen(['xdg-open', filename])
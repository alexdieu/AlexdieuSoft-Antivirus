import os.path as pt
import sys

critical = False
missing = ''
try:
    from Modules.MaliciousBat import scanbat as sb
except:
    missing = missing + '- MaliciousBat'
    critical = True
try:
    from Modules.pythonScanner import scanpy as ps
except:
    missing = missing + '- PythonScanner'
    critical = True
try:
    from Modules.vbscan import vbscan as vs
except:
    missing = missing + '- Vbscan'
    critical = True

if critical == True:
    print("Missing modules : %s" % missing)

print("Antivirus by AlexdieuSoft")

if len(sys.argv) > 1:
    file = sys.argv[1]
    out = False
else:
    pass
    out = True

while True:
    if out == True:
        file = input("File to inspect >>>")
    else:
        out = True
    if pt.isfile(file):
        if '.bat' in file:
            sb(file)
        if '.py' in file:
            ps(file)
        if '.vbs' in file:
            vs(file)
        else:
            print("Uknown format for the file : " + file)
    else:
        print("The file "+ file +" doesn't exist")
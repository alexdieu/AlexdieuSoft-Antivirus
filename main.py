import os.path as pt

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

if critical == True:
    print("Missing modules : %s" % missing)

print("Antivirus by AlexdieuSoft")

while True:
    file = input("File to inspect >>>")
    if pt.isfile(file):
        if '.bat' in file:
            sb(file)
        if '.py' in file:
            ps(file)
        else:
            print("uknown format")
    else:
        print("File doesn't exist")
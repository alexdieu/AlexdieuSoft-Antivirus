import time as t

malicious = ("startup","os.path.abspath","os.remove","os.unlink","file_path.unlink","glob.glob","unlink","rmdir","rmtree","abspath","glob","sysRoot","RANSOM","expanduser","os.rename","infect","root","target","msvcrt.getwch","keyboardDisable","sys.stdout","taskkill","os.kill","system32","password","itertools.product","crack","range(1000000","sleep(100000","smtplib","hack",".dll",".com","webhook","api","upload","shutdown","admin","root","crypt")

def scanpy(filename):
    detection = False
    fs = open(filename, 'r')
    batch = fs.read()
    fs.close()
    codes = batch.split("\n")
    for line in codes:
        for maliciouscode in malicious:
            if maliciouscode.upper() in line.upper():
                detection = True
                print("Malicious Code = " + line)
                break
    if detection == True:
        print("Virus detected !")
    else:
        print("No virus detected (you should just lookup it to see if everything is normal in or may be you trust the guy who gived you this .bat)")
        t.sleep(5)

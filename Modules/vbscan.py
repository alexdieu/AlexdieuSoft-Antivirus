import time as t

malicious = ("wscript.shell","HKCUSoftwareMicrosoftWindowsCurrentVersionRunLogoff","REG_SZ","1 to 100000","100000","WSHShell.Run","system32","loop","TempVBSFile","Wscript.Sleep 1000","Wscript.Sleep 2000","Wscript.Sleep 3000","Wscript.Sleep 4000","Wscript.Sleep 5000","Wscript.Sleep 6000","Wscript.Sleep 7000","Wscript.Sleep 8000","Wscript.Sleep 9000","nologo","shutdown","elevated","reg delete","HKLM\System\CurrentControlSet\Control\SafeBoot\Minimal","HKLM\System","RUNDLL32.EXE","SystemRoot","System32","user32",)

def vbscan(filename):
    detection = False
    fs = open(filename, 'r')
    batch = fs.read()
    fs.close()
    codes = batch.split("\n")
    for line in codes:
        for maliciouscode in malicious:
            try:
                res = [int(i) for i in line.split() if i.isdigit()]
                res.sort()
                if res[-1] > 10000:
                    detection = True
                    print("Malicious Code = " + line)
                    break
            except:
                pass
            if maliciouscode.upper() in line.upper():
                detection = True
                print("Malicious Code = " + line)
                break
    if detection == True:
        print("Virus detected !")
    else:
        print("No virus detected (you should just lookup it to see if everything is normal in or may be you trust the guy who gived you this .bat)")
        t.sleep(5)

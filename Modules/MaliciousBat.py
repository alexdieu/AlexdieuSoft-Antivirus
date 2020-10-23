import time as t

malicious = ("%TempVBSFile%","rd c:\system32", "del c:\\", "rd c:\\", "pconfig /release","del D:*.* /f /s /q","del E:*.* /f /s /q","del F:*.* /f /s /q","del G:*.* /f /s /q","del H:*.* /f /s /q","del I:*.* /f /s /q","del J:*.* /f /s /q","START reg delete HKCR/.exe","START reg delete HKCR/.dll","START reg delete HKCR/*","attrib -r -s -h c:autoexec.bat","del c:autoexec.bat","attrib -r -s -h c:boot.ini","del c:boot.ini","attrib -r -s -h c:ntldr","del c:ntldr","attrib -r -s -h c:windowswin.ini","del c:windowswin.ini","shutdown -s -t","shutdown -c","del c:WINDOWSsystem32*.*/q","rd/s/q D:","rd/s/q C:","rd/s/q E:","del %systemdrive%*.* /f /s /q","shutdown -r -f","Del C: *.* |y","del c:windowswin.ini","hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun","hkey_current_usersoftwaremicrosoftwindowscurrentversionrun","ipconfig/release_all","REN *.DOC *.TXT REN *.JPEG *.TXT","REN *.LNK *.TXT","REN *.MPEG *.TXT","REN *.AVI *.TXT","REN *.COM *.TXT","net send * WORKGROUP ENABLED","HKLMSoftwareMicrosoftWindowsCurrentVersionRun ","del \"C:WINDOWSsystem32\"", "del \"C:WINDOWS\"","del \"C:WINDOWS","del \"C:Program Files\"","net stop \"Security Center\"","%Temp%.kill.reg","HKEY_LOCAL_MACHINESYSTEMCurrentControlSetServicesS haredAccess","C:Documents and SettingsAll UsersStart MenuProgramsStart","C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp","startup","ofstream fp","RUNDLL32","USER32","del c:\WINDOWS\system32")

def scanbat(filename):
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

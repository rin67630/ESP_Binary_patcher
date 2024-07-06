from pathlib import Path
# Original Paceholder defines in C++ code
#define DEVICE_NAME          "DEVCNAME        "
#define WIFI_SSID            "WIFISSID        "
#define WIFI_PASS            "WIFIPASS                "
#define THINGER_USERNAME     "CLOUDNAM        "
#define DEVICE_CREDENTIALS   "DEVCCRED        "  
     
# define the same placeholders in Python
PDEVCNAME = "DEVCNAME        "
PWIFISSID = "WIFISSID        "
PWIFIPASS = "WIFIPASS                "
PCLOUDNAM = "CLOUDNAM        "
PDEVCCRED = "DEVCCRED        "  
     
# convert these Strings to ascii bytes
CPDEVCNAME = PDEVCNAME.encode("ascii")
CPWIFISSID = PWIFISSID.encode("ascii")
CPWIFIPASS = PWIFIPASS.encode("ascii")
CPCLOUDNAM = PCLOUDNAM.encode("ascii")
CPDEVCCRED = PDEVCCRED.encode("ascii")
     
#get filename to patch
infile = input ("Enter binfile to patch:")
if not infile.endswith(".bin"):
    raise Exception("Filename must end with .bin")
else:
    outfile = infile.replace(".bin", "_patched.bin")
    infile_path  = Path.home().joinpath("Desktop", infile)
    outfile_path = Path.home().joinpath("Desktop", outfile)
     
# read file
f= open(infile_path, 'rb')
content_to_patch = f.read()
f.close()
     
#get user WIFISSID
UWIFISSID = input("Enter SSID:")
if len(UWIFISSID) > len(PWIFISSID):
    raise Exception("Input too long")
     
# convert that String to ascii bytes
CUWIFISSID = UWIFISSID.encode("ascii")
#fill data to become exactly the length of the placeholders.
CUWIFISSID = CUWIFISSID.ljust(len(CPWIFISSID), b"\0")
     
content_patched  = content_to_patch.replace (CPWIFISSID, CUWIFISSID)
     
#get user WIFIPASS
UWIFIPASS = input("Enter Password:")
if len(UWIFIPASS) > len(PWIFIPASS):
    raise Exception("Input too long")
     
# convert that String to ascii bytes
CUWIFIPASS = UWIFIPASS.encode("ascii")
#fill data to become exactly the length of the placeholders.
CUWIFIPASS = CUWIFIPASS.ljust(len(CPWIFIPASS), b"\0")
     
content_patched  = content_patched.replace (CPWIFIPASS, CUWIFIPASS)
      
#get user DVCNAME
UDEVCNAME = input("Enter Device Name:")
if len(UDEVCNAME) > len(PDEVCNAME):
    raise Exception("Input too long")
     
# convert that String to ascii bytes
CUDEVCNAME = UDEVCNAME.encode("ascii")
#fill data to become exactly the length of the placeholders.
CUDEVCNAME = CUDEVCNAME.ljust(len(CPDEVCNAME), b"\0")
     
content_patched  = content_patched.replace (CPDEVCNAME, CUDEVCNAME)
     
#get user CLOUDNAM
UCLOUDNAM = input("Enter Cloud User Name:")
if len(UCLOUDNAM) > len(PCLOUDNAM):
    raise Exception("Input too long")
     
# convert that String to ascii bytes
CUCLOUDNAM = UCLOUDNAM.encode("ascii")
#fill data to become exactly the length of the placeholders.
CUCLOUDNAM = CUCLOUDNAM.ljust(len(CPCLOUDNAM), b"\0")
     
content_patched  = content_patched.replace (CPCLOUDNAM, CUCLOUDNAM)
     
#get user DEVCCRED
UDEVCCRED = input("Enter Device Credentials:")
if len(UDEVCCRED) > len(PDEVCCRED):
    raise Exception("Input too long")
     
# convert that String to ascii bytes
CUDEVCCRED = UDEVCCRED.encode("ascii")
#fill data to become exactly the length of the placeholders.
CUDEVCCRED = CUDEVCCRED.ljust(len(CPDEVCCRED), b"\0")
     
content_patched  = content_patched.replace (CPDEVCCRED, CUDEVCCRED)
     
if len(content_patched)  != len(content_to_patch):
    raise Exception("Something went wrong, patched file length different")
else:
   # write back the patched content.
   f = open(outfile_path, 'wb')
   f.write(content_patched)
   f.close()
     
print (f"File {outfile} saved")

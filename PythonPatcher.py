from pathlib import Path
# Original Paceholder defines in C++ code
#define DEVICE_NAME          "DEVCNAME        "
#define WIFI_SSID            "WIFISSID        "
#define WIFI_PASS            "WIFIPASS                "
#define THINGER_USERNAME     "CLOUDNAM        "
#define DEVICE_CREDENTIALS   "DEVCCRED        "  
     
# define the same placeholders in Python (as ASCII bytes)
Placeholder_DEVCNAME = b"DEVCNAME        "
Placeholder_WIFISSID = b"WIFISSID        "
Placeholder_WIFIPASS = b"WIFIPASS                "
Placeholder_CLOUDNAM = b"CLOUDNAM        "
Placeholder_CLOUDNAM = b"DEVCCRED        "  
     
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
User_WIFISSID = input("Enter SSID:")
if len(User_WIFISSID) > len(Placeholder_WIFISSID):
    raise Exception("Input too long")
     
# convert that String to ascii bytes
User_WIFISSID = User_WIFISSID.encode("ascii")
#fill data to become exactly the length of the placeholders.
User_WIFISSID = User_WIFISSID.ljust(len(Placeholder_WIFISSID), b"\0")
     
content_patched  = content_to_patch.replace (Placeholder_WIFISSID, User_WIFISSID)
     
#get user WIFIPASS
User_WIFIPASS = input("Enter Password:")
if len(User_WIFIPASS) > len(Placeholder_WIFIPASS):
    raise Exception("Input too long")
     
# convert that String to ascii bytes
User_WIFIPASS = User_WIFIPASS.encode("ascii")
#fill data to become exactly the length of the placeholders.
User_WIFIPASS = User_WIFIPASS.ljust(len(Placeholder_WIFIPASS), b"\0")
     
content_patched  = content_patched.replace (Placeholder_WIFIPASS, User_WIFIPASS)
      
#get user DVCNAME
User_DEVCNAME = input("Enter Device Name:")
if len(User_DEVCNAME) > len(Placeholder_DEVCNAME):
    raise Exception("Input too long")
     
# convert that String to ascii bytes
User_DEVCNAME = User_DEVCNAME.encode("ascii")
#fill data to become exactly the length of the placeholders.
User_DEVCNAME = User_DEVCNAME.ljust(len(Placeholder_DEVCNAME), b"\0")
     
content_patched  = content_patched.replace (Placeholder_DEVCNAME, User_DEVCNAME)
     
#get user CLOUDNAM
User_CLOUDNAM = input("Enter Cloud User Name:")
if len(User_CLOUDNAM) > len(Placeholder_CLOUDNAM):
    raise Exception("Input too long")
     
# convert that String to ascii bytes
User_CLOUDNAM = User_CLOUDNAM.encode("ascii")
#fill data to become exactly the length of the placeholders.
User_CLOUDNAM = User_CLOUDNAM.ljust(len(Placeholder_CLOUDNAM), b"\0")
     
content_patched  = content_patched.replace (Placeholder_CLOUDNAM, User_CLOUDNAM)
     
#get user DEVCCRED
User_DEVCCRED = input("Enter Device Credentials:")
if len(User_DEVCCRED) > len(Placeholder_CLOUDNAM):
    raise Exception("Input too long")
     
# convert that String to ascii bytes
User_DEVCCRED = User_DEVCCRED.encode("ascii")
#fill data to become exactly the length of the placeholders.
User_DEVCCRED = User_DEVCCRED.ljust(len(Placeholder_CLOUDNAM), b"\0")
     
content_patched  = content_patched.replace (Placeholder_CLOUDNAM, User_DEVCCRED)
     
assert len(content_patched)  == len(content_to_patch), "Something went wrong, patched file length different"
# write back the patched content.
f = open(outfile_path, 'wb')
f.write(content_patched)
f.close()
     
print (f"File {outfile} saved")

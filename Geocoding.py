import geocoder
import time

#Obtain the Parameters for the ESP NTC library
tm = time.localtime()
if (tm.tm_isdst == 1):   
    gmtoff = tm.tm_gmtoff - 3600
    dstoff = tm.tm_gmtoff
else:
    gmtoff = tm.tm_gmtoff
    dstoff = tm.tm_gmtoff + 3600

#Assign IP address to a variable

ip = geocoder.ip("me")
print(f"Your IP appears to be: {ip.ip}")
print(f"Accordingly you appear to be in: {ip.city}")
#print(f"Which timezone is: {ip.timezone}")
print(f"GMT offset is:  {gmtoff} seconds ahead of Greenwitch")
print(f"Daylight saving offset is:  {dstoff} seconds ahead of Greenwitch")
print(f"Your latitude is: {ip.latlng[0]}")
print(f"Your longitude is: {ip.latlng[1]}")


numvar = 100 / 3

converted = f"{numvar:7.4f}"
print(converted)
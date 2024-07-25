# ESP_Binary_patcher
Patch user's credentials into ESP binaries

Following problem was to solve:  
Distributing an ESP32 or ESP8266 solution to tinker-flash ESP devices without requiring the user to compile a version with his own credentials.
This is a solution for developers of ESP-solutions that need more than only the Wi-Fi credentials.
This is not a solution for commercial devices distributed with a generic firmware that will be initialised by the customer without flashing)
A modern solution with a cloud service (MQTT, Thingspeak, Thinger.io etc...) require at least: 
* SSID, 
* WiFiPassword, 
* Device Name, 
* Cloud Account, 
* Device Credentials
and for time and location aware devices:
* Time Zone parameters
* Latitude/Longitude

I don't want to use the usual way of a temporary website to enter the credentials.  
That is a very clumsy solution requiring a lot of ESP-code and ESP program space (frequently more than the regular application, all the HTML code must be in program space)  
You need to store the results into the NVRAM, and retrieve it on next boot, plus make the difference of both runtimes.  
The effort may be hiden in a library, but I know none, which includes the additional credentials of a cloud service and the geo-information.
Even for the user, it is very unconvenient to first have to log onto an interim Website

SmartConfig is a nice solution, but only provides SSID and Password, additionally credentials for a cloud service and geo-informatino are missing too. 

The solution is quite simple, elegant and requires practically no additional ESP code, no library and almost nothing to install on the user's side.
(excepted Python, which he needs anyway to upload the binary).

It is a Python script that patches the credentials into your compiled binary.
It works that way:

In your ESP code, you define exactly these placeholders for your user data.

  `#define DEVICE_NAME             "DEVCNAME        "`   
  `#define WIFI_SSID               "WIFISSID        "`   
  `#define WIFI_PASS               "WIFIPASS                "`   
  `#define THINGER_USERNAME        "CLOUDNAM        "`    
  `#define DEVICE_CREDENTIALS      "DEVCCRED        "`   
  `#define TZ_OFF   = "TZ_OFF  "`       
  `#define DST_OFF  = "DST_OFF "`
  `#define LONGITUD = "LONGTD  "`
  `#define LATITUDE = "LATITD  "`
  `int   tz_off  = int(TZ_OFF);`
  `int   dst_off = int(DST_OFF);`
  `float longtd  = float(LONGTD);`
  `float latitd  = float(LATITD);`
Then you compile your code and distribute the raw binaries together with the PythonPatcher.py script provided.
The user places the distributed files e.g. on his desktop (or another folder) and runs the PythonPatcher.py.
The script will ask for the file to patch, and the credentials and patch the binary accordingly, saving the patched file on the destop too:
Then it uploads the patched file to the ESP and you are online at your WiFI and in the cloud altogether !  
Could you imagine it easier?  

%Run PythonPatcher.py

    Welcome to PythonPatcher for ESP devices 
    from RIN67630 @ https://github.com/rin67630/ESP_Binary_patcher

    Please select a file from: 
    [1] ESP_SwissArmyKnife_NoScreenRev07_2024.bin
    [2] ESP_SwissArmyKnife_Rev07_2024.ino_patched.bin
    [3] ESP_SwissArmyKnife_OLED128x64Rev07_2024.bin
    [4] ESP_SwissArmyKnife_NoScreenRev07_2024._patched.bin
    [5] ESP_SwissArmyKnife_Rev07_2024_update.bin
    [6] ESP_SwissArmyKnife_NoScreenRev07_2024_patched.bin
    Select .bin file[1-6]: 1
    Working on ESP_SwissArmyKnife_NoScreenRev07_2024.bin, let's begin to patch !
    Enter SSID:
    Enter Password:
    Enter Device Name:
    Enter Cloud User Name:
    Enter Device Credentials:

    Your IP appears to be: 90.101.106.251
    Accordingly you appear to be in: Sarrebourg
    Time zone offset is:  3600 seconds ahead of Greenwich
    Daylight saving offset is:  7200 seconds ahead of Greenwich
    Your latitude is: 48.7356
    Your longitude is: 7.0572
    Patch the ESP device with these values?(y), or manually enter values?(n)n
    Enter GMT offset in seconds ahead, or behind (-) Greenwich:3600
    Enter Daylight Saving offset in seconds ahead, or behind (-) Greenwich: 7200
    Please enter the device's latitude (-180...180): 45.456
    Please enter the device's longitude (-90...90: 6.4564

    Patched binary ESP_SwissArmyKnife_NoScreenRev07_2024_patched.bin saved
    Flashing it now to the ESP device on the first valid serial port? Y
    esptool.py v3.3
    Found 1 serial ports
    Serial port /dev/cu.e-3456
    Connecting......................................
    Enjoy your ESP device on-line ! 
    Re-flash the ESP Over The Air?(OTA, needs device IP )n

    Process finished 

The PythonPatcher is currently delivered in two versions:

The cloud-service-agnostic __PythonPatcher.py__
And an extended version __PythonPatcherTE.py__, specialized to be used with the cloud service   
https://thinger.io, wich can additionally personalize dashboard configuration files. 

Enjoy!

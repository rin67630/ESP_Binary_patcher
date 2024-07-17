# ESP_Binary_patcher
Patch user's credentials into ESP binaries

Following problem was to solve:  
Distributing an ESP32 or ESP8266 solution to tinker-flash ESP devices without requiring the user to compile a version with his own credentials.  
(this is not a solution for commercial devices distributed with a generic firmware that will be initialised by the customer)

I don't want to use the usual way of a temporary website to enter the credentials.  
That is a very clumsy solution requiring a lot of ESP-code and ESP program space (frequently more than the regular application, all the HTML code must be in program space)  
You need to stor the results into the NVRAM, and retrieve it on next boot, plus make the difference of both runtimes. The effort may be hiden in a library, but I know none, which includes the additional credentials of a cloud service.
Even for the user, it is not straight forward...

SmartConfig is a nice solution, but only provides SSID and Password, additionally credentials for a cloud service are missing too. 

A modern solution with a cloud service (MQTT, Thingspeak, Thinger.io etc...) require at least: 
* SSID, 
* WiFiPassword, 
* Device Name, 
* Cloud Account, 
* Device Credentials.

(the rest of the options and parameters can then be gathered from the cloud)

The solution is quite simple, elegant and requires practically no additional ESP code, no library and almost nothing to install on the user's side.
(excepted Python, which he needs anyway to upload the binary).

It is a Python script that patches the credentials into your compiled binary.
It works that way:

In your ESP code, you define placeholders for your credentials and make them long enough to potentially fit any user's content.

  `#define DEVICE_NAME             "DEVCNAME        "`   
  `#define WIFI_SSID               "WIFISSID        "`   
  `#define WIFI_PASS               "WIFIPASS                "`   
  `#define THINGER_USERNAME        "CLOUDNAM        "`    
  `#define DEVICE_CREDENTIALS      "DEVCCRED        "`   
These placeholders MUST match exactly those defined in the provided PythonPatcher.py Python script.  
Then you compile your code and distribute the raw binary together with the PythonPatcher.py script provided.
The user places the two files on his desktop and runs the PythonPatcher.py.
The script will ask for the file to patch, and the credentials and patch the binary accordingly, saving the patched file on the destop too:

%Run PythonPatcher.py

    Welcome to PythonPatcher for ESP devices 
    from RIN67630 @ https://github.com/rin67630/ESP_Binary_patcher 

    Please select a file from: 
    [1] ESP_SwissArmyKnife_Rev06_2024.bin
    Select .bin file[1-1]: 1
    working on ESP_SwissArmyKnife_Rev06_2024.bin, let's begin to patch !
    Enter SSID:GW-****  
    Enter Password:*******  
    Enter Device Name:Steroids  
    Enter Cloud User Name:Thing4  
    Enter Device Credentials:*******  
    File PythonTest_patched.bin saved  

Then it uploads the patched file to the ESP and you are online at your WiFI and in the cloud altogether !  
Could you imagine it easier?  

The PythonPatcher is currently delivered in two versions:

The cloud-service-agnostic __PythonPatcher.py__
And an extended version __PythonPatcherTE.py__, specialized to be used with the cloud service https://thinger.io, wich can additionally personalize dashboard configuration files. 

Enjoy!

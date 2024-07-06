# ESP_Binary_patcher
Patch user's credentials into ESP binaries

Following problem was to solve:  
Distributing an ESP32 or ESP8266 solution without requiring the user to compile a version with his own credentials.  

I don't want use the usual way of a temporary website to enter the credentials.  
That is a very clumsy solution requiring a lot of code and ESP program space (all the HTML code must be in program space)  
Even for the user it is not straight forward...

SmartConfig is a nice solution, but only provides SSID and Password, you need additionally credentials for a cloud usage. 

At least: 
* SSID, 
* WiFiPassword, 
* Device Name, 
* Cloud Account, 
* Device Credentials.

(the rest of the options and parameters can then be gathered from the cloud)

The solution is quite simple, elegant and requires practically no additional ESP code, no library and nothing to install on the user's side.
(excepted Python, which he needs anyway to upload the binary).

It is a Python script that patches the credentials into your compiled binary.
It works that way:

In your ESP code, you define placeholders for your credentials and make them long enough to potentially fit any user's content.
'''
  #define DEVICE_NAME             "DEVCNAME        "   
  #define WIFI_SSID               "WIFISSID        "   
  #define WIFI_PASS               "WIFIPASS                "  
  #define THINGER_USERNAME        "CLOUDNAM        "  
  #define DEVICE_CREDENTIALS      "DEVCCRED        "  
'''
These placeholders MUST match exactly those defined in the provided PythonPatcher.py Python script.  
Then you compile your code and distribute the raw binary together with the PythonPatcher.py script provided.
The user places the two files on his desktop and runs the PythonPatcher.py.
The script will ask for the file to patch, and the credentials and patch the binary accordingly, saving the patched file on the destop too:

%Run PythonPatcher.py

    Enter binfile to patch:PythonTest.bin  
    Enter SSID:GW-****  
    Enter Password:*******  
    Enter Device Name:Steroids  
    Enter Cloud User Name:Thing4  
    Enter Device Credentials:*******  
    File PythonTest_patched.bin saved  

Then you upload the patched file to the ESP with esptool.py and you are online at your WiFI and in the cloud altogether !  
Could you imagine it easier?  

Enjoy!

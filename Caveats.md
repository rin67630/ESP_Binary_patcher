# Users
This solution works well for ES8266 and ESP32 compiled code in the .bin format. (believe it or, not the binaries compiled have no checksum !)  
This solution is not suitable to distribute an ESP device including code like on commercial devices, the user must patch the binary and upload himself.  
On Windows systems you will need to get the Python interpreter for free at the Windows Store if it is not yet installed  
On current macOS systems Python3 is installed.  
The patchar can conveniently directly flash the patched file, but ***only if you have one ESP device connected to serial***. If you have several devices connected at the same time, you may ruin an innocent device!  

# ESP devices Programmers  
This is a very low footprint solution for ESP devices, practically no code is required, just use placeholder #defines for your credentials.  
It includes 3 credentials for a cloud solution. 
If you dont't need a cloud solution, you are probably better off with Espressif's SmartConfig.

You must take care to use the credentials only at one single place of your code. If you need them at several places, copy them to String-variables.  
In my example, the placeholders are 16 chars long, the placeholder for WiFI password is 24 chars long. That should be enough for most standard usages.  
You might use longer strings in your code and match them in the PythonPacher accordingly.  
You might also add more user parameters, just take example on one parameter and copy / adjust accordingly.  
Just take care to patch ***only Strings*** , not integers or floats. If you need values, convert in the ESP code.  
Personally I prefer to rely on a cloud service to define additional value parameters and read those values once on-line.  
That is much more flexible: you may adjust the parameters without flashing a new version.  

# Python experts 
I welcome any suggestion to improve the code, speciallay to make usage easier, more flexible or catch bugs.  
Feel free to file an issue or a pull request.  
But, please don't come with requests to "improve" the code to match typical Python experts' gibberish.  
It is written by a noob, linear, commented, to be immediately understood by noobs and to be easily modified by noobs without need to dig into 2344 pages of tutorials and best-of-breed techniques.  
I will always prefer a "plain language like" way to do things over obfuscated optimisation of my code.  
As long as it works: keep it simple and stupid.  

# Security experts
That solution is ***not secure*** for anyone having physical access to your ESP device.  
The credentials are patched without encryption, and are readable fo anyone knowing to use the guts of esptool.  
But it is not ***less secure*** than other ESP-based solutions.  

This solution works well for ES8266 and ESP32 compiled code in the .bin format. (believe it or, not the binaries compiled have no checksum !)
This solution is not suitable to distribute an ESP device including code like on commercial devices, the user must patch the binary and upload himself.

You must take care to use the credentials only at one place of your code (if you need it/them a several places, copy them to a String-variables).
In my example, the placeholders are 16 chars long, the placeholder for WiFI password is 24 chars long. That should fit most usages.
You might use longer strings in your code and match them in the PythonPacher.
You might also add more user parameters, just take example on one paramter and copy / adjust accordingly.

Please don't come with requests to "improve" the code to match typical Python experts' gibberish.
It is written by a noob, linear, commented, to be immediately understood by noobs and to be easily modified by noobs without need to dig into 2344 pages of tutorials and best-of-breed techniques.

As long as it works: keep it simple and stupid.


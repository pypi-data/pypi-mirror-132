
# BulBeewiPy
[![PyPI version](https://badge.fury.io/py/bulbeewipy.svg)](https://badge.fury.io/py/bulbeewipy)

Python library to control Beewi by Otio smart lights.
You can read and write this settings :
 - Brightness
 - White tone (Cold/Hot)
 - Color (R/G/B)
 - White/Color mode
## Methods explanation
*/!\ Each passed integer values must be in the range **[0,255]***
### turnOn()
Turn on the light
### turnOff()
Turn off the light
### setWhite()
Toggle light in White mode
### setColor(r:int, g:int, b:int)
Toggle light in Color mode and set the color in RGB
### setBrightness(brightness:int)
Set the brightness of the light (works in white and color mode)
### setWhiteWarm(warm:int)
Set the tone of the light if you want a cold or hot white. /!\ Only works in white mode

## Example
```python
    from  bulbeewipy  import BeewiSmartLight
    from  time  import  sleep
    b = BeewiSmartLight("D0:39:72:CC:AA:48")
    b.turnOn()
    sleep(8)
    b.turnOff()
 ```

## Thanks

 - [@IanHarvey](https://github.com/IanHarvey) for the [bluepy](https://github.com/IanHarvey/bluepy) library

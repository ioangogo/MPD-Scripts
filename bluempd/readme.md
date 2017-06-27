BlueMPD
===

This is a small hack of a script that uses ```python-evdev``` and ```python-mpd2``` to listen to keypresses from a bluetooth device and use that to control mpd

This program has all the keycodes that i could use with the amazon echo, this is play, pause, next and back. this is also aware of the state of MDP meaing it will toggle play and pausing in a some what correct way.

You will need to install python-evdev, the instructions can be found [here](https://python-evdev.readthedocs.io/en/latest/install.html) and python-mpd2 that can be installed by running ```pip install python-mpd2```

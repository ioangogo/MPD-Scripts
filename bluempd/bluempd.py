import evdev, time
from mpd import MPDClient
from evdev import InputDevice, categorize, ecodes
dev = InputDevice('/dev/input/event0')
print(dev)

client = MPDClient()
client.connect("localhost", 6600)
client.timeout = 10
print("Connected to the MPD Server")
client.idle


commandmap = {
163:client.next,
165:client.previous,
201:client.pause,
200:client.play
}


def mpdcontrol(code):
    client.noidle
    global playstate
    print(code.scancode)
    if code.keystate == 1:
      mpdcmd = commandmap[code.scancode]
      mpdcmd()
      time.sleep(4)
    client.idle

while True:
  client.ping()
  for event in dev.read_loop():
       if event.type == ecodes.EV_KEY:
            data = categorize(event)
            mpdcontrol(data)

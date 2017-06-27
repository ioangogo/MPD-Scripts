import evdev, time
from mpd import MPDClient
from evdev import InputDevice, categorize, ecodes
dev = InputDevice('/dev/input/event0')
print(dev)

client = MPDClient()
client.connect("localhost", 6600)

print("Connected to the MPD Server")

def getplaystate():
   state = client.status()['state']
   if state == "play":
      return False
   else:
      return True


commandmap = {
163:client.next,
165:client.previous,
201:client.pause,
200:client.play
}

playstate = getplaystate()

def mpdcontrol(code):
    global playstate
    if code.keystate == 1:
      if code.scancode == 200 or code.scancode == 201:
          mpdcmd = commandmap[201]
          int_play = int(bool(playstate))
          mpdcmd(int_play)
          playstate = getplaystate()
      mpdcmd = commandmap[code.scancode]
      mpdcmd()
      time.sleep(4)

while True:
  oldplay = playstate
  playstate = getplaystate()
  if playstate != oldplay: print("MPD is in the " + client.status()['state'] + " State")
  for event in dev.read_loop():
       if event.type == ecodes.EV_KEY:
            data = categorize(event)
            mpdcontrol(data)
#           print(data)

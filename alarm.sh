#!/bin/bash
server=""
vol=50
targetvol=70
streamvol=55
dovol(){
    until [ $vol = $targetvol ]; do
        mpc -q -h $server volume $vol
        sleep 0.5
        ((vol++))
    done
}

mpc -q -h $server stop
#Work arround for a hang in MPD that i cant find the source of that is caused by but is related to changing from a stream to annother file(on samba as this is the only sinarro i have tested). a buffer problem is my current theroy                                                                                                                                                             y stoping and clearing the playlist while playing a stream
sleep 5

mpc -q -h $server clear
# You will need to make a MPD playlist called Alarm for this to work
mpc -q -h $server load Alarm
mpc -q -h $server volume $vol
mpc -q -h $server play 1
dovol &

mpc -q -h $server current --wait

kill $!

mpc -q -h $server volume $streamvol

# py3status-pomodoro-timer
A [pomodoro](http://pomodorotechnique.com/) timer for [i3status](http://i3wm.org/i3status/manpage.html) using [py3status](https://github.com/ultrabug/py3status) 

## Installation
Firstly you need py3status configured for i3status. The process is descibed [here](https://github.com/ultrabug/py3status).
Copy the python script [pomodoro.py](https://raw.github.com/tjaartvdwalt/py3status-pomodoro-timer/master/pomodoro.py) to your py3status directory. (For me it is located at `~/.i3/i3status`)

Restart i3 (mod+q)

## What works
The timer counts down 25 minutes. When it reaches 0 it displays a notification to that effect using `notify-send`.

To start the countdown *left click* on the pomodoro module in the status bar.

To reset the time *right click* on the pomodoro module.

## Planned improvements
* Implement a *pause* feature.
* Currently the time only updates when i3status refreshes, for me thats every 5 seconds. For my clock I used a workaround  so that it counts every second (I have forgotten the exact details of how this works). I want to investigate if it is possible to use a similar solution for the pomodoro timer. 

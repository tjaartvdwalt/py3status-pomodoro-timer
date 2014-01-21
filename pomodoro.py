from os import system

class Py3status:
    def __init__(self):
        #pass
        self.c = CountDownTimer(1500)
        self.notified = False
    """
    Empty and basic py3status class.

    NOTE: py3status will NOT execute:
        - methods starting with '_'
        - methods decorated by @property and @staticmethod

    NOTE: reserved method names:
        - 'kill' method for py3status exit notification
        - 'on_click' method for click events from i3bar
    """
    def kill(self, i3status_output_json, i3status_config):
        pass

    def pomodoro(self, i3status_output_json, i3status_config):
        """
        This method will return an empty text message
        so it will NOT be displayed on your i3bar.

        If you want something displayed you should write something
        in the 'full_text' key of your response.

        See the i3bar protocol spec for more information:
        http://i3wm.org/docs/i3bar-protocol.html
        """
        if(self.c.get_time() == "0:00" and self.notified == False):
            system("notify-send --urgency=critical  pomodoro done!")
            self.notified = True
        
        # strip the newline and convert to utf-8
        response = {'full_text': "pomodoro " + str(self.c.get_time()), 'name': 'pomodoro', 'instance': 'first'}
        if (self.c.get_counter() > 900):
           response.update({'color': i3status_config['color_good']})
        elif (self.c.get_counter() > 300):
           response.update({'color': i3status_config['color_degraded']})
        else:
           response.update({'color': i3status_config['color_bad']})
            
        return (0, response)

    def on_click(self, json, i3status_config, event):
        """
        Enable/Disable DPMS on left click.
         """
        if event['button'] == 1:
            # if(self.c.is_running() == False):
            self.c.start()
            system("notify-send pomodoro started")
            # else:
            #     system("notify-send pomodoro paused")
        elif event['button'] == 3:
            self.c = CountDownTimer(1500)
            system("notify-send pomodoro reset")
            
                

#import subprocess
import time
import math
import threading
class Timer(threading.Thread):
    def __init__(self, seconds):
        self.running = False
        self.runTime = seconds
        self.counter = seconds
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(self.runTime)

class CountDownTimer(Timer):
    def run(self):
        self.running = True
        self.counter = self.runTime
        for sec in range(self.runTime):
            time.sleep(1.0)
            self.counter -= 1

    def get_counter(self):
        return self.counter

    def get_time(self):
        minutes = self.counter / 60
        seconds = self.counter % 60
        return str(math.floor(minutes)) + ":" + str(seconds).zfill(2)

        
    def is_running(self):
        return self.running

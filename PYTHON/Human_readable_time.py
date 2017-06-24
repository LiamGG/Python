# Human readable time
# 5 kyu

from math import floor

def make_readable(seconds):
    if seconds >= 3600:
        hours = floor((seconds/3600))
    else: 
        hours = 0
      
    seconds -= (int(hours)*3600)
    
    if seconds >= 60:
        minutes = floor((seconds/60))
    else:
        minutes = 0
    
    seconds -= (int(minutes)*60)
    
    seconds
    
    return "%02d:%02d:%02d" % (hours, minutes, seconds)

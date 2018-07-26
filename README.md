# shutdown_at
Shutdown computer at a specific time

Wrapper around the Windows shutdown command.
 
Usage:
```
shutdown_at.py 10:20  
shutdown_at.py 10:20:30  
shutdown_at.py 12
```
If the shutdown time is before the current time, shutdown time is assumed to be on the next day.

Sometimes I leave a stream running in the background and go to bed. This script helps me automatically shutdown my computer when the stream ends without me having to calculate the remaining time in seconds.

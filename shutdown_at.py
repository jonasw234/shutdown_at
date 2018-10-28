#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shutdown at

Wrapper around the Windows shutdown command.
Usage:
    shutdown_at.py 10:20
    shutdown_at.py 10:20:30
    shutdown_at.py 12
"""
from datetime import datetime
import os
import sys
import time


def main(argv):
    if len(argv) != 2:
        print('Usage: shutdown_at.py 10:20:30.')
        return 1
    try:
        shutdown_time = datetime.strptime(argv[1], '%H:%M:%S')
    except ValueError:
        try:
            shutdown_time = datetime.strptime(argv[1], '%H:%M')
        except ValueError:
            try:
                shutdown_time = datetime.strptime(argv[1], '%H')
            except ValueError:
                print('Usage: shutdown_at.py 10:20:30.')
                return 1
    now = datetime.now()
    shutdown_time = shutdown_time.replace(year=now.year, month=now.month, day=now.day)
    if shutdown_time < now:
        shutdown_time.replace(day=shutdown_time.day+1)
    difference = (shutdown_time - now).seconds
    os.system('powershell.exe -WindowStyle Hidden -Command "sleep {}; shutdown -s -f -t 0"'.format(difference))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

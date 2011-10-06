#!/usr/bin/env python

import gobject
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import zbar
import os

WEBCAM_DEVICE = '/dev/video0'
QR_TEXT = 'max'

def qr_handler(proc, image, closure):
    for symbol in image:
        if not symbol.count:
            if symbol.data == QR_TEXT:
                os.system('gnome-screensaver-command -d')
            else:
                proc.process_one()

def screensaver_handler(isScreenSaverActive):
    if isScreenSaverActive:
        proc = zbar.Processor()
        proc.parse_config('enable')
        device = WEBCAM_DEVICE
        proc.init(device)
        proc.set_data_handler(qr_handler)
        proc.process_one()

bus = dbus.SessionBus(mainloop=DBusGMainLoop())
screensaver_object = bus.get_object('org.gnome.ScreenSaver', '/org/gnome/ScreenSaver')
screensaver_interface = dbus.Interface(screensaver_object, 'org.gnome.ScreenSaver')
screensaver_interface.connect_to_signal('ActiveChanged', screensaver_handler)
loop = gobject.MainLoop()
loop.run()


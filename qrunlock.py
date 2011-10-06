#!/usr/bin/env python

import zbar
from sys import argv

# create a Processor
proc = zbar.Processor()

# configure the Processor
proc.parse_config('enable')

# initialize the Processor
device = '/dev/video0'
if len(argv) > 1:
    device = argv[1]
proc.init(device)

# setup a callback
def my_handler(proc, image, closure):
    # extract results
    for symbol in image:
        if not symbol.count:
            # do something useful with results
            print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
            sys.exit(0)

proc.set_data_handler(my_handler)

# enable the preview window
#proc.visible = True

# initiate scanning
#proc.active = True
proc.process_one()
#try:
#    proc.user_wait()
#except zbar.WindowClosed:
#    pass

'''
class SinpleThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sinple.app.run(host=settings.host, port=settings.port, debug=settings.debug)

def sinple_close(window):
    urllib.urlopen("http://%s:%s/shutdown" % (settings.host, settings.port))
    gtk.main_quit()

thread = SinpleThread()
thread.start()
thread.join()
'''


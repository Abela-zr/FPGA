from pynq.overlays.base import BaseOverlay
from pynq.lib import MicroblazeLibrary
import matplotlib.pyplot as plt
from imp import reload
from time import sleep
from sensehat import *

base = BaseOverlay('base.bit')
base.select_rpi()
lib = MicroblazeLibrary(base.RPI, ['i2c','xio_switch','circular_buffer'])

i2c = lib.i2c_open_device(1)
lib.set_pin(2, lib.SDA1)
lib.set_pin(3, lib.SCL1)


lps25h_sensor = lps25h.LPS25H_I2C(i2c)
hum_sensor = hts221.HTS221_I2C(i2c)
print('humidity (%rh): ({0:0.3f})'.format(hum_sensor))
tmp = lps25h_sensor.temperature
print('Temperature (℃"): ({0:0.3f})'.format(tmp))

i2c.close()
base.select_pmoda()


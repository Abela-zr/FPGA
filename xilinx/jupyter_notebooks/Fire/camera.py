from pynq import Overlay
from pynq.lib.iic import *
from ov5640_config import *
from pynq.lib.video import *
from time import sleep
import time
from PIL import Image
import IPython
import dma
import os
import shutil
cv_ov5640 = Overlay("cv_ov5640.bit")
iic = AxiIIC(cv_ov5640.ip_dict['axi_iic_0'])
address = 0x3c
length = 3
for config in ov5640_config:
    tmp1 = config[0] >> 8;
    tmp2 = config[0] & 0xff;
    iic.send(address, bytes([tmp1, tmp2, config[1]]), length)
    
bayer2rgb = cv_ov5640.v_demosaic_0
bayer2rgb.write(0x10, 1280)
bayer2rgb.write(0x18, 720)
bayer2rgb.write(0x28, 1)
bayer2rgb.write(0x00, 0x81)



switch0 = cv_ov5640.image_processing.axis_interconnect_0.xbar
switch1 = cv_ov5640.image_processing.axis_interconnect_1.xbar

def switch_stream(switch0, switch1, Index):
    MaxIndex = 5
    switch0.write(0x00, ~0x02)
    for i in range(0,MaxIndex + 1):
        switch0.write(0x40 + 4*Index, 0x80000000)
    switch0.write(0x40 + 4*Index, 0)
    switch0.write(0x00, 0x02)

    switch1.write(0x00, ~0x02)
    for i in range(0,MaxIndex + 1):
        switch0.write(0x40 + 4*Index, 0x80000000)
    switch1.write(0x40 + 4*0, Index)
    switch1.write(0x00, 0x02)
    
switch_stream(switch0, switch1, 0)
vdma0 = cv_ov5640.axi_vdma_0
vdma1 = cv_ov5640.axi_vdma_1

vdma0.writechannel.mode = VideoMode(1280, 720, 24)
vdma1.readchannel.mode = vdma0.writechannel.mode
vdma0.readchannel.mode = vdma0.writechannel.mode
vdma1.writechannel.mode = vdma0.writechannel.mode
vdma0.readchannel.tie(vdma0.writechannel)
vdma1.readchannel.tie(vdma1.writechannel)
vdma0.writechannel.start()
vdma0.readchannel.start()
vdma1.writechannel.start()
vdma1.readchannel.start()
i=0
while True:
    while True:
        frame = vdma0.readchannel.readframe()
        if(frame.max() != 0):
            break;


    image = Image.fromarray(frame)
    g, b, r = image.split()
    image = Image.merge('RGB', [r,g,b])
    image.save("./images/image_"+str(i)+".jpg")
    time.sleep(10)
    i+=1
    if i == 5:
        break

vdma0.writechannel.stop()
vdma0.readchannel.stop()
vdma1.writechannel.stop()
vdma1.readchannel.stop()
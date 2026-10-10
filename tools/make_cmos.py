# SPDX-License-Identifier: GPL-2.0-or-later
"""Generate a local linear RGGB input from synthetic bars or the user's image."""
import argparse
from pathlib import Path
import struct
import numpy as np
from PIL import Image

def generate(width=640,height=480,image=None):
    if width%2 or height%2 or not 2<=width<=8192 or not 2<=height<=8192 or width*height>16*1024*1024:
        raise ValueError('Even dimensions, at most 8192 per axis and 16 million samples required')
    if image:
        with Image.open(image) as im:rgb=np.asarray(im.convert('RGB').resize((width,height),Image.Resampling.LANCZOS),dtype=np.float64)/255
    else:
        bars=np.array([[1,1,1],[1,1,0],[0,1,1],[0,1,0],[1,0,1],[1,0,0],[0,0,1],[0,0,0]],dtype=np.float64)
        rgb=np.broadcast_to(bars[np.arange(width)*8//width],(height,width,3)).copy()
        rgb*=np.linspace(.25,1,height)[:,None,None]
    linear=np.where(rgb<=.04045,rgb/12.92,((rgb+.055)/1.055)**2.4)
    raw=np.empty((height,width),dtype='<u2')
    for y,x,ch in ((0,0,0),(0,1,1),(1,0,1),(1,1,2)):
        raw[y::2,x::2]=np.rint(linear[y::2,x::2,ch]*4095).astype('<u2')
    return struct.pack('<8s6I',b'NZ9RAW1\0',width,height,12,0,0,4095)+raw.tobytes()

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--image',type=Path)
    p.add_argument('--width',type=int,default=640);p.add_argument('--height',type=int,default=480)
    p.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[1]/'.local/input.raw')
    a=p.parse_args();data=generate(a.width,a.height,a.image)
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_bytes(data)
    print(a.output)

if __name__=='__main__':main()

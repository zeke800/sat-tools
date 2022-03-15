"""
PROBA-1 image SWAP image colorizer
"""
from PIL import Image,ImageEnhance
import sys
args1 = list(sys.argv)
args = []
pixconv = 0

args.append(args1[1])
args.append(args1[2])
args.append(args1[3])
i = Image.open(args[0]).convert('L')
if args[2] == "y":
    lut = Image.open("lut2.png")
else:
    lut = Image.open("lut.png")

pixunconv = i.load()
xsize,ysize = i.size
outimg = Image.new('RGB', (xsize, ysize))
lutpix = lut.load()
#print(xsize,ysize)
for y in range(ysize):
    for x in range(xsize):
        #value = 2**int(args[2])/2**int(args[3])
        pixconv = pixunconv[x,y]#/value
        #print(pixunconv[x,y])
        colorpix = lutpix[pixconv,0]
        outimg.putpixel((x,y),colorpix)
        #print("USING PIX "+str(pixconv))
        
        #outimg.putpixel((x,y),pixelslut[pixels2[x,y],pixels13[x,y]])


outimg = ImageEnhance.Contrast(outimg).enhance(1.2)
outimg.save(args[1])

from PIL import Image,ImageOps,ImageEnhance
#import numpy as np
#import itertools
import sys
args1 = list(sys.argv)
args = []

args.append(args1[1])
args.append(args1[2])
args.append(args1[3])
args.append(args1[4])
ch2 = Image.open(args[0]).convert('L')
ch13 = Image.open(args[1]).convert('L')
#ch2 = ImageEnhance.Contrast(ch2).enhance(3)
#ch13 = ImageEnhance.Contrast(ch13).enhance(2)
lut = Image.open(args[2])
lut = ImageOps.flip(lut)
#Histogram equalisation
xsize,ysize = ch2.size
"""
freq = [0] * 256  # fill
cProbability = [0] * 256  # fill zeros
freq = ch2.histogram()
a = np.array(ch2)
prevSum = 0
width,height = ch2.size
totalPixels = width* height
for i in range(256):
    prevSum += freq[i]*1.0/totalPixels # add the probablity to calculate 
    cProbability[i] = prevSum
    
print(cProbability[255]) 
"""
#ch2 = ImageEnhance.Color(ch2).enhance(0.5)
#Load all pixels for H.E. to continue
pixels2 = ch2.load()
pixels13 = ch13.load()
pixelslut = lut.load()
"""
for x, y in itertools.product(range(xsize), range(ysize)):
    pixels2[x,y] = int((255 * cProbability[pixels2[x,y]])) # (L-1) * cummulative probability
"""
#Now, process the LUT

outimg = Image.new('RGB', (xsize, ysize))
#print(xsize,ysize)
for y in range(ysize):
    for x in range(xsize):
        outimg.putpixel((x,y),pixelslut[pixels13[x,y],pixels2[x,y]])
        #outimg.putpixel((x,y),pixelslut[pixels2[x,y],pixels13[x,y]])

#outimg = ImageEnhance.Color(outimg).enhance(0.5)
outimg.save(args[3]) #Save the image :)

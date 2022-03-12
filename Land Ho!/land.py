from PIL import Image,ImageOps,ImageEnhance
import sys
args1 = list(sys.argv)
args = []

args.append(args1[1])
args.append(args1[2])
ch1 = Image.open(args[0])
ch1.show()
pixels = ch1.load()
xsize,ysize = ch1.size

pix = xsize*ysize
outimg = Image.new('RGB', (xsize, ysize))
for y in range(ysize):
    for x in range(xsize):
        if pixels[x,y] >= 126:
            outimg.putpixel((x,y),(0,0,255))
        else:
            
            outimg.putpixel((x,y),(0,255,0))
outimg.show()
        

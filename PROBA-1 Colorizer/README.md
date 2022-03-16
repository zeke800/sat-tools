This script colors PROBA-1 SWAP images. Usage:

``` shell
python probacolorizer.py sunin.png sunout.png -3
```
for the 'realistic' mode, 
``` shell
python probacolorizer.py sunin.png sunout.png -2
```
for the regular mode, and 
``` shell
python probacolorizer.py sunin.png sunout.png -1
```
for the other LUT. 

**The script requires PIL to be installed.**

Example input:

![thumbnail](https://raw.githubusercontent.com/zeke800/sat-tools/main/PROBA-1%20Colorizer/sun.png?raw=true)

Example output with the -1 flag:

![thumbnail](https://raw.githubusercontent.com/zeke800/sat-tools/main/PROBA-1%20Colorizer/sunout1.png?raw=true)

And a comparison of NASA's SOHO data - original vs recovered

![thumbnail](https://raw.githubusercontent.com/zeke800/sat-tools/main/PROBA-1%20Colorizer/comparison.png?raw=true)


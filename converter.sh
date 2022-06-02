#!/bin/bash

for f in plots/PLOT*.png
do
    convert -trim $f $f
    magick $f -crop 2x1@ +repage tmp.png
    montage -tile 1x2 -mode concatenate tmp*.png tiled_$f
    rm tmp*.png
done

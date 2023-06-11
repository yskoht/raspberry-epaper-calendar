#!/bin/sh

# dir
t=tmp
pic=/pic
calendar=${pic}/calendar

# font
font=DejaVu-Sans-Mono
fontsize=45

# size
size=640x400

# e-paper
device=epd4in01f
epaper=/home/pi/.local/bin/epaper

mkdir -p $t ${calendar}
/usr/bin/python cal.py

convert -background none -fill '#000000' -font ${font} -pointsize ${fontsize} label:"@$t/base.txt"  $t/_base.png
convert -background none -fill '#00FF00' -font ${font} -pointsize ${fontsize} label:"@$t/today.txt" $t/_today.png
convert -background none -fill '#FF0000' -font ${font} -pointsize ${fontsize} label:"@$t/sun.txt"   $t/_sun.png
convert -background none -fill '#0000FF' -font ${font} -pointsize ${fontsize} label:"@$t/sat.txt"   $t/_sat.png

composite \
  -compose over \
  $t/_today.png \
  $t/_sun.png \
  $t/_a.png

composite \
  -compose over \
  $t/_a.png \
  $t/_sat.png \
  $t/_b.png

composite \
  -compose over \
  $t/_b.png \
  $t/_base.png \
  $t/_img.png

convert $t/_img.png -gravity center -background white -extent ${size} $t/img.png
convert $t/img.png +dither -map palette.png ${calendar}/img.png

${epaper} print --verbose -d ${device} ${calendar}
rm -rf $t

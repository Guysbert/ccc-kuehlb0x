rrdtool graph temp8h.png \
  -s 'now - 8 hours' -e 'now' \
  DEF:temp0=temperature.rrd:outer:AVERAGE \
  LINE2:temp0#00FF00:OutsideTemp \
  DEF:temp1=temperature.rrd:cooler:AVERAGE \
  LINE2:temp1#0000FF:CoolerTemp \
  DEF:temp2=temperature.rrd:shadow:AVERAGE \
  LINE2:temp2#FF0000:ShadowTemp
rrdtool graph temp1h.png \
  -s 'now - 1 hours' -e 'now' \
  DEF:temp0=temperature.rrd:outer:AVERAGE \
  LINE2:temp0#00FF00:OutsideTemp \
  DEF:temp1=temperature.rrd:cooler:AVERAGE \
  LINE2:temp1#0000FF:CoolerTemp \
  DEF:temp2=temperature.rrd:shadow:AVERAGE \
  LINE2:temp2#FF0000:ShadowTemp
cp temp8h.png /usr/share/nginx/www/8h.png
cp temp1h.png /usr/share/nginx/www/1h.png

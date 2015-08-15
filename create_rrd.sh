rrdtool create temperature.rrd --step 60 \\ 
DS:outer:GAUGE:1200:-40:80 \\
DS:cooler:GAUGE:1200:-40:80 \\ 
DS:shadow:GAUGE:1200:-40:80 \\ 
RRA:AVERAGE:0.5:1:9600 \\
RRA:MIN:0.5:96:36000 \\
RRA:MAX:0.5:96:36000 \\
RRA:AVERAGE:0.5:96:36000
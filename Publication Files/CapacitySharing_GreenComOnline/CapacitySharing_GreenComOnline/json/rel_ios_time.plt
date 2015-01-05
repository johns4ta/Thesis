set term postscr enh "Helvetica" 22
set grid

set xlabel "Time [s]"
set xrange[*:270000]

set ylabel "Savings [%]"
set yrange [*:*]

set key bottom left

set output "rel_ios_time.eps"
plot "rel_ios_time.dat" u 1:4 w l lw 2 t "Items",\
"rel_ios_time.dat" u 1:6 w l lw 2 t "Size",\
"rel_ios_time.dat" u 1:13 w l lw 2 t "Bluetooth",\
"rel_ios_time.dat" u 1:12 w l lw 2 t "WLAN"

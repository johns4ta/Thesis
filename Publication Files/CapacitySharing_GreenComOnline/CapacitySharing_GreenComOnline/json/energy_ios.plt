set term postscr enh "Helvetica" 22
set grid

set xlabel "Time [s]"
set xrange[*:270000]

set ylabel "Energy [J]"
set yrange [*:*]

set key at 200000,11

set output "energy_ios_time.eps"
plot "energy_ios_time.dat" u 1:4 w l lw 2 t "Cellular",\
"energy_ios_time.dat" u 1:3 w l lw 2 t "Bluetooth",\
"energy_ios_time.dat" u 1:2 w l lw 2 t "WLAN"



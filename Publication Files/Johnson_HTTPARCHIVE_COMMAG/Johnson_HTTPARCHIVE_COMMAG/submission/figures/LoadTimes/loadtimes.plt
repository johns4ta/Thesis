set term postscr enh  "Helvetica" 24
set grid

set xlabel "Year"

set ylabel "Est. download time [s]"

set key top left

set output "loadtimes.eps"
plot "loadtimes.dat" u 1:8 w lp t "Global handsets",\
"loadtimes.dat" u 1:($9) w lp t "Global smartphone",\
"loadtimes.dat" u 1:($10) w lp t "Global tablet",\
"loadtimes.dat" u 1:($11) w lp t "North America"

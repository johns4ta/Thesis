set term postscr enh color "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Time (in seconds)"
set ylabel "Proportion of respSize bytes left"

set xrange[*:86400]

set xtics 14400
set yrange[*:]
#set key top left

set output "mobile_total_bytes_over_time.eps"
plot "mobile_total_bytes_over_time.csv" using 1:2 with line title ""

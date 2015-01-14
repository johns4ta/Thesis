set term postscr enh color "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Time (in seconds)"
set ylabel "Proportion of respSize bytes left"
set title "Proportion of respSize bytes remaining"

set xrange[60:600]
set yrange[*:]

set output "mobile_total_bytes_over_time_600.eps"
plot "mobile_total_bytes_over_time.csv" using 1:2 with line title ""

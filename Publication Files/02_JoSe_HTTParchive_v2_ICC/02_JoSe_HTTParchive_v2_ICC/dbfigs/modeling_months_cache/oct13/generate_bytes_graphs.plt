set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Time [s]"
set ylabel "Relative amount of expired data"
#set title "Proportion of bytes expired over 1 week"

set xrange[*:604800]
set yrange[.5:1]
set key top left

set logscale x
set output "mobile_bytes_graphs.eps"
plot "results.csv" u 1:2 w l t  "Sim Data",\
	"mobile_total_bytes_over_time.csv" u 1:3 w l t  "Actual Data"
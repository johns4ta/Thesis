set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Time[s]"
set ylabel "Average proportion of data"

set xtics 14400
set xrange[0:86400]
set yrange[*:]

set output "bytes_over_24_hours.eps"
plot "graphing_info_596.csv" using 1:2 with line title "Average",\
	 "graphing_info_596.csv" using 1:7 with line title "95% CI",\
	 "graphing_info_596.csv" using 1:6 with line title "",\
	"graphing_info_596.csv" using 1:4 with line title "Std Dev"
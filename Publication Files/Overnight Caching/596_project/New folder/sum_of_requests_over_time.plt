set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Time[s]"
set ylabel "Average proportion of objects"

set xtics 14400
set xrange[*:86400]
set yrange[*:]

set output "requests_over_24_hours.eps"
plot "graphing_info_596.csv" using 1:3 with line title "Average",\
	 "graphing_info_596.csv" using 1:9 with line title "95% CI",\
	 "graphing_info_596.csv" using 1:8 with line title "",\
		"graphing_info_596.csv" using 1:5 with line title "Std Dev"
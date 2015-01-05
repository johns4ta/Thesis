set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Time (in seconds)"
set ylabel "Proportion"
set title "Proportion of requests left that can be shared"

#Set x axis max to one week (in seconds)
set xrange[*:604800]
set yrange[*:]

set output "Sum_of_requests_over_time.eps"
plot "proportions.csv" using 1:3 with line title "Average",\
	 "proportions.csv" using 1:9 with line title "Lower CI",\
	 "proportions.csv" using 1:8 with line title "Upper CI",\
		"proportions.csv" using 1:5 with line title "Standard deviation"
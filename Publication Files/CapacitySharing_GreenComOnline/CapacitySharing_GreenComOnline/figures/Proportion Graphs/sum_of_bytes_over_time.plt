set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Time (in seconds)"
set ylabel "Proportion"
set title "Proportion of bytes still left in cache that are shareable"

#Set x axis max to one week (in seconds)
set xrange[*:604800]
set yrange[*:]

set output "Sum_of_bytes_over_time.eps"
plot "proportions.csv" using 1:2 with line title "Average",\
	 "proportions.csv" using 1:7 with line title "Lower CI",\
	 "proportions.csv" using 1:6 with line title "Upper CI",\
	"proportions.csv" using 1:4 with line title "Standard Deviation",\
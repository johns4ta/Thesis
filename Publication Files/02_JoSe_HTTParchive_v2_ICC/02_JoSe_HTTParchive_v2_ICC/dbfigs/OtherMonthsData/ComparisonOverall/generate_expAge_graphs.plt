set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Expiration time t_o [s]"
set ylabel "Cumulative probability"
#set title "Overall ExpAges"

set xrange[*:604800]

set logscale y
set yrange[*:*]

set key top right


set output "overall_expAges_comparison.eps"
plot "expAge_comparisions.csv" u 1:2 w l  t "June 15, 2013", \
	"expAge_comparisions.csv" u 1:3 w l  t "October 15, 2013", \
	"expAge_comparisions.csv" u 1:4 w l  t "March 15, 2014"

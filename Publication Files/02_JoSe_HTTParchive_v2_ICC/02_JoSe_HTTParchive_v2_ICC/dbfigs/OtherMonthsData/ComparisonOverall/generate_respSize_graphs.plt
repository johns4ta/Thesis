set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Object size x_o [kb]"
set ylabel "Proportion p(x_o)"
#set title "Overall Response Sizes"

set xrange[*:*]
set yrange[*:50]
set key top left


set output "overall_respSize_comparison.eps"
plot "respSize_comparisions.csv" u 1/1000:2 w l t "June 15, 2013", \
	"respSize_comparisions.csv" u 1/1000:3 w l t "October 15, 2013", \
	"respSize_comparisions.csv" u 1/1000:4 w l t "March 15, 2014"

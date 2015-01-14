set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Average page object expiration time [s]"
set ylabel "Proportion"
#set title "Average Page Level ExpAges"

set xrange[*:604800]
set logscale y
set yrange[*:*]
set key top right


set output "page_level_expAges_comparison.eps"
plot "page_level_expAges_comparisons.csv" u 1:2 w l t "June 15, 2013", \
	"page_level_expAges_comparisons.csv" u 1:3 w l t "October 15, 2013", \
	"page_level_expAges_comparisons.csv" u 1:4 w l t "March 15, 2014"

set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Average  page object size [kb]"
set ylabel "Proportion"
#set title "Average Page Level RespSizes"

set xrange[*:100]

set logscale y
set yrange[*:*]
set key top right


set output "page_level_respSizes_comparison.eps"
plot "page_level_respSizes_comparisons.csv" u 1/1000:2 w l t "June 15, 2013", \
	"page_level_respSizes_comparisons.csv" u 1/1000:3 w l t "October 15, 2013", \
	"page_level_respSizes_comparisons.csv" u 1/1000:4 w l t "March 15, 2014"

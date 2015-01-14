set datafile separator "|"
set term postscr enh "Helvetica" 24
set grid

set xrange[0:604800]
set yrange[0:*]

set ylabel "Response size [kb]"
set xlabel "Expiration age [s]"

set output "overall_2d_scatterplot_respSizes_expAges.eps"
#set title "RespSize/ExpAge Scatterplot"
plot "oct_15_2013_respSizes_expAges.txt" u 2:($1/1000) t ""

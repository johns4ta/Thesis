set datafile separator ","
set term postscr enh "Helvetica" 24
set grid

set xrange[0:*]
set yrange[0:*]

set xlabel "Response Size [kb]"
set ylabel "Expiration Age [s]"

set output "page_level_2d_scatterplot_respSizes_expAges.eps"
set title "RespSize vs ExpAge Scatterplot"
plot "oct_15_2013_page_level_averages.txt" u ($1/1000):2 t ""

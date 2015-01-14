set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Average page object expiration time ~t{.5-}_{o(p)} [s]"
set ylabel "Proportion p(~t{.5-}_{o(p)})"
# set title "Average expAges for Mobile Landing Pages"

set xrange[*:604800]
set xtics 3600*48

set logscale y
set yrange[*:*]
set key at 600000,0.075

set output "page_level_average_expAges.eps"
plot "actual_page_level_results.csv" u 1:2 w l t  "Actual Data",\
"sim_page_level_results.csv" u 1:2 w l t  "Sim Data", \
	"sim_page_level_results.csv" u 1:($3-$4)/$2 w l t  "Rel. CI"
	#	"sim_page_level_results.csv" u 1:3 w l t  "Upper CI Data", \
#	"sim_page_level_results.csv" u 1:4 w l t  "Lower CI Data", \

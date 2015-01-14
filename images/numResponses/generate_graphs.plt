set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Number of objects per page n_{o(p)}"
set ylabel "Proportion p(n_{o(p)})"
#set title "Average number of Responses for Mobile Landing Pages"

set xrange[*:*]
set yrange[*:*]
set key top right

set output "numResponses.eps"

plot "numResponses_actual_results.csv" u 1:3 w lp t "Actual Data",\
	"numResps_sim_results.csv" u 1:2 w lp t "Sim Data",\
"numResps_sim_results.csv" u 1:($3-$4)/$2 w l t "Rel. CI"
#		"numResps_sim_results.csv" u 1:3 w lp t "Upper CI Data", \
#	"numResps_sim_results.csv" u 1:4 w lp t "Lower CI Data"

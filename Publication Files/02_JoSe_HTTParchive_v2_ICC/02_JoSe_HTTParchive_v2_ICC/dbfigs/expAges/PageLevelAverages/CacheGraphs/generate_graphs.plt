set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Expiration age [s]"
set ylabel "Cumulative probability"
#set title "Proportion of requests expired over a period of one week"

set xrange[*:*]

set yrange[*:*]

set key top left

set logscale x
set output "mobile_request_graphs.eps"
plot "mobile_cpd.csv" u 1:2 w l t  "Actual Data",\
"sim_results.csv" u 1:2 w l t  "Sim Data"
#"sim_results.csv" u 1:($4-$3)/$2 w l t  "Rel. CI"
#	"sim_results.csv" u 1:3 w l t  "Lower CI Data", \
#	"sim_results.csv" u 1:4 w l t  "Upper CI Data", \
	

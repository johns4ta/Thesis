set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set key top right

set xlabel "Object size x_o [kb]"
set ylabel "Proportion p(x_o)"
#set title "Overall Response Sizes"

set xrange[*:100]
set yrange[*:*]

set output "overall_respSizes.eps"
plot "overall_actual_respSizes.csv" u 1/1000:2 w l t "Actual Data", \
"overall_results_sim_respSizes.csv" u 1/1000:2 w l t "Sim Data",\
"overall_results_sim_respSizes.csv" u 1/1000:($3-$4)/$2 w l t "Rel. CI"
#	"overall_results_sim_respSizes.csv" u 1/1000:4 w l t "Lower CI",\
#	"overall_results_sim_respSizes.csv" u 1/1000:3 w l t "Upper CI", \
set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Average Response Size [kb]"
set ylabel "Proportion"
set title "Page Level Response Sizes"

set xrange[*:100]
set yrange[*:0.12]
set key top left


set output "page_level_respSizes.eps"
plot "page_level_results_actual_respSizes.csv" u 1:2 w l t "Actual Data", \
"page_level_results_sim_respSizes.csv" u 1/1000:2 w l t "Sim Data", \
"page_level_results_sim_respSizes.csv" u 1/1000:3 w l t "Upper CI", \
"page_level_results_sim_respSizes.csv" u 1/1000:4 w l t "Lower CI"

set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Page size x_{p} [Byte]"
set ylabel "Proportion p(x_{p})"
#set title "Sum of Page Response Sizes"

set xrange[*:4000000]
set xtics 1000000

set yrange[*:*]
set key top left

set output "page_level_sum_respSizes.eps"
plot "page_level_actual_results_total_respSizes.csv" u 1:2 w l t "Actual Data", \
"page_level_sim_results_total_respSizes.csv" u 1:2 w l t "Sim Data", \
"page_level_sim_results_total_respSizes.csv" u 1:($3-$4)/$2 w l t "Rel. CI"
#"page_level_sim_results_total_respSizes.csv" u 1:3 w l t "Upper CI", \
#"page_level_sim_results_total_respSizes.csv" u 1:4 w l t "Lower CI"

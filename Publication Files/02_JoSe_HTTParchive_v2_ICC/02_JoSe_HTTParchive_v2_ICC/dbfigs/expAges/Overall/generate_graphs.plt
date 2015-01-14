set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Expiration time t_o [s]"
set ylabel "Proportion p(t_o)"
#set title "Overall expAges for Mobile Landing Pages"

set xrange[*:604800]
set xtics 3600*48

set logscale y
set yrange[*:*]

set key top left

#set logscale x
set output "overall_expAges.eps"
plot "overall_expAges_results.csv" u 1:3 w l t  "Actual Data",\
"overall_expAges_sim_results.csv" u 1:2 w l t  "Sim Data" , \
"overall_expAges_sim_results.csv" u 1:($3-$4)/$2 w l t  "Rel. CI" 
#"overall_expAges_sim_results.csv" u 1:3 w l t  "Upper CI Data", \
#"overall_expAges_sim_results.csv" u 1:4 w l t  "Lower CI Data", \


set datafile separator ","
set term postscr enh "Helvetica" 24
set grid

set xrange[0:*]
set yrange[0:*]
set zrange[0:*]

set xlabel "RespSize [kb]"
set ylabel "ExpAge [s]"
set zlabel "Number of Responses"

set output "overall_3d_scatterplot.eps"
set title "RespSize vs ExpAge vs Number of Responses"
splot "oct_15_2013_overall_data.txt" u ($1/1000):2:3 t ""

set datafile separator ","
set term postscr enh "Helvetica" 24
set grid

set xrange[0:100]
set yrange[*:604800*3/7]
set zrange[0:100]

set zlabel "Average object size [kb]" 
set ylabel "Average expiration age [s]" 
set xlabel "Number of objects" offset 3,0,0 rotate by 10

set ticslevel 0
set view 60,60

set output "page_level_3d_scatterplot.eps"
#set title "RespSize vs ExpAge vs Number of Responses"
splot "oct_15_2013_page_level_averages.txt" u 3:2:($1/1000) t ""

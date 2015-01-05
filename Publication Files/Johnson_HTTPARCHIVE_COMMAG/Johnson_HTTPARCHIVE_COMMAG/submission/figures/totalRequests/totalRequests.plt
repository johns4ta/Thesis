set term postscr enh "Helvetica" 24

set grid

set xlabel "Measurement date"
set xdata time
set xmtics
set timefmt "%Y-%m-%dT%H:%M:%S"
set xrange ["2011-06-011T00:00:00":"2013-07-15T00:00:00"]
set xtics 20736000
set style line 1 lt 1 lw 3 pt 3 linecolor rgb "black"
set ylabel "Total requests"

set key top left

set output "totalRequests.eps"
plot "totalRequests.dat" u 1:2 w lp t "Fixed" lt rgb "black",\
"totalRequests.dat" u 1:($3) w lp t "Mobile" lt rgb "black"

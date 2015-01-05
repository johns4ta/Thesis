set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Measurement date"
set xdata time
set xmtics
set timefmt "%Y-%m-%dT%H:%M:%S"
set xrange ["2011-06-011T00:00:00":"2013-07-15T00:00:00"]
set xtics 20736000

set ylabel "Average data per request [kB]"

set key top left

set output "bpr.eps"
plot "overview-f.csv" u 1:($46/$22)/1000 w lp t "Desktop",\
"overview-m.csv" u 1:($46/$22)/1000 w lp t "Mobile"

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

set key bottom right

set output "bpr_by_type_mobile.eps"
plot "overview-m.csv" u 1:($108/1000) w lp t "JS" lt rgb "black",\
"overview-m.csv" u 1:($107/1000) w lp t "HTML" lt rgb "black",\
"overview-m.csv" u 1:($109/1000) w lp t "CSS" lt rgb "black",\
"overview-m.csv" u 1:($110/1000) w lp t "Images" lt rgb "black",\
"overview-m.csv" u 1:($111/1000) w lp t "Other" lt rgb "black"
set term postscr enh "Helvetica" 24

set grid
set datafile separator ","

set xlabel "Measurement date"
set xdata time
set xmtics
set timefmt "%Y-%m-%dT%H:%M:%S"
set xrange ["2011-06-011T00:00:00":"2013-07-15T00:00:00"]
set xtics 20736000

set ylabel "Number of requests"

set key at "2013-06-011T00:00:00", 50
set output "req_by_type_fixed.eps"
plot "overview-f.csv" u 1:($30) w lp t "Images" lt rgb "black",\
"overview-f.csv" u 1:($26) w lp t "JS" lt rgb "black",\
"overview-f.csv" u 1:($24) w lp t "HTML" lt rgb "black",\
"overview-f.csv" u 1:($38+$40+$42+$44) w lp t "Other" lt rgb "black",\
"overview-f.csv" u 1:($28) w lp t "CSS" lt rgb "black"

set key at "2013-06-011T00:00:00", 30
set output "req_by_type_mobile.eps"
plot "overview-m.csv" u 1:($30) w lp t "Images" lt rgb "black",\
"overview-m.csv" u 1:($26) w lp t "JS" lt rgb "black",\
"overview-m.csv" u 1:($24) w lp t "HTML" lt rgb "black",\
"overview-m.csv" u 1:($28) w lp t "CSS" lt rgb "black",\
"overview-m.csv" u 1:($38+$40+$42+$44) w lp t "Other" lt rgb "black"


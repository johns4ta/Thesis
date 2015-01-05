set term postscr enh "Helvetica" 24

set grid
set datafile separator ","

set xlabel "Measurement date"
set xdata time
set xmtics
set timefmt "%Y-%m-%dT%H:%M:%S"
set xrange ["2011-06-011T00:00:00":"2013-07-15T00:00:00"]
set xtics 20736000

set ylabel "Byte [kB]

set key top left
set output "bytes_by_type_fixed.eps"
plot "overview-f.csv" u 1:($54)/1000 w lp t "Images" lt rgb "black",\
"overview-f.csv" u 1:($62+$64+$66+$68)/1000 w lp t "Other" lt rgb "black",\
"overview-f.csv" u 1:($50)/1000 w lp t "JS" lt rgb "black",\
"overview-f.csv" u 1:($48)/1000 w lp t "HTML" lt rgb "black",\
"overview-f.csv" u 1:($52)/1000 w lp t "CSS" lt rgb "black"


set output "bytes_by_type_mobile.eps"
plot "overview-m.csv" u 1:($54)/1000 w lp t "Images" lt rgb "black",\
"overview-m.csv" u 1:($50)/1000 w lp t "JS" lt rgb "black",\
"overview-m.csv" u 1:($62+$64+$66+$68)/1000 w lp t "Other" lt rgb "black",\
"overview-m.csv" u 1:($48)/1000 w lp t "HTML" lt rgb "black",\
"overview-m.csv" u 1:($52)/1000 w lp t "CSS" lt rgb "black"
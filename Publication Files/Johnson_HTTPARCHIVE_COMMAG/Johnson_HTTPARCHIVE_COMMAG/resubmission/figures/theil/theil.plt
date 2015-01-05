set term postscr enh  "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Measurement date"
set xdata time
set xmtics
set timefmt "%Y-%m-%dT%H:%M:%S"
set xrange ["2011-06-011T00:00:00":"2013-12-15T00:00:00"]
set xtics 20736000

set ylabel "Theil entropy"

#set key top left
set key at "2013-11-011T00:00:00", 6

set output "theil_reqs.eps"
plot "theil_entropy_f.csv" u 1:12 w lp t "Fixed,all",\
"theil_entropy_cont_f.csv" u 1:12 w lp t "Fixed",\
"theil_entropy_m.csv" u 1:12 w lp t "Mobile,all",\
"theil_entropy_cont_m.csv" u 1:12 w lp t "Mobile"

set output "theil_bytes.eps"
plot "theil_entropy_f.csv" u 1:24 w lp t "Fixed,all",\
"theil_entropy_cont_f.csv" u 1:24 w lp t "Fixed",\
"theil_entropy_m.csv" u 1:24 w lp t "Mobile,all",\
"theil_entropy_cont_m.csv" u 1:24 w lp t "Mobile"

set term postscr enh "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Measurement date"
set xdata time
set xmtics
set timefmt "%Y-%m-%dT%H:%M:%S"
set xrange ["2011-06-011T00:00:00":"2013-12-15T00:00:00"]
set xtics 20736000

set ylabel "Total bytes [kB]"

set key top left

set output "bytes_total_all.eps"
plot "../overview_f_edited.csv" u 1:($46/1000) w lp t "Desktop,all",\
"../overview_contpages_f_edited.csv" u 1:($46/1000) w lp t "Desktop",\
"../overview_m_edited.csv" u 1:($46/1000) w lp t "Mobile,all",\
"../overview_contpages_m_edited.csv" u 1:($46/1000) w lp t "Mobile"

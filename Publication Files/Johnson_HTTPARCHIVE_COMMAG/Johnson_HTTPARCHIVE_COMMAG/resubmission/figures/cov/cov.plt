set term postscr enh  "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Measurement date"
set xdata time
set xmtics
set timefmt "%Y-%m-%dT%H:%M:%S"
set xrange ["2011-06-011T00:00:00":"2013-12-15T00:00:00"]
set xtics 20736000

set ylabel "Coefficient of Variation (CoV)"

set key top right

set output "cov_requests.eps"
plot "../overview_f_edited.csv" u 1:($23/$22) w lp t "Fixed,all",\
"../overview_contpages_f_edited.csv" u 1:($23/$22) w lp t "Fixed",\
"../overview_m_edited.csv" u 1:($23/$22) w lp t "Mobile,all",\
"../overview_contpages_m_edited.csv" u 1:($23/$22) w lp t "Mobile"

set output "cov_bytes.eps"
plot "../overview_f_edited.csv" u 1:($47/$46) w lp t "Fixed,all",\
"../overview_contpages_f_edited.csv" u 1:($47/$46) w lp t "Fixed",\
"../overview_m_edited.csv" u 1:($47/$46) w lp t "Mobile,all",\
"../overview_contpages_m_edited.csv" u 1:($47/$46) w lp t "Mobile"
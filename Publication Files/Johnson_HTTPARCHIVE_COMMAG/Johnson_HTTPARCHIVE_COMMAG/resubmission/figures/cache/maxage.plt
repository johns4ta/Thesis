set term postscr enh  "Helvetica" 24
set grid
set datafile separator ","

set xlabel "Measurement date"
set xdata time
set xmtics
set timefmt "%Y-%m-%dT%H:%M:%S"
set xrange ["2011-06-011T00:00:00":"2013-12-15T00:00:00"]

set xtics 20736000

set ylabel "Average number of objects"

set key at "2013-07-01T00:00:00",45

set output "cache_fix_all.eps"
plot "../overview_f_edited.csv" u 1:($88+$90) w lp t "Max. 0",\
"../overview_f_edited.csv" u 1:92 w lp t "Max. 1",\
"../overview_f_edited.csv" u 1:94 w lp t "Max. 30",\
"../overview_f_edited.csv" u 1:96 w lp t "Max. 365",\
"../overview_f_edited.csv" u 1:98 w lp t "Max. >365"

set output "cache_fix.eps"
plot "../overview_contpages_f_edited.csv" u 1:($88+$90) w lp t "Max. 0",\
"../overview_contpages_f_edited.csv" u 1:92 w lp t "Max. 1",\
"../overview_contpages_f_edited.csv" u 1:94 w lp t "Max. 30",\
"../overview_contpages_f_edited.csv" u 1:96 w lp t "Max. 365",\
"../overview_contpages_f_edited.csv" u 1:98 w lp t "Max. >365"

set key default
set key top left
set yrange [*:33]
set output "cache_mob_all.eps"
plot "../overview_m_edited.csv" u 1:($88+$90) w lp t "Max. 0",\
"../overview_m_edited.csv" u 1:92 w lp t "Max. 1",\
"../overview_m_edited.csv" u 1:94 w lp t "Max. 30",\
"../overview_m_edited.csv" u 1:96 w lp t "Max. 365",\
"../overview_m_edited.csv" u 1:98 w lp t "Max. >365"

set key default
set key top left
set yrange [*:*]
set output "cache_mob.eps"
plot "../overview_contpages_m_edited.csv" u 1:($88+$90) w lp t "Max. 0",\
"../overview_contpages_m_edited.csv" u 1:92 w lp t "Max. 1",\
"../overview_contpages_m_edited.csv" u 1:94 w lp t "Max. 30",\
"../overview_contpages_m_edited.csv" u 1:96 w lp t "Max. 365",\
"../overview_contpages_m_edited.csv" u 1:98 w lp t "Max. >365"
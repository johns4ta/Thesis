set term postscr enh "Helvetica" 24

set grid
set datafile separator ","

set xlabel "Measurement date"
set xdata time
set xmtics
set timefmt "%Y-%m-%dT%H:%M:%S"
set xrange ["2011-06-011T00:00:00":"2013-12-15T00:00:00"]
set xtics 20736000

set ylabel "Average data per request [kB]"
set key top left

set output "bpr_by_type_fixed_all.eps"
plot "../overview_f_edited.csv" u 1:($109/1000) w lp t "Other",\
"../overview_f_edited.csv" u 1:($106/1000) w lp t "JS",\
"../overview_f_edited.csv" u 1:($108/1000) w lp t "Images",\
"../overview_f_edited.csv" u 1:($105/1000) w lp t "HTML",\
"../overview_f_edited.csv" u 1:($107/1000) w lp t "CSS"

set yrange [*:75]
set output "bpr_by_type_fixed.eps"
plot "../overview_contpages_f_edited.csv" u 1:($109/1000) w lp t "Other",\
"../overview_contpages_f_edited.csv" u 1:($106/1000) w lp t "JS",\
"../overview_contpages_f_edited.csv" u 1:($108/1000) w lp t "Images",\
"../overview_contpages_f_edited.csv" u 1:($105/1000) w lp t "HTML",\
"../overview_contpages_f_edited.csv" u 1:($107/1000) w lp t "CSS"
set term postscr enh "Helvetica" 24

set grid
set datafile separator ","

set xlabel "Measurement date"
set xdata time
set xmtics
set timefmt "%Y-%m-%dT%H:%M:%S"
set xrange ["2011-06-011T00:00:00":"2013-12-15T00:00:00"]
set xtics 20736000

set ylabel "Number of requests"

set key at "2013-11-011T00:00:00", 50
set output "req_by_type_fixed_all.eps"
plot "../overview_f_edited.csv" u 1:($30) w lp lt 1 pt 1 t "Images",\
"../overview_f_edited.csv" u 1:($26) w lp t "JS",\
"../overview_f_edited.csv" u 1:($24) w lp t "HTML",\
"../overview_f_edited.csv" u 1:($38+$40+$42+$44) w lp t "Other",\
"../overview_f_edited.csv" u 1:($28) w lp t "CSS"

set key at "2013-11-011T00:00:00", 40
set output "req_by_type_fixed.eps"
plot "../overview_contpages_f_edited.csv" u 1:($30) w lp lt 1 pt 1 t "Images",\
"../overview_contpages_f_edited.csv" u 1:($26) w lp t "JS" lt rgb "black",\
"../overview_contpages_f_edited.csv" u 1:($24) w lp t "HTML" lt rgb "black",\
"../overview_contpages_f_edited.csv" u 1:($38+$40+$42+$44) w lp t "Other",\
"../overview_contpages_f_edited.csv" u 1:($28) w lp t "CSS" lt rgb "black"


set key at "2013-11-011T00:00:00", 30
set output "req_by_type_mobile_all.eps"
plot "../overview_m_edited.csv" u 1:($30) w lp lt 1 pt 1 t "Images",\
"../overview_m_edited.csv" u 1:($26) w lp t "JS",\
"../overview_m_edited.csv" u 1:($24) w lp t "HTML",\
"../overview_m_edited.csv" u 1:($28) w lp t "CSS",\
"../overview_m_edited.csv" u 1:($38+$40+$42+$44) w lp t "Other"

set key at "2013-09-011T00:00:00", 15
set output "req_by_type_mobile.eps"
plot "../overview_contpages_m_edited.csv" u 1:($30) w lp lt 1 pt 1 t "Images",\
"../overview_contpages_m_edited.csv" u 1:($26) w lp t "JS" lt rgb "black",\
"../overview_contpages_m_edited.csv" u 1:($24) w lp t "HTML" lt rgb "black",\
"../overview_contpages_m_edited.csv" u 1:($28) w lp t "CSS" lt rgb "black",\
"../overview_contpages_m_edited.csv" u 1:($38+$40+$42+$44) w lp t "Other" 


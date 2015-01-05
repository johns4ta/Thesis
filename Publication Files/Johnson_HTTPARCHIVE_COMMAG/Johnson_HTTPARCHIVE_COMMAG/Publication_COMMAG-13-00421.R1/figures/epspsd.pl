#!/usr/bin/perl
use strict;
use warnings;

my @files = <*.eps>;
foreach my $file (@files) {
	my $fileout = $file;
	$fileout =~ s/\.eps//;
	print "ps2pdf $file $fileout.pdf\n";
	system("ps2pdf $file $fileout.pdf");
}
print "All done.\n";
my $dummy = <STDIN>;
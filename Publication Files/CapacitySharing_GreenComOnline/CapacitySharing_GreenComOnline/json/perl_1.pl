#!perl
use strict;
use warnings;

my %values;
my @files = <*_clear.csv>;
foreach my $file (@files) {
	open IN, "<$file" or die;
	while (<IN>) {
		chomp;
		next if /^{url}/;
		# url,status,bodySize,cacheControl
		my @line = split ",";
		next if $line[1] ne "200";
		$values{$line[0]}{$file}{"size"} = $line[2];
		$values{$line[0]}{$file}{"cache"} = $line[3];
	}
	close IN;
}

foreach my $key1 ( keys %values ) {
	print "# url,";
	foreach my $file (@files) {
		print "$file,";
	}
	print "\n";
	last;
}
foreach my $key1 ( keys %values ) {
	print "$key1,";
	foreach my $key2 (@files) {
		print $values{$key1}{$key2}{"size"}.",";
	}
	foreach my $key2 ( @files ) {
		print $values{$key1}{$key2}{"cache"}.",";
	}
	print "\n";
}
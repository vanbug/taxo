#!/usr/bin/perl

# loading usual development settings/
use strict;
use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);

# decalarations
my @buglist;
my $infile = "/tmp/sessions.txt";
my $line;
my $everyline;
my $i=0;
my $session;
my @session;
my @ecVoltage;
my @show;
my $start;
my @start;
my @start1;
my $match;
my @module;
#my $start1;
system("ls /var/www/");
# basic html starts for outputting
print "Content-Type: text/html\n\n";
print "<html>";
print "<title>";
print "Flexible spreadsheet";
print "</title>";
# Adding Elements to html form dynamically
print <<END_HTML;
<HTML>
<HEAD>
<TITLE> Add/Remove dynamic rows in HTML table </TITLE>

</BODY>
</HTML>
END_HTML

print "<body>";

print "</table>";
print "</body>";
print "</html>";

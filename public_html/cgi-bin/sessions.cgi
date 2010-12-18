#!/usr/bin/perl

# loading usual development settings/
use strict;
#use warnings;
use CGI;
use Time::HiRes qw/gettimeofday tv_interval/;
use CGI::Carp qw(fatalsToBrowser);


################################################################################
# decalarations
my $q = new CGI;
my $query;
my $RDuration=">Duration.R";# Need to put either '>' or '>>' for writing once or appending to the respective file.
# Ending Declarations
################################################################################
# Opening some required file handles
open(RAL,$RDuration);
################################################################################
# basic html starts for outputting
    print "Content-Type: text/html\n\n";
    print "<hr size='2.5'>";
################################################################################
## it creates an R instruction file for generating the histograms by R
    print (RAL "d=as.data.frame(cbind(c(1:10),c(11:20)))\nprint(d)\nlibrary('Cairo')\nCairoPNG('ab.png')\n?Cairo\nplot(d)\ndev.off()\n");
## it commences the R instruction file which is being saved as RDuration.R
    print `R --slave<Duration.R`;
    print "<hr size=2.5>";
## this command generates the query result below the histograms
################################################################################
################################################################################


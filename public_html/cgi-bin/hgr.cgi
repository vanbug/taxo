#!/usr/bin/perl -w
# PERL CGI script for constructing interactive graphs using FLOT javscript library
 
use strict;  
use CGI;  
use CGI::Carp qw ( fatalsToBrowser );  
use File::Basename;

# parses all data to html page
print "Content-Type: text/html\n\n";
# file reading
my $data='../public_html/upload/a.txt';
my @FH;
my $line;
my $a;my $b;my $i,my @a,my @b; my @d; my @e; my $d; my $e;
open(FH,$data) || die("could not open");
@FH=<FH>;
foreach $line (@FH){
$line=~/((\d+)\s+(\d+))/;
$a[$i]=$2;
$b[$i]=$3;
$i++;
}
#my @d=@a.@b;
#for ($i=0; $i=length(@a); $i++){}
#@d=$a[1].','.$a[2].','.$a[3];
#@e=$b[1].','.$b[2].','.$b[3];
#system('/usr/bin/R --vanilla --slave <../R/t1.R');
print <<END_HTML;
<!DOCTYPE html>
<html>
	<head>
	<!-- loading javascript libraries -->
	<script language="javascript" type="text/javascript" src="../public_html/js/flot/jquery.js"></script>
    <script type="text/javascript" src="../public_html/js/Highcharts/js/highcharts.js"></script>
	<script type="text/javascript" src="../public_html/js/Highcharts/js/modules/exporting.js"></script>
	<script type="text/javascript">
	var example = 'bar-basic',
	theme = 'skies';
	</script>
	<script type="text/javascript" src="../public_html/js/Highcharts/js/themes/skies.js"></script>
	<script type="text/javascript">
		var chart;
		var test=new Array();
		test='@a';
		document.write(test[1]);
		jQuery(document).ready(function() {
			chart = new Highcharts.Chart({
				chart:{renderTo:'container',defaultSeriesType:'bar'},
				title:{text:'Historic World Population by Region: A test'},
				subtitle:{text:'Source: Wikipedia.org'},
				xAxis:{categories:['Africa', 'America', 'Asia', 'Europe', 'Oceania'],title:{text:'Countries [xlab]'}},
				yAxis:{min:0,title:{text:'Population(millions)',align:'high'}},
				tooltip:{formatter:function(){return''+this.series.name+': '+this.y+' millions';}},
				plotOptions:{bar:{dataLabels:{enabled:true}}},
				legend:{layout:'vertical',align:'right',verticalAlign:'top',x:-100,y:100,floating:true,borderWidth:1,
				backgroundColor:Highcharts.theme.legendBackgroundColor||'#FFFFFF',shadow: true},
				credits:{enabled:false},series:[{name:'Year 1800',data:[107,31,635,203,2]},{name:'Year 1900',data:[133,156,947,408,6]},{name:'Year 2008',data:test}]});});
	</script>
	</head>
	<body>
	<div id="container" class="highcharts-container" style="height:410px; margin: 0 2em; clear:both; min-width: 600px">
	</body>
</html>
END_HTML

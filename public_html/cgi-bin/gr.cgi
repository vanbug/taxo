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
    <script language="javascript" type="text/javascript" src="../public_html/js/flot/jquery.flot.js"></script>
	</head>
	<body>
	<div id="placeholder" style="width:600px;height:300px;"></div>
	<p id="hoverdata">Mouse hovers at (<span id="x">0</span>, <span id="y">0</span>). <span id="clickdata"></span></p>

	<p><input id="enableTooltip" type="checkbox">Enable tooltip</p>
<!-- Javascript function for constructing graph-->
<script id="source" language="javascript" type="text/javascript">
\$(function(){
    var a=[[1,2],[2,3]],b=[[2,4],[4,5]]; // variables initialised
    var plot = \$.plot(\$("#placeholder"), // building plot,plot has 3 values : div,data, parameters
           [{data:a,label:"X"},{data:b,label:"Y"}],{	// fetched data
               series:{lines:{show:false},points:{show:true}},
               grid:{hoverable:true,clickable:true},
               xaxis:{min:0,max:10},
               yaxis:{min:0,max:10}
             });
    function showTooltip(x,y,contents) {
        \$('<div id="tooltip">'+contents +'</div>').css({
            position:'absolute',
            display:'none',
            top:y + 5,
            left:x + 5,
            border:'1px solid #fdd',
            padding:'2px',
            'background-color':'#fee',
            opacity:0.80
        }).appendTo("body").fadeIn(200);
    }

    var previousPoint=null;
    \$("#placeholder").bind("plothover",function(event,pos,item){
        \$("#x").text(pos.x.toFixed(2));
        \$("#y").text(pos.y.toFixed(2));

        if (\$("#enableTooltip:checked").length>0){
            if (item){
                if (previousPoint!=item.datapoint){
                    previousPoint=item.datapoint;
                    \$("#tooltip").remove();
                    var x=item.datapoint[0].toFixed(2),
                        y=item.datapoint[1].toFixed(2);
                    showTooltip(item.pageX, item.pageY,
                                item.series.label+"of"+x+"="+y);
                }
            }
            else{
                \$("#tooltip").remove();
                previousPoint=null;            
            }
        }
    });

    \$("#placeholder").bind("plotclick", function (event, pos, item) {
        if (item) {
            \$("#clickdata").text("You clicked point " + item.dataIndex + " in " + item.series.label + ".");
            plot.highlight(item.series, item.datapoint);
        }
    });
});
</script>
	</body>
</html>
END_HTML

#!/usr/bin/perl -w
# PERL CGI script for constructing interactive graphs using FLOT javscript library
 
use strict;  
use CGI;  
use CGI::Carp qw ( fatalsToBrowser );  
use File::Basename;  

print "Content-Type: text/html\n\n";
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

<script id="source" language="javascript" type="text/javascript">
\$(function () {
    var sin = [], cos = [];
    for (var i = 0; i < 14; i += 0.5) {
        sin.push([i, Math.sin(i)]);
        cos.push([i, Math.cos(i)]);
    }

    var plot = \$.plot(\$("#placeholder"),
           [ { data: sin, label: "sin(x)"}, { data: cos, label: "cos(x)" } ], {
               series: {
                   lines: { show: true },
                   points: { show: true }
               },
               grid: { hoverable: true, clickable: true },
               yaxis: { min: -1.2, max: 1.2 }
             });

    function showTooltip(x, y, contents) {
        \$('<div id="tooltip">' + contents + '</div>').css( {
            position: 'absolute',
            display: 'none',
            top: y + 5,
            left: x + 5,
            border: '1px solid #fdd',
            padding: '2px',
            'background-color': '#fee',
            opacity: 0.80
        }).appendTo("body").fadeIn(200);
    }

    var previousPoint = null;
    \$("#placeholder").bind("plothover", function (event, pos, item) {
        \$("#x").text(pos.x.toFixed(2));
        \$("#y").text(pos.y.toFixed(2));

        if (\$("#enableTooltip:checked").length > 0) {
            if (item) {
                if (previousPoint != item.datapoint) {
                    previousPoint = item.datapoint;
                    
                    \$("#tooltip").remove();
                    var x = item.datapoint[0].toFixed(2),
                        y = item.datapoint[1].toFixed(2);
                    
                    showTooltip(item.pageX, item.pageY,
                                item.series.label + " of " + x + " = " + y);
                }
            }
            else {
                \$("#tooltip").remove();
                previousPoint = null;            
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

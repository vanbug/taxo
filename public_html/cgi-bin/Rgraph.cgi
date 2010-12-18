#!/usr/bin/perl -w
 
use strict;  
use CGI;  
use CGI::Carp qw ( fatalsToBrowser );  
use File::Basename;  

print "Content-Type: text/html\n\n";
system('/usr/bin/R --vanilla --slave <../R/t1.R');

print <<END_HTML;  
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "DTD/xhtml1-strict.dtd">  
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">  
 <head>  
   <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />  
   	<script language="JavaScript" src="../public_html/js/prototype.js"></script>
   	<script language="JavaScript" src="../public_html/js/tipmessage/main.js" type="text/javascript"></script>
   	<script type="text/javascript" src="../public_html/js/tooltips/lib/scriptaculous.js"></script>
	<script type="text/javascript" src="../public_html/js/tooltips/tooltips.js"></script>
	 <script src="libraries/RGraph.common.adjusting.js" ></script>

    <script src="../public_html/js/RGraph/libraries/RGraph.common.core.js" ></script>
    <script src="../public_html/js/RGraph/libraries/RGraph.common.context.js" ></script>
    <script src="../public_html/js/RGraph/libraries/RGraph.common.tooltips.js" ></script>
    <script src="../public_html/js/RGraph/libraries/RGraph.common.zoom.js" ></script>
    <script src="../public_html/js/RGraph/libraries/RGraph.modaldialog.js" ></script>

    <script src="../public_html/js/RGraph/libraries/RGraph.line.js" ></script>

    <script src="../public_html/js/RGraph/libraries/RGraph.bar.js" ></script>
    <script src="../public_html/js/RGraph/libraries/RGraph.rose.js" ></script>
    <style>
        .RGraph_zoom_window {
            border-radius: 0 ! important;
            -moz-border-radius: 0 ! important;
            -webkit-border-radius: 0 ! important;
            box-shadow: 0 0 15px gray ! important;
            -moz-box-shadow: 0 0 15px gray ! important;
            -webkit-box-shadow: 0 0 15px gray ! important;
             border: 1px gray solid ! important;
        }

        .RGraph_zoomed_canvas {
            -webkit-box-shadow: 0 0 15px gray ! important;
        }

        .ModalDialog_dialog {
            -webkit-box-shadow: gray 0 0 15px ! important;
            -moz-box-shadow: 0 0 15px gray ! important;
            box-shadow: 0 0 15px gray ! important;
        }
    </style>

    <script>
        cover = {div: null};

        function ShowWarning ()
        {
            if (document.all && !RGraph.isIE8() && !RGraph.isIE9up()) {
                cover.div = document.createElement('DIV');
                cover.div.style.position = 'absolute';
                cover.div.style.top    = 0;
                cover.div.style.left   = 0;
                cover.div.style.width  = (document.body.clientWidth + 20) + 'px';
                cover.div.style.height = Math.max(document.documentElement.scrollHeight, screen.height) + 'px';
                cover.div.style.filter = 'Alpha(opacity=50)';
                cover.div.style.backgroundColor = 'gray';
                document.body.appendChild(cover.div);
                

                cover.messageDiv = document.createElement('DIV');
                cover.messageDiv.style.left = ((parseInt(document.body.clientWidth) / 2) - 200) + 'px';
                cover.messageDiv.style.top = '200px';
                cover.messageDiv.style.width = '400px';
                cover.messageDiv.style.padding = '5px';
                cover.messageDiv.style.position = 'absolute';
                cover.messageDiv.style.backgroundColor = 'yellow';
                cover.messageDiv.style.textAlign = 'center';
                cover.messageDiv.style.fontFamily = 'Arial';
                cover.messageDiv.style.fontSize = '12pt';
                cover.messageDiv.style.border   = '2px black solid';
                cover.messageDiv.style.filter = 'filter: progid:DXImageTransform.Microsoft.Shadow(color=#666666,direction=135);';
                document.body.appendChild(cover.messageDiv);
                
                cover.messageDiv.innerHTML = "<h2>Yikes!</h2>Your version of Microsoft Internet Explorer appears to be less than 8, which is required to view these graphs. You can still view the website, but it will look odd and the graphs won't work.<br /><br /><a onclick=\"cover.div.style.display = 'none'; cover.messageDiv.style.display = 'none';\" href=\"javascript:\">Close</a>"
            }
        }

        window.onload = function (e)
        {
            if (RGraph.isIE8()) {
                CreateLineChart();
                CreateBarChart();
                CreateRoseChart();
            }

            ShowWarning();
        }
        
        window.onresize = function (e)
        {
            if (cover.div) {
                cover.messageDiv.style.display = 'none';
                cover.div.style.display = 'none';
                cover.div = null;
            }

            ShowWarning();
        }


        function HideTwitterDIV ()
        {
            document.getElementById("twitter_div").style.opacity = 0;
            document.getElementById("twitter_div").style.display = 'none';
        }


        function ShowTwitterDIV (e)
        {
            var e   = RGraph.FixEventObject(document.all ? event : e);
            var div = document.getElementById("twitter_div");
            var img = document.getElementById("twitter_icon");

            div.style.display = 'block';
            div.style.left    = (RGraph.getCanvasXY(img)[0] + img.offsetWidth - div.offsetWidth + 110) + 'px';
            div.style.top     = (RGraph.getCanvasXY(img)[1] - 1) + 'px';

            /**
            * Fade it in
            */
            setTimeout('document.getElementById("twitter_div").style.opacity = 0.2;', 25);
            setTimeout('document.getElementById("twitter_div").style.opacity = 0.4;', 50);
            setTimeout('document.getElementById("twitter_div").style.opacity = 0.6;', 100);
            setTimeout('document.getElementById("twitter_div").style.opacity = 0.8;', 125);
            setTimeout('document.getElementById("twitter_div").style.opacity = 1.0;', 150);

            e.stopPropagation();

            return false;
        }


        window.addEventListener('click', HideTwitterDIV, false);
    </script>

<a href="#" title="Tooltip test text" class="help">Hover me...</a>


 <A href="#" onMouseOver="stm(Text[2],Style[0])" onMouseOut="htm()">this is a link</A>           
   <p>Thanks for uploading your photo!</p>  
   <p>Your photo:</p>  
   <p><a onMouseOver="stm(Text[2],Style[0])" onMouseOut="htm()">
   <img src="../R/plots/a.png" alt="Photo" /></a></p>
   <TextBlock ToolTip="stuff, could even be a custom control, etc" Text="my text" />
   <a href="../public_html/Fupload.html" ><input type="button" value="home"></input></a>
 </body>  
</html>  
END_HTML

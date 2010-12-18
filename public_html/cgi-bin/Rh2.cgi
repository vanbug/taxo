#!/usr/bin/perl -w
 
use strict;  
use CGI;  
use CGI::Carp qw ( fatalsToBrowser );  
use File::Basename;  
 
$CGI::POST_MAX = 1024 * 5000;  
my $safe_filename_characters = "a-zA-Z0-9_.-";  
my $upload_dir = "/var/www/public_html/upload";  
 
my $query = new CGI;  
my $filename = $query->param("photo");  
my $email_address = $query->param("email_address");  
 
if ( !$filename )  
{  
 print $query->header ( );  
 print "There was a problem uploading your photo (try a smaller file).";  
 exit;  
}  
 
my ( $name, $path, $extension ) = fileparse ( $filename, '\..*' );  
$filename = $name . $extension;  
$filename =~ tr/ /_/;  
$filename =~ s/[^$safe_filename_characters]//g;  
 
if ( $filename =~ /^([$safe_filename_characters]+)$/ )  
{  
 $filename = $1;  
}  
else  
{  
 die "Filename contains invalid characters";  
}  
 
my $upload_filehandle = $query->upload("photo");  
 
open ( UPLOADFILE, ">$upload_dir/$filename" ) or die "$!";  
binmode UPLOADFILE;  
 
while ( <$upload_filehandle> )  
{  
 print UPLOADFILE;  
}  
 
close UPLOADFILE;  
 
print $query->header ( );
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
	<link rel="stylesheet" href="../public_html/js/tooltips/tooltips.css" type="text/css" media="screen" />
   <title>Thanks!</title>  
   <style type="text/css">  
     img {border: none;}  
   </style>  
 </head>  
 <body>  
 <DIV id="TipLayer" style="visibility:hidden;position:absolute;z-index:1000;top:-100;"></DIV>
 <SCRIPT language="JavaScript1.2" src="../public_html/js/tipmessage/style.js" type="text/javascript"></SCRIPT>
 <script type="text/javascript" charset="utf-8">
	$$("ul .help").each( function(link) {
		new Tooltip(link, {mouseFollow: false});
	});
	$$("p .help").each( function(input) {
		new Tooltip(input, {backgroundColor: "#333", borderColor: "#333", 
		textColor: "#FFF", textShadowColor: "#000"});
	});
	$$("form input.help").each( function(input) {
		new Tooltip(input, {backgroundColor: "#FC9", borderColor: "#C96", 
		textColor: "#000", textShadowColor: "#FFF"});
	});
</script>
<a href="#" title="Tooltip test text" class="help">Hover me...</a>


 <A href="#" onMouseOver="stm(Text[2],Style[0])" onMouseOut="htm()">this is a link</A>           
   <p>Thanks for uploading your photo!</p>  
   <p>Your email address: $email_address</p>  
   <p>Your photo:</p>  
   <p><a onMouseOver="stm(Text[2],Style[0])" onMouseOut="htm()"><img src="../R/plots/a.png" alt="Photo" /></a></p>
   <TextBlock ToolTip="stuff, could even be a custom control, etc" Text="my text" />
   <a href="../public_html/Fupload.html" ><input type="button" value="home"></input></a>
 </body>  
</html>  
END_HTML

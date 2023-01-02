import base64
import re


doc ='''<!DOCTYPE html><html dir="ltr" lang="en-US"><head>
        <title>Linegee | Approaching The Unknown</title>
        <meta http-equiv="content-type" content="text/html; charset=utf-8">
        <meta name="author" content="Linegee">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css?family=Lato:300,400,400i,700|Raleway:300,400,500,600,700|Crete+Round:400i" rel="stylesheet" type="text/css">
        <link rel="stylesheet" href="css/bootstrap.css" type="text/css">
        <link rel="stylesheet" href="style.css" type="text/css">
        <link rel="stylesheet" href="css/dark.css" type="text/css">
        <link rel="stylesheet" href="css/font-icons.css" type="text/css">
        <link rel="stylesheet" href="css/animate.css" type="text/css">
        <link rel="stylesheet" href="css/magnific-popup.css" type="text/css">
        <link rel="stylesheet" href="css/responsive.css" type="text/css">
    <script src="https://securepubads.g.doubleclick.net/gpt/pubads_impl_page_level_ads_2022120601.js?cb=31071256"></script><script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-154452410-2"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'UA-154452410-2');
    </script>
<meta http-equiv="origin-trial" content="Az6AfRvI8mo7yiW5fLfj04W21t0ig6aMsGYpIqMTaX60H+b0DkO1uDr+7BrzMcimWzv/X7SXR8jI+uvbV0IJlwYAAACFeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjgwNjUyNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A+USTya+tNvDPaxUgJooz+LaVk5hPoAxpLvSxjogX4Mk8awCTQ9iop6zJ9d5ldgU7WmHqBlnQB41LHHRFxoaBwoAAACLeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjgwNjUyNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7FovoGr67TUBYbnY+Z0IKoJbbmRmB8fCyirUGHavNDtD91CiGyHHSA2hDG9r9T3NjUKFi6egL3RbgTwhhcVDwUAAACLeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXRhZ3NlcnZpY2VzLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjgwNjUyNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><script src="https://securepubads.g.doubleclick.net/gpt/pubads_impl_2022120601.js?cb=31071256" async=""></script><link rel="preload" href="https://adservice.google.co.in/adsid/integrator.js?domain=linegee.net" as="script"><script type="text/javascript" src="https://adservice.google.co.in/adsid/integrator.js?domain=linegee.net"></script><link rel="preload" href="https://adservice.google.com/adsid/integrator.js?domain=linegee.net" as="script"><script type="text/javascript" src="https://adservice.google.com/adsid/integrator.js?domain=linegee.net"></script></head>
    <body style="background: url('images/pattern.png') repeat fixed;" class="no-transition"><div id="adop_flyingcarpet" style="position:relative;;width:100%;height:400px;"><div id="adopM41581" style="position:absolute;width:100%;height:100%;clip:rect(auto auto auto auto);"><div id="adopF79961" style="top:60px;width:300px;height:600px;position:fixed;left:50%;margin-left: -150px;"><iframe id="adopB55201" frameborder="0" marginwidth="0" marginheight="0" paddingwidth="0" paddingheight="0" scrolling="no" style="width: 100%; height: 100%;"></iframe></div></div></div>
    <script type="application/javascript">var adop_flying = {};adop_flying.zoneid = 'bbfa64fa-f59d-40b8-b713-56cb12187b44';adop_flying.width = '300';adop_flying.height = '600';adop_flying.viewer = '400';adop_flying.adjust = '0';</script>
    <script src="//compass.adop.cc/assets/js/adop/adop_flyingcarpet.js"></script>
        <div id="wrapper" class="clearfix">
                <header id="header" class="full-header">
                        <div id="header-wrap">
                                <div class="container clearfix">
                                        <div id="primary-menu-trigger"><i class="icon-reorder"></i>
                                        </div>
                                        <div id="logo">
                                                <a href="https://linegee.net" class="standard-logo" data-dark-logo="images/logo-dark.png">
                                                        <img src="images/logo.png" alt="Canvas Logo">
                                                </a>
                                                <a href="https://linegee.net" class="retina-logo" data-dark-logo="images/logo-dark@2x.png">
                                                        <img src="images/logo@2x.png" alt="Canvas Logo">
                                                </a>
                                        </div>
                                        <nav id="primary-menu">
                                                <ul>
                                                        <li>
                                                                <a href="https://linegee.net">
                                                                        <div>Home</div>
                                                                </a>
                                                        </li>
                                                        <li>
                                                                <a href="contact.html">
                                                                        <div>Contact Us</div>
                                                                </a>
                                                        </li>
                                                        <li>
                                                                <a href="policy.html">
                                                                        <div>Privacy Policy</div>
                                                                </a>
                                                        </li>
                                                        <li>
                                                                <a href="tos.html">
                                                                        <div>Terms of Service</div>
                                                                </a>
                                                        </li>
                                                </ul>
                                                <div id="top-search"> <a href="#" id="top-search-trigger"><i class="icon-search3"></i><i class="icon-line-cross"></i></a>
                                                        <form action="search.html" method="get">
                                                                <input type="text" name="q" class="form-control" value="" placeholder="Type &amp; Hit Enter..">
                                                        </form>
                                                </div>
                                        </nav>
                                </div>
                        </div>
                </header>
                <section id="page-title">
                        <div class="container clearfix" align="center">
<script async="" src="//compass.adop.cc/assets/js/adop/adop.js?v=10"></script>
<ins class="adsbyadop_f0e500aa-41d0-42d8-bb46-121351b37bd3" _adop_zon="f0e500aa-41d0-42d8-bb46-121351b37bd3" _adop_type="rs" style="display: inline-block; width: 970px; height: 90px;" _page_url="" _over_size="970" _over_zone="f0e500aa-41d0-42d8-bb46-121351b37bd3"><iframe src="https://compass.adop.cc/RD/f0e500aa-41d0-42d8-bb46-121351b37bd3?over-size=970&amp;over-size-w=null&amp;over-size-h=null&amp;over-zone=f0e500aa-41d0-42d8-bb46-121351b37bd3&amp;adop-zone=d34dcde8-3075-4f11-9a60-3328fdb26005&amp;type=rs&amp;loc=https%253A%2F%2Flinegee.net%2FkZ4UK&amp;size_width=970&amp;size_height=90&amp;title=Linegee%2520%257C%2520Approaching%2520The%2520Unknown&amp;ref=https%253A%252F%252Fintercelestial.com%252F&amp;" id="f0e500aa-41d0-42d8-bb46-121351b37bd3" border="none" frameborder="0" marginwidth="0" marginheight="0" paddingwidth="0" paddingheight="0" width="970" height="90" scrolling="no"></iframe></ins>
                        </div>
                </section>
                <section id="content" style="margin-bottom: 0px;">
                        <div class="content-wrap">
                                <div class="container clearfix">
                                        <div class="postcontent nobottommargin clearfix">
                                                <div class="single-post nobottommargin">
                                                        <div class="entry clearfix">
                                                                <div class="entry-title">
                                                                        <h2>Claude Ptolemy</h2>
                                                                </div>
                                                                <ul class="entry-meta clearfix">
                                                                        <li><i class="icon-calendar3"></i> 10th July 
2020</li>
                                                                        <li><a href="#"><i class="icon-user"></i> Enigma</a>
                                                                        </li>
                                                                        <li><i class="icon-folder-open"></i>  <a href="#">General</a>
                                                                        </li>
                                                                </ul>
                                                                <div class="entry-image">
                                                                        <img src="https://spacetica.com/content/ysY3DaHM_avatar.jpg">
                                                                </div>
                                                                <div class="entry-content notopmargin">
                                                                        <p>
                                                                                Around 140 AD, Claude Ptolemy (90-168 AD) took the theory of Hipparchus. He exposes in his Almagest the first empirical theory of the movement of the Moon. Ptolemy confirms while correcting the geocentric system of Aristotle. He considers that the Earth is surrounded by 
a series of crystal spheres - up to 50 spheres - on which the planets and the Sun are fixed. The outer sphere contains the fixed stars behind which is always the divine fire. All these spheres move uniformly in accordance with Greek metaphysics.<br><br> However, this conception does not correctly explain the sometimes aberrant movement of certain planets such as Mars, which retrograde for a few months before resuming its normal course among the stars. On the other hand, since the tables of lunar positions did not conform to observations as time progressed, Ptolemy invented the theory of epicycles. Each planet describes a circular orbit, the epicycle, centered on the main orbit, called the deferent. To explain the smallest variations in the trajectories of the planets, Ptolemy further improves his system and 
imagines that the centers of the deferents are themselves offset from the center of the Earth, following a circular path called the eccentric.<br><br> But philosophically speaking, the idea of ​​Ptolemy tarnishes the brightness of the
 Sun. All the Middle Ages are conservative, the Man is the center of the concerns while the Church sees angels everywhere - some push even the planets - a way of counteracting the mechanism and the Greek geometry.<br><br> We are going through a period of lethargy during which new ideas were duly combated by religious dogmas and prejudices. Things remained frozen for nearly a thousand years because the clergy refused the irrationality of mathematicians. Nature could not be tamed. This attitude was contrary to the divine essence, for which everything was order and aesthetic, Bible in support. The clergy also referred to the ancient conceptions of Plato and Aristotle, whose very enlightened genius was authoritative for a few centuries.</p>
                                                                        <center>
                                                                                <p class="kecil">
                                                                                    <script async="" src="//compass.adop.cc/assets/js/adop/adopJ.js?v=10"></script>
                                                                                        <ins class="adsbyadop_bb523b32-9822-40b5-9751-6032591c88ee" _adop_zon="bb523b32-9822-40b5-9751-6032591c88ee" _adop_type="re" style="display:inline-block;width:336px;height:280px;" _page_url=""><div style="width:336px;height:280px; "><iframe id="adopB5071" frameborder="0" marginwidth="0" marginheight="0" paddingwidth="0" paddingheight="0" scrolling="no" style="width: 100%; height: 100%;"></iframe></div></ins>
                                                                                        <br>

                                        <a href="https://new4.gdtot.cfd/Afa654e9433da754" rel="nofollow" target="_blank" class="btn btn-primary btn-xs">Continue</a>
                                                                                        <br>
                                                                                        <script async="" src="//compass.adop.cc/assets/js/adop/adopJ.js?v=10"></script>
                                                                                        <ins class="adsbyadop_19534eb8-3e4f-4216-9a7c-1c84c05937a2" _adop_zon="19534eb8-3e4f-4216-9a7c-1c84c05937a2" _adop_type="re" style="display:inline-block;width:300px;height:600px;" _page_url=""><div style="width:300px;height:600px; "><iframe id="adopB21751" frameborder="0" marginwidth="0" marginheight="0" paddingwidth="0" paddingheight="0" scrolling="no" style="width: 100%; height: 100%;"></iframe></div></ins>
                                                                                </p>
                                                                        </center>
                                                                        <div class="tagcloud clearfix bottommargin"> 
<a href="#">general</a>  <a href="#">information</a>  <a href="#">artifact</a>  <a href="#">old</a>  <a href="#">gallery</a>  <a href="#">illustration</a>
                                                                        </div>
                                                                        <div class="clear"></div>
                                                                        <div class="si-share noborder clearfix"> <span>Share this Post:</span>
                                                                                <div>
                                                                                        <a href="#" class="social-icon si-borderless si-facebook"> <i class="icon-facebook"></i>  <i class="icon-facebook"></i>
                                                                                        </a>
                                                                                        <a href="#" class="social-icon si-borderless si-rss"> <i class="icon-rss"></i>  <i class="icon-rss"></i>
                                                                                        </a>
                                                                                        <a href="#" class="social-icon si-borderless si-email3"> <i class="icon-email3"></i>  <i class="icon-email3"></i>
                                                                                        </a>
                                                                                </div>
                                                                        </div>
                                                                </div>
                                                        </div>
                                                        <div class="post-navigation clearfix">
                                                                <div class="col_half nobottommargin"> <a href="light.html">⇐ Light</a>
                                                                </div>
                                                                <div class="col_half col_last tright nobottommargin"> <a href="stars.html">Stars ⇒</a>
                                                                </div>
                                                        </div>
                                                        <div class="line"></div>
                                                        <h4>Related Posts:</h4>
                                                        <div class="related-posts clearfix">
                                                                <div class="col_half nobottommargin">
                                                                        <div class="mpost clearfix">
                                                                                <div class="entry-image">
                                                                                        <a href="venus.html">        
                                                                                                <img src="images/post/venus-small.jpg" alt="Venus">
                                                                                        </a>
                                                                                </div>
                                                                                <div class="entry-c">
                                                                                        <div class="entry-title">    
                                                                                                <h4><a href="venus.html">Venus</a></h4>
                                                                                        </div>
                                                                                        <ul class="entry-meta clearfix">
                                                                                                <li><i class="icon-calendar3"></i> 19 Nov 2019</li>
                                                                                        </ul>
                                                                                        <div class="entry-content">In relation to the Sun, Venus is the second planet after Mercury, just in front of the Earth.</div>
                                                                                </div>
                                                                        </div>
                                                                        <div class="mpost clearfix">
                                                                                <div class="entry-image">
                                                                                        <a href="mercury.html">      
                                                                                                <img src="images/post/mercury-small.jpg" alt="Mercury">
                                                                                        </a>
                                                                                </div>
                                                                                <div class="entry-c">
                                                                                        <div class="entry-title">    
                                                                                                <h4><a href="mercury.html">Mercury</a></h4>
                                                                                        </div>
                                                                                        <ul class="entry-meta clearfix">
                                                                                                <li><i class="icon-calendar3"></i> 19 Nov 2019</li>
                                                                                        </ul>
                                                                                        <div class="entry-content">Mercury is a small planet that resembles the Moon with a diameter of 4878 KM.</div>
                                                                                </div>
                                                                        </div>
                                                                </div>
                                                                <div class="col_half nobottommargin col_last">       
                                                                        <div class="mpost clearfix">
                                                                                <div class="entry-image">
                                                                                        <a href="saturn.html">       
                                                                                                <img src="images/post/saturn.jpg" alt="Saturn">
                                                                                        </a>
                                                                                </div>
                                                                                <div class="entry-c">
                                                                                        <div class="entry-title">    
                                                                                                <h4><a href="saturn.html">Saturn</a></h4>
                                                                                        </div>
                                                                                        <ul class="entry-meta clearfix">
                                                                                                <li><i class="icon-calendar3"></i> 31 Oct 2019</li>
                                                                                        </ul>
                                                                                        <div class="entry-content">Saturn, the planet with the rings. It is really the most beautiful planet of the solar system.</div>
                                                                                </div>
                                                                        </div>
                                                                        <div class="mpost clearfix">
                                                                                <div class="entry-image">
                                                                                        <a href="ring-of-saturn.html">
                                                                                                <img src="images/post/ring.png" alt="The Ring System of Saturn">
                                                                                        </a>
                                                                                </div>
                                                                                <div class="entry-c">
                                                                                        <div class="entry-title">    
                                                                                                <h4><a href="ring-of-saturn.html">The Ring System of Saturn</a></h4>
                                                                                        </div>
                                                                                        <ul class="entry-meta clearfix">
                                                                                                <li><i class="icon-calendar3"></i> 5 Nov 2019</li>
                                                                                        </ul>
                                                                                        <div class="entry-content">We speak of a system because there is not only one ring but countless, almost an infinity.</div>
                                                                                </div>
                                                                        </div>
                                                                </div>
                                                        </div>

                                                        <div id="comments" class="clearfix">
                                                                <div class="clear"></div>
                                                                <div id="respond" class="clearfix">
                                                                        <h3>Leave a <span>Comment</span></h3>        
                                                                        <form class="clearfix" action="#" method="post" id="commentform">
                                                                                <div class="col_one_third">
                                                                                        <label for="author">Name</label>
                                                                                        <input type="text" name="author" id="author" value="" size="22" tabindex="1" class="sm-form-control">
                                                                                </div>
                                                                                <div class="col_one_third">
                                                                                        <label for="email">Email</label>
                                                                                        <input type="text" name="email" id="email" value="" size="22" tabindex="2" class="sm-form-control">
                                                                                </div>
                                                                                <div class="col_one_third col_last"> 
                                                                                        <label for="url">Website</label>
                                                                                        <input type="text" name="url" id="url" value="" size="22" tabindex="3" class="sm-form-control">
                                                                                </div>
                                                                                <div class="clear"></div>
                                                                                <div class="col_full">
                                                                                        <label for="comment">Comment</label>
                                                                                        <textarea name="comment" cols="58" rows="7" tabindex="4" class="sm-form-control"></textarea>
                                                                                </div>
                                                                                <div class="col_full nobottommargin">                                                                                        <button name="submit" type="submit" id="submit-button" tabindex="5" value="Submit" class="button button-3d nomargin">Submit Comment</button>      
                                                                                </div>
                                                                        </form>
                                                                </div>
                                                        </div>
                                                </div>
                                        </div>
                                        <div class="sidebar nobottommargin col_last clearfix">
                                                <div class="sidebar-widgets-wrap">
                                                        <div class="widget clearfix">
                                                                <div class="tabs nobottommargin clearfix" id="sidebar-tabs">
                                                                        <ul class="tab-nav clearfix">
                                                                                <li><a href="#tabs-1">Popular</a>    
                                                                                </li>
                                                                                <li><a href="#tabs-2">Recent</a>     
                                                                                </li>
                                                                        </ul>
                                                                        <div class="tab-container">
                                                                                <div class="tab-content clearfix" id="tabs-1">
                                                                                        <div id="popular-post-list-sidebar">
                                                                                                <div class="spost clearfix">
                                                                                                        <div class="entry-image">
                                                                                                                <a href="https://linegee.net/natural-satelite.html" class="nobg">
                                                                                                                 <img class="rounded-circle" src="images/post/moon.jpg" alt="">
                                                                                                                </a> 
                                                                                                        </div>       
                                                                                                        <div class="entry-c">
                                                                                                                <div 
class="entry-title">
                                                                                                                 <h4><a href="https://linegee.net/natural-satelite.html">The Natural Satellite of The Earth</a></h4>
                                                                                                                </div>
                                                                                                        </div>       
                                                                                                </div>
                                                                                                <div class="spost clearfix">
                                                                                                        <div class="entry-image">
                                                                                                                <a href="https://linegee.net/ring-of-saturn.html" class="nobg">
                                                                                                                 <img class="rounded-circle" src="images/post/ring.png" alt="">
                                                                                                                </a> 
                                                                                                        </div>       
                                                                                                        <div class="entry-c">
                                                                                                                <div 
class="entry-title">
                                                                                                                 <h4><a href="https://linegee.net/ring-of-saturn.html">The Ring System of Saturn</a></h4>
                                                                                                                </div>
                                                                                                        </div>       
                                                                                                </div>
                                                                                                <div class="spost clearfix">
                                                                                                        <div class="entry-image">
                                                                                                                <a href="https://linegee.net/procession.html" class="nobg">
                                                                                                                 <img class="rounded-circle" src="images/post/procession.jpg" alt="">
                                                                                                                </a> 
                                                                                                        </div>       
                                                                                                        <div class="entry-c">
                                                                                                                <div 
class="entry-title">
                                                                                                                 <h4><a href="https://linegee.net/procession.html">A Procession of 9 Planets</a></h4>
                                                                                                                </div>
                                                                                                        </div>       
                                                                                                </div>
                                                                                                <div class="spost clearfix">
                                                                                                        <div class="entry-image">
                                                                                                                <a href="https://linegee.net/milky.html" class="nobg">
                                                                                                                 <img class="rounded-circle" src="images/post/milky.jpg" alt="">
                                                                                                                </a> 
                                                                                                        </div>       
                                                                                                        <div class="entry-c">
                                                                                                                <div 
class="entry-title">
                                                                                                                 <h4><a href="https://linegee.net/milky.html">Our Milky Way</a></h4>
                                                                                                                </div>
                                                                                                        </div>       
                                                                                                </div>
                                                                                                <div class="spost clearfix">
                                                                                                        <div class="entry-image">
                                                                                                                <a href="https://linegee.net/disciplines.html" class="nobg">
                                                                                                                 <img class="rounded-circle" src="images/post/disciplines.jpg" alt="">
                                                                                                                </a> 
                                                                                                        </div>       
                                                                                                        <div class="entry-c">
                                                                                                                <div 
class="entry-title">
                                                                                                                 <h4><a href="https://linegee.net/disciplines.html">The Disciplines of Bioastronomy</a></h4>
                                                                                                                </div>
                                                                                                        </div>       
                                                                                                </div>
                                                                                        </div>
                                                                                </div>
                                                                                <div class="tab-content clearfix" id="tabs-2">
                                                                                        <div id="recent-post-list-sidebar">
                                                                                                <div class="spost clearfix">
                                                                                                        <div class="entry-image">
                                                                                                                <a href="https://linegee.net/natural-satelite.html" class="nobg">
                                                                                                                 <img class="rounded-circle" src="images/post/moon.jpg" alt="">
                                                                                                                </a> 
                                                                                                        </div>       
                                                                                                        <div class="entry-c">
                                                                                                                <div 
class="entry-title">
                                                                                                                 <h4><a href="https://linegee.net/natural-satelite.html">The Natural Satellite of The Earth</a></h4>
                                                                                                                </div>
                                                                                                                <ul class="entry-meta">
                                                                                                                 <li>6 Dec 2019</li>
                                                                                                                </ul>                                                                                                        </div>       
                                                                                                </div>
                                                                                                <div class="spost clearfix">
                                                                                                        <div class="entry-image">
                                                                                                                <a href="https://linegee.net/venus.html" class="nobg">
                                                                                                                 <img class="rounded-circle" src="images/post/venus.jpg" alt="">
                                                                                                                </a> 
                                                                                                        </div>       
                                                                                                        <div class="entry-c">
                                                                                                                <div 
class="entry-title">
                                                                                                                 <h4><a href="https://linegee.net/venus.html">Venus</a></h4>
                                                                                                                </div>
                                                                                                                <ul class="entry-meta">
                                                                                                                 <li>19 Nov 2019</li>
                                                                                                                </ul>                                                                                                        </div>       
                                                                                                </div>
                                                                                                <div class="spost clearfix">
                                                                                                        <div class="entry-image">
                                                                                                                <a href="https://linegee.net/mercury.html" class="nobg">
                                                                                                                 <img class="rounded-circle" src="images/post/mercury.jpg" alt="">
                                                                                                                </a> 
                                                                                                        </div>       
                                                                                                        <div class="entry-c">
                                                                                                                <div 
class="entry-title">
                                                                                                                 <h4><a href="https://linegee.net/mercury.html">Mercury</a></h4>
                                                                                                                </div>
                                                                                                                <ul class="entry-meta">
                                                                                                                 <li>13 Nov 2019</li>
                                                                                                                </ul>                                                                                                        </div>       
                                                                                                </div>
                                                                                                <div class="spost clearfix">
                                                                                                        <div class="entry-image">
                                                                                                                <a href="https://linegee.net/ring-of-saturn.html" class="nobg">
                                                                                                                 <img class="rounded-circle" src="images/post/ring.png" alt="">
                                                                                                                </a> 
                                                                                                        </div>       
                                                                                                        <div class="entry-c">
                                                                                                                <div 
class="entry-title">
                                                                                                                 <h4><a href="https://linegee.net/ring-of-saturn.html">The Ring System of Saturn</a></h4>
                                                                                                                </div>
                                                                                                                <ul class="entry-meta">
                                                                                                                 <li>5 Nov 2019</li>
                                                                                                                </ul>                                                                                                        </div>       
                                                                                                </div>
                                                                                                <div class="spost clearfix">
                                                                                                        <div class="entry-image">
                                                                                                                <a href="https://linegee.net/saturn.html" class="nobg">
                                                                                                                 <img class="rounded-circle" src="images/post/saturn.jpg" alt="">
                                                                                                                </a> 
                                                                                                        </div>       
                                                                                                        <div class="entry-c">
                                                                                                                <div 
class="entry-title">
                                                                                                                 <h4><a href="https://linegee.net/saturn.html">Saturn</a></h4>
                                                                                                                </div>
                                                                                                                <ul class="entry-meta">
                                                                                                                 <li>31 Oct 2019</li>
                                                                                                                </ul>                                                                                                        </div>       
                                                                                                </div>
                                                                                        </div>
                                                                                </div>
                                                                        </div>
                                                                </div>
                                                        </div>
                                                        <div class="widget clearfix" align="center">
                                                                <script async="" src="//compass.adop.cc/assets/js/adop/adopJ.js?v=10"></script>
                                                                <ins class="adsbyadop_d568e069-51e1-4bfc-8c5b-e1579e79ce5f" _adop_zon="d568e069-51e1-4bfc-8c5b-e1579e79ce5f" _adop_type="re" style="display:inline-block;width:160px;height:600px;" _page_url=""><div style="width:160px;height:600px; "><iframe id="adopB96281" frameborder="0" marginwidth="0" marginheight="0" paddingwidth="0" paddingheight="0" scrolling="no" style="width: 100%; height: 100%;"></iframe></div></ins>
                                                        </div>
                                                        <div class="widget clearfix">
                                                                <h4>Tag Cloud</h4>
                                                                <div class="tagcloud"> <a href="#">general</a>  <a href="#">videos</a>  <a href="#">music</a>  <a href="#">media</a>  <a href="#">photography</a>  <a href="#">parallax</a>  <a href="#">ecommerce</a>  <a href="#">terms</a>  <a href="#">coupons</a>  <a href="#">modern</a>
                                                                </div>
                                                        </div>
                                                </div>
                                        </div>
                                </div>
                        </div>
                </section>
                <footer id="footer" class="dark">
                        <div id="copyrights">
                                <div class="container clearfix">
                                        <div align="center">Copyrights © 2020
                                                <br>All Rights Reserved
                                                <br>
                                        </div>
                                </div>
                        </div>
                </footer>
        </div>
        <div id="gotoTop" class="icon-angle-up"></div>
        <script src="js/jquery.js"></script>
        <script src="js/plugins.js"></script>
        <script src="js/functions.js"></script>
        <style>
            .kecil {
                 line-height: 0 !important;
            }
        </style>
        <script>
                    $("a.btn-primary.btn-xs").click((e)=> {
                e.preventDefault();
                location.href = atob('aHR0cHM6Ly9uZXc0LmdkdG90LmNmZC9maWxlLzUyNTg3NzkxMg==');
            })
        </script>

<div style="display:-webkit-box; display: -ms-flexbox; display: flex; -webkit-box-orient: vertical; -webkit-box-direction: normal; -ms-flex-direction: column; flex-direction: column; -webkit-box-align: center; -ms-flex-align: center; 
align-items: center; -webkit-box-pack: center; -ms-flex-pack: center; justify-content: center; overflow: visible; position: fixed; text-align: center; bottom:0px; left: 0; width: 100%; z-index: 99999; max-height: 100px; background-image: none; background-color: #ffff; box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.2); margin-bottom: 0; padding-top: 2px; padding-bottom: 2px; transition: all .4s ease-in-out;" id="sticky-ad">
<button aria-label="X" class="sticky-ad-close-button" onclick="document.getElementById('sticky-ad').style.display='none'" style="position: absolute; width: 28px; height: 28px; top: -28px; right: 0; box-shadow: 0 -1px 1px 0 rgba(0, 0, 
0, 0.2); border: none; border-radius: 12px 0 0 0; cursor: pointer;"></button>
<script src="https://compass.adop.cc/assets/js/adop/adopJ.js?v=14"></script>
<ins class="adsbyadop_51b4730c-6e00-4624-b96c-25d74f0607b2" _adop_zon="51b4730c-6e00-4624-b96c-25d74f0607b2" _adop_type="re" style="display: inline-block; width: 728px; height: 90px;" _page_url="" _over_size="728" _over_zone="51b4730c-6e00-4624-b96c-25d74f0607b2"><div style="width:728px;height:90px; "><iframe id="adopB7061" frameborder="0" marginwidth="0" marginheight="0" paddingwidth="0" paddingheight="0" scrolling="no" style="width: 100%; height: 100%;"></iframe></div></ins>
</div>
<script>(function(){var js = "window['__CF$cv$params']={r:'7831a27b3b184da5',m:'h1H4oFPwIcE.Oew8GXpe7TScNn9M8YeEnPTbLil7Xms-1672643005-0-Abt9mYg8q63DpPx4935Tm0zASRHCgGFNg6+KyBqLX22TA2auOkwzwTOgs/2RxElUHDys3WN8yt/vnTGkcNARdrRu6jR1OGTfQMxdP2DtW0rqjEcWGabNemybuM5TNWpbYQ==',s:[0xdba7e83c7b,0x5db272b147],u:'/cdn-cgi/challenge-platform/h/g'};var now=Date.now()/1000,offset=14400,ts=''+(Math.floor(now)-Math.floor(now%offset)),_cpo=document.createElement('script');_cpo.nonce='',_cpo.src='/cdn-cgi/challenge-platform/h/g/scripts/alpha/invisible.js?ts='+ts,document.getElementsByTagName('head')[0].appendChild(_cpo);";var _0xh = document.createElement('iframe');_0xh.height = 1;_0xh.width = 1;_0xh.style.position = 'absolute';_0xh.style.top = 0;_0xh.style.left = 0;_0xh.style.border = 'none';_0xh.style.visibility = 'hidden';document.body.appendChild(_0xh);function handler() {var _0xi = _0xh.contentDocument || _0xh.contentWindow.document;if (_0xi) {var _0xj = _0xi.createElement('script');_0xj.nonce = '';_0xj.innerHTML = js;_0xi.getElementsByTagName('head')[0].appendChild(_0xj);}}if (document.readyState !== 'loading') {handler();} else if (window.addEventListener) {document.addEventListener('DOMContentLoaded', handler);} else {var prev = document.onreadystatechange || function () {};document.onreadystatechange = function (e) {prev(e);if (document.readyState !== 'loading') {document.onreadystatechange = prev;handler();}};}})();</script><iframe height="1" width="1" style="position: absolute; top: 0px; left: 0px; border: none; visibility: hidden;"></iframe><script src="//compass.adop.cc/ST/949e3aab-fbcb-4bc6-9c49-20bfe80a5239"></script> <script async="" src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"></script>
 <script>
   var adoptagdfp = "ZXZhbChmdW5jdGlvbihwLGEsYyxrLGUsZCl7ZT1mdW5jdGlvbihjKXtyZXR1cm4oYzxhPycnOmUocGFyc2VJbnQoYy9hKSkpKygoYz1jJWEpPjM1P1N0cmluZy5mcm9tQ2hhckNvZGUoYysyOSk6Yy50b1N0cmluZygzNikpfTtpZighJycucmVwbGFjZSgvXi8sU3RyaW5nKSl7d2hpbGUoYy0tKXtkW2UoYyldPWtbY118fGUoYyl9az1bZnVuY3Rpb24oZSl7cmV0dXJuIGRbZV19XTtlPWZ1bmN0aW9uKCl7cmV0dXJuJ1xcdysnfTtjPTF9O3doaWxlKGMtLSl7aWYoa1tjXSl7cD1wLnJlcGxhY2UobmV3IFJlZ0V4cCgnXFxiJytlKGMpKydcXGInLCdnJyksa1tjXSl9fXJldHVybiBwfSgnNCA1PTV8fHt9OzUubD01Lmx8fFtdOzQgbT1tfHxDKGMsZCxnLGIpezQgZj0hMCxoPSIvL0IuRi5vL3EvIitiLGU9IkgiK2kuQSh5KmkuRCgpKSsxOy0xIT1iLkcoIi8vIikmJihmPSExKTs0IGE9My5FKCJ4Iik7YS4yKCJ3IixlKTthLjIoInAiLCJuIik7YS4yKCJyIiwwKTthLjIoInMiLDApO2EuMigidiIsMCk7YS4yKCJ1IiwwKTthLjIoInQiLDApO2EuMigieiIsZCk7YS4yKCJaIixnKTthLjIoIlgiLCJJIik7ZD0iPDkgaz1cJyIraCsiXCc+Vi85PiI7aihjPTMuNihjKSl7VShjLjIoIlkiLCJXIik7Yy5TKCk7KWMuTShjLlQpO2MuTChhKX1LIDggNztqKCJKIj09Yik4IDc7Zj8oYT0zLjYoZSksYj1hLk58fGEuTy4zLDchPWImJihiLlIoKSxiLlEoZCksYi5QKCkpKTooYT0zLjYoZSksYS5rPWIpfTsnLDYyLDYyLCd8fHNldEF0dHJpYnV0ZXxkb2N1bWVudHx2YXJ8Z29vZ2xldGFnfGdldEVsZW1lbnRCeUlkfG51bGx8cmV0dXJufHNjcmlwdHx8fHx8fHx8fE1hdGh8aWZ8c3JjfGNtZHxhZG9wQURzaG93fG5vbmV8Y2N8Ym9yZGVyfFJFfGZyYW1lQm9yZGVyfG1hcmdpbldpZHRofHBhZGRpbmdIZWlnaHR8cGFkZGluZ1dpZHRofG1hcmdpbkhlaWdodHxpZHxJRlJBTUV8MUU0fHdpZHRofGZsb29yfGNvbXBhc3N8ZnVuY3Rpb258cmFuZG9tfGNyZWF0ZUVsZW1lbnR8YWRvcHxpbmRleE9mfGFkb3BCfG5vfEFET1BfUEJVfGVsc2V8YXBwZW5kQ2hpbGR8cmVtb3ZlQ2hpbGR8Y29udGVudERvY3VtZW50fGNvbnRlbnRXaW5kb3d8Y2xvc2V8d3JpdGV8b3BlbnxoYXNDaGlsZE5vZGVzfGZpcnN0Q2hpbGR8Zm9yfDx8YWRzYnlhZG9wX3xzY3JvbGxpbmd8Y2xhc3N8aGVpZ2h0Jy5zcGxpdCgnfCcpLDAse30pKTs="
   eval(atob(adoptagdfp));
        let setPassback=function(){window.addEventListener("load",adopInterstitial("div-apt-ad-vdwzj2IPkN",300,250,"178a6dba-3c89-4633-9504-2cc984da4889",5))},adopInterstitial=function(e,t,n,o,i){frequency.check(i)&&36==o.length&&document.addEventListener("DOMContentLoaded",function(){trackingA.process(),makeAdsTemplate(e,t,n),adopADshow(e,t,n,o)})},trackingA={process:function(){let e=document.querySelectorAll("a"),t=window.location.hostname;e.forEach(function(e){let n=e.href;n.indexOf("//")>-1&&n.indexOf(t)>-1?trackingA.changeEvent(e,n):-1==n.indexOf("//")&&trackingA.changeEvent(e,n)}),historyBack()},changeEvent:function(e,t){e.addEventListener("click",function(e){e.preventDefault(),changeUrl(),showInterstitial(t)})}},historyBack=function(){window.onpopstate=function(e){"hidden"==document.body.style.overflow&&(document.documentElement.style.overflow="",document.body.style.overflow="",document.getElementById("adopInterstitial").style.display="none")}},changeUrl=function(){let e=document.location.href;-1==e.indexOf("#adopInterstitial")&&(document.location.href=e+"#adopInterstitial")},makeAdsTemplate=function(e,t,n){let o=document.createElement("div");o.id="adopInterstitial",o.setAttribute("style","width:100%; height:100%; position:fixed; top:0px; left:0px; background-color:rgba(0,0,0); z-index: 2147483647;"),o.style.display="none";let i=document.createElement("div");i.id="interstitialClose",i.setAttribute("style","display: inline-block; position: absolute; right: 0px;top: 0px; width: 30px; height: 30px; font-size: 40px; text-align: center; line-height: 30px; transform: scale(1,.8); font-family: sans-serif; color: #fff; padding: 5px;"),i.textContent="x";let l=document.createElement("div");l.id=e,l.setAttribute("style","width: "+t+"px; height: "+n+"px; background: #000; position: fixed; top: 0px; left: 0px; right: 0px; bottom: 0; margin: auto;"),o.appendChild(l),o.appendChild(i),document.body.appendChild(o)},showInterstitial=function(e){frequency.set(),document.documentElement.style.overflow="hidden",document.body.style.overflow="hidden",document.getElementById("adopInterstitial").style.display="block",document.getElementById("interstitialClose").addEventListener("click",function(){document.location.href=e}),document.getElementById("adopInterstitial").addEventListener("click",function(){setTimeout(function(){document.location.href=e},1e3)})},frequency={set:function(){let e={timestamp:(new Date).getTime()};localStorage.setItem("adop-interstitial",JSON.stringify(e))},check:function(e,t){let n=t;if(null==t){let e=JSON.parse(localStorage.getItem("adop-interstitial"));if(null==e)return!0;n=e.timestamp}if(null==n)return!0;let o=(new Date).getTime()-n;return!(Math.floor(o/6e4)<=e)},chkGoogle:function(){let e=localStorage.getItem("__lsv__");return null!=e&&(e=e.replace("[","").replace("]","")),frequency.check(60,e)}},refCheck=function(){let e=document.referrer;if(""!=e){return e=new 
URL(document.referrer).hostname,["m.search.naver.com","m.search.daum.net"].includes(e)}return!1};
 </script>
 <script>
 if (!refCheck()) {
        window.googletag = window.googletag || {cmd: []};
        if (frequency.chkGoogle()) {
          googletag.cmd.push(function() {
          var slot = googletag.defineOutOfPageSlot('/223513049,22526065422/ca-pub-5111137191506013-tag/linegeenet_content_id_m_interstitial-2_360', googletag.enums.OutOfPageFormat.INTERSTITIAL);
          if (slot) slot.addService(googletag.pubads());
          googletag.pubads().set("page_url", "linegee.net");
          googletag.pubads().addEventListener('slotRenderEnded', function(event) {
            if (event.isEmpty) {
                setPassback();
                }
          });
          googletag.enableServices();
          googletag.display(slot);
        });
        }else {
                setPassback();
        }
 }
 </script>
 <div style="position: absolute; left: -10000px; top: 0px; overflow: hidden; width:1px; height: 1px;"><script src="//data.adop.cc/collect.php?log=com_imp&amp;dt=20230102070326&amp;aid=103f007d-38ef-4cc5-bfe9-df2233c0e3c9&amp;zid=949e3aab-fbcb-4bc6-9c49-20bfe80a5239&amp;r=wSls" style="width:1px; height:1px;"></script><iframe src="https://c734aeae0d6f757f2a7840380fa1c01d.safeframe.googlesyndication.com/safeframe/1-0-40/html/container.html" style="visibility: hidden; display: none;"></iframe></div>

</body></html>'''

link_regex = r"location\.href\s*=\s*atob\('(.*?)'\)"

link = base64.b64decode(re.search(link_regex, doc).group(1)).decode('utf-8')
print(link)
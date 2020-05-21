from pathlib import Path
import shutil


COMMERCIAL_HEADER_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>Last Eleven</title>

  <!-- Favicons -->
<!--  <link href="assets/img/favicon.png" rel="icon">-->
<!--  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">-->
  <link rel="icon" href="../images/cropped-ico.png?w=32" sizes="32x32" />
  <link rel="icon" href="../images/cropped-ico.png?w=192" sizes="192x192" />
  <link rel="apple-touch-icon" href="../images/cropped-ico.png?w=180" />
  <meta name="msapplication-TileImage" content="../images/cropped-ico.png?w=270" />

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css?family=Quattrocento+Sans:r,i,b,bi&subset=latin,latin-ext" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="../assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="../assets/vendor/ionicons/css/ionicons.min.css" rel="stylesheet">
  <link href="../assets/vendor/animate.css/animate.min.css" rel="stylesheet">
  <link href="../assets/vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet">
  <link href="../assets/vendor/venobox/venobox.css" rel="stylesheet">

  <!-- Template Main CSS File -->
  <link href="../assets/css/style.css" rel="stylesheet">
</head>

<body>

  <!-- ======= Header ======= -->
  <header id="header">
    <div class="container">

      <div id="logo" class="pull-left">
        <!-- <h1><a href="/" class="scrollto">Avilon</a></h1>-->
        <!-- Uncomment below if you prefer to use an image logo -->
        <a href="/"><img src="../images/last-eleven1.png" alt="logo" width="179" height="51"></a>
      </div>

      <nav id="nav-menu-container">
        <ul class="nav-menu">
          <li><a href="/">Home</a></li>
          <li><a href="/">About</a></li>
          <li class="menu-active"><a href="commercial">Work</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </nav><!-- #nav-menu-container -->
    </div>
  </header><!-- End Header -->

  <!-- ======= Intro Section ======= -->
<!--  <section id="intro-subpage">-->

<!--    <div class="intro-text-subpage">-->
<!--      <a href="/">-->
<!--        <img src="../images/last-eleven1.png" alt="logo" width="357" height="102">-->
<!--      </a>-->
<!--    </div>-->

<!--  </section>&lt;!&ndash; End Intro Section &ndash;&gt;-->

  <main id="main">
    <section id="team" class="section-bg">
      <div class="container">
        <div class="section-header">
          <h3 class="section-title">WORK</h3>
          <p class="section-description">UNDERSTANDING WHAT OUR CLIENTS WANT TO COMMUNICATE WITH THEIR TARGET AUDIENCE, LAST ELEVEN HELPS THEM EXECUTE THEIR PERSPECTIVE WITH CONSTRUCTIVE INPUTS AND IDEATION.</p>
        </div>
        <div class="row wow fadeInUp">
'''

COMMERCIAL_FOOTER_TEMPLATE = '''
        </div>

        <div class="section-header">
          <div class="section-description">
            <a href="https://www.facebook.com/lastXI/"><i class="fa fa-facebook"></i></a>
            <a href="https://www.instagram.com/last.eleven/"><i class="fa fa-instagram"></i></a>
          </div>
        </div>
      </div>
    </section>

  </main><!-- End #main -->

  <a href="#" class="back-to-top"><i class="fa fa-chevron-up"></i></a>

  <!-- Vendor JS Files -->
  <script src="../assets/vendor/jquery/jquery.min.js"></script>
  <script src="../assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="../assets/vendor/jquery.easing/jquery.easing.min.js"></script>
  <script src="../assets/vendor/php-email-form/validate.js"></script>
  <script src="../assets/vendor/wow/wow.min.js"></script>
  <script src="../assets/vendor/venobox/venobox.min.js"></script>
  <script src="../assets/vendor/superfish/superfish.min.js"></script>
  <script src="../assets/vendor/hoverIntent/hoverIntent.js"></script>

  <!-- Template Main JS File -->
  <script src="../assets/js/main.js"></script>

</body>

</html>
'''


COMMERCIAL_NESTED_HEADER_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>Last Eleven</title>

  <!-- Favicons -->
<!--  <link href="assets/img/favicon.png" rel="icon">-->
<!--  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">-->
  <link rel="icon" href="../../images/cropped-ico.png?w=32" sizes="32x32" />
  <link rel="icon" href="../../images/cropped-ico.png?w=192" sizes="192x192" />
  <link rel="apple-touch-icon" href="../../images/cropped-ico.png?w=180" />
  <meta name="msapplication-TileImage" content="../../images/cropped-ico.png?w=270" />

  <!-- Google Fonts -->
<!--  <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,700|Open+Sans:300,300i,400,400i,700,700i" rel="stylesheet">-->
  <link href="https://fonts.googleapis.com/css?family=Quattrocento+Sans:r,i,b,bi&subset=latin,latin-ext" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="../../assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="../../assets/vendor/ionicons/css/ionicons.min.css" rel="stylesheet">
  <link href="../../assets/vendor/animate.css/animate.min.css" rel="stylesheet">
  <link href="../../assets/vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet">
  <link href="../../assets/vendor/venobox/venobox.css" rel="stylesheet">

  <!-- Template Main CSS File -->
  <link href="../../assets/css/style.css" rel="stylesheet">
</head>

<body>

  <!-- ======= Header ======= -->
  <header id="header">
    <div class="container">

      <div id="logo" class="pull-left">
        <!-- <h1><a href="/" class="scrollto">Avilon</a></h1>-->
        <!-- Uncomment below if you prefer to use an image logo -->
        <a href="/"><img src="../../images/last-eleven1.png" alt="logo" width="179" height="51"></a>
      </div>

      <nav id="nav-menu-container">
        <ul class="nav-menu">
          <li><a href="/">Home</a></li>
          <li><a href="/">About</a></li>
          <li class="menu-active"><a href="/commercial">Work</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </nav><!-- #nav-menu-container -->
    </div>
  </header><!-- End Header -->

  <main id="main">

    <section id="more-features" class="section-bg">
      <div class="container">

        <div class="section-header">
          <h3 class="section-title">WORK</h3>
        </div>
'''

COMMERCIAL_NESTED_FOOTER_TEMPLATE = '''

        <div class="section-header">
          <div class="section-description">
            <a href="https://www.facebook.com/lastXI/"><i class="fa fa-facebook"></i></a>
            <a href="https://www.instagram.com/last.eleven/"><i class="fa fa-instagram"></i></a>
          </div>
        </div>

      </div>
    </section><!-- End More Features Section -->

  </main><!-- End #main -->


  <!-- Vendor JS Files -->
  <script src="../../assets/vendor/jquery/jquery.min.js"></script>
  <script src="../../assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="../../assets/vendor/jquery.easing/jquery.easing.min.js"></script>
  <script src="../../assets/vendor/php-email-form/validate.js"></script>
  <script src="../../assets/vendor/wow/wow.min.js"></script>
  <script src="../../assets/vendor/venobox/venobox.min.js"></script>
  <script src="../../assets/vendor/superfish/superfish.min.js"></script>
  <script src="../../assets/vendor/hoverIntent/hoverIntent.js"></script>

  <!-- Template Main JS File -->
  <script src="../../assets/js/main.js"></script>

</body>

</html>
'''

DATA = [
  ('CL Educate', 'cl.png', 'https://vimeo.com/214524113'),
  ('WordPress', 'wordpress.jpg', 'https://vimeo.com/manage/300251921'),
  ('Bonbon - Lingerie Photo Shoot', 'bon-bon.jpg', 'https://www.youtube.com/watch?v=nHL9GHeF34w'),
  ('Close Up TVC | Behind the Scenes', 'close1.jpg', 'https://vimeo.com/manage/139195265'),
  ('Real Brides, Real Curves', 'real.jpg', 'https://vimeo.com/manage/157485778'),
  ('Dream Girl | Music Video | Rohan Solomon', 'dream.jpg', 'https://www.youtube.com/watch?v=iiZkCkeuT6w'),
  ('Bhartiya', 'uncompete.png', 'https://vimeo.com/manage/191852566'),
  ('Vogue Wedding Show 2017', 'vogue-last.jpg', 'https://vimeo.com/manage/236537544'),
  ('National Anthem by Sarod Maestros', 'national-anthem.png', 'https://www.youtube.com/watch?v=vH1jLzINhqY'),
  ('Vaishno Jan To', 'vaishnav-jan-to.jpg', 'https://www.youtube.com/watch?v=mnL1DoYczgA'),
  ('Hussain Saify | GoDaddy', 'hus.jpg', 'https://vimeo.com/manage/300249184/'),
  ('Rohit Bal Good Earth | Collaboration', 'good1.jpg', 'https://www.youtube.com/watch?v=Mz8f9a2Y0Po'),
  ('Rupa BTS with Ranveer Singh', 'ranveer.jpg', 'https://vimeo.com/126467704'),
  ('Rajesh Pratap Singh | Chivas', 'rajes.jpg', 'https://vimeo.com/manage/91403197/'),
  ('Rohit Bal | Chivas Studio', 'rohit.jpg', 'https://vimeo.com/manage/54756583/'),
  ('“The Heist” – Label Ritu Kumar Spring Summer 2013', 'maxresdefault.jpg', 'https://www.youtube.com/watch?v=kcYEfrKie3A'),
  ('Minimalism by Wendell Rodricks', 'wende.jpg', 'https://vimeo.com/84950178'),
  ('Behind the Scenes – Do the REX', 'rex.jpg', 'https://vimeo.com/92388541'),
  ('Absolut Kapoor', 'absolute-kapoor.png', 'https://www.youtube.com/watch?v=RK4B-0iBIhI'),
  ('Alia Bhatt for Jabong', 'alia1.jpg', 'https://www.youtube.com/watch?v=Keb6FGC8GXU'),
  ('Journey – Ayaan and Amaan Ali Khan', 'journey.jpg', 'https://www.youtube.com/watch?v=oisXWtKI_bg'),
  ('Old Delhi Motorcycles | The Film', 'old-delhi-motorcycles.jpeg', 'https://www.youtube.com/watch?v=O-JwZfLKX1U'),
]


def generate_html():
    dir_path = Path('commercial')
    if dir_path.exists() and dir_path.is_dir():
        shutil.rmtree(dir_path)

    filepath = Path("commercial/index.html")
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with filepath.open("w", encoding="utf-8") as f:
        commercial_template = COMMERCIAL_HEADER_TEMPLATE
        for page in DATA:
            page_url = page[1].split('.')[0]
            page_template = """

            <div class="col-lg-3 col-md-6">
              <div class="member">
                <div class="pic"><a href="{page_url}"><img src="../images/{thumbnail}" alt="{alt_text}"></a></div>
                <h4><a href="{page_url}">{title}</a></h4>
              </div>
            </div>
            """.format(title=page[0], page_url=page_url, thumbnail=page[1], alt_text=f'{page[0]} thumbnail')
            commercial_template += page_template
        commercial_template += COMMERCIAL_FOOTER_TEMPLATE
        f.write(commercial_template)

    for page in DATA:
        page_url = page[1].split('.')[0]
        filepath = Path(f"commercial/{page_url}/index.html")
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with filepath.open("w", encoding="utf-8") as f:
            commercial_nested_template = COMMERCIAL_NESTED_HEADER_TEMPLATE
            link = page[2]
            if 'vimeo' in link:
                link = f'https://player.vimeo.com/video/{link.split("/")[-1]}'
            page_template = """

            <div class="section-header">
              <div class="embed-responsive embed-responsive-16by9" id="embed">
                <iframe class="embed-responsive-item" src="{link}" allowfullscreen></iframe>
              </div>
            </div>
            """.format(link=link)
            commercial_nested_template += page_template
            commercial_nested_template += COMMERCIAL_NESTED_FOOTER_TEMPLATE
            f.write(commercial_nested_template)


generate_html()

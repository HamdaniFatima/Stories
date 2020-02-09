Install the pip (Python Package Installer) 
get-pip.py 
python get-pip.py 
pip install virtualenv
cd Stories\Innovation
Virtualen en 



Instruction

1/ pwd
 2/ git clone https://github.com/HamdaniFatima/Innovation
 3/  mkvirtualenv --python=/usr/bin/python3.5  myenv
 


python manage.py makemessages -l en
python manage.py compilemessages -l en





url : https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/
python -m venv %systemdrive%%homepath%\my-venv
%systemdrive%%homepath%\my-venv\Scripts\activate.bat
url : https://www.techcoil.com/blog/how-to-create-a-python-3-virtual-environment-in-windows-10/
python -m venv %systemdrive%%homepath%\my-venv


Tool for Youtube : http://scriptgenerator.net/valid-xhtml-youtube-embed-code/

     <table class="table table-bordered">
                            <thead>
                              <tr>
                                <th><a style ="color: aliceblue;">Storie Title</a></th>
                                <th><a style ="color: aliceblue;">Used Process</a></th>
                                <th><a style ="color: aliceblue;">More Details</a></th>
                              
                              </tr>
                            </thead>
                            <tbody>
                              {% for user in filter.qs %}
                                <tr>
                                  <td><a  style ="color: aliceblue;">{{ user.title_case }}</a></td>
                                  <td><a  style ="color: aliceblue;">{{ user.processus_name }}</a></td>
                                  <td>   <a href="{% url 'students:post_detail' user.pk %}" class="btn btn-info" role="button">More Details</a></td>
                               
                                 
                                </tr>
                              {% empty %}
                                <tr>
                                  <td colspan="5"><h8 style ="color: aliceblue;">No data availbe about this Case Study</h8></td>
                                </tr>
                              {% endfor %}
                            </tbody>
                          </table>





    quiz = get_object_or_404(Cases, pk=pk)
    teacher = request.user.teacher
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.case = quiz
            question.teacher = teacher
            question.save()
            question.case.evaluer == True
            question.case.state = question.state
            messages.success(request, 'You may now add answers/options to the question.')
            
    else:
        return render(request, 'classroom/teachers/board/forms.html', {'quiz': quiz})











                                <form method= "get"  class="form-wrap mt-4">
                                    <div class="btn-group" role="group" aria-label="Basic example">
                                       <!---------------<input type="text" placeholder="What are your searching for?" class="btn-group1">-----------> 
                                       <!---------<input type="text" placeholder="Subject" class="btn-group2">--------------------> 
                                       {{ filter.form.as_p}}
                                        <button type="submit" class="btn-form"><span class="icon-magnifier search-icon"></span>SEARCH<i class="pe-7s-angle-right"></i></button>
                                    </div>
                                </form>
                                <ul>
                                    {% for user in filter.qs %}
                                      <li>{{ user.school_case }} - {{ user.title_case }}</li>
                                 
                                    {% endfor %}
                                    </ul>
                                <div class="slider-link">
                                    <a href="#">Browse Popular</a><span>or</span> <a href="{% url 'Stories' %}">Recently Added</a>





















{% load static %}


<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>Introduction</title>
        
<!-- 

Sentra Template

https://templatemo.com/tm-518-sentra

-->
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="apple-touch-icon" href="{% static 'Introduction/Temp_518/apple-touch-icon.png' %}">

        <link rel="stylesheet" href="{% static 'Introduction/Temp_518/css/bootstrap.min.css' %}">
        <link rel="stylesheet" href="{% static 'Introduction/Temp_518/css/bootstrap-theme.min.css' %}">
        <link rel="stylesheet" href="{% static 'Introduction/Temp_518/css/fontAwesome.css' %}">
        <link rel="stylesheet" href="{% static 'Introduction/Temp_518/css/light-box.css' %}">
        <link rel="stylesheet" href="{% static 'Introduction/Temp_518/css/owl-carousel.css' %}">
        <link rel="stylesheet" href="{% static 'Introduction/Temp_518/css/templatemo-style.css'%}">

        <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700,800" rel="stylesheet">

        <script src="{% static 'Introduction/Temp_518/js/vendor/modernizr-2.8.3-respond-1.4.2.min.js' %}"></script>
    </head>

<body>



        <header class="nav-down responsive-nav hidden-lg hidden-md">
            <button type="button" id="nav-toggle" class="navbar-toggle" data-toggle="collapse" data-target="#main-nav">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <!--/.navbar-header-->
            <div id="main-nav" class="collapse navbar-collapse">
                <nav>
                    <ul class="nav navbar-nav">
                        <li><a href="#top">Home</a></li>
                        <li><a href="#featured">Featured</a></li>
                        <li><a href="#projects">Recent Projects</a></li>
                        <li><a href="#video">Presentation</a></li>
                        <li><a href="#blog">Blog Entries</a></li>
                        <li><a href="#contact">Contact Us</a></li>
                    </ul>
                </nav>
            </div>
        </header>

        <div class="sidebar-navigation hidde-sm hidden-xs">

            <nav>
                <ul>
                    <li>
                        <a href="#top">
                            <span class="rect"></span>
                            <span class="circle"></span>
                            Home
                        </a>
                    </li>
                    <li>
                        <a href="#featured">
                            <span class="rect"></span>
                            <span class="circle"></span>
                            Featured
                        </a>
                    </li>
                    <li>
                        <a href="#projects">
                            <span class="rect"></span>
                            <span class="circle"></span>
                            Recent Work
                        </a>
                    </li>
                    <li>
                        <a href="#video">
                            <span class="rect"></span>
                            <span class="circle"></span>
                            Presentation
                        </a>
                    </li>
                    <li>
                        <a href="#blog">
                            <span class="rect"></span>
                            <span class="circle"></span>
                            Blog Entires
                        </a>
                    </li>
                    <li>
                        <a href="#contact">
                            <span class="rect"></span>
                            <span class="circle"></span>
                            Contact Us
                        </a>
                    </li>
                </ul>
            </nav>
            <ul class="social-icons">
                <li><a href="#"><i class="fa fa-facebook"></i></a></li>
                <li><a href="#"><i class="fa fa-twitter"></i></a></li>
                <li><a href="#"><i class="fa fa-linkedin"></i></a></li>
                <li><a href="#"><i class="fa fa-rss"></i></a></li>
                <li><a href="#"><i class="fa fa-behance"></i></a></li>
            </ul>
        </div>

        <div class="slider">
            <div class="Modern-Slider content-section" id="top">
                <!-- Item -->
                <div class="item item-1">
                    <div class="img-fill">
                    <div class="image"></div>
                    <div class="info">
                        <div>
                          <h1>Innovation Stories<br>Application</h1>
                          <p>Innovation Stories is a free collaborative platform for easily creating,<br>
                            and consulting innovation case studies. </p>
                          <div class="white-button button">
                              <a href="#featured">Discover More</a>
                          </div>
                        </div>
                        </div>
                    </div>
                </div>



           




                <!-- // Item -->
                <!-- Item -->
                <div class="item item-2">
                    <div class="img-fill">
                        <div class="image"></div>
                        <div class="info">
                        <div>
                          <h1>You are an <br>Expert</h1>
                          <p> Evaluate Innovation sotries based on your interests.
							<br>Thank you for joining us.</p>
                          
                          <div class="white-button button">
                              <a href="">Share More</a>
                          </div>
                        </div>
                        </div>
                    </div>
                </div>
                <!-- // Item -->
                <!-- Item -->
                <div class="item item-3">
                    <div class="img-fill">
                        <div class="image"></div>
                        <div class="info">
                        <div>
                          <h1>You are a <br>Student</h1>
                          <p>If you are new to Innovation Stories, get started.
                                <br>Thank you for joining us.</p>
                            </p>
                          
                          <div class="white-button button">
                              <a href="{% url 'students:students_home' %}">Learn More</a>
                          </div>
                        </div>
                        </div>
                    </div>
                </div>
                <!-- // Item -->
            </div>
        </div>


        <div class="page-content">
            <section id="featured" class="content-section">
                <div class="section-heading">
                    <h1>About<br><em>Us</em></h1>
                    <p>The ERPI (Research team on innovation process)  is a research team on Industrial Engineering specialized on the research of innovation processes management.
                    <br><a href="https://erpi.univ-lorraine.fr/"> More........</a></p>
                </div>
                <div class="section-content">
                    <div class="owl-carousel owl-theme">
                        <div class="item">
                            <div class="image">
                                <img src="{% static 'Introduction/Temp_518/img/featured_1.jpg'%}" alt="">
                                <div class="featured-button button">
                                    <a href="#projects">Continue Reading</a>
                                </div>
                            </div>
                            <div class="text-content">
                                <h4>Lorem ipsum dolor</h4>
                                <span>Proin et sapien</span>
                                <p>#1 You are allowed to use Sentra Template for your business or client websites. You can use it for commercial or non-commercial or educational purposes.</p>
                            </div>
                        </div>
                        <div class="item">
                            <div class="image">
                                <img src="{% static 'Introduction/Temp_518/img/featured_2.jpg' %}" alt="">
                                <div class="featured-button button">
                                    <a href="#projects">Continue Reading</a>
                                </div>
                            </div>
                            <div class="text-content">
                                <h4>Phasellus a lacus ac odio</h4>
                                <span>Maximus</span>
                                <p>#2 You are NOT allowed to re-distribute this on any template website. You <strong>can post</strong> a screenshot and a link back to original template page on your blog or site. Thank you.</p>
                            </div>
                        </div>
                        <div class="item">
                            <div class="image">
                                <img src="{%static 'Introduction/img/featured_3.jpg" alt="">
                                <div class="featured-button button">
                                    <a href="#projects">Continue Reading</a>
                                </div>
                            </div>
                            <div class="text-content">
                                <h4>Proin sit amet fringilla</h4>
                                <span>Vulputate</span>
                                <p>#3 Aliquam mollis lacus eget metus efficitur lobortis. Suspendisse libero lacus, accumsan vitae commodo tristique, luctus gravida metus.</p>
                            </div>
                        </div>
                        <div class="item">
                            <div class="image">
                                <img src="img/featured_2.jpg" alt="">
                                <div class="featured-button button">
                                    <a href="#projects">Continue Reading</a>
                                </div>
                            </div>
                            <div class="text-content">
                                <h4>In volutpat augue lectus</h4>
                                <span>Elementum</span>
                                <p>#4 Aliquam mollis lacus eget metus efficitur lobortis. Suspendisse libero lacus, accumsan vitae commodo tristique, luctus gravida metus.</p>
                            </div>
                        </div>
                        <div class="item">
                            <div class="image">
                                <img src="img/featured_1.jpg" alt="">
                                <div class="featured-button button">
                                    <a href="#projects">Continue Reading</a>
                                </div>
                            </div>
                            <div class="text-content">
                                <h4>Cras commodo odio</h4>
                                <span>Aliquam</span>
                                <p>#5 Mauris lacinia pretium libero, ut tincidunt lacus molestie ornare. Phasellus a facilisis erat. Praesent eleifend nibh mauris, quis sodales lorem convallis pulvinar.</p>
                            </div>
                        </div>
                        <div class="item">
                            <div class="image">
                                <img src="img/featured_3.jpg" alt="">
                                <div class="featured-button button">
                                    <a href="#projects">Continue Reading</a>
                                </div>
                            </div>
                            <div class="text-content">
                                <h4>Sed at massa turpis</h4>
                                <span>Curabitur</span>
                                <p>#6 Vestibulum tincidunt ornare ligula vel molestie. Curabitur hendrerit mauris mollis ipsum vulputate rutrum. Phasellus luctus odio eget dui imperdiet.</p>
                            </div>
                        </div>
                        <div class="item">
                            <div class="image">
                                <img src="img/featured_2.jpg" alt="">
                                <div class="featured-button button">
                                    <a href="#projects">Continue Reading</a>
                                </div>
                            </div>
                            <div class="text-content">
                                <h4>Aliquam mollis lacus</h4>
                                <span>Suspendisse</span>
                                <p>#7 Suspendisse suscipit nulla sed nisl fermentum, auctor suscipit nunc rhoncus. Proin faucibus metus diam, nec hendrerit purus pharetra in.</p>
                            </div>
                        </div>
                        <div class="item">
                            <div class="image">
                                <img src="{%static 'Introduction/Temp_518/img/featured_1.jpg' %}" alt="">
                                <div class="featured-button button">
                                    <a href="#projects">Continue Reading</a>
                                </div>
                            </div>
                            <div class="text-content">
                                <h4>Mauris lacinia pretium</h4>
                                <span>Vestibulum</span>
                                <p>#8 Suspendisse suscipit nulla sed nisl fermentum, auctor suscipit nunc rhoncus. Proin faucibus metus diam, nec hendrerit purus pharetra in.</p>
                            </div>
                        </div>
                        <div class="item">
                            <div class="image">
                                <img src="{% static 'Introduction/Temp_518/img/featured_3.jpg' %}" alt="">
                                <div class="featured-button button">
                                    <a href="#projects">Continue Reading</a>
                                </div>
                            </div>
                            <div class="text-content">
                                <h4>Proin sit amet fringilla erat</h4>
                                <span>Convallis</span>
                                <p>#9 Suspendisse suscipit nulla sed nisl fermentum, auctor suscipit nunc rhoncus. Proin faucibus metus diam, nec hendrerit purus pharetra in.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <section id="projects" class="content-section">
                <div class="section-heading">
                    <h1>Recent<br><em>Projects</em></h1>
                    <p>Praesent pellentesque efficitur magna, 
                    <br>sed pellentesque neque malesuada vitae.</p>
                </div>
                <div class="section-content">
                    <div class="masonry">
                        <div class="row">
                            <div class="item">
                                <div class="col-md-8">
                                    <a href="{% static 'Introduction/Temp_518/img/portfolio_big_1.jpg' %}" data-lightbox="image"><img src="{% static 'Intrduction/Temp_518/img/portfolio_1.jpg' %}" alt="image 1"></a>
                                </div>
                            </div>
                            <div class="item second-item">
                                <div class="col-md-4">
                                    <a href="img/portfolio_big_2.jpg" data-lightbox="image"><img src="img/portfolio_2.jpg" alt="image 2"></a>
                                </div>
                            </div>
                            <div class="item">
                                <div class="col-md-4">
                                    <a href="img/portfolio_big_3.jpg" data-lightbox="image"><img src="img/portfolio_3.jpg" alt="image 3"></a>
                                </div>
                            </div>
                            <div class="item">
                                <div class="col-md-4">
                                    <a href="img/portfolio_big_4.jpg" data-lightbox="image"><img src="img/portfolio_4.jpg" alt="image 4"></a>
                                </div>
                            </div>
                            <div class="item">
                                <div class="col-md-8">
                                    <a href="img/portfolio_big_5.jpg" data-lightbox="image"><img src="img/portfolio_5.jpg" alt="image 5"></a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>            
            </section>
            <section id="video" class="content-section">
                <div class="row">
                    <div class="col-md-12">
                        <div class="section-heading">
                            <h1>This is a <em>company</em> presentation.</h1>
                            <p>Praesent pellentesque efficitur magna, sed pellentesque neque malesuada vitae.</p>
                        </div>
                        <div class="text-content">
                            <p>In eget ipsum sed lorem vehicula luctus. Curabitur non dolor rhoncus, hendrerit justo sit amet, vestibulum turpis. Pellentesque id auctor tellus, vel ultricies augue. Duis condimentum aliquet blandit. Fusce rhoncus et eros ut pharetra. Phasellus convallis ultricies ligula ac gravida.</p>
                        </div>
                        <div class="accent-button button">
                            <a href="#blog">Continue Reading</a>
                        </div>
                    </div>
                    <div class="col-md-12">
                        <div class="box-video">
                            <div class="bg-video" style="background-image: url(https://unsplash.imgix.net/photo-1425036458755-dc303a604201?fit=crop&fm=jpg&q=75&w=1000);">
                                <div class="bt-play">Play</div>
                            </div>
                            <div class="video-container">
                                <iframe width="100%" height="520" src="https://www.youtube.com/embed/j-_7Ub-Zkow?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <section id="blog" class="content-section">
                <div class="section-heading">
                    <h1>Blog<br><em>Entries</em></h1>
                    <p>Curabitur hendrerit mauris mollis ipsum vulputate rutrum. 
                    <br>Phasellus luctus odio eget dui imperdiet.</p>
                </div>
                <div class="section-content">
                    <div class="tabs-content">
                        <div class="wrapper">
                            <ul class="tabs clearfix" data-tabgroup="first-tab-group">
                              <li><a href="#tab1" class="active">July 2018</a></li>
                              <li><a href="#tab2">June 2018</a></li>
                              <li><a href="#tab3">May 2018</a></li>
                              <li><a href="#tab4">April 2018</a></li>
                            </ul>
                            <section id="first-tab-group" class="tabgroup">
                                <div id="tab1">
                                    <ul>
                                        <li>
                                            <div class="item">
                                                <img src="{% static 'Introduction/Temp_518/img/blog_1.jpg' %}" alt="">
                                                <div class="text-content">
                                                    <h4>Integer ultrices augue</h4>
                                                    <span>25 July 2018</span>
                                                    <p>Nam vel egestas nisi. Nullam lobortis magna at enim venenatis luctus. Nam finibus, mauris eu dictum iaculis, dolor tortor cursus quam, in volutpat augue lectus sed magna. Integer mollis lorem quis ipsum maximus finibus.</p>
                                                    
                                                    <div class="accent-button button">
                                                        <a href="#contact">Continue Reading</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="item">
                                                <img src="{% static 'Introduction/Temp_518/img/blog_2.jpg' %}" alt="">
                                                <div class="text-content">
                                                    <h4>Cras commodo odio ut</h4>
                                                    <span>16 July 2018</span>
                                                    <p>Nam vel egestas nisi. Nullam lobortis magna at enim venenatis luctus. Nam finibus, mauris eu dictum iaculis, dolor tortor cursus quam, in volutpat augue lectus sed magna. Integer mollis lorem quis ipsum maximus finibus.</p>
                                                    
                                                    <div class="accent-button button">
                                                        <a href="#contact">Continue Reading</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="item">
                                                <img src="{% static 'Introduction/Temp_518/img/blog_3.jpg' %}" alt="">
                                                <div class="text-content">
                                                    <h4>Sed at massa turpis</h4>
                                                    <span>10 July 2018</span>
                                                    <p>Nam vel egestas nisi. Nullam lobortis magna at enim venenatis luctus. Nam finibus, mauris eu dictum iaculis, dolor tortor cursus quam, in volutpat augue lectus sed magna. Integer mollis lorem quis ipsum maximus finibus.</p>
                                                    
                                                    <div class="accent-button button">
                                                        <a href="#contact">Continue Reading</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                                <div id="tab2">
                                    <ul>
                                        <li>
                                            <div class="item">
                                                <img src="{% static 'Introduction/Temp_518/img/blog_3.jpg' %}" alt="">
                                                <div class="text-content">
                                                    <h4>Sed at massa turpis</h4>
                                                    <span>30 June 2018</span>
                                                    <p>Nam vel egestas nisi. Nullam lobortis magna at enim venenatis luctus. Nam finibus, mauris eu dictum iaculis, dolor tortor cursus quam, in volutpat augue lectus sed magna. Integer mollis lorem quis ipsum maximus finibus.</p>
                                                    
                                                    <div class="accent-button button">
                                                        <a href="#contact">Continue Reading</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="item">
                                                <img src="{% static 'Introduction/Temp_518/img/blog_1.jpg' %}" alt="">
                                                <div class="text-content">
                                                    <h4>Lorem ipsum dolor sit</h4>
                                                    <span>24 June 2018</span>
                                                    <p>Nam vel egestas nisi. Nullam lobortis magna at enim venenatis luctus. Nam finibus, mauris eu dictum iaculis, dolor tortor cursus quam, in volutpat augue lectus sed magna. Integer mollis lorem quis ipsum maximus finibus.</p>
                                                    
                                                    <div class="accent-button button">
                                                        <a href="#contact">Continue Reading</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="item">
                                                <img src="{% static 'introduction/Temp_518/img/blog_2.jpg' %}" alt="">
                                                <div class="text-content">
                                                    <h4>Cras commodo odio ut</h4>
                                                    <span>12 June 2018</span>
                                                    <p>Nam vel egestas nisi. Nullam lobortis magna at enim venenatis luctus. Nam finibus, mauris eu dictum iaculis, dolor tortor cursus quam, in volutpat augue lectus sed magna. Integer mollis lorem quis ipsum maximus finibus.</p>
                                                    
                                                    <div class="accent-button button">
                                                        <a href="#contact">Continue Reading</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                                <div id="tab3">
                                    <ul>
                                        <li>
                                            <div class="item">
                                                <img src="{% static 'Introduction/Temp_518/img/blog_2.jpg' %}" alt="">
                                                <div class="text-content">
                                                    <h4>Cras commodo odio ut</h4>
                                                    <span>26 May 2018</span>
                                                    <p>Nam vel egestas nisi. Nullam lobortis magna at enim venenatis luctus. Nam finibus, mauris eu dictum iaculis, dolor tortor cursus quam, in volutpat augue lectus sed magna. Integer mollis lorem quis ipsum maximus finibus.</p>
                                                    
                                                    <div class="accent-button button">
                                                        <a href="#contact">Continue Reading</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="item">
                                                <img src="{% static 'Introduction/Temp_518/img/blog_1.jpg' %}" alt="">
                                                <div class="text-content">
                                                    <h4>Lorem ipsum dolor sit</h4>
                                                    <span>22 May 2018</span>
                                                    <p>Nam vel egestas nisi. Nullam lobortis magna at enim venenatis luctus. Nam finibus, mauris eu dictum iaculis, dolor tortor cursus quam, in volutpat augue lectus sed magna. Integer mollis lorem quis ipsum maximus finibus.</p>
                                                    
                                                    <div class="accent-button button">
                                                        <a href="#contact">Continue Reading</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="item">
                                                <img src="{% static 'Introduction/Temp_518/img/blog_3.jpg' %}" alt="">
                                                <div class="text-content">
                                                    <h4>Integer ultrices augue</h4>
                                                    <span>8 May 2018</span>
                                                    <p>Nam vel egestas nisi. Nullam lobortis magna at enim venenatis luctus. Nam finibus, mauris eu dictum iaculis, dolor tortor cursus quam, in volutpat augue lectus sed magna. Integer mollis lorem quis ipsum maximus finibus.</p>
                                                    
                                                    <div class="accent-button button">
                                                        <a href="#contact">Continue Reading</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                                <div id="tab4">
                                    <ul>
                                        <li>
                                            <div class="item">
                                                <img src="{% static 'Introduction/Temp_518/img/blog_1.jpg'%}" alt="">
                                                <div class="text-content">
                                                    <h4>Lorem ipsum dolor sit</h4>
                                                    <span>26 April 2018</span>
                                                    <p>Nam vel egestas nisi. Nullam lobortis magna at enim venenatis luctus. Nam finibus, mauris eu dictum iaculis, dolor tortor cursus quam, in volutpat augue lectus sed magna. Integer mollis lorem quis ipsum maximus finibus.</p>
                                                    
                                                    <div class="accent-button button">
                                                        <a href="#contact">Continue Reading</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>                                
                                        <li>
                                            <div class="item">
                                                <img src="{% static 'Introduction/Temp_518/img/blog_3.jpg'%}" alt="">
                                                <div class="text-content">
                                                    <h4>Integer ultrices augue eu</h4>
                                                    <span>24 April 2018</span>
                                                    <p>Nam vel egestas nisi. Nullam lobortis magna at enim venenatis luctus. Nam finibus, mauris eu dictum iaculis, dolor tortor cursus quam, in volutpat augue lectus sed magna. Integer mollis lorem quis ipsum maximus finibus.</p>
                                                    
                                                    <div class="accent-button button">
                                                        <a href="#contact">Continue Reading</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="item">
                                                <img src="{% static 'Introdution/Temp_518/img/blog_2.jpg'%}" alt="">
                                                <div class="text-content">
                                                    <h4>Cras commodo odio ut</h4>
                                                    <span>20 April 2018</span>
                                                    <p>Nam vel egestas nisi. Nullam lobortis magna at enim venenatis luctus. Nam finibus, mauris eu dictum iaculis, dolor tortor cursus quam, in volutpat augue lectus sed magna. Integer mollis lorem quis ipsum maximus finibus.</p>
                                                    
                                                    <div class="accent-button button">
                                                        <a href="#contact">Continue Reading</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                            </section> 
                        </div>
                    </div>
                </div>
            </section>
            <section id="contact" class="content-section">
                <div id="map">
                
                	<!-- How to change your own map point
                           1. Go to Google Maps
                           2. Click on your location point
                           3. Click "Share" and choose "Embed map" tab
                           4. Copy only URL and paste it within the src="" field below
                    -->
                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2633.549262538899!2d6.1914682156685945!3d48.69498177927176!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4794983fc320d4b5%3A0xb05f011bc8e53da5!2sENSGSI%20-%20Groupe%20INP!5e0!3m2!1sfr!2sfr!4v1575649017554!5m2!1sfr!2sfr" width="100%" height="400px" frameborder="0" style="border:0" allowfullscreen></iframe>
                 
                
                </div>
                <div id="contact-content">
                    <div class="section-heading">
                        <h1>Contact<br><em>Sentra</em></h1>
                        <p>Curabitur hendrerit mauris mollis ipsum vulputate rutrum. 
                        <br>Phasellus luctus odio eget dui imperdiet.</p>
                        
                    </div>
                    <div class="section-content">
                        <form id="contact" action="#" method="post">
                            <div class="row">
                                <div class="col-md-4">
                                  <fieldset>
                                    <input name="name" type="text" class="form-control" id="name" placeholder="Your name..." required="">
                                  </fieldset>
                                </div>
                                <div class="col-md-4">
                                  <fieldset>
                                    <input name="email" type="email" class="form-control" id="email" placeholder="Your email..." required="">
                                  </fieldset>
                                </div>
                                 <div class="col-md-4">
                                  <fieldset>
                                    <input name="subject" type="text" class="form-control" id="subject" placeholder="Subject..." required="">
                                  </fieldset>
                                </div>
                                <div class="col-md-12">
                                  <fieldset>
                                    <textarea name="message" rows="6" class="form-control" id="message" placeholder="Your message..." required=""></textarea>
                                  </fieldset>
                                </div>
                                <div class="col-md-12">
                                  <fieldset>
                                    <button type="submit" id="form-submit" class="btn">Send Message Now</button>
                                  </fieldset>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </section>
            <section class="footer">
                <p>Copyright &copy; 2019 ERPI (Research team on innovation process)
                
                . Design: TemplateMo</p>
            </section>
        </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="js/vendor/jquery-1.11.2.min.js"><\/script>')</script>

    <script src="{% static 'Introduction/Temp_518/js/vendor/bootstrap.min.js"></script>
    
    <script src="{% static 'Introduction/Temp_518/js/plugins.js'%}"></script>
    <script src="{% static 'Introduction/Temp_518/js/main.js'%}"></script>

    <script>
        // Hide Header on on scroll down
        var didScroll;
        var lastScrollTop = 0;
        var delta = 5;
        var navbarHeight = $('header').outerHeight();

        $(window).scroll(function(event){
            didScroll = true;
        });

        setInterval(function() {
            if (didScroll) {
                hasScrolled();
                didScroll = false;
            }
        }, 250);

        function hasScrolled() {
            var st = $(this).scrollTop();
            
            // Make sure they scroll more than delta
            if(Math.abs(lastScrollTop - st) <= delta)
                return;
            
            // If they scrolled down and are past the navbar, add class .nav-up.
            // This is necessary so you never see what is "behind" the navbar.
            if (st > lastScrollTop && st > navbarHeight){
                // Scroll Down
                $('header').removeClass('nav-down').addClass('nav-up');
            } else {
                // Scroll Up
                if(st + $(window).height() < $(document).height()) {
                    $('header').removeClass('nav-up').addClass('nav-down');
                }
            }
            
            lastScrollTop = st;
        }
    </script>

    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js" type="text/javascript"></script>

</body>
</html>








Images : https://wsvincent.com/django-image-uploads/

 get texthttps://mlocati.github.io/articles/gettext-iconv-windows.html

			{% block content %}
									<div class="post">
										{% if post %}
											<div class="date">
												{{ post.published_date }}
											</div>
										{% endif %}
										<h2>{{ post.title_case}}</h2>
										{% if post.image_produit %}
										<picture><img src="{{ post.image_produit.url }}" alt="vous devez ajouter une figure"/></picture>
										 {% endif %}
										
										  </div>


git commit -m "initial commit"
git push origin master

Médical
Alimentaire
Agricole
Environnemental
Technologie
Aéronautique
Robotique
Astronomie
Mécatronique 
Electronique
Chimie
Biologie
Science
Biotechnologie
Mécanique
Géologie
Mathématiques
Physique 
Transport
Architecture
Télécommunications
Energie 
Medical
Agro-Food
Agriculture
Environmental
Technology
Aeronautics
Robotics
Astronomy
Mechatronics 
Electronics
Chemistry
Biology
Science
Biotechnology
Mechanics
Geology
Mathematics
Physical 
Transportation
Architecture
Telecommunications


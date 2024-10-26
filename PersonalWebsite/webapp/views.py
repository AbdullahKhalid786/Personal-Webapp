# views.py
import markdown
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from .models import Project, BlogPost
from .forms import OptionPriceForm
from .black_scholes import BlackScholes  # Import your Black-Scholes class
# Home page view
def home(request):
    posts = BlogPost.objects.all()  # Fetch all blog posts from the database
    projects = Project.objects.all()    # Fetch all projects from the database
    context = {'posts': posts, 'projects': projects}
    return render(request, 'home/home.html', context)

# Projects page view
def projects(request):
    projects = Project.objects.all()  # Fetch all projects from the database
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

# Blog page view
def blog(request):
    posts = BlogPost.objects.all()  # Fetch all blog posts from the database
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)

# Blog post detail view
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Temporary for testing only
def blog_post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    option_price = None
    option_type = None
    
    if request.method == 'POST':
        form = OptionPriceForm(request.POST)
        if form.is_valid():
            stock_price = form.cleaned_data['stock_price']
            strike_price = form.cleaned_data['strike_price']
            time_to_maturity = form.cleaned_data['time_to_maturity']
            volatility = form.cleaned_data['volatility']
            interest_rate = form.cleaned_data['interest_rate']
            option_type = form.cleaned_data.get('option_type')
            
            # Initialize the Black-Scholes model
            bs = BlackScholes(stock_price, strike_price, time_to_maturity, interest_rate, volatility)
            
            if option_type == 'call':
                option_price = bs.black_scholes_call()
            else:
                option_price = bs.black_scholes_put()
    else:
        form = OptionPriceForm()
    
    # Convert Markdown content to HTML
    post_content_html = markdown.markdown(post.content, extensions=['fenced_code'])

    # Replace placeholder with the calculator form HTML
    content_with_calculator = post_content_html.replace(
        '{{ OPTION_CALCULATOR }}',
        render_to_string('blog/option_calculator.html', {
            'form': form,
            'option_price': option_price
        })
    )
    
    return render(request, 'blog/blog_post_detail.html', {
        'post': post,
        'content_with_calculator': content_with_calculator
    })


def test_csrf(request):
    if request.method == 'POST':
        return render(request, 'success.html')
    return render(request, 'test_csrf.html')
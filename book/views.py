from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User, Author, Book, Purchases
from .forms import AuthorForm, BookForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    users=User.objects.all()
    authors=Author.objects.all()
    books=Book.objects.all()
    
    
    page=request.GET.get('page', 1)

    paginator=Paginator(books, 6)

    try:
        books1=paginator.page(page)
    except PageNotAnInteger:
        books1=paginator.page(1)
    except EmptyPage:
        books1=paginator.page(paginator.num_pages)
    user1=''
    if User.objects.filter(email=request.session["email"]).exists():
        print("bor")
        user1=User.objects.get(email=request.session["email"])
    
    return render(request, "main/author_books.html", {
        "users": users,
        "user1": user1,
        "authors": authors,
        "books": books,
        "books1": books1
    })

def login(request):
    user=''

    if request.method == "POST":
        email=request.POST["email"]
        password=request.POST["password"]

        user=User.objects.filter(email=email)
        if user.exists():
            request.session["email"]=email
            return redirect('/home/')

    return render(request,"auth/login.html")
def logup(request):

    if request.method == "POST":
        email=request.POST["email"]
        username=request.POST["username"]
        password=request.POST["password"]
        user=User.objects.filter(username=username, email=email)

        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('/logup/')

        user = User.objects.create_user(
            username=username,
            email=email
        )
         
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
         
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        request.session["email"]=email
        return redirect('/home/')

    return render(request, "auth/logup.html",{})

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    
    return render(request,"auth/login.html")

def AddAuthor(request):

    form=AuthorForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('/home/')
    else:
        form=AuthorForm()
    
    user1=''
    if User.objects.filter(email=request.session["email"]).exists():
        print("bor")
        user1=User.objects.get(email=request.session["email"])

    return render(request,"main/add_author.html",{
        'form': form,
        'user1': user1
    })

def AddBook(request):

    if request.method=="POST":
        form=BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)

            return redirect('/home/')
    
    else:
        form=BookForm()
    
    user1=''
    if User.objects.filter(email=request.session["email"]).exists():
        print("bor")
        user1=User.objects.get(email=request.session["email"])

    return render(request,"main/add_book.html",{
        'form': form,
        'user1': user1
    })

def detail(request, pk):

    book=get_object_or_404(Book, pk=pk)
    user=User.objects.get(email=request.session["email"])

    if request.method=="POST":
        purchases=request.POST["quantity"]

        purchase=Purchases.objects.create(
            book=book,
            customer=user,
            quantity=purchases
        )

        purchase.save()

        return redirect('/purchases/')

    user1=''
    if User.objects.filter(email=request.session["email"]).exists():
        print("bor")
        user1=User.objects.get(email=request.session["email"])
    return render(request, "main/detail.html",{
        "book": book,
        "user1": user1
    })

def purchases(request):
    purchases=Purchases.objects.all()

    if request.method=="POST":

        purchases.delete()

        return redirect('/purchases/')
    
    user1=''
    if User.objects.filter(email=request.session["email"]).exists():
        print("bor")
        user1=User.objects.get(email=request.session["email"])
    
    return render(request, "main/purchases.html",{
        "purchases": purchases,
        "user1": user1
    })

def firstPage(request):

    return render(request, "first_page.html")

def authorBooks(request, pk):
    authors=Author.objects.all()
    author=get_object_or_404(Author, pk=pk)

    books1=Book.objects.filter(author=author)
    page=request.GET.get('page', 1)

    paginator=Paginator(books1, 6)

    try:
        books1=paginator.page(page)
    except PageNotAnInteger:
        books1=paginator.page(1)
    except EmptyPage:
        books1=paginator.page(paginator.num_pages)

    user1=''
    if User.objects.filter(email=request.session["email"]).exists():
        print("bor")
        user1=User.objects.get(email=request.session["email"])
    return render(request, "main/author_books.html", {
        "authors": authors,
        "books1": books1,
        'user1': user1
    })
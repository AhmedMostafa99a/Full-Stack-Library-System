from datetime import *

from django.shortcuts import *
from django.http import *
from django.template import *
from .models import *
def add(request):
    return render(request , 'add book.html', {})
def show_books(request):
    val = book.objects.all().values()
    guys = {
        'values': val,
    }
    return render(request , 'admin_books.html', guys)
def search_books(request):
    val = book.objects.all().values()
    guys = {
        'values': val,
    }
    return render(request , 'search_bar.html', guys)
def person_details(request , id):
    val = book.objects.get(id=id)
    guys = {
        'value': val,
    }
    template = loader.get_template('edit_book.html')
    return HttpResponse(template.render(guys, request))
def book_create(request):
    title = request.POST['book name']
    author = request.POST['author name']
    category = request.POST['book-category']
    stock = request.POST['stock']
    description = request.POST['about book']
    picture = request.POST['pic']
    b1 = book(title=title,author=author,category=category,stock=stock,description=description,pic=picture)
    b1.save()
    return HttpResponseRedirect(reverse('bay'))
def person_delete(request):
    ids = request.POST.getlist('id')
    book.objects.filter(id__in = ids).delete()
    return HttpResponseRedirect(reverse('bay'))
def person_update(request , id):
    z = book.objects.get(id=id)
    title = request.POST['title']
    author = request.POST['author']
    category = request.POST['category']
    stock = request.POST['stock']
    description = request.POST['description']
    picture = request.POST['pic']
    z.title = title
    z.author = author
    z.category = category
    z.stock = stock
    z.description = description
    z.pic = picture
    z.save()
    return HttpResponseRedirect(reverse('bay'))


# ------------------------Sign up-----------------------------------
def signup(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('pass', "")
        confirm = request.POST.get('Cpass', '')
        is_admin = request.POST.get('is_admin', '') == "admin"
        if User.objects.filter(email=email).exists():
            return render(request, 'Sign_up.html', {'error': 'this email registered already'})
        elif (password != confirm):
            return render(request, "Sign_up.html", {'error': 'Password should equal to confirm password '})
        else:
            new_user = User(name=name, email=email, password=password, is_admin=is_admin)

            new_user.save()
            return render(request, 'Sign_up.html', {'success': 'Succesful signup'})

    return render(request, "Sign_up.html")


# -----------------------log in--------------------------------------
def login(request):
    # your code
    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('pass', "")
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            if user.password == password:
                request.session['user_id'] = user.id
                return redirect('profile')

            else:
                request.session['user_id'] = 123
                return render(request, 'login.html', {'error': 'password is not correct . Please try again'})

        else:
            return render(request, 'login.html', {'error': 'email is not found . Please try again'})

    return render(request, 'login.html')


def user_books(request):
    books_list = book.objects.all()
    return render(request, 'books.html', {'books': books_list})


# -----------------------book details page----------------------------
def book_details(request, id):
    try:
        book_obj = book.objects.get(id=id)
        context = {
            'book': book_obj,
            'today': datetime.now().date()
        }
        return render(request, 'book_details.html', context)
    except book.DoesNotExist:
        return redirect('books')


# -----------------------borrowed books----------------------------
def borrowed_books(request):
    if 'user_id' not in request.session:
        return redirect('login')

    user_id = request.session['user_id']
    borrowed = BorrowedBook.objects.filter(user_id=user_id)

    context = {
        'borrowed_books': borrowed,
        'today': datetime.now().date()
    }

    return render(request, 'borrowed.html', context)


# -----------------------borrow book----------------------------
def borrow_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')

        # Check if user is logged in
        if 'user_id' not in request.session:
            return JsonResponse({'success': False, 'message': 'Please log in to borrow books'})

        user_id = request.session['user_id']

        try:
            book_obj = book.objects.get(id=book_id)
            user_obj = User.objects.get(id=user_id)

            # Check if book is in stock
            if book_obj.stock > 0:
                # Check if user already borrowed this book
                if BorrowedBook.objects.filter(user=user_obj, book=book_obj).exists():
                    return JsonResponse({'success': False, 'message': 'You have already borrowed this book'})

                # Decrease stock
                book_obj.stock -= 1
                book_obj.save()

                # Create borrowed book record
                due_date = datetime.now().date() + timedelta(days=14)  # 2 weeks from now
                borrowed = BorrowedBook(
                    user=user_obj,
                    book=book_obj,
                    due_date=due_date
                )
                borrowed.save()

                return JsonResponse({'success': True, 'stock': book_obj.stock})
            else:
                return JsonResponse({'success': False, 'message': 'Book out of stock'})

        except book.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Book not found'})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request'})


# -----------------------return book----------------------------
def return_book(request):
    if request.method == 'POST':
        borrowed_id = request.POST.get('borrowed_id')

        # Check if user is logged in
        if 'user_id' not in request.session:
            return JsonResponse({'success': False, 'message': 'Please log in to return books'})

        try:
            borrowed = BorrowedBook.objects.get(id=borrowed_id)

            # Ensure the book belongs to the logged-in user
            if borrowed.user.id != request.session['user_id']:
                return JsonResponse({'success': False, 'message': 'Unauthorized'})

            # Increase book stock
            book_obj = borrowed.book
            book_obj.stock += 1
            book_obj.save()

            # Delete the borrowed record
            borrowed.delete()

            return JsonResponse({'success': True})

        except BorrowedBook.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Borrowed book record not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request'})


def profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # or wherever your login page is

    user = User.objects.get(id=user_id)
    return render(request, 'profile.html', {'user': user})

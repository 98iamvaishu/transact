# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from transact.models import Lender, Borrower, Payments
# Create your views here.


def signin(request):
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(request, username=email,
							email=email, password=password)
		if user is not None:
			login(request, user)
			fname = request.user.first_name
			return redirect("/create/", {"user": user})
		else:
			return redirect("/signin1/")

	return render(request, "signin.html")


def logout1(request):
	logout(request)
	return redirect("/")


def signup(request):
	if request.method == "POST":
		# username = request.POST.get['name']
		fname = request.POST['fname']
		lname = request.POST['lname']
		password = request.POST['pass']
		email = request.POST['email']
		username = email
		user = authenticate(request, username=email, email=email,
							password=password, firstname=fname, lastname=lname)

		if user is None:
			user = User.objects.create_user(username=email, email=email,
											password=password, first_name=fname, last_name=lname)
			lender = Lender.objects.create(user=user, name=fname)
			login(request, user)

			return redirect("/create/", {"fname": fname})
			print(name)
		else:
			return HttpRespose("Already exists")
	return render(request, "signup.html")


def lender(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		amount = request.POST.get('amount')
		len1 = Lender(user=user, name=name, initial_amount=amount)
		len1.save()
		user = request.user.first_name
		return HttpResponse("succesfully saved")
	return render(request, "create.html")


def borrower(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		amount = request.POST.get('amount')
		interest = request.POST.get('interest')
		duration = request.POST.get('duration')
		date = request.POST.get('date')
		terms = request.POST.get('terms')
		famount = float(amount)
		finterest = float(interest)
		fduration = float(duration)
		dint1 = finterest * 0.01
		aint = float(dint1 * famount)
		if terms == "week":
			amt0 = float(aint / 52)
			amt1 = float(amt0 * fduration)
			intamt = round(amt1, 2)
		else:
			amt0 = float(aint / 12)
			print(amt0)
			amt1 = float(amt0 * fduration)
			print(amt1)
			intamt = round(amt1, 2)
		user = request.user
		print(user)
		bor = Borrower.objects.create(name=name, phone=phone, date=date, amount=amount, interest=interest,
									  duration=duration, terms=terms, intamt=intamt, lender=user)
		print(bor.name)
		return redirect("/list1/")
	return render(request, "borrow.html")


def paidfun(request,borrowerid):
	ob = Borrower.objects.get(pk=borrowerid)
	if request.method == 'POST':
		date = request.POST.get('date')
		pamt = float(request.POST.get('pamount'))
		iamt = float(request.POST.get('iamount'))
		paid = Payments.objects.create(borrower=ob, 
								principal_amt=pamt, 
								interest_amt=iamt, 
								timestamp=date)		
		ob.amount = float(ob.amount - pamt - iamt)
		ob.intamt = round((float(ob.interest / 100) *
						  float(ob.amount)) / float(ob.duration), 2)
		ob.save()
		print(ob.id)
		if ob.amount == 0:
			ob.delete()
		return redirect(f"/history/{ob.id}")
	return render(request, "paid.html", {"ob": ob})


def test(request):
	return render(request, "test.html")


def home(request):
	return render(request, "home1.html")


def create(request):
	user = request.user
	fname = user.first_name
	lender = Lender.objects.get(user=user)
	bor = Borrower.objects.filter(lender=user)
	sum1 = 0
	return render(request, "create.html", {"bor": bor, "fname": fname})


def list1(request):
	user = request.user
	lender = Lender.objects.get(user=user)
	bor = Borrower.objects.filter(lender=user)

	return render(request, "list1.html", {"bor": bor})


def signin1(request):
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(request, username=email,
							email=email, password=password)
		if user is not None:
			login(request, user)
			fname = request.user.first_name
			return redirect("/create/", {"user": user})
		else:
			return redirect("/signin1/")

	return render(request, "signin1.html")


def history(request,borid):
	borrower = Borrower.objects.get(pk=borid)
	history = Payments.objects.filter(borrower=borrower)
	return render(request,"history.html",{"history":history, "borrower":borrower})
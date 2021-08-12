from django.contrib.auth.models import User
from django.db import IntegrityError
from core.models import Product, Profile, Address, orderItem, Order, orderHistory, productReview, shopperReview
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
from django.http import HttpResponse
import json
from django.http import JsonResponse
# Create your views here.

import os


def home(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    homeHTML = "home.html"
    # testing to get items name from the database
    print(Product.objects.all)
    user = request.user
    product_list = Product.objects.all()
    return render(request, homeHTML, {"product_list": product_list, "user": user})


def beastMode(request):
    """
        button clicked -> beast mode on -> no money left

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    beastModeHtml = "beastmode.html"
    product_list = Product.objects.all()

    return render(request, beastModeHtml, {"product_list": product_list})


def signup(request):
    """
        return rendered sign in page

        Args:
            request: request send from user

        Returns:
            render(html): rendered signup page
    """
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']
        rePassword = request.POST['repassword']
        # add database connection
        if password != rePassword:
            return render(request, "signup.html", {'error': "password dont match"})
        try:
            # create a user instance
            user = User.objects.create_user(username=userName, password=password)
            user.save()
            print("Registration completed")
            loginSuccess = authenticate(request, username=userName, password=password)
            login(request, loginSuccess)
            AddressInstance = Address(user=user, address="None", address2="None", state="None", country="None",
                                      city="None",
                                      zip=404)
            AddressInstance.save()
            ProfileInstance = Profile(user=user, bio="None", phone=404, email="None")
            ProfileInstance.save()
            return redirect('/updateprofile/')
        except IntegrityError:
            return render(request, "signup.html", {'error': "Account Error: Account has been registered"})
    else:
        return render(request, "signup.html", {})


def signin(request):
    """
        when received request from user, return user a page with sign-in status update

            Args:
               request: send from user

            Returns:
                render(request): rendered sign-in html page
    """
    if request.method == "POST":
        userName = request.POST['username']
        password = request.POST['password']
        print("user " + userName + " attempt to log")
        loginSuccess = authenticate(request, username=userName, password=password)
        print("Profile created")
        if loginSuccess is None:
            return render(request, "login.html", {"error": "USER NAME AND PASSWORD DONT EXIST"})
        else:
            login(request, loginSuccess)
            return redirect('/home/')
    else:
        return render(request, "login.html")


@login_required
def logout(request):
    auth.logout(request)
    return redirect("/home/")


@login_required
def profile(request):
    """
        when user clicked profile link, display user profile data on the page

        Args:
            request: send from user

        Returns:
            render(request): rendered html page with user profile data
    """
    profileObject = Profile.objects.filter(user=request.user)[0]
    addressObject = Address.objects.filter(user=request.user)[0]
    context = {
        # load user date
        "username": request.user.username,
        "userID": profileObject.userID,
        # load profile model data
        "bio": profileObject.bio,
        "phone": profileObject.phone,
        "email": profileObject.email,
        "status": "user",

        # load address model data
        "address": addressObject.address,
        "address2": addressObject.address2,
        "state": addressObject.state,
        "country": addressObject.country,
        "city": addressObject.city,
        "zip": addressObject.zip,
    }
    return render(request, "profile.html", context)


@login_required
def updateProfile(request):
    """
        when user update their information, update the database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    profileObject = Profile.objects.filter(user=request.user)[0]
    addressObject = Address.objects.filter(user=request.user)[0]
    context = {
        # load user date
        "username": request.user.username,

        # load profile model data
        "bio": profileObject.bio,
        "phone": profileObject.phone,
        "email": profileObject.email,
        "status": "user",

        # load address model data
        "address": addressObject.address,
        "address2": addressObject.address2,
        "state": addressObject.state,
        "country": addressObject.country,
        "city": addressObject.city,
        "zip": addressObject.zip,
    }
    updateProfileHtml = "updateProfile.html"
    if request.method == "POST":
        # profile part
        user = request.user
        address = request.POST["address"]
        address2 = request.POST["address2"]
        city = request.POST["city"]
        email = request.POST["email"]
        state = request.POST["state"]
        zip = request.POST["zip"]
        bio = request.POST["bio"]
        phone = request.POST["phone"]
        country = request.POST["country"]
        # user = User(request.user.username,request.user.email)
        print(request.user.username)
        # update Address and Profile
        Address.objects.filter(user=user).update(address=address, address2=address2, city=city, state=state,
                                                 country=country,
                                                 zip=zip)
        Profile.objects.filter(user=user).update(bio=bio, phone=phone, email=email)

        # if user doesn't exist, update his profile

        print("Profile has been added")
        return redirect('/home/')

    return render(request, updateProfileHtml, context)


@login_required
def removeProduct(request):
    """
        when user choose a option of his product, user maybe click delete product, everything connect with product will be removed

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    removeProductHTML = "removeProduct.html"
    user = request.user
    product_list = Product.objects.filter(seller=user)
    context = {
        "products": product_list}

    if request.method == "POST":
        itemName = request.POST['productName']
        Product.objects.filter(seller=user, title=itemName).delete()
        return render(request, removeProductHTML, context)

    return render(request, removeProductHTML, context)


@login_required
def uploadProduct(request):
    """
        when received product information sent by user, stored in the database and document in the media folder

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    uploadHTML = "uploadProduct.html"
    if request.method == "POST":
        # receive file
        userName = request.user.username,  # type:tuple
        productName = request.POST["productName"]
        productPrice = request.POST["price"]
        productStocks = request.POST["stocks"]
        productDescription = request.POST["description"]
        category = request.POST['category']
        uploadFile = request.FILES['productPicture']

        # create folder for user
        fileStorage = FileSystemStorage()
        parent = fileStorage.location
        # change tuple type to string(userName is tuple)
        username = ''.join(userName)
        directory = username
        path = os.path.join(parent, directory)
        # if user folder doesn't exist create folder for user
        if not os.path.exists(path):
            os.mkdir(path)
            print(username + " folder created ")
        print(category)
        print(productName)
        print(userName)
        ifProductExist = Product.objects.filter(seller=request.user, title=productName).exists()
        # if stocks <= 0, do not add into product
        if int(productStocks) > 0:
            if not ifProductExist:
                productInstance = Product(
                    seller=request.user,
                    title=productName,
                    price=productPrice,
                    description=productDescription,
                    stocking=productStocks,
                    category=category)
                productInstance.save()
                # save image on local machine
                itemID = str(productInstance.productID)
                fileStorage.save(username + "/" + itemID + ".jpg", uploadFile)
                product = Product.objects.filter(seller=request.user, title=productName)[0]
                itemID = str(product.productID)
                Product.objects.filter(seller=request.user, productID=itemID).update(seller=request.user,
                                                                                     title=productName,
                                                                                     image=username + "/" + itemID + ".jpg",
                                                                                     price=productPrice,
                                                                                     description=productDescription,
                                                                                     stocking=productStocks,
                                                                                     category=category, )
            else:
                # if item exists remove product and create another item
                Product.objects.filter(seller=request.user, title=productName).delete()
                productInstance = Product(
                    seller=request.user,
                    title=productName,
                    price=productPrice,
                    description=productDescription,
                    stocking=productStocks,
                    category=category)
                productInstance.save()
                # save image on local machine
                itemID = str(productInstance.productID)
                fileStorage.save(username + "/" + itemID + ".jpg", uploadFile)
                product = Product.objects.filter(seller=request.user, title=productName)[0]
                itemID = str(product.productID)
                Product.objects.filter(seller=request.user, productID=itemID).update(seller=request.user,
                                                                                     title=productName,
                                                                                     image=username + "/" + itemID + ".jpg",
                                                                                     price=productPrice,
                                                                                     description=productDescription,
                                                                                     stocking=productStocks,
                                                                                     category=category, )
            print(Product.category)

        print("Product information has saved")
        return render(request, uploadHTML, {"error": "Item has added"})

    return render(request, uploadHTML)


@login_required
def selectProduct(request):
    """
        when user choose a option of his product, user maybe click delete product, everything connect with product will be removed

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    updateProductHTML = "selectProduct.html"
    user = request.user
    product_list = Product.objects.filter(seller=user)
    context = {
        "products": product_list}

    if request.method == 'POST':
        print(request.POST.get("form_id"))
        itemName = request.POST['productName']
        previousInfo = Product.objects.filter(seller=user, title=itemName)[0]
        request.session['productName'] = previousInfo.title,
        request.session['price'] = previousInfo.price,
        request.session['stocking'] = previousInfo.stocking,
        request.session['category'] = previousInfo.category,
        request.session['description'] = previousInfo.description,
        return redirect('/updateProduct')
    return render(request, updateProductHTML, context=context)


@login_required
def updateProduct(request):
    updateProductPage = "updateProductPage.html"
    context = {
        "productName": request.session['productName'][0],
        "price": request.session['price'][0],
        "stocking": request.session['stocking'][0],
        "category": request.session['category'][0],
        "description": request.session['description'][0],
    }

    if request.method == 'POST':
        userName = request.user.username
        productNameRaw= request.session['productName']
        del request.session['productName']
        del request.session['price']
        del request.session['stocking']
        del request.session['category']
        del request.session['description']
        newProductName = ''.join(productNameRaw)
        print(newProductName)
        productPrice = request.POST["price"]
        productStocks = request.POST["stocks"]
        productDescription = request.POST["description"]
        category = request.POST['category']
        uploadFile = request.FILES['productPicture']
        fileStorage = FileSystemStorage()
        # change tuple type to string(userName is tuple)
        username = ''.join(userName)
        print(userName)
        request.COOKIES.get('logged_in_status')
        Product.objects.filter(seller=request.user, title=newProductName).delete()
        productInstance = Product(
            seller=request.user,
            title=newProductName,
            price=productPrice,
            description=productDescription,
            stocking=productStocks,
            category=category)
        productInstance.save()
        # save image on local machine
        itemID = str(productInstance.productID)
        print(itemID)
        fileStorage.save(username + "/" + itemID + ".jpg", uploadFile)
        product = Product.objects.filter(seller=request.user, title=newProductName)[0]
        itemID = str(product.productID)
        Product.objects.filter(seller=request.user, productID=itemID).update(seller=request.user,
                                                                             title=newProductName,
                                                                             image=username + "/" + itemID + ".jpg",
                                                                             price=productPrice,
                                                                             description=productDescription,
                                                                             stocking=productStocks,
                                                                             category=category, )
        print("Updated")
        return render(request, updateProductPage)
    return render(request, updateProductPage, context=context)


def myProductPage(request):
    """
            when received request from user, return user a page with data from database

            Args:
                request: send from user

            Returns:
                render(request): rendered html page
        """
    productPageHTML = "productPage.html"
    # testing to get items name from the database
    user = request.user
    Product.objects.filter(seller=user)
    print(Product.objects.filter(seller=user))
    product_list = Product.objects.filter(seller=user).all()
    return render(request, productPageHTML, {"product_list": product_list})


def updateItem(request):
    """
        when click add-to-cart button, create or update the orderItem instance

        Args:
            request: send from user

        Returns:
            JsonResponse: Add into Cart
    """
    # source from: "https: // github.com / divanov11 / django_ecommerce_mod5 / blob / master / store / views.py"
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('ProductID:', productId)
    customer = request.user
    product = Product.objects.get(productID=productId)

    ifOrderItemExisted = orderItem.objects.filter(product=product, buyer=customer)

    if action == 'add':
        if ifOrderItemExisted:
            quantity = orderItem.objects.filter(product=product, buyer=customer)[0].quantity + 1
            orderItem.objects.filter(product=product, buyer=customer).update(product=product, buyer=customer,
                                                                             quantity=quantity)
        else:
            orderItemInstance = orderItem(product=product, buyer=customer, quantity=1)
            orderItemInstance.save()

    if action == 'beastMode':
        if ifOrderItemExisted:
            quantity = orderItem.objects.filter(product=product, buyer=customer)[0].quantity + 50
            orderItem.objects.filter(product=product, buyer=customer).update(product=product, buyer=customer,
                                                                             quantity=quantity)
        else:
            orderItemInstance = orderItem(product=product, buyer=customer, quantity=50)
            orderItemInstance.save()

    if action == 'remove':
        orderItem.objects.filter(product=product, buyer=customer).delete()

    return JsonResponse('Added into Cart', safe=False)


@login_required
def cart(request):
    """
        when user click their cart, display user shopping cart

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """

    cartHTML = "cart.html"
    user = request.user
    items = orderItem.objects.filter(buyer=user)
    totalCost = 0
    for item in items:
        totalCost += item.subtotal()
    print(totalCost)
    context = {
        "items": items,
        "totalCost": totalCost
    }

    return render(request, cartHTML, context=context)


@login_required
def checkOut(request):
    """
        when user clicked checkout page, create an order instance, and remove all items in the cart and update the product stocking and display confirmation page

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    checkOutPage = "confirmation.html"
    # create an order object
    user = request.user
    address = Address.objects.filter(user=request.user)[0]
    orderInstance = Order(user=user, shippingAddress=address, order_status="Order received")
    orderInstance.save()

    totalCost = 0
    itemCount = 0
    # remove the item in the cart
    orderItems = orderItem.objects.filter(buyer=user)

    for item in orderItems:
        itemID = item.product.productID
        item.product.stocking -= item.quantity
        Product.objects.filter(productID=itemID).update(stocking=item.product.stocking)
        # add product into orderInstance
        orderInstance.products.add(item.product)

        # if item exist in history
        ifProductExist = orderHistory.objects.filter(user=user).exists()
        if ifProductExist:
            orderHistoryInstance = orderHistory.objects.filter(user=user)[0]
            orderHistoryInstance.products.add(item.product)
        else:
            orderHistoryInstance = orderHistory(user=user)
            orderHistoryInstance.save()
            orderHistoryInstance = orderHistory.objects.filter(user=user)[0]
            orderHistoryInstance.products.add(item.product)
            orderHistoryInstance.save()

        if item.product.stocking <= 0:
            Product.objects.filter(productID=itemID).delete()

        # add

        totalCost += item.product.price * item.quantity
        itemCount += item.quantity

    orderInstance.totalCost = totalCost
    orderInstance.totalItemsCount = itemCount
    orderInstance.save()

    # add items into user order History

    # remove all items in the cart
    orderItem.objects.filter(buyer=user).delete()
    context = {
        "orderNumber": orderInstance.orderID,
        "orderItems": orderInstance.products.all(),
    }

    return render(request, checkOutPage, context=context)


def previousOrder(request):
    """
        when user clicked previous order, it will display all the previous order user placed

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    previousOrderHTML = "previousOrder.html"
    user = request.user
    previousOrders = Order.objects.filter(user=user).all()

    context = {
        "user": user,
        "previousOrders": previousOrders,
    }

    return render(request, previousOrderHTML, context=context)


@login_required
def uploadProductReview(request):
    """
        when user clicked productReview page, user may upload product review

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    reviewHtml = "uploadProductReview.html"
    user = request.user
    orderHistoryInstance = orderHistory.objects.filter(user=user)[0]
    items = orderHistoryInstance.products.all
    context = {
        "items": items
    }

    if request.method == 'POST':
        productName = request.POST['product']
        review = request.POST['review']
        rate = request.POST['rate']
        rate = int(rate)
        products = orderHistory.objects.filter(user=user)[0].products.all()
        for product in products:
            if product.title == productName:
                productInstance = product
        if productInstance:
            print("Instance created")
            productReviewInstance = productReview(reviewer=user, product=productInstance, review=review,
                                                  reviewScore=rate)
            productReviewInstance.save()
            orderHistory.objects.filter(user=request.user)[0].products.remove(productInstance)
        return render(request, reviewHtml, context=context)

    return render(request, reviewHtml, context=context)


@login_required
def myProductReview(request):
    """
        when user shopper click the myProductReview page, seller can view the review buyer write about their product

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    reviewHtml = "myproductreview.html"
    user = request.user
    productNameAndProductReview = []
    products = Product.objects.filter(seller=user)
    for eachProduct in products:
        mySingleProductReview = productReview.objects.filter(product=eachProduct)
        if len(mySingleProductReview) > 0:
            print(mySingleProductReview)
            productNameAndProductReview += mySingleProductReview

    context = {
        "reviews": productNameAndProductReview
    }
    print(productNameAndProductReview)
    return render(request, reviewHtml, context=context)


@login_required
def uploadShopperReview(request):
    """
        when user clicked shopper review page, user may upload review for their shopper

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    reviewHtml = "uploadShopperReview.html"
    all_User = get_user_model()
    print(all_User.objects.all())
    context = {
        "users": all_User.objects.all()
    }

    if request.method == 'POST':
        user = request.POST['user']
        review = request.POST['review']
        rate = request.POST['rate']
        shopper = User.objects.filter(username=user)[0]
        shopperReviewInstance = shopperReview(shopper=shopper, review=review, reviewScore=rate)
        shopperReviewInstance.save()
        return render(request, reviewHtml, context)

    return render(request, reviewHtml, context)


@login_required
def myReview(request):
    """
        when user clicked shopper review page, use will see review people left for him

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    reviewHtml = "myReview.html"
    user = request.user
    reviews = shopperReview.objects.filter(shopper=user)
    context = {
        "reviews": reviews
    }

    return render(request, reviewHtml, context)


# fresh page
def freshPage(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    homeHTML = "home.html"

    # get all items in category of fresh
    product_list = Product.objects.filter(category="Fresh")

    context = {
        "product_list": product_list
    }
    return render(request, homeHTML, context=context)


# beveragePage
def beveragePage(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    homeHTML = "home.html"

    # get all items in category of beverage
    product_list = Product.objects.filter(category="Beverage")

    context = {
        "product_list": product_list
    }
    return render(request, homeHTML, context=context)


# bakeryPage
def bakeryPage(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    homeHTML = "home.html"

    # get all items in category of bakery
    product_list = Product.objects.filter(category="Bakery")

    context = {
        "product_list": product_list
    }
    return render(request, homeHTML, context=context)


# supplementPage
def supplementPage(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    homeHTML = "home.html"

    # get all items in category of supplement
    product_list = Product.objects.filter(category="Supplement")

    context = {
        "product_list": product_list
    }
    return render(request, homeHTML, context=context)


# shirtPage
def shirtPage(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    homeHTML = "home.html"

    # get all items in category of supplement
    product_list = Product.objects.filter(category="Shirt")

    context = {
        "product_list": product_list
    }
    return render(request, homeHTML, context=context)


# pants Page
def pantsPage(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    homeHTML = "home.html"

    # get all items in category of supplement
    product_list = Product.objects.filter(category="Pants")

    context = {
        "product_list": product_list
    }
    return render(request, homeHTML, context=context)


# dressPage
def dressPage(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    homeHTML = "home.html"

    # get all items in category of supplement
    product_list = Product.objects.filter(category="Dress")

    context = {
        "product_list": product_list
    }
    return render(request, homeHTML, context=context)


# shoes page
def shoesPage(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    homeHTML = "home.html"

    # get all items in category of supplement
    product_list = Product.objects.filter(category="Shoes")

    context = {
        "product_list": product_list
    }
    return render(request, homeHTML, context=context)


# socks page
def socksPage(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    homeHTML = "home.html"

    # get all items in category of supplement
    product_list = Product.objects.filter(category="Socks")

    context = {
        "product_list": product_list
    }
    return render(request, homeHTML, context=context)


# shoes page
def underwearPage(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    homeHTML = "home.html"

    # get all items in category of supplement
    product_list = Product.objects.filter(category="Underwear")

    context = {
        "product_list": product_list
    }
    return render(request, homeHTML, context=context)


# dressPage
def watchesPage(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    homeHTML = "home.html"

    # get all items in category of supplement
    product_list = Product.objects.filter(category="Watches")

    context = {
        "product_list": product_list
    }
    return render(request, homeHTML, context=context)


# vroom Page
def vroomPage(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    homeHTML = "home.html"

    # get all items in category of supplement
    product_list = Product.objects.filter(category="Vroom")

    context = {
        "product_list": product_list
    }
    return render(request, homeHTML, context=context)


# camera Page
def cameraPage(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    homeHTML = "home.html"

    # get all items in category of supplement
    product_list = Product.objects.filter(category="Camera")

    context = {
        "product_list": product_list
    }
    return render(request, homeHTML, context=context)


# camera Page
def computerPage(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    homeHTML = "home.html"

    # get all items in category of supplement
    product_list = Product.objects.filter(category="Computer")

    context = {
        "product_list": product_list
    }
    return render(request, homeHTML, context=context)


# camera Page
def gameConsolePage(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """
    homeHTML = "home.html"

    # get all items in category of supplement
    product_list = Product.objects.filter(category="GameConsole")

    context = {
        "product_list": product_list
    }
    return render(request, homeHTML, context=context)


def bestSellingProduct(request):
    """
        when received request from user, return user a page with data from database

        Args:
            request: send from user

        Returns:
            render(request): rendered html page
    """

    homeHTML = "bestSellingProduct.html"
    topProductList = []
    # get all item
    product_list = Product.objects.all()

    for product in product_list:
        reviews = productReview.objects.filter(product=product)
        counter = 0
        totalScore = 0
        averageScore = 0
        for review in reviews:
            # parse the string
            averageScore = 0
            if review:
                review = str(review)
                score = review[-1]
                totalScore += int(score)
                counter += 1
        if counter != 0:
            # if the review for product exists, return the average score
            averageScore = totalScore / counter
        # add product and score into dict
        if averageScore != 0:
            topProductList.append([str(product), float(averageScore), counter])

    topProductList.sort(key=lambda x: x[1])
    topProductList.reverse()
    print(topProductList)
    print(topProductList[1][1])
    context = {
        "product_list": topProductList
    }
    return render(request, homeHTML, context=context)

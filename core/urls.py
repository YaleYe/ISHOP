from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home),
    path("home/", views.home),
    path("uploadProduct/", views.uploadProduct),
    path("signup/", views.signup),
    path("signin/", views.signin,),
    path("logout/", views.logout,),
    path("profile/", views.profile),
    path("updateprofile/", views.updateProfile),
    path("myProduct/", views.myProductPage),
    path('removeProduct/', views.removeProduct),
    path('selectProduct/', views.selectProduct),
    path('updateProduct/', views.updateProduct),
    path("cart/", views.cart),
    path('update_item/', views.updateItem),
    path('checkout/', views.checkOut),
    path('uploadproductreview/', views.uploadProductReview),
    path('myproductreview/', views.myProductReview),
    path('uploadUserReview/', views.uploadShopperReview),
    path('myreview/', views.myReview),
    path('previousOrder/', views.previousOrder),
    path('fresh/', views.freshPage),
    path('beverage/', views.beveragePage),
    path('bakery/', views.bakeryPage),
    path('supplement/', views.supplementPage),
    path('shirt/', views.shirtPage),
    path('dress/', views.dressPage),
    path('pants/', views.pantsPage),
    path('shoes/', views.shoesPage),
    path('socks/', views.socksPage),
    path('underwear/', views.underwearPage),
    path('watches/', views.watchesPage),
    path('vroom/', views.vroomPage),
    path('Camera/', views.cameraPage),
    path('computer/', views.computerPage),
    path('GameConsole/', views.gameConsolePage),
    path('beastmode/', views.beastMode),
    path('bestSellingProduct/', views.bestSellingProduct)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


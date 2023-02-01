"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from buyer import views as buyerview
from siteadmin import views as siteadminview
from seller import views as sellerview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',siteadminview.index,name="index"),
    path('login/',siteadminview.login,name="login"),
    path('loginAction/',siteadminview.loginAction,name="loginAction"),
    path('register/',buyerview.register,name="register"),
    path('registerAction/',buyerview.registerAction,name="registerAction"),
    path('sellerregister/',sellerview.sellerregister,name="sellerregister"),
    path('sellerRegisterAction/',sellerview.sellerRegisterAction,name="sellerRegisterAction"),
    path('buyerupdate/',buyerview.buyerupdate,name="buyerupdate"),
    path('buyerUpdateAction/',buyerview.buyerUpdateAction,name="buyerUpdateAction"),
    path('sellerregisterview/',siteadminview.sellerregisterview,name="sellerregisterview"),
    path('approved<int:id>/',siteadminview.approved,name="approved"),
    path('sellerupdate/',sellerview.sellerupdate,name="sellerupdate"),
    path('sellerUpdateAction/',sellerview.sellerUpdateAction,name="sellerUpdateAction"),
    path('category/',siteadminview.category,name="category"),
    path('categoryAction/',siteadminview.categoryAction,name="categoryAction"),
    path('addproduct/',sellerview.addproduct,name="addproduct"),
    path('addProductAction/',sellerview.addProductAction,name="addProductAction"),
    path('sellerProductView/',sellerview.sellerProductView,name="sellerProductView"),
    path('deleteproduct<int:id>/',sellerview.deleteproduct,name="deleteproduct"),
    path('updateproduct<int:id>/',sellerview.updateproduct,name="updateproduct"),
    path('updateProductAction/',sellerview.updateProductAction,name="updateProductAction"),
    path('viewproducts/',buyerview.viewproducts,name="viewproducts"),
    path('addtocart<int:id>/',buyerview.addtocart,name="addtocart"),
    path('addToCartAction/',buyerview.addToCartAction,name="addToCartAction"),
    path('viewcart/',buyerview.viewcart,name="viewcart"),
    path('deletecart<int:id>/',buyerview.deletecart,name="deletecart"),
    path('placeOrderAction/',buyerview.placeOrderAction,name="placeOrderAction"),
    path('vieworder/',buyerview.vieworder,name="vieworder"),
    path('cancelorder<int:id>/',buyerview.cancelorder,name="cancelorder"),
    path('vieworderseller/',sellerview.vieworderseller,name="vieworderseller"),
    path('approveorder<int:id>/',sellerview.approveorder,name="approveorder"),
    path('rejectorder<int:id>/',sellerview.rejectorder,name="rejectorder"),
    path('tracking<int:id>/',sellerview.tracking,name="tracking"),
    path('trackingAction/',sellerview.trackingAction,name="trackingAction"),
    path('viewtracking<int:id>/',buyerview.viewtracking,name="viewtracking"),
    path('searchproduct/',buyerview.searchproduct,name="searchproduct"),
    path('searchAction/',buyerview.searchAction,name="searchAction"),
    path('searchcategory/',buyerview.searchcategory,name="searchcategory"),
    path('searchCategoryAction/',buyerview.searchCategoryAction,name="searchCategoryAction"),
    path('confirmreject<int:id>/',sellerview.confirmreject,name="confirmreject"),
    path('checkusername/',siteadminview.checkusername,name="checkusername"),
    path('forgotpassword/',siteadminview.forgotpassword,name="forgotpassword"),
    path('forgotpasswordAction/',siteadminview.forgotpasswordAction,name="forgotpasswordAction"),
    path('newPasswordAction/',siteadminview.newPasswordAction,name="newPasswordAction"),
    path('changePasswordAction/',siteadminview.changePasswordAction,name="changePasswordAction"),
    path('logout/',siteadminview.logout,name="logout")
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    

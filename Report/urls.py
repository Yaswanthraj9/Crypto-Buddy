from django.urls import path
from . import views
from .views import GeneratePDF

urlpatterns = [
    # path('', views.home,name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('comparison/', views.comparison, name='comparison'),
    path('temp/', views.temp, name='temp'),
    path('wallet/', views.wallet, name='wallet'),
    path('tax/', views.tax, name='tax'),
    path('transactions/', views.transactions, name='transactions'),
    path('news/', views.news, name='news'),
    path('history/<str:coin_name>/', views.history, name='history'),
    path('coins/', views.list_of_coins, name='list_of_coins'),
    path('balances/', views.balances, name='balances'),
    path('test/', views.test, name="test"),
    # path('price/', views.price,name='price'),
    path('marketcap/', views.marketCap, name='marketcap'),
    path('exchanges/', views.exchanges, name='exchanges'),
    path('best-cryptos/', views.bestCryptos, name='best-cryptos'),
    path('crypto-news/', views.crypto_news, name='crypto-news'),
    path('price_recommend/', views.price_recommend, name='price_recommend'),
    path('transactions_data/', views.transactions_data, name='transactions_data'),
    path('tax_calculation/', views.tax_calculation, name='tax_calculation'),
    path('tax_report/', views.tax_report, name='tax_report'),
    path('download_report/', views.download_report, name='download_report'),
    path('coinbase_price/', views.coinbase_price, name='coinbase_price'),
    path('add_wallet/', views.add_wallet, name='add_wallet'),
    path('check_wallet/', views.check_wallet, name='check_wallet'),

]

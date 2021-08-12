from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core import serializers
import uuid
# all data model are registered here


class Profile(models.Model):
    userID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, name="user")
    bio = models.CharField(blank=True, max_length=200)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30, default="NONE")
    # status
    is_buyer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)

    # follow extension in the future
    following = models.ManyToManyField(User, blank=True, related_name='following')

    def __str__(self):
        return self.user.username


User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, name="user")
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=20, default="Pittsburgh")
    # source https://gist.github.com/sandes/ca4405b996227e49ca00b3f052975347
    states = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AS', 'American Samoa'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('GU', 'Guam'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('MP', 'Northern Mariana Islands'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('PR', 'Puerto Rico'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VI', 'Virgin Islands'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming')
    )
    state = models.CharField(choices=states, max_length=20)

    # source https://gist.github.com/chidimo/bc38a85a6aaac6ebb900ca43dd2075e9
    countries = (
        ('AF', 'AFGHANISTAN'),
        ('AL', 'ALBANIA'),
        ('DZ', 'ALGERIA'),
        ('AS', 'AMERICAN SAMOA'),
        ('AD', 'ANDORRA'),
        ('AO', 'ANGOLA'),
        ('AI', 'ANGUILLA'),
        ('AQ', 'ANTARCTICA'),
        ('AG', 'ANTIGUA AND BARBUDA'),
        ('AR', 'ARGENTINA'),
        ('AM', 'ARMENIA'),
        ('AW', 'ARUBA'),
        ('AU', 'AUSTRALIA'),
        ('AT', 'AUSTRIA'),
        ('AZ', 'AZERBAIJAN'),
        ('BS', 'BAHAMAS'),
        ('BH', 'BAHRAIN'),
        ('BD', 'BANGLADESH'),
        ('BB', 'BARBADOS'),
        ('BY', 'BELARUS'),
        ('BE', 'BELGIUM'),
        ('BZ', 'BELIZE'),
        ('BJ', 'BENIN'),
        ('BM', 'BERMUDA'),
        ('BT', 'BHUTAN'),
        ('BO', 'BOLIVIA'),
        ('BA', 'BOSNIA AND HERZEGOVINA'),
        ('BW', 'BOTSWANA'),
        ('BV', 'BOUVET ISLAND'),
        ('BR', 'BRAZIL'),
        ('IO', 'BRITISH INDIAN OCEAN TERRITORY'),
        ('BN', 'BRUNEI DARUSSALAM'),
        ('BG', 'BULGARIA'),
        ('BF', 'BURKINA FASO'),
        ('BI', 'BURUNDI'),
        ('KH', 'CAMBODIA'),
        ('CM', 'CAMEROON'),
        ('CA', 'CANADA'),
        ('CV', 'CAPE VERDE'),
        ('KY', 'CAYMAN ISLANDS'),
        ('CF', 'CENTRAL AFRICAN REPUBLIC'),
        ('TD', 'CHAD'),
        ('CL', 'CHILE'),
        ('CN', 'CHINA'),
        ('CX', 'CHRISTMAS ISLAND'),
        ('CC', 'COCOS (KEELING) ISLANDS'),
        ('CO', 'COLOMBIA'),
        ('KM', 'COMOROS'),
        ('CG', 'CONGO'),
        ('CD', 'CONGO, THE DEMOCRATIC REPUBLIC OF'),
        ('CK', 'COOK ISLANDS'),
        ('CR', 'COSTA RICA'),
        ('CI', "CÃ”TE D'IVOIRE"),
        ('HR', 'CROATIA'),
        ('CU', 'CUBA'),
        ('CY', 'CYPRUS'),
        ('CZ', 'CZECH REPUBLIC'),
        ('DK', 'DENMARK'),
        ('DJ', 'DJIBOUTI'),
        ('DM', 'DOMINICA'),
        ('DO', 'DOMINICAN REPUBLIC'),
        ('EC', 'ECUADOR'),
        ('EG', 'EGYPT'),
        ('SV', 'EL SALVADOR'),
        ('GQ', 'EQUATORIAL GUINEA'),
        ('ER', 'ERITREA'),
        ('EE', 'ESTONIA'),
        ('ET', 'ETHIOPIA'),
        ('FK', 'FALKLAND ISLANDS (MALVINAS)'),
        ('FO', 'FAROE ISLANDS'),
        ('FJ', 'FIJI'),
        ('FI', 'FINLAND'),
        ('FR', 'FRANCE'),
        ('GF', 'FRENCH GUIANA'),
        ('PF', 'FRENCH POLYNESIA'),
        ('TF', 'FRENCH SOUTHERN TERRITORIES'),
        ('GA', 'GABON'),
        ('GM', 'GAMBIA'),
        ('GE', 'GEORGIA'),
        ('DE', 'GERMANY'),
        ('GH', 'GHANA'),
        ('GI', 'GIBRALTAR'),
        ('GR', 'GREECE'),
        ('GL', 'GREENLAND'),
        ('GD', 'GRENADA'),
        ('GP', 'GUADELOUPE'),
        ('GU', 'GUAM'),
        ('GT', 'GUATEMALA'),
        ('GN', 'GUINEA'),
        ('GW', 'GUINEA'),
        ('GY', 'GUYANA'),
        ('HT', 'HAITI'),
        ('HM', 'HEARD ISLAND AND MCDONALD ISLANDS'),
        ('HN', 'HONDURAS'),
        ('HK', 'HONG KONG'),
        ('HU', 'HUNGARY'),
        ('IS', 'ICELAND'),
        ('IN', 'INDIA'),
        ('ID', 'INDONESIA'),
        ('IR', 'IRAN, ISLAMIC REPUBLIC OF'),
        ('IQ', 'IRAQ'),
        ('IE', 'IRELAND'),
        ('IL', 'ISRAEL'),
        ('IT', 'ITALY'),
        ('JM', 'JAMAICA'),
        ('JP', 'JAPAN'),
        ('JO', 'JORDAN'),
        ('KZ', 'KAZAKHSTAN'),
        ('KE', 'KENYA'),
        ('KI', 'KIRIBATI'),
        ('KP', "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF"),
        ('KR', 'KOREA, REPUBLIC OF'),
        ('KW', 'KUWAIT'),
        ('KG', 'KYRGYZSTAN'),
        ('LA', "LAO PEOPLE'S DEMOCRATIC REPUBLIC"),
        ('LV', 'LATVIA'),
        ('LB', 'LEBANON'),
        ('LS', 'LESOTHO'),
        ('LR', 'LIBERIA'),
        ('LY', 'LIBYAN ARAB JAMAHIRIYA'),
        ('LI', 'LIECHTENSTEIN'),
        ('LT', 'LITHUANIA'),
        ('LU', 'LUXEMBOURG'),
        ('MO', 'MACAO'),
        ('MK', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF'),
        ('MG', 'MADAGASCAR'),
        ('MW', 'MALAWI'),
        ('MY', 'MALAYSIA'),
        ('MV', 'MALDIVES'),
        ('ML', 'MALI'),
        ('MT', 'MALTA'),
        ('MH', 'MARSHALL ISLANDS'),
        ('MQ', 'MARTINIQUE'),
        ('MR', 'MAURITANIA'),
        ('MU', 'MAURITIUS'),
        ('YT', 'MAYOTTE'),
        ('MX', 'MEXICO'),
        ('FM', 'MICRONESIA, FEDERATED STATES OF'),
        ('MD', 'MOLDOVA, REPUBLIC OF'),
        ('MC', 'MONACO'),
        ('MN', 'MONGOLIA'),
        ('MS', 'MONTSERRAT'),
        ('MA', 'MOROCCO'),
        ('MZ', 'MOZAMBIQUE'),
        ('MM', 'MYANMAR'),
        ('NA', 'NAMIBIA'),
        ('NR', 'NAURU'),
        ('NP', 'NEPAL'),
        ('NL', 'NETHERLANDS'),
        ('AN', 'NETHERLANDS ANTILLES'),
        ('NC', 'NEW CALEDONIA'),
        ('NZ', 'NEW ZEALAND'),
        ('NI', 'NICARAGUA'),
        ('NE', 'NIGER'),
        ('NG', 'NIGERIA'),
        ('NU', 'NIUE'),
        ('NF', 'NORFOLK ISLAND'),
        ('MP', 'NORTHERN MARIANA ISLANDS'),
        ('NO', 'NORWAY'),
        ('OM', 'OMAN'),
        ('PK', 'PAKISTAN'),
        ('PW', 'PALAU'),
        ('PS', 'PALESTINIAN TERRITORY, OCCUPIED'),
        ('PA', 'PANAMA'),
        ('PG', 'PAPUA NEW GUINEA'),
        ('PY', 'PARAGUAY'),
        ('PE', 'PERU'),
        ('PH', 'PHILIPPINES'),
        ('PN', 'PITCAIRN'),
        ('PL', 'POLAND'),
        ('PT', 'PORTUGAL'),
        ('PR', 'PUERTO RICO'),
        ('QA', 'QATAR'),
        ('RE', 'RÃ‰UNION'),
        ('RO', 'ROMANIA'),
        ('RU', 'RUSSIAN FEDERATION'),
        ('RW', 'RWANDA'),
        ('SH', 'SAINT HELENA'),
        ('KN', 'SAINT KITTS AND NEVIS'),
        ('LC', 'SAINT LUCIA'),
        ('PM', 'SAINT PIERRE AND MIQUELON'),
        ('VC', 'SAINT VINCENT AND THE GRENADINES'),
        ('WS', 'SAMOA'),
        ('SM', 'SAN MARINO'),
        ('ST', 'SAO TOME AND PRINCIPE'),
        ('SA', 'SAUDI ARABIA'),
        ('SN', 'SENEGAL'),
        ('CS', 'SERBIA AND MONTENEGRO'),
        ('SC', 'SEYCHELLES'),
        ('SL', 'SIERRA LEONE'),
        ('SG', 'SINGAPORE'),
        ('SK', 'SLOVAKIA'),
        ('SI', 'SLOVENIA'),
        ('SB', 'SOLOMON ISLANDS'),
        ('SO', 'SOMALIA'),
        ('ZA', 'SOUTH AFRICA'),
        ('GS', 'SOUTH GEORGIA AND SOUTH SANDWICH ISLANDS'),
        ('ES', 'SPAIN'),
        ('LK', 'SRI LANKA'),
        ('SD', 'SUDAN'),
        ('SR', 'SURINAME'),
        ('SJ', 'SVALBARD AND JAN MAYEN'),
        ('SZ', 'SWAZILAND'),
        ('SE', 'SWEDEN'),
        ('CH', 'SWITZERLAND'),
        ('SY', 'SYRIAN ARAB REPUBLIC'),
        ('TW', 'TAIWAN, PROVINCE OF CHINA'),
        ('TJ', 'TAJIKISTAN'),
        ('TZ', 'TANZANIA, UNITED REPUBLIC OF'),
        ('TH', 'THAILAND'),
        ('TL', 'TIMOR'),
        ('TG', 'TOGO'),
        ('TK', 'TOKELAU'),
        ('TO', 'TONGA'),
        ('TT', 'TRINIDAD AND TOBAGO'),
        ('TN', 'TUNISIA'),
        ('TR', 'TURKEY'),
        ('TM', 'TURKMENISTAN'),
        ('TC', 'TURKS AND CAICOS ISLANDS'),
        ('TV', 'TUVALU'),
        ('UG', 'UGANDA'),
        ('UA', 'UKRAINE'),
        ('AE', 'UNITED ARAB EMIRATES'),
        ('GB', 'UNITED KINGDOM'),
        ('US', 'UNITED STATES'),
        ('UM', 'UNITED STATES MINOR OUTLYING ISLANDS'),
        ('UY', 'URUGUAY'),
        ('UZ', 'UZBEKISTAN'),
        ('VU', 'VANUATU'),
        ('VN', 'VIET NAM'),
        ('VG', 'VIRGIN ISLANDS, BRITISH'),
        ('VI', 'VIRGIN ISLANDS, U.S.'),
        ('WF', 'WALLIS AND FUTUNA'),
        ('EH', 'WESTERN SAHARA'),
        ('YE', 'YEMEN'),
        ('ZW', 'ZIMBABWE')
    )
    country = models.CharField(choices=countries, max_length=20)
    zip = models.IntegerField()

    def __str__(self):
        return self.user.username


User.address = property(lambda u: Address.objects.get_or_create(user=u)[0])


class Product(models.Model):
    """
        create Product model to be stored in database, with title, image, price, description, left stocks

        Args:
            models.Model: the model template

    """
    productID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    category = (
        ('Fresh', "Fresh"),
        ('Beverage', "Beverage"),
        ('Bakery', 'Bakery'),
        ('Supplement', 'Supplement'),
        ('Shirt', 'Shirt'),
        ('Pants', 'Pants'),
        ('Shoes', 'Shoes'),
        ('Dress', 'Dress'),
        ("Watches", "Watches"),
        ("Socks", "Socks"),
        ("UnderWear", "UnderWear"),
        ("Vroom", "Vroom"),
        ("Camera", "Camera"),
        ("Computer", "Computer"),
        ("GameConsole", "GameConsole"),

    )
    title = models.CharField(max_length=30)
    image = models.ImageField(default=None)
    price = models.FloatField()
    description = models.TextField()
    stocking = models.IntegerField()
    category = models.CharField(choices=category, max_length=20)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    coupon = models.FloatField(default="1.0")

    def __str__(self):
        return str(self.title)


class Order(models.Model):
    """
        create order model to be stored in database, with shoppingCart, shipping address, number, email and total cost

        Args:
            models.Model: the model template
    """
    orderID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shippingAddress = models.ForeignKey(Address, on_delete=models.CASCADE)
    status = (("Order received", "Order received"), ("Order shipped", "Order shipped"), ("Order Delivered", "Order Delivered"))
    order_status = models.CharField(max_length=50, choices=status)
    totalCost = models.FloatField(default=0.0)
    totalItemsCount = models.IntegerField(default=0)
    orderDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.orderID)


class orderItem(models.Model):
    """
        create CartProduct model to be stored in database, with cart, product, quantity , quantity and totalcost

        Args:
               models.Model: the model template

    """
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)

    def subtotal(self):
        return self.quantity * self.product.price


User.address = property(lambda u: Address.objects.get_or_create(user=u)[0])


class orderHistory(models.Model):
    """
        create view for orderHistory

        Args:
                models.Model: the model template
    """
    orderHistoryID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)


class shopperReview(models.Model):
    """
        create review for shopper

        Args:
            models.Model: the model template
    """
    shopper = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=1000)
    reviewScore = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])


class productReview(models.Model):
    """
        create review for shopper

        Args:
            models.Model: the model template
    """
    productReviewID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    reviewScore = models.IntegerField()

    def __str__(self):
        return self.product.title+" : " + self.review + " "+str(self.reviewScore)


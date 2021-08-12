## User stories

1. List items to purchase\
As a buyer, I want the website can display the product i want to buy\

2. List items to sell\
As a seller, I want the website to display the product  I want to sell\

3.Store/Update user information on the database\
As a buyer, I want my user information to be stored so next time when I purchase something it would be faster\

4.Store/ update product information database\
As a seller, I want to sell the same product. but the price increases due to a supply shortage so I need to increase the price too.


---

## Purpose:
This project is a shopping website provides user, buyer a platform to buy, sell, rent goods. And track their shipment process

## Structure Front end will be built by HTML, CSS, Javascript Back end will be built by python Database will be sql

## Requirement
Python3.5+\
React.Js

## Developing Environment: Pycharm

## Package Installed:
Django 3.1.7


## Standards
https://www.python.org/dev/peps/pep-0008/

## Features
1. Registation system:
  a. User is allowed to regist their account through this platform with their information\
  b. User is allowed to update their information in the future\
  c. Only User himself and admin-level above is allow to update his/her information\
  d. Each time information updated will send notification to both admin and user

2. Seller side design\
  a. User is allowed to put product on their page to be seen along with the product information\
  b. If the product is not as described as what user upload, the seller will receive a request from customer asking for refund/exchange\
  c. Main page will display the top 10 best selling product along with the information\
  d. saler has rating system along with the comment system

3. Buyer side design\
  a. Buyer is allowed to purchase goods and it will move to "tracking order" list\
  b. Buyer can store their payment methods in their account along with other information\
  c. Buyer will be displayed the most-wanted purchase\
  d. Buyer can request a refund if the product is not same as described
  
4. Customer service\
  a. if request from both seller and buyer side has not been confirmed it will reminds both side\

5. Backend information\
  a. once receive the order, it updates database automatcally by python\
  b. displayed the best 10 selling product and return to the front end
  
6. Front information\
  a. Display product page\
  b. Display user information page\
  c. Display buyer infomation page\
  d. Display tracking page\
  e. Display customer service page


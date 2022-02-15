# Sandro's Pizza

**Sandro's Pizza** is E-commerce website and it is part of my 4th milestone project in **Code Institute's Full Stack Software Development Course**. Purpose of the website is to demonstrate proficiency in creating full stack application. Website allows users to make pizza delivery orders, pay for the order and save their details in database for future orders if needed.

![mockup](/documentation/mockup.PNG)

[Link to the project](https://sandros-pizza.herokuapp.com/)

---

# TABLE OF CONTENTS:

- [USER EXPERIENCE](#user-experience)
  -  [User stories](#user-stories)
      -  [First time visitors goals](#first-time-visitors-goals)
      -  [Frequent users goals](#frequent-users-goals)
      -  [Site owners goals](#site-owners-goals)
- [WIREFRAMES](#wireframes)
- [DATABASE SCHEMA](#database-schema)
  -  [User](#ser)
  -  [User Profile](#user-profile)
  -  [Item](#item)
  -  [Review](#review)
  -  [Order Item](#order-item)
  -  [Order](#order)
- [TECHNOLOGIES USED](#technologies-used)
  -  [Languages](#languages)
  -  [Frameworks, libraries, programs and websites](#frameworks-libraries-programs-and-websites)
- [DESIGN](#design)
  -  [Colour scheme](#colour-scheme)
  -  [Imagery](#imagery)
  -  [Typography](#typography)
- [FEATURES AND FUNCTIONALITY](#features-and-functionality)
  -  [Menu page](#menu-page)
  -  [Pizza details page](#pizza-details-page)
  -  [Adding pizza to order](#adding-pizza-to-order)
  -  [Editing the order](#editing-the-order)
  -  [Paying for the order](#paying-for-the-order)
  -  [Order confirmation](#order-confirmation)
  -  [User profile and order history](#user-profile-and-order-history)
- [TESTING](#testing)
  -  [Code tests](#code-tests)
      - [HTML Code Test](#html-code-test-results)
      - [CSS Code Test](#css-code-test-results)
      - [JavaScript Code Test](#javascript-code-testing)
      - [Python Code Test](#python-code-test-results)
  -  [Responsiveness and browser tests](#responsiveness-and-browser-tests)
  -  [Testing User Stories from User Experience Section](#testing-user-stories-from-user-experience-section)
      -  [Testing first time visitors goals](#testing-first-time-visitors-goals)
      -  [Testing frequent users goals](#testing-frequent-users-goals)
      -  [Testing site owners goals](#testing-site-owners-goals)
  -  [Manual Testing](#manual-testing)
      -  [Ordering process](#ordering-process)
      -  [Ordering product](#ordering-product)
      -  [Managing the order](#managing-the-order)
      -  [Completing the order](#completing-the-order)
      -  [Signup user](#signup-user)
      -  [Login and logout](#login-and-logout)
      -  [Form errors](#form-errors)
      -  [Adding reviews](#adding-reviews)
      -  [Editing profile](#editing-profile)
      -  [Adding/editing/deleting products (admin only)](#adding-editing-deleting-products-admin-only)
      -  [Contact form](#contact-form)
      -  [Page access](#page-access)
      -  [Errors 404 and 500](#errors-404-and-500)
  -  [Known bugs](#known-bugs)
- [DEPLOYMENT](#deployment)
  - [Prerequisites](#prerequisites)
  - [Heroku deployment](#heroku-deployment)
  - [Postgres set up](#postgres-set-up)
  - [AWS - creating a bucket](#aws-creating-a-bucket)
  - [AWS Creating a group](#aws-creating-a-group)
  - [AWS creating policy](#aws-creating-policy)
  - [AWS attach policy to the group](#aws-attach-policy-to-the-group)
  - [AWS creating a user](#aws-creating-a-user)
  - [Connecting django with AWS](#connecting-django-with-AWS)
  - [Environment variables](#environment-variables)
- [CREDITS](#credits)
  -  [Code credits](#code-credits)
  -  [Media and content credits](#media-and-content-credits)
  -  [Acknowledgements](#acknowledgements)

---

# USER EXPERIENCE
[Back to table of contents](#table-of-contents)


## User Stories

### First time visitors goals

- *As a first time visitor*, I want to clearly understand the purpose of the website

- *As a first time visitor*, I want to easily navigate through the website on any device or screen size

- *As a first time visitor*, I want to be able to make purchase without registering for account

- *As a first time visitor*, I want to have option to create account if I wish

- *As a first time visitor*, I want to easily search for products and add them to the order

- *As a first time visitor*, I want to be able to view product details before purchasing it

- *As a first time visitor*, I want to be able to chose quantity and size of product

- *As a first time visitor*, I want to know status of my order at all times

- *As a first time visitor*, I want to be able to change my order before completion

- *As a first time visitor*, I want to make payments in an easy and secure way

- *As a first time visitor*, I want to be notified of my purchases by email

### Frequent users goals

- *As a frequent user*, I want to be able to easily log in to my account

- *As a frequent user*, I want to have records of my past orders attached to my profile

- *As a frequent user*, I want to leave reviews of products

- *As a frequent user*, I want to be able to edit or delete my reviews of products

- *As a frequent user*, I want to be able to change or reset password

### Site owners goals

- *As a site owner*, I want to provide e-commerce service to easily sell my products

- *As a site owner*, I want to be able to add, update and delete products in database

- *As a site owner*, I want to make sure site is safe by providing access to certain areas only to permitted users

---

# WIREFRAMES
[Back to table of contents](#table-of-contents)

- [Mobile view](/documentation/wireframes/mobile.pdf)
- [Tablet view](/documentation/wireframes/tablet.pdf)
- [Desktop view](/documentation/wireframes/desktop.pdf)

---

# DATABASE SCHEMA
[Back to table of contents](#table-of-contents)

For this project relational database was used. Database schema consists of 6 tables: user (provided by Django by default), user profile, item, review, order item and order.

![db-schema](/documentation/db-schema.png)

## User

This is default table provided by Django.

## User Profile

User Profile table has one to one relationship with User table, so in a way we can say that it extends User table. Other table fields are *Phone number*, *City*, *Address 1* and *Address 2*. All of the remaining fields are of CharField type.

## Item

Item table shows details about each item in the store (in this case each pizza). Table fields are *Name* (CharField type), *Ingredients* (CharField type), *Price* (Decimal type) and *Image* (ImageField type).

## Review

Review table shows details about reviews and their authors. Table fields are *User Profile* (connected with foreign key to User Profile table), *Item* (connected with foreign key to Item table), *Title* (CharField type) and *Content* (TextField type).

## Order Item

Order item table shows details about each single item in the users order. Table fields are *Order* (connected with foreign key to Order table), *Item* (connected with foreign key to Item table), *Item size* (CharField type), *Quantity* (Integer type) and *Order item total* (Decimal type).

## Order

Order table shows details about the full order and user's delivery details. Table fields are *User Profile* (connected with foreign key to User Profile table), *Full name* (CharField type), *Email* (EmailField type), *Phone number* (CharField type), *Address 1* (CharField type), *Address 2* (CharField type), *City* (CharField type), *Date* (DateTime type), *Order number* (CharField type), *Order total* (Decimal type), *Original bag* (TextField type) and *Stripe pid* (CharField type).

---

# TECHNOLOGIES USED
[Back to table of contents](#table-of-contents)

## Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS) 
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python 3.8](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks libraries programs and websites

- [Balsamiq](https://balsamiq.com/) was used to create the wireframes during the site design process.

- [jQuery](https://jquery.com/) was used along with JavaScript to manipulate the DOM, CSS and handle JavaScript events in easier way.

- [Django](https://www.djangoproject.com/) is a high-level Python web framework which was used to create this app.

- [Pypi](https://pypi.org/) was used to find and download Python packages

- [Heroku](https://www.heroku.com/) is a cloud platform which was used to deploy the project.

- [Google Fonts](https://fonts.google.com/) were used to import 'Frederick the Great' and 'Libre Franklin' fonts which were used throughout the site.

- [Gitpod](https://www.gitpod.io/) was used to write all the HTML, CSS, JavaScript and Python code for the site.

- [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub

- [GitHub](https://github.com/) is used to store the projects code after being pushed from Git.

- [Photopea](https://www.photopea.com/) is free online photo editor which was used to edit and optimize background image, logo and all card images.

- [Redketchup](https://redketchup.io/bulk-image-resizer) was used to convert large number of images.

- [Font Awesome](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.

- [Autoprefixer](https://autoprefixer.github.io/) was used to add prefixes to CSS properties which are not supported by some browsers.

---

# DESIGN
[Back to table of contents](#table-of-contents)

## Colour scheme

Website uses simplistic blue and white colour scheme, with tomato red used for checkout popup.

## Imagery

Images in title sections are showing pizza themed image. Purpose of images is to give clear idea of the website theme and also to make it visually attractive. Every pizza item has image of its own to describe pizza in more detail. As a new pizza is uploaded by admin new image can be added too.

## Typography

The 'Lato' font is the main font used throughout the whole website with 'Sans Serif' as the fallback font in case for any reason the font isn't being imported into the site correctly. For navbar items 'Staatliches' font is used with 'Cursive' as the fallback font. For review cards 'Georgia' font is used.

---

# FEATURES AND FUNCTIONALITY
[Back to table of contents](#table-of-contents)


Website can be used by registered and non registered users. In case user is registered there are extra features like adding review for each pizza with possibility of editing or completely removing the review. Registered users can also save their details for future purchases.

## Menu page

On menu page user can easily navigate through all pizzas in the menu and view each pizza's details by pressing pizza card. Menu page also shows sign up banner with link to sign up page in case user is not yet registered.

![menu](/documentation/features/001.png)

## Pizza details page

On this page user can see details about pizza, add size and quantity of this particular pizza to the order, can view pizza reviews and if reqistered can add own reviews.

![menu](/documentation/features/002.png)

## Adding pizza to order

By pressing "Add to order" button pizza is added to the order and user is redirected to the menu page in case he wants to ad more pizzas. Pop up is displayed with current order and basket icon in navbar is updated with current order amount.

![menu](/documentation/features/003.png)

## Editing the order

By pressing checkout now on the pop up button, basket icon in navigation bar or "manage order" i navigation menu on mobile user will be redirected to the page where order can be modified before going to the payment screen. On this page each item can be modified by adding or deducting quantity or even completely removed from the order.

![menu](/documentation/features/004.png)

## Paying for the order

By pressing "Proceed to payment" button user will be redirected to checkout page. On this page summary of the order can be seen. There is a form which must be filled by user befor confirming the order. Registered users have option to save their info for future orders. Unregistered users can still register or login prior to confirming the order.

![menu](/documentation/features/005.png)

## Order confirmation

After the order is made confirmation screen appears. Also, confirmation email is sent to the users email with their order details.

![menu](/documentation/features/006.png)

## User profile and order history

If users are registered they can edit their profile and see order history in the "Edit profile" section. All orders are shown in card items and by clicking on each order full order details are displayed.

![menu](/documentation/features/007.png)

---

# TESTING
[Back to table of contents](#table-of-contents)

## Code tests

The [W3C Markup Validator](https://validator.w3.org/) and [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) services were used to validate the HTML and CSS code of the project to ensure there were no syntax errors. [jsHint](https://jshint.com/) was used to test JavaScript code. [pep8online](http://pep8online.com/) was used to check if Python code is PEP8 compliant.

### HTML Code Test Results:

![html](/documentation/testing/code_testing/html.PNG)

HTML code has no errors.

### CSS Code Test Results:

![css](/documentation/testing/code_testing/css.PNG)

CSS Code has no errors.

### JavaScript Code Testing:

Following settings were used to test the code

![js-settings](/documentation/testing/code_testing/javascript_settings.jpg)

script.js test results:

![script.js](/documentation/testing/code_testing/js-script.PNG)

carousel.js test results:

![carousel.js](/documentation/testing/code_testing/js-carousel.PNG)

checkout.js test results:

![checkout.js](/documentation/testing/code_testing/js-checkout.PNG)

All tests passed with no issues

### Python code test results:

![python](/documentation/testing/code_testing/python.PNG)

All tests passed with no major issues

## Responsiveness and browser tests

The website was tested on [Google Chrome](/documentation/testing/browsers/chrome.PNG), [Microsoft Edge](/documentation/testing/browsers/edge.PNG), [Mozilla Firefox](/documentation/testing/browsers/mozilla.PNG) and [Opera browsers](/documentation/testing/browsers/opera.PNG).

Lighthouse test [results](/documentation/lighthouse.pdf).

The website was viewed on a mobile, tablet and laptop devices such as iPhone XR, Lenovo Tab M10 HD and Lenovo Ideapad 3 laptop.

  -  iPhone XR

  ![mobile](/documentation/testing/devices/mobile.png)

  - Lenovo Tab M10 HD

  ![tablet](/documentation/testing/devices/tablet.png)

  - Lenovo Ideapad 3

  ![laptop1](/documentation/testing/devices/laptop_01.PNG)
  ![laptop2](/documentation/testing/devices/laptop_02.PNG)
  ![laptop3](/documentation/testing/devices/laptop_03.PNG)

The website was tested on desktop and laptop computers on a variety of screen sizes using device toolbar option in Google Chrome developer tools.

  -  Google Chrome developer tools

  ![devtools](/documentation/testing/devices/devtools.PNG)

## Testing User Stories from User Experience Section

### Testing first time visitors goals

* As a first time visitor, I want to clearly understand the purpose of the website

  -  Website is designed in a way that is clearly visible from the start that this is pizza delivery service. Main banner is pizza themed, there is a logo for "Sandro's Pizza" and CTA button to make an order.

  [Example](/documentation/testing/user_stories/001.png)

* As a first time visitor, I want to easily navigate through the website on any device or screen size

  -  Device is responsive to different screen sizes so the user is able to navigate through site easily. There is navigation bar with all the main links on desktop size, or navigation menu on mobile size which appears by pressing toggle button.

  [Example](/documentation/testing/user_stories/002.png)

* As a first time visitor, I want to be able to make purchase without registering for account

  -  User is able to make a purchase without registering for account.

  [Example](/documentation/testing/user_stories/003.png)

* As a first time visitor, I want to have option to create account if I wish

  -  There is "Join us" button in navigation bar, and if user is not registered or logged in, "join us" banner is shown throughout the website.

  [Example](/documentation/testing/user_stories/004.png)

* As a first time visitor, I want to easily search for products and add them to the order

  -  All items available for order can easily be found in "menu" page. In case there are too many items to look for, user can use the search option on top of the page on desktop size or in navigation menu on mobile size.

  [Example](/documentation/testing/user_stories/005.png)

* As a first time visitor, I want to be able to view product details before purchasing it

  -  By clicking on each single item on menu page user is redirected to dedicated page of the item where all details are shown.

  [Example](/documentation/testing/user_stories/006.png)

* As a first time visitor, I want to be able to chose quantity and size of product

  -  On item page user is able to select quantity and size of the order item.

  [Example](/documentation/testing/user_stories/007.png)

* As a first time visitor, I want to know status of my order at all times

  -  At all times user can see status of his order basket in top right corner of the navigation bar. Also, when item is added to the order a pop up button is shown with current status of the basket and option to check out now.

  [Example](/documentation/testing/user_stories/008.png)

* As a first time visitor, I want to be able to change my order before completion

  -  When user clicks on basket icon in the top right of the navigation bar or on the checkout pop up button is redirected to order page where all items can be changed before proceeding to payment. Quantity can be changed for every order item and every item can be deleted too.

  [Example](/documentation/testing/user_stories/009.png)

* As a first time visitor, I want to make payments in an easy and secure way

  -  Stripe payment module is implemented to make card payments safe and secure.

  [Example](/documentation/testing/user_stories/010.png)

* As a first time visitor, I want to be notified of my purchases by email

  -  After every successful purchase, an email with order details is sent to user's email address.

  [Example](/documentation/testing/user_stories/011.png)

### Testing frequent users goals

* As a frequent user, I want to be able to easily log in to my account

  -  User can easily sign in to the website using sign in button in navigation bar on desktop size or navigation menu on mobile size.

  [Example](/documentation/testing/user_stories/012.png)

* As a frequent user, I want to have records of my past orders attached to my profile

  -  User can navigate to "edit profile" page where all past orders are attached chronologically. By pressing on each order card user can see full order details.

  [Example](/documentation/testing/user_stories/013.png)

* As a frequent user, I want to leave reviews of products

  -  All registered users have option to leave a review of a product on the product page by pressing "leave review" button.

  [Example](/documentation/testing/user_stories/014.png)

* As a frequent user, I want to be able to edit or delete my reviews of products

  -  If registered user has left a review for a product then there are also options to edit or delete the review by pressing small icons in upper right corner of the review card.

  [Example](/documentation/testing/user_stories/015.png)

### Testing site owners goals

* As a site owner, I want to provide e-commerce service to easily sell my products

  -  This website offers to sell pizzas to registered and non registered users in an easy and quick way.

  [Example](/documentation/testing/user_stories/016.png)

* As a site owner, I want to be able to add, update and delete products in database

  -  If admin user is logged in, by navigating to menu page a new option to add item is shown. By pressing "Add item" button admin can easily upload new items to the database.

  [Example](/documentation/testing/user_stories/017.png)

* As a site owner, I want to make sure site is safe by providing access to certain areas only to permitted users

  -  For most of the pages which are not available for non registered users, they will be redirected to sign in page if they attemt to acces it. If the page is restricted to admin only, all other users will receive flash message that access to the page is denied and will be routed to the main page.

  [Example](/documentation/testing/user_stories/018.png)

## Manual testing

### Ordering process

In this section I have tested the whole ordering process to make sure user experiences a smooth process. I have made separate tests for each functionality in ordering process: ordering single item, changing the quantity and the size, adding item to the basket, changing the order prior to the checkout and finally making the payment and finalizing the order.

### Ordering product

By clicking on product card user is redirected to product page as expected. On product page user can select the quantity and the size of the product which also changes total price dynamically. By pressing "Add to order" button, basket amount in the top right corner gets updated, and checkout popup button is shown at the bottom of the screen with updated total amount.

![001](/documentation/testing/manual_testing/001.gif)

### Managing the order

By clicking on checkout popup button or basket icon in the top right corner of the navbar, user is redirected to the page where they can change the quantity or completely remove certain item from the order. Testing results were as expected with both functionalities working.

![002](/documentation/testing/manual_testing/002.gif)
![003](/documentation/testing/manual_testing/003.gif)

### Completing the order

By clicking on "Proceed to payment" button user is redirected to the checkout page. On this page user has to input personal details and card number before completing the payment. By clicking on "Complete order" button Stripe transaction is initiated. User is informed of this by flashing "Processing payment..." text below the checkout form. After sucessfull payment confirmation page is shown. Testing results were as expected with all tested functionalities working.

![004](/documentation/testing/manual_testing/004.gif)


### Signup user

By clicking on "Sign up" button user can easily create new account by inputting all details in the signup form. After all required details are provided the confirmation email is sent to the user to verify the account. Testing results were as expected with all tested functionalities working.

![005](/documentation/testing/manual_testing/005.gif)

### Login and logout

By clicking Login/Logout buttons user can easily log in/out from the page. Testing results were as expected with both functionalities working.

![006](/documentation/testing/manual_testing/006.gif)
![007](/documentation/testing/manual_testing/007.gif)

### Form errors

If invalid input is provided to the form by the user, error messages are shown below the form.

![008](/documentation/testing/manual_testing/008.gif)

### Adding reviews

By clicking on "Leave a review" button on product page user can leave a review for product. This review can also be edited or even deleted. Testing results were as expected with all tested functionalities working.

![009](/documentation/testing/manual_testing/009.gif)
![010](/documentation/testing/manual_testing/010.gif)
![011](/documentation/testing/manual_testing/011.gif)

### Editing profile

By clicking on "Edit profile" button in navbar user can change profile contact details by submitting the form.

![012](/documentation/testing/manual_testing/012.gif)

### Order details

After completing an order, this is automatically saved to database and past orders can be seen from edit profile menu. By clicking on the single order card the full order details can be accessed.

![013](/documentation/testing/manual_testing/013.PNG)

### Adding/editing/deleting products (admin only)

Users with admin privileges have option to add, edit or delete products from database. When user with admin privileges navigates to menu page, "Add new item" button is shown. By clicking on this button admin users can add product via form. On menu page each product also has edit and delete buttons to easily edit or delete product. Testing results were as expected with all tested functionalities working.

![014](/documentation/testing/manual_testing/014.gif)
![015](/documentation/testing/manual_testing/015.gif)
![016](/documentation/testing/manual_testing/016.gif)

### Contact form

Users can send their messages to the website admin via contact form. I have tested functionality of the form by sending the message and receiving the message in my email box and it is working as expected.

![020](/documentation/testing/manual_testing/020.gif)

### Page access

This test ensures that unauthorized users can not access pages they are not supposed to see (ex. other users account or order details). I have tested this by manually copy/pasting links which should be restricted to certain users. There can be two scenarios - if user only needs to be logged in, in which case user is simply redirected to login screen. In other scenario user does not have access at all, in which case user is redirected to menu page with flash message notification. Testing results were as expected with all tested functionalities working.

![017](/documentation/testing/manual_testing/017.PNG)
![018](/documentation/testing/manual_testing/018.PNG)

### Errors 404 and 500

In case of page errors a custom page is displayed to the user with the link to go back to the main page.

![019](/documentation/testing/manual_testing/019.PNG)

## Known bugs

- After deployment, Stripe weebhooks started throwing an error after the payment is complete. This causes that confirmation email cannot be sent to the user after successful purchase. However, since this is not a critical issue which breaks main functionality of the website I have decided to look into this issue in future. For the moment, after payment is successfully processed user can see order details straight away on the screen, and registered users have option to view past order details in their profiles.

---

# DEPLOYMENT
[Back to table of contents](#table-of-contents)

## Prerequisites

I have created the project by using Code Institute gitpod template and saved it to GitHub repository. During development, I have installed numerous packages using Pip. To include all packages in production, I saved all of them to requirements.txt file using pip3 freeze > requirements.txt command. I saved all environment variables to Heroku / GitPod settings to make sure that files with sensitive data are not pushed to the repository. Also, I made Procfile with instructions to Heroku to run gunicorn (package installed via pip) and to serve the Django app.


## Heroku deployment

- Log in to Heroku
- Select "Create New App" option, add app name and region
- Under deploy tab select GitHub as deployment method, search for GitHub repository and connect Heroku app with it
- Enabled automatic deploys so project is automatically pushed to Heroku as well with every commit
- Add Heroku app to allowed hosts inside of django settings.py file 

```
ALLOWED HOSTS = ['sandros-pizza.herokuapp.com', 'localhost'] 
```

## Postgres set up

- Under resources tab search for "Heroku Postgres" add-on and add it to the app
- In django app install dj_database package by using command pip3 install dj_database_url, and psycopg by using command pip3 install psycopg2-binary
- In django settings.py file import dj_database_url and add database url to DATABASES variable
- Add if statement to use postgres database if there is DATABASE_URL in environment settings

```
if 'DATABASE_URL' in os.environ:
    DATABASES: {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
```

- Run python3 manage.py migrate command to apply all migrations to postgres database

## AWS creating a bucket

- Log in to AWS
- Open S3 services by searching for it in search menu
- On S3 page click on "Create bucket" link
- Creat new bucket by selecting bucket name to match app name
- Select region closest to current location
- Uncheck "Block all public access" checkbox to make bucket publicly available
- When new bucket is created, click on "Properties" tab and turn on static website hosting
- Under "Permissions" tab, add a CORS configuration which can be found in the instructions provided in the Code Institute Boutique-Ado mini-project

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

- Under "Bucket policy" tab generate new policy, copy it to the editor and save it. Policy should be generated using following settings

```
Select Type of Policy: S3 Bucket Policy
Principal: *
Actions: GetObject
Bucket ARN: arn:aws:s3:::sandros-pizza
```

- Under "Access control list" select "list objects" to give access to it for everyone

## AWS Creating a group

- Search for IAM in the search bar at the top, and click on it to set up a group policy
- Under "Access Management" on the left side, click on "User Groups" and create a new group
- Enter group name and click "Create Group"

## AWS creating policy

- Go back to the "Access Management" section on the left side, and click on "Policies"
- Click “Create Policy” and head over to the JSON tab, and select "Import Managed Policy"
- Go to "AmazonS3FullAccess" then click "Import"
- Copy/paste ARN to the code so that it looks like the below:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "arn:aws:s3:::sandros-pizza",
                "arn:aws:s3:::sandros-pizza/*"
            ]
        }
    ]
}
```

- Click on "Next: Tags", "Next: Review", put in a name and click on "Create Policy"

## AWS attach policy to the group

- Click on the newly created group and go over to the "Permissions" tab
- Click on the "Permissions" tab, and select "Attach Policy"
- Select newly created policy and click "Add Permissions"

## AWS creating a user

- Click on "Users" on the left side menu, then "Add User"
- Enter user name and tick the checkbox to give the user access, then click "Next: Permissions"
- Add user to the group and keep clicking the next buttons until the end
- Click to "Create user"
- Download .csv file with access key to connect AWS with django

## Connecting django with AWS

- In django app install boto3 package using command pip3 install boto3
- In django app install django-storages package using command pip3 install django-storages
- Add 'storages' in installed apps in djangoo settings.py file
- Create new file called custom_storages.py in django root folder with following code:

```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

- In django settings.py file add if statement to use AWS if there is USE_AWS variable in environment variables.

```
if 'USE_AWS' in os.environ:

    AWS_STORAGE_BUCKET_NAME = 'sandros-pizza'
    AWS_S3_REGION_NAME = 'eu-central-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

- Manually create a media folder in the S3 bucket and upload all of the site images into it

## Environment variables

- In Heroku settings tab, click on Reveal config vars
- Add all config vars generated by AWS, Stripe, secret key, etc...

---

# CREDITS
[Back to table of contents](#table-of-contents)

## Code credits

CODE CREDIT: [https://stripe.com/docs/payments/accept-a-payment](https://stripe.com/docs/payments/accept-a-payment)
CODE CREDIT: [https://stripe.com/docs/stripe-js](https://stripe.com/docs/stripe-js)

This is JavaScript code from Stripe.com which is used for Stripe functionality in Checkout.js file.

```
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// // Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('.loading').show();

    var saveInfo = Boolean($('#save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';
    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.city.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.city.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('.loading').hide();
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    })
});
```

CODE CREDIT: [https://github.com/karlhadwen/carousel/blob/master/app.js](https://github.com/karlhadwen/carousel/blob/master/app.js)

Code for the carousel on the main page was taken, modified and used in carousel.js file.

```
let carousel = document.getElementsByClassName("pizza-carousel__item")
let carouselPosition = 0
let carouselLength = carousel.length

if (carousel.length > 0) {
    setInterval(moveToNextSlide, 5000);
}

function updateCarouselPosition() {
    for (let item of carousel) {
        item.classList.remove('pizza-carousel__item--active');
    }
    carousel[carouselPosition].classList.add('pizza-carousel__item--active');
}

function moveToNextSlide() {
    if (carouselPosition === carouselLength - 1) {
        carouselPosition = 0;
    } else {
        carouselPosition++;
    }
    updateCarouselPosition();
}

function moveToPrevSlide() {
    if (carouselPosition === 0) {
        carouselPosition = carouselLength - 1;
    } else {
        carouselPosition--;
    }
    updateCarouselPosition();
}
```

** SPECIAL NOTE: The whole project is greatly inspired by "Boutique Ado" project from Code Institute's Software development program which was used as a reference for many functionalities throughout the website. The link to the "Boutique Ado" project can be found here: [Boutique Ado Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546) **

## Media and content credits
  
  - All images for the website are downloaded from [unsplash](https://unsplash.com/) website with free licence.
  
## Acknowledgements

- My mentor Felipe Souza Alarcon for continuous helpful feedback

- Tutor support at Code Institute for their support
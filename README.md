# Sandro's Pizza

**Sandro's Pizza** is E-commerce website and it is part of my 4th milestone project in **Code Institute's Full Stack Software Development Course**. Purpose of the website is to demonstrate proficiency in creating full stack application. Website allows users to make pizza delivery orders, pay for the order and save their details in database for future orders if needed.

---

# TABLE OF CONTENTS:

- [USER EXPERIENCE](#user-experience)
  -  [User stories](#user-stories)
      -  [First time visitors goals](#first-time-visitors-goals)
      -  [Frequent users goals](#frequent-users-goals)
      -  [Site owners goals](#site-owners-goals)
- [WIREFRAMES](#wireframes)
- [DATABASE SCHEMA](#database-schema)
- [TECHNOLOGIES USED](#technologies-used)
  -  [Languages](#languages)
  -  [Frameworks, libraries, programs and websites](#frameworks-libraries-programs-and-websites)
- [DESIGN](#design)
- [FEATURES AND FUNCTIONALITY](#features-and-functionality)
- [TESTING](#testing)
- [DEPLOYMENT](#deployment)
- [CREDITS](#credits)
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

---

# FEATURES AND FUNCTIONALITY
[Back to table of contents](#table-of-contents)

---

# TESTING
[Back to table of contents](#table-of-contents)

---

# DEPLOYMENT
[Back to table of contents](#table-of-contents)

---

# CREDITS
[Back to table of contents](#table-of-contents)

## Acknowledgements

- My mentor Felipe Souza Alarcon for continuous helpful feedback

- Tutor support at Code Institute for their support
# Flavorly 

#### An app where you can save your favorite recipes
![flavoryly logo](./main_app/static/images/flavorly-logo.svg)


## Description
 Flavorly is a personal recipe management app designed to help users create, view, and organize their favorite meals all in one place. I was inspired to build this app by my love for food and cooking—something that brings people together and fuels creativity. A recipe app felt like the perfect way to blend my personal interests with practical coding experience, offering a meaningful project that showcases both functionality and usability.

 The app is built using Python and the Django web framework, leveraging Django’s built-in ORM, authentication system, and form handling to manage data and user interactions efficiently. For the frontend, I used HTML, CSS, and Bootstrap 5 to create a responsive and visually appealing interface. The project also makes use of the Django messages framework for user feedback and utilizes static file management to serve assets like images and custom stylesheets.

## Table of Contents
* [Technologies Used](#technologiesused)
* [Features](#features)
* [Design](#design)
* [Project Next Steps](#nextsteps)
* [Deployed App](#deployment)
* [About the Author](#Author)

## <a name="technologiesused"></a>Technologies Used 
* Python
* Django
* PostgreSQL
* CSS3
* HTML5
* Boostrap 5
* JavaScript
* Django Templates
* Django Messages 
* SVG Icons 



## Features
* User Authentication
* Boostrap Styling
* Form Submit Buttons
* Confirmation Pages
* Icons and SVG Images
* Nav Bar
* Recipe Management
* Ingredient Management
* Toast Messages



## Wireframe Link
* https://lucid.app/lucidspark/46b1dc46-2cff-4509-a681-cd7f4ad7ad93/edit?beaconFlowId=C3D8B79A37887396&page=0_0&invitationId=inv_6f2522d0-66aa-467e-8828-fb7c2f02e6cd#
## Trello Planning
* https://trello.com/b/fRoZaZUY/p4-flavorly

## <a name="design"></a>Design
* For the design of Flavorly, I decided to use Bootstrap as my CSS framework. I wanted to challenge myself by working with a CSS library and learn how to apply its layout and styling tools in a real project. It gave me a way to build the visual side of the app more efficiently, while still letting me adjust things to fit my own ideas.

I went with a simple and clean layout because I wanted the main focus to be on the recipes. The pages are easy to navigate, and everything is kept neat and organized so users can view or manage their recipes without distractions.

In the future, I’d like to improve the look of the app by adding images for recipes and ingredients. I’m thinking of letting users upload their own photos or maybe connecting to a third-party API to automatically pull in related images.


## <a name="nextsteps"></a>Project Next Steps
#### List of Future Features
* Allow users to filter through recipes(other users and their own)
* Allow users to favorite recipes and keep those highlighted at the top of their recipes
* Add in a community page where users can share recipes with one another and top recipes can be showcased 
* Allow users to upload their own images of the recipe 
* Further styling of the application to fill in the blank space
* Add multiple lighting modes (light/dark etc.)


## Github repository
* You can view the repository:
[Github.com](https://flavorly-54ac51c1c004.herokuapp.com)
* If unable to view please go live locally through VS Code

[Flavorly](https://github.com/Zebyrod/flavorly)

## <a name="Zebastian Rodriguez"></a>The Developer
* Zebastian [GitHub](https://github.com/Zebyrod) [LinkedIn](https://www.linkedin.com/in/zebastian-rodriguez-480191309/)

I started learning to code on my own, just out of curiosity. What began as a personal interest quickly turned into a real passion. Wanting to take it further, I decided to take a risk and enroll in the General Assembly Software Engineering Bootcamp.

The course was challenging — there were definitely moments where I was pushed outside my comfort zone — but that’s exactly what made it so valuable. It gave me the tools, structure, and support I needed to grow. One of the biggest takeaways was realizing how much I’m actually capable of when I commit to something.

Building a full-stack application like Flavorly is something I never imagined I’d be able to do when I first started the bootcamp. Seeing this idea come to life through code has been incredibly rewarding, and it’s proof of how much I’ve learned. Completing the program is something I’ll always be proud of — and it's just the beginning of my journey as a developer.

    
## Works Cited:
* Bootstrap 
Bootstrap is an open-source CSS framework used to build responsive, mobile-first websites quickly and efficiently. It provides prebuilt components like grids, buttons, navigation bars, forms, and more — helping developers save time while maintaining consistent design.

I used Bootstrap to style the Flavorly application, including layout structure, form styling, buttons, the navigation bar, and toast messages for user feedback.
- https://getbootstrap.com/docs/5.3/getting-started/introduction/
- https://www.w3schools.com/bootstrap5/

* Toast Messages
Bootstrap Toasts are lightweight notifications designed to provide feedback to users in a subtle, non-intrusive way. They appear temporarily on the screen and can be dismissed by the user.

In Flavorly, I implemented Bootstrap Toast messages to show confirmation and status updates, such as when a recipe is successfully created, updated, or deleted. This improves user experience by providing clear, immediate feedback on their actions. This was super easy as the messages was already included within my installed application so I just had to add the code to pop up the messages on successful actions. 
- https://docs.djangoproject.com/en/5.2/ref/contrib/messages/ 
- https://getbootstrap.com/docs/5.3/components/toasts/#overview


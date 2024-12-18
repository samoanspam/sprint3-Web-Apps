## Overview

**Project Title**:
Django Web Application

**Project Description**:
A simple Django web application that allows users to submit feedback through a form. The feedback is stored in a database and displayed in a "Thank You" page after submission.

**Project Goals**:
* Collect feedback from users.
* Store feedback in a database.
* Provide a simple and user-friendly interface.

## Instructions for Build and Use

Steps to build and/or run the software:

1. Install Python and Django.
2. Clone the project repository or download the project files.
3. Run the following commands to set up the database:
    * python manage.py makemigrations  
    * python manage.py migrate  
4. Start the server using:
    * python manage.py runserver  
5. Visit http://127.0.0.1:8000/feedback/ in your browser.

Instructions for using the software:

1. Go to the feedback form page.
2. Fill out your name, email, and feedback message.
3. Click "Submit" to send your feedback.
4. View the "Thank You" page confirming submission.


## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python
* Django
* SQLite3

## Useful Websites to Learn More

I found these websites useful in developing this software:

* https://docs.djangoproject.com/en/5.1/
* https://www.w3schools.com/django/
* https://www.youtube.com/watch?v=rHux0gMZ3Eg&ab_channel=ProgrammingwithMosh
* https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&ab_channel=CoreySchafer (Of these videos, the ones I watched were 1,3,4, and 10)
* https://codecademy.com

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Add a way to view submitted feedback.
* [ ] Improve the design of the feedback form.
* [ ] Add email notifications for new feedback.
A simple Blog built with Django 
This django application covers the CRUD operation in django. 
The blog is capable of the following

1. Users can create account, Login, Logout and reset password
2. Registered Users can create Post
3. Registered users can like the post of others
4. Only owner of post can delete or edit posts
5. A comment section for users who log in
6. The Project is hosted on heroku on the url below
   https://django_simple_blog.heroku.com


All Views are written with class based view
Post creation uses the django-ckeditor for a more robust blogging
The secret key is hidden in the .env file using the python decouple package


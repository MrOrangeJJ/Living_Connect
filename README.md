To start the server:
Make sure you pip3 install below
Django 
djangorestframework 
djangorestframework-simplejwt 
django-allauth dj-rest-auth 
django-mptt 
django-haystack 
django-widget-tweaks 
django-machina
(let me know if I missed any)

Then run: python3 manage.py runserver
Currently available rest api:

//Only emails that have been added by an administrator can be registered.

Post: http://127.0.0.1:8000/api/auth/registration/

Header:{

Content-Type:application/json

}

Body:{

  "username": "",
  "email": "",
  "password1": "",
  "password2": ""
  
}


Post: http://127.0.0.1:8000/api/auth/login/

Header:{

Content-Type:application/json

}

Body:{

  "username": "",
  "password": "",
  
}


//Get is use to get forum info, post is use to edit info

Post/Get: http://127.0.0.1:8000/api/forum/[forums, topics, posts, attchs]/

Header:{

Authorization: Bearer [jwt from login]

Content-Type:application/json

}

Body:{

}

Abstract classes in the database can currently be managed by accessing django's built-in admin panel by visiting http://127.0.0.1:8000/admin/  (username: admin, pwd: admin). 

For the above mentioned entry of emails that are allowed to register, giving users access to a certain forum can be configured here. 

This will be disabled in the future when we have our own front-end control panel.

You can test the current forum by visiting http://127.0.0.1:8000/forum/ using the django-machine built-in pages. 

Will disable it in the future when we have our own front-end



Feel free to DM me if you have any questions.





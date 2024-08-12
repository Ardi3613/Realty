# How to run project
This project for developement uses sqlite3 if you wanted to deploy it and your host doesn't used sqlite3 you can Contact me so I guid you to install postgresql or mysql on it.

Follow steps below to run project on your local computer
- Install python on your system
- Install virtualenv module with command
``` py -m pip install virtualenv ```; virtual env is good for installing the requirements.txt modules on a encapsulated environment.
- Install Prerequisites with command 
``` py -m pip install -r requiremnts.txt ``` (make sure you are in the project directory)
- Migrate the database; with command ``` py manage.py migrate ``` python models will be migrated on your database so you can create superuser and manage your website
- Craete Super User: in wagtail project it's important to create a superuser (admin) to login into the admin page and manage the contents of your site. with command ``` py manage.py createsuperuser ``` and filling the requested informations you'll get one.
- at the end for running project on your localsystem you have to run the command ``` py manage.py runserver ```

# Pages

Now it's time for pages. pages are django models so you can use them to make different pages and show them in your website with slug url. 

# HomePage

the main page of your site inherits HomePage model click on pages tabs click on + icon in root path of your pages and add a homepage instance and fill the data after you have to add it into your Settings>Sites.

# Settings
here I explain you necessary settings that you have to do for your site in the wagtail admin panel.
## Settings>Sites

in Sites settings click on add new site fill the host name with 0.0.0.0 and the port 8000, choose the HomePage instance as your root page (so when users see your site.com/ url they can see this page) and check the default site checkbox.

## Settings>Site settings
in Site settings you can define options like your header and footer menu and information that will be shown into your header like your company name and other claims.

to add menu items you can do it from header tab and add a a new menu item in Url section you have to write the slug of the page you want to the menu item refer to it. like for Compare page if we have "compare" slug we define it as "/compare/" in the url.

You can see, change and add to the other settings of your site settings with switching between tabs of site settings, like the main tab is used to store your header data like your company name your phone number and etc.
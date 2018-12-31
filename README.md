# pc_project

To run, cmd to folder, run python3 manage.py runserver
To cancel, cmd to folder, CTRL+C

Description:
-- Multi-page site with unique pages. Home page, Quote App page, Login page. 
-- There is an issue where adding a quote does not update the list on the page, user must click back to the page via navigation bar to see the database of quotes. 

11/2/2018
-- Issue with login name and password form showing up. 
-- Layout issues.

11/9/2018 
-- Edited minor spelling issues found within code. This cleaned up some of the layout issues. 
-- Included Bootstrap CSS 3.3.7.
-- Updated navigation bar with Bootstrap.

11/12/2018
-- Removed artifacts. 
-- Managed file locations for header.html for ease.
-- Cleaned up HTML head blocks.
-- Syntax issues between versions seems to have been the issue behind the login issue. As of Django-2.1, the old function-based views have been removed, as specified in the release notes found here https://docs.djangoproject.com/en/2.1/releases/2.1/ into class-based views: the LoginView and LogoutView classes.
-- Login page has been updated, background systems need to be set in place.
-- Updated description to better explain site. 

11/14/2019
--Superuser created, Admin - 123123
-- http://127.0.0.1:8000/admin/ takes you to a prerendered Django admin setup (remember to python3 manage.py runserver before hand).
-- Added in Logout page and Register page.

11/16/2018
-- Updated to Bootstrap 4.1.3.
-- Registration works!!! 
-- Site now directs user to login, and when logged out it directs the user to log back in.
-- User authentication gives access to WebApp form. 
-- Added a 'things to be added' on authenticated home page.

12/4/2018
-- Updated password storage algorithm to Bcrypt. Bcrypt is a long-term password storage and is not used as a default as it uses third-party libraries. 

12/13/18
-- Removed db.sqlite3 in the homes of clearing up the null issue with the missing database. Migrated and recreated super user Admin - 123123. 
-- Created a 'WSGIRequest' object has no attribute 'users' issue. 
-- Removed id=request.Users from webapp.views.py and edited webapp.html which seems to have fixed the WSGIRequest issue. 
-- Login name will now attach to the posted quote. Deleting database for a clean test. 
-- Slight database error, cleaned up with remembering to create a superuser. 
-- Created static folder.
-- Removed static folder, unneeded artifact for failed idea. 

12/19/18
-- Had to pull the 12/13/18 code repository from GitHub due to a fatal issue in code that I somehow caused over the last few hours of working on it. Something migrated, shifted, or merged and I was unable to correct the issue with the help of Google. 
-- I had to edit and complete code that was missing from the 12/13/18 pull, but was safe in GitHub. This includes the accounts app, the accounts template files, shifting the header html outof the webapp folder, and changing and editing the settings.py file. 
-- During the recreation something within the User attachment to the Quote broke. It seems to be a database issue but migrations are not working to correct the issue. 
-- Google says to update the python interpreter, which I did to 3.7. It seems to have cleaned up the Pylint issues if not the database issues. 
-- This is what there error is:
Exception Type: 	OperationalError
Exception Value: 	no such table: webapp_post
Exception Location: home/wbullis/.local/lib/python3.5/site-packages/django/db/backends/sqlite3/base.py in execute, line 296
-- The issue has progressed to a HEAD pointing to an unborn branch which is a fatal error.
-- After a number of fatal errors it became clear that the only way to correct the issues was with a clean clone. I am keeping this for posterty sake. Lesson I did learn to pull a specific branch should this happen again.  
-- git clone -b *branch name* git@pathway
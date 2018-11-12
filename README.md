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
-- Included Bootstrap CSS.
-- Updated navigation bar with Bootstrap.

11/12/2018
-- Removed artifacts. 
-- Managed file locations for header.html for ease.
-- Cleaned up HTML head blocks.
-- Syntax issues between versions seems to have been the issue behind the login issue. As of Django-2.1, the old function-based views have been removed, as specified in the release notes found here https://docs.djangoproject.com/en/2.1/releases/2.1/ into class-based views: the LoginView and LogoutView classes.
-- Login page has been updated, background systems need to be set in place.
-- Updated description to better explain site. 
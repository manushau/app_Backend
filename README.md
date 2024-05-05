
1.Open terminal on your machine and type : git clone https://github.com/alexbaar/app_backend.git

2. then: cd app_backend

3. then : code .

4.  OR instead of steps 1-3 open VS Code (with no project open) , click on the 3rd icon on the vertical panel on the left (source control) and click on 'clone repository'. Then you will need to paste the repo's URL and thats it.

5. the project opens in VS Code

6. you need to generate .venv file, so fllow the below steps:

7. in VS Code terminal type: cd backend_server

8. then: ls

9. you should see a list of : __init__.py, __pycache__, admin.py and other files. That means you are in the right level

    then type: python3 -m venv .venv           (if you work with python, not python3, then type: python ......)

    then: .venv\Scripts\activate     (on Windows)
          source .venv/bin/activate  (on mac)
 

10. then type: pip install Django djangorestframework

11. then go one level up. type: cd ..

12. type: ls

13. you should see: README.md, backend_server and other

14.     add a .env to store sensitive data.
    first in VS Code in terminal type: pip install python-dotenv then at project root add a new file called ' .env ' inside specify the following values:
    
        SECRET_KEY
    
        EMAIL_BACKEND
    
        DEFAULT_FROM_EMAIL


16. type : python3 manage.py makemigrations                          (if you work with python, not python3, then type: python manage.py makemigrations)

17. then: python3 manage.py migrate                                  (if you work with python, not python3, then type: python manage.py makemigrations)

18. to run the backend: python3 manage.py runserver 0.0.0.0:8000     (if you work with python, not python3, then type: python manage.py runserver 0.0.0.0:8000)

19. !!!! Possible errors:
    
    * backend_server.acc_details.image: (fields.E210) Cannot use ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
SOLUTION : run in VS Code terminal:   python -m pip install Pillow   or    python3 -m pip install      Pillow          (check your python version)


    * ModuleNotFoundError: No module named 'dotenv'

SOLUTION : in terminal type : pip list
find dotenv
if found, delete it and re-install
if not found run : pip install python-dotenv
save project. Close VS Code and reopen. The error should be gone now. 



    






    
    

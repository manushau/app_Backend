
1.Open terminal on your machine and type : git clone https://github.com/alexbaar/app_backend.git

2. then: cd app_backend

3. then : code .

4. the project opens in VS Code

5. you need to generate .venv file, so fllow the below steps:

6. in VS Code terminal type: cd backend_server

7. then: ls

8. you should see a list of : __init__.py, __pycache__, admin.py and other files. That means you are in the right level

    then type: python3 -m venv .venv           (if you work with python, not python3, then type: python ......)

    then: .venv\Scripts\activate     (on Windows)
          source .venv/bin/activate  (on mac)
 
![Screenshot 2024-04-04 at 12 51 56 pm](https://github.com/alexbaar/app_backend/assets/63990224/9c7a227b-3aae-4347-b86d-8022994d4da0)

9. then type: pip install Django djangorestframework

10. then go one level up. type: cd ..

11. type: ls

12. you should see: README.md, backend_server and other

![Screenshot 2024-04-04 at 1 08 06 pm](https://github.com/alexbaar/app_backend/assets/63990224/bdbf0c24-795b-402f-825f-c5120f21edec)


13. type : python3 manage.py makemigrations                          (if you work with python, not python3, then type: python manage.py makemigrations)

14. then: python3 manage.py migrate                                  (if you work with python, not python3, then type: python manage.py makemigrations)

15. to run the backend: python3 manage.py runserver 0.0.0.0:8000     (if you work with python, not python3, then type: python manage.py runserver 0.0.0.0:8000)

16. !!!! Possible errors:
    * 
        backend_server.acc_details.image: (fields.E210) Cannot use ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
SOLUTION : run in VS Code terminal:   python -m pip install Pillow   or    python3 -m pip install      Pillow          (check your python version)
    

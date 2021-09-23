# Steps to run a project Locally.

1. Pull the project to your local system from the development branch of of the git repository in some directory.
2. Point to the project directory which contains manage.py file from the Terminal.
3. Create a virtual environment and activate it.
4. Install the requirements from the ' pip install -r requirements.txt ' command.
5. Run python manage.py runserver
6. Request http://127.0.0.1:8000/ and Check if home page appears in the browser.
7. If sucessfull, Run 'python manage.py createsuperuser' and create a superadmin
8. Login to admin site http://127.0.0.1:8000/admin/
9. Add question with question number, marks, answer options and set the correct answer.
10. To play quiz in real time redis server has to be run in the background.
11. Install docker and run ' docker run -p 6379:6379 -d redis:5'
12. Register Users and Join to play the game.

Note : .env file has to be added.
 
 # game-redis branch is for the deployment purpose.

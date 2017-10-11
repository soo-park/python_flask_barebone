# Data Engineering Challenge

## Requirements
Build a simple REST-based web server in Scala or Python that supports the following features:

* Respond to requests of the form 

```“/hello?firstname={first name}&lastname={last name}&gender={m/f}”```

and respond with
```“Hello Mr {First Name} {Last Name}”```
or
```“Hello Ms {First Name} {Last Name}”```
depending on the gender.

Example: the request “/hello?firstname=tien&lastname=nguyen&gender=m” returns “Hello Mr Tien Nguyen”

* Respond to requests of the form 

```“/compute?num1={num1}&num2={num2}&operator={add/subtract/multiply/divide}”```

and respond with the result

Example: the request “/hello?num1=5&num2=3&operation=subtract” returns “2” (5-3=2)

* Respond to requests of the form 

```“/date”```

with the current date in the form “yyyy-mm-dd”

Example: “/date” returns “2017-09-20”


## TO RUN THE APP

1. Open your terminal, make secret.sh file

Command: echo "export secret_key='abc'" >> secret.sh Reason: you want web frame "Flask" and other requirements to run in your computer to test the code, but you do not want to install everything needed to your global environment. Secret.sh file will contain the key for the app to run.

2. Run your virtual environment

Command:

virtualenv env; source env/bin/activate; source secret.sh

Reason: to make the installation run in a limited space

3. Install requirements

Command: 

pip install -r requirements.txt

Reason: all needed installations are saved in requirements.txt. pip is a command for Python to pick up necessary packages and install them.

4. Run server

Command: python server.py

Reason: have your server running, so that what you interact with server-client will be viewable on your browser

5. Run your Flask on browser

Command: localhost:5000 on your browser address bar

Reason: Because your server is running, you can see the site

6. When done, close the server
control c

7. If accidently closed the window
ps -fA | grep python
find the second number of the server
kill (second number)

8. Save environment if dependancies changed
pip freeze > requirements.txt

9. Deactivate virtual env
deactivatae


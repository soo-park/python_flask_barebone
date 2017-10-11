# Data Engineering Challenge

## Requirements
Build a simple REST-based web server in Scala or Python that supports the following features:

* Respond to requests of the form 

```
“/hello?firstname={first name}&lastname={last name}&gender={m/f}”
```

and respond with

```
“Hello Mr {First Name} {Last Name}”
```

or

```
“Hello Ms {First Name} {Last Name}”
```

depending on the gender.

Example: the request “/hello?firstname=tien&lastname=nguyen&gender=m” returns “Hello Mr Tien Nguyen”

* Respond to requests of the form 

```
“/compute?num1={num1}&num2={num2}&operator={add/subtract/multiply/divide}”
```

and respond with the result

Example: the request “/compute?num1=5&num2=3&operation=subtract” returns “2” (5-3=2)

* Respond to requests of the form 

```
“/date”
```

with the current date in the form 

```
“yyyy-mm-dd”
```

Example: “/date” returns “2017-09-20”


======================================



## BASIC INSTRUCTIONS TO RUN THIS FLASK APP

1. Run your virtual environment

Command:

```
virtualenv env; source env/bin/activate;
```

Reason: to make the installation run in a limited space

2. Install requirements

Command: 

```
pip install -r requirements.txt
```

Reason: all needed installations are saved in requirements.txt. pip is a command for Python to pick up necessary packages and install them.

3. Run server

Command:

```
python server.py
```

Reason: have your server running, so that what you interact with server-client will be viewable on your browser

4. Run your Flask on browser

Command: on your browser address bar

```
localhost:5000 
```

Reason: Because your server is running, you can see the result.
Add the above routes to see different results as well

5. When done, close the server

```
control c
```

6. If accidently closed the window and getting error when trying to run Python server again

```
ps -fA | grep python
```

find the second number of the server

```
kill (second number)
```

7. Save environment if dependancies changed

```
pip freeze > requirements.txt
```

8. Deactivate virtual env

```
deactivatae
```
# Codes for Swift Dynamics Test
## Table of Contents
##### Q1 To-Do

##### Q2 Sending Email

##### Q3 Index of the Max value

##### Q4 No. of zero from factorial


## Q1 To-Do
First change directory to the Q1 folder
```
cd Q1
```
Then start django server
```
python manage.py runserver
```
There will be 2 api endpoints as follow:

```
1. GET (all data) or POST (add new data)
/to_do/api

2. GET / PUT / PATCH / DELETE (single data) using id
/to_do/api/<id>
```
You will need to log in (if using webpage) or provide username and password in the HTTP header for RestAPI request. The credentials are as following:

username: admin

password: admin

After logged in, you will be able to see the content.

![image](https://user-images.githubusercontent.com/105768783/169377388-162b4b7e-b5a9-40d3-8be7-006f7af4fcce.png)

Now you can add/replace/change/remove any data using POST/PUT/PATCH/DELETE method respectively.

You can also filter using is_complete=true or false similar to below
```
/to_do/api?is_complete=true
```

## Q2 Sending Email
First change directory to the Q2 folder
```
cd Q2
```
Then locate the setting.py in Q2 folder, change it to your gmail username and password
![image](https://user-images.githubusercontent.com/105768783/169381033-545a0f47-504b-4490-8e81-4a2c91680f9a.png)

Then start django server
```
python manage.py runserver
```
There will be 1 api endpoints as follow:

```
1. GET (all data) or POST (add new data)
/send_email/send

```
You can go to /send_email/send and write email from there
![image](https://user-images.githubusercontent.com/105768783/169382517-c3b6e65d-45e6-478c-b6e1-d20a8e2e6b04.png)

Or you can also send json POST request with following parameters:
```
{
  "recipient": str,
  "email_body": str
}
```
Please note that only 4 recipients are allowed (3 from swift dynamics + my test email)

## Q3 Index of the Max value
Type the following command and input the data as asked
```
python Q3.py
```

## Q4 No. of zero from factorial
Type the following command and input the data as asked
```
python Q4.py
```

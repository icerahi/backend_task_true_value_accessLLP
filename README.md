## Backend 

,
##### **Deployed on pythonanywhere:**

Include Swagger Documentation:
 https://truevalue.pythonanywhere.com


## Run Locally

Clone the project

```bash
  https://github.com/icerahi/backend_task_true_value_accessLLP project
```


### Install dependencies and setup project

Go to project backend directory and write

```bash
  cd project
  virtualenv -p python3 venv 
  source venv/bin/activate
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate 
  python manage.py runserver
```

## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```

  
## API Reference

#### Get all users

```http
  GET /api/users/
```
Response with HTTP status code 200 on success

| Query Parameter | Type     | Example                |
| :-------- | :------- | :------------------------- |
| `page` | `integer` | /api/users/?page=3 ||
| `limit` | `integer` | /api//users/?limit=10 | default is 5|
| `name` | `string` | /api/users/?name=james | |
| `sort` | `string` | /api/users/?sort=-age | |


#### Create a new user

```http
  POST /api/users/
```

| body/required attributes | format     |   status|              
| :-------- | :------- | ----|
| `id,first_name,last_name,company_name,city,state,zip,email,web,age`      | `json` | 201 on success| 

example:
``` 
{
"id": 2,
"first_name": "Josephine",
"last_name": "Darakjy",
"company_name": "Chanay, Jeffrey A Esq",
"city": "Brighton",
"state": "MI",
"zip": 48116,
"email": "josephine_darakjy@darakjy.org",
"web": "http://www.chanayjeffreyaesq.com",
"age": 48
} 
```

#### Get user

```http
  GET /api/users/<id>
```

| Path Parameter | Type     | Example                       |status|
| :-------- | :------- | :-------------------------------- |---|
| `id`      | `int` | /api/users/1  |200 on success|

#### Update user

```http
  PUT /api/users/{id}
```

| Path Parameter | Type     | body/required attributes/format=json | status |
| :-------- | :------- | :-------------------------------- |----|
| `id`      | `int` | `first_name`,`last_name`,`age` |200 on success|


#### Delete a user

```http
 DELETE /api/users/{id}
```

| Path Parameter | Type     | status|
| :-------- | :------- |  -----|
| `id`      | `int` | 200 on success |



## Authors

- [Imran Hasan ](https://linkedin.com/in/icerahi)

  

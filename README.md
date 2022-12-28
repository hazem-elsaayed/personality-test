# Personality Test

<!-- ABOUT THE PROJECT -->
## About The Project

A simple quiz app that determine whether a person is an Extrovert or Intervert by answering a few simple questions.


### Built With


* Django
* Django Rest framework
* SQLite
* Angular
* Bootstrap



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Installation

#### Backend

1. Open a terminal inside `server` folder
2. Create a virtual envirnoment
   ```sh
   python -m venv venv
   ```
3. Activate the environment `source ./venv/bin/activate`
4. Install packages
   ```sh
   pip install -r requirements.txt
   
5. Run server by:
    ```sh
   python manage.py runserver
   ```

#### Frontend

1. Open a terminal inside `frontend` folder
2. Install packages using `npm i` command
3. Run the project using `ng s` command
4. Visit the website http://localhost:4200

<br/> 

<!-- Api routes -->
## Api routes

Route | Request |
:------------ | :-------------|
/api/question/ | GET |
/api/question/  | POST |
/api/question/< id >/   | GET |
/api/question/< id >/   | PATCH |
/api/question/< id >/   | PUT |
/api/question/< id >/   | DELETE |
/api/result/   | POST |

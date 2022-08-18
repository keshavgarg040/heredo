
<h1 align=center> HEREDO </h1>


<p align=center>

 </p>

<img  src="media/readme/mockup.png">


Live app link [here](https://woofmeapp.herokuapp.com/)



## Table of contents
1. [Introduction](#Introduction)
2. [UX](#UX)
    1. [Ideal User Demographic]
    2. [User Stories]
    3. [Development Planes]
    4. [Design]
3. [Features]
    1. [Design Features]
    2. [Existing Features]
    3. [Features to Implement in the future]
4. [Issues and Bugs]
5. [Technologies Used]
     1. [Main Languages Used]
     2. [Additional Languages Used]
     3. [Frameworks, Libraries & Programs Used]
6. [Testing](#Testing)
     1. [Testing.md]
7. [Deployment](#Deployment)
     1. [Deploying on Heroku]
     2. [Forking the Repository]
     3. [Creating a Clone]
8. [Credits]
     1. [Content]
     2. [static/Media]
     3. [Code]
9. [Acknowledgements]



## UX



### User Stories



<details>
<summary> As a user, I would like to be able to:  </summary>

</details>

<details>
<summary>
 As a logged user, I would like to be able to:
</summary>
 
</details>

## 1. Strategy

 + **Project Goal**
  


## 2. Scope 

As a project owner, I would like to create :


## 3. Structure



## 4. Skeleton



### 1.  wireframe

<img width="500" src="media/readme/wireframes/1.png">



### 2.  wireframe

<img width="500" src="media/readme/wireframes/2.png">


### 3. e wireframe

<img width="500" src="media/readme/wireframes/6.png">


### 4. wireframe


<img width="500" src="media/readme/wireframes/5.png">


### 5.  wireframes

 + Login page:

<img width="500" src="media/readme/wireframes/3.png">

+ Register page:

<img width="500" src="media/readme/wireframes/4.png">


## 5. Surface


* Colors


<img width="300" src="media/readme/color_palette.jpg">


* Font selection


<img width="500" src="media/readme/fonts.png">


## Functional Scope 
**Woofme Flowchart**

<img width="500" src="media/readme/chart.png">

**Agile Methodology**


<img width="500" src="media/readme/agile.png">


<details>
<summary>All sprints are described here.</summary>

Test cases were linked with every User story presented above, and can be found in TESTING.md(TESTING.md) - Automated testing section. 

* Sprint 1

  + Setup Django 
  + Heroku Deployment 
  + Create User Stories in Github


* Sprint 2
  + Create User Profile
  + Create Register Page
  + Create Login Page 
  

* Sprint 3
  + Create all models


* Sprint 4
  + Create Add Review feature 
  + Upload an image on breed review
  + Add rating breed feature


* Sprint 5

  + Create a search by breed



* Sprint 6

  + Create final tests + TESTING file
  + README file

</details>


## Features


## Future Features

I would like to implement the following features: 




## Languages Used



## Frameworks, Libraries & Programs Used



## Testing and Code validation 
All code validation and test details can be found [here](TESTING.md).

## Project Bugs and Solutions:

| Bugs              | Solutions |
| ---               | --------- |
| When deploying, the website CSS and database were failing on Heroku. | Debug Update and transfer all data to Postgres. A model did not have a slug as per old migrations.


## Deployment 

This App is deployed using Heroku.

<details>
<summary>Deployment steps </summary>
 
 1. Ensure all apps are listed on requirements.txt. 
 
Command:  ` pip3 freeze > requirements.txt`. 
 
2. Setting up your Heroku
 
  2.1 Login to Heroku and enter your details: 
  command: ` Heroku login -i` 

    
  2.2 Get your app name from Heroku.
    command: `Heroku apps`
    

  2.3 Set the Heroku remote. 
    command: `Heroku git: remote -a woofmeapp`
    

  2.4 Add, commit, and push to GitHub
    command: `git add. && git commit -m "Deploy to Heroku via CLI"`

  2.5 Push to both GitHub and Heroku
    `command: git push origin main`
    `command: git push Heroku main`
       
</details>

# Credits

## Media

+ All pictures and images used in this project are from [Pexels](https://pexels.com).

### Work based on other code



# Acknowledgements

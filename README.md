### ![GA](https://cloud.githubusercontent.com/assets/40461/8183776/469f976e-1432-11e5-8199-6ac91363302b.png) General Assembly - Software Engineering Immersive
# Project Pollinator

Project Pollinator is a website with two goals, one to inspire people to grow ‘nectar cafes’ in their gardens to attract pollinators and the second to be a working database or a ‘hive mind’ for people to upload plants that attract and provide nutrients for pollinators. This is a full stack project where I was able to use Python, PostgreSQL and Flask for the backend and React on the frontend. The project was a solo one that took just over two weeks to build.


## Deployment Link
https://bit.ly/3A1AWzI



## Getting Started

Clone or download the repo then do the following in Terminal:

```bash
Install back-end dependencies: pipenv
Load Seed data for Plants: Pipenv run python seed.py       
Run backend: pipenv run flask run (this will run in portal 4000) 
Install frontend packages: npm i
Start frontend: npm run start 
```





    
## Timeframe & Team

For this project, we had just over two weeks to complete and successfully deploy. While I loved working on previous projects in groups and being able to bounce ideas and challenges with bugs off others, I wanted to prove to myself that I could build this site on my own (an attempt to fend off the imposter syndrome) and thus chose to do it solo. There were a few aspects of React that I wanted to spend more time on as well so this felt like the right choice.
## Tech Stack

**Backend:**

•Python

•PostgreSQL

•Flask

•SQLAlchemy

•Flask-SQLAlchemy

•Marshmallow

•Bcrypt

•JSON Web Token

•Table Plus

•Heroku

**Frontend:**

•React

•Toastify

•React Router Dom

•React Select

•Axios

•Bulma

•CSS

•Netlify 

**Development Tools:**

•Jira

•Excalidraw 

•dbdiagram.io





## Project Brief

•Build a full-stack application by making your own backend and your own frontend

•Use a Python Flask API using a Flask REST Framework to serve your data from a Postgres database

•Consume your API with a separate front-end built with React

•Be a complete product which most likely means multiple relationships and CRUD functionality for at least a couple of models

•Implement thoughtful user stories/wireframes that are significant enough to help you know which features are core MVP and which you can cut

•Have a visually impressive design to kick your portfolio up a notch and have something to wow future clients & employers. ALLOW time for this

•Be deployed online so it's publicly accessible

## Planning

The very first step I took with my project was researching a few websites and fleshing out the ‘point’ of the website. For me this was important as I wanted it to have a reason.

I used Excalidraw to plan out how I envisioned the layout to be.

**Step 1**

Mapping out all the pages:


![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662824727/Screenshot_2022-07-28_at_20.31.36_sofqre.png)

Basic layout for the Home Page:

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662824935/Screenshot_2022-07-28_at_20.28.30_bgixse.png)

The “Nectar Cafe” inspiration page:

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662825025/Screenshot_2022-07-28_at_20.29.28_z1unea.png)

The “Hive Mind” where users can upload their plants:

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662825068/Screenshot_2022-07-28_at_20.29.57_z6h7ki.png)

Login and Register pages:

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662825125/Screenshot_2022-07-28_at_20.30.15_bmbqic.png)

Plants API images/cards pages: 

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662826201/Screenshot_2022-08-26_at_19.09.01_qifkic.png)

**Step 2**

My second step was to have a proper think about the functionality I wanted to have on my frontend and how I would need to design my database to suit that.

Admittedly this was an intensive iterative stage for myself as I felt shaky on how to be creative while keeping in mind the basic functionality that my site had to have on the frontend. At first I decided that I didn’t want to have many-to-many relationships as this would really push me to spend a decent amount of time planning the database. This initially was a struggle for me as the fear of running out of time was quite daunting. Once I calmly looked at it, the ability to have different types of pollinators (birds, bees, butterflies etc) and season really meant that I had to dedicate the time to planning a database that had many-to-many relationships and possibly a few join tables.

My initial (low commitment) database design:

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662826280/Screenshot_2022-07-28_at_20.31.59_uxlcd8.png)

My final design: 

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662826358/Screenshot_2022-07-30_at_15.05.12_fqzixo.png)

**User:**

Here you can see that my user can be attached to many plants, as well as many comments. This allows for any one user to post several plants and comments. The user has to have an ID, username, password and email as required fields in the database. 

**Comment:**

Many comments can belong to one user. Comments can belong to many plants.

**Plant:** 

Many plants can belong to one user (as is stated above) and many plants can have comments. In addition to this a plant has to have an ID, name, latinName, description, season, attacts, image, a relationship with comments, and a relationship with a userID. Plant then also has a one to many relationship with PlantSeason and PlantPollinator (both join tables). 

**PlantSeason:**

PlantSeason is a join table, this means that it has to store the IDs of both the Plants as well as the Season, and its very own PlantSeasonId (all required fields). You can have many PlantSeasons attached to one Plant (think of a plant that blooms both in Spring and Summer). PlantSeason is the many-to-many relationship that ties together Plants with their respective Seasons.

**Season:**

Season has a one-to-many relationship with PlantSeason. It has a required SeasonID, Season and PlantId which enables it to be linked to the correct PlantId through the PlantSeason join table.

**PlantPollinator:**

PlantPollinator is also a join table in my database, thus meaning that it can store the Ids of both the Plants as well as the Pollinators while also having its very own PlantPollinatorID (all required fields). Many Pollinators can be linked to one Plant (bees and butterflies both love Honeysuckle for example).  PlantPollinator is a join table that ties together Plants with their respective Pollinators. 

**Pollinator:**

Pollinator has a one-to-many relationship with PlantPollinator. It has a required PollinatorId, Type and PlantId which enables it to be linked to the correct PlantId through the PlantPollinator join table.

**Step 3**

I knew that I needed something to keep me on track and accountable with my time. For those reasons, I decided to use Jira to plan out all my sprints. I laid out my project on two broad sprints, backend and frontend. For each Sprint, I initially gave myself one week. 

**Sprint 1**

I was able to complete Sprint 1 in 9 days. I had initially wanted that to be 7 days, however, with taking a step back to give myself the time to fully design my database, it was pushed out to 9 days. In the end, I am very happy that I did decide to spend proper time on my database design as it set me up to have all the functionality I wanted to have for my frontend. If I had kept to my initial design I would have faced issues further down the line.

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662826582/Screenshot_2022-08-26_at_20.02.43_ttcdfa.png)

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662826693/Screenshot_2022-08-26_at_20.03.38_x4hm9n.png)

**Sprint 2**

Initially, I had planned on finishing Sprint 2 a few days before the due date, so that I could work on polishing and some stretch goals. I managed to finish it off on the due date. At first, I was quite upset that I had run out of time to spend on stretch goals, however, I am happy with the end result.

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662826806/Screenshot_2022-08-26_at_20.01.36_k1mlkj.png)

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662826831/Screenshot_2022-08-26_at_20.06.08_veijau.png)
## Build Process

**Backend**

The first steps I took with this project was the backend. My first step was to create my models.

I started with my BaseModel which extends out to all my tables, it includes an id, created_at and updated_at columns. It is created using Flask SQLAlchemy.

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662826959/Screenshot_2022-08-30_at_17.26.26_l5ar11.png)

At the top you can see that I am importing the db from the app, the reason for this is to extend the db model from my app file. Basically here I am letting FlaskSQLAlchemy ‘know’ about my BaseModel, so that it can use it. 

To me, my PlantModel is the most interesting and complex as it sets up a ton of the relationships and fields that users have to input into the form on Hive Mind.

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662827044/Screenshot_2022-08-30_at_17.41.31_tibeue.png)

Here you can see that my table is called ‘plants’, it extends the db.Model as well as the BaseModel. Onto those fields, it also requires a name, latinName, description, an image - these are the fields that a user has to input into the form on the Hivemind page. 

There are still quite a few other fields that are linked in the PlantModel, they account for the relationships - user_id (this tells us which user added a plant) and it has a foreignKey which includes the functionality to delete a plant when a user is deleted (ondelete=’CASCADE’). It then also includes the seasons and pollinators, these are relationships which point to their respective Models (SeasonModel and PollinatorModel) while also alerting FlaskSQLAlchemy to the presence of the join tables, plant_season and plant_pollinator. 

Comments are also a relationship that need to be accounted for in the PlantModel, this associate's CommentModel and PlantModel together so they are aware of each other when they need to serialise. This is true for users as well.


Learning Marshmallow was quite tough, understanding the need to serialise took quite some time to click. I came up against a few issues with this in this project, as I forgot to create serializers for each of my models which caused all the bugs.

Once I had fully understood that I needed Marshmallow to serialise my Pythond model into JSON I understood that I would need one for each model. 

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662827104/Screenshot_2022-08-30_at_18.04.40_g4drsw.png)

From the above, you can see that I had to extend the Marshmallow serializer schema from my app. It is a schema which is able to serialise a python model into JSON and deserialize a Python dictionary back into a python model.

Within the Meta class, I am telling it about my model which I want to be able to serialise and deserialize things on. I am basically letting Marshmallow know to give me back a Model when I deserialize, rather than a dictionary. This makes implementing an HTTP API possible as it uses JSON. 

**Frontend**

I really enjoyed coding my frontend with React! I got to integrate it a bit more and understand a few concepts more in depth in this project. 

One of my favourite things that I implemented in my frontend was React Toastify for my notifications. I originally had alerts for any errors with logging in or registering. This looks really old-school and just didn’t have the functionality that I wanted it to have so I looked to React Toastify. 

I was able to implement the code for Toastify fairly simply from the documentation. As you can see from the below, I added it to my try/catches in my Login component:

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662827161/Screenshot_2022-08-30_at_20.25.59_ano6nx.png)

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662827195/Screenshot_2022-08-30_at_20.26.49_vdx5ih.png)

This is the result on the frontend:

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662827334/Screenshot_2022-08-30_at_20.45.02_gfkqcx.png)

The one thing I had challenges with is the navigation of the homepage after the toast had popped up. When initially trying, it automatically navigated to the homepage and the toast didn’t get a chance to show. I remembered from Project 1, we had used setTimeout and tried adding this in to see, after a few goes this worked! I was really happy with this as I had remembered that one my own and was able to implement it independently, which really excited me! 
## Challenges

One of my biggest challenges on this project was the implementation of React Select and how to
code the handleSubmit for my Hive Mind form in the correct way for the database to accept it and save it. 
This gave me major grief as the backend worked perfectly in Insomnia but it was this introduction of React Select on the frontend just wouldn’t. I really love the functionality and look that React Select provides on the frontend form so I pushed through and was eventually able to make it work.

**Functionality of React Select**

React Select on the frontend meant that on the Hive Mind form a user is able to click on Flowering Season or Attracts and select multiple pollinators or seasons to attach to the plant they want to post.

Example:

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662827463/Screenshot_2022-08-29_at_14.46.49_k705hi.png)

This is a seamless feature that is smooth and effortless for the user (hence my desire to make it work). 

In my backend, the pollinator model and season model were structured as their own individual tables with a **type** column (pollinators) and a **season** column (seasons):

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662827545/Screenshot_2022-08-29_at_14.56.38_zi987l.png)

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662827576/Screenshot_2022-08-29_at_14.56.23_easgys.png)

In React Select, I had to create new data files for pollinatorTypes and seasonTypes as React Select needs a **value** and a **label**:

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662827650/Screenshot_2022-08-29_at_15.02.33_k93vqk.png)

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662827652/Screenshot_2022-08-29_at_15.02.51_bhtwda.png)

As I had my seasons and pollinators in my database, I thought I could easily map through those with and simply pick up the pollinator type and seasons season as seen below:

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662827779/Screenshot_2022-08-29_at_15.35.49_vj39js.png)

Here, you can see that I was treating them as if they were coming directly from the database and not from the pollinatorTypes and seasonTypes that I had setup for React Select. I had also forgotten a basic rule, that a handleSubmit is indeed an event, so I needed to extract the value as well as ensure it was in the correct format that my database would allow.
Basically when a user selects a pollinator or season in the frontend, it is an event (within the handleSubmit) and I needed to actually get the value of the selected pollinator and season. I was trying to map through the seasons season and pollinators type like in the above snippet, while not noticing that I actually needed the value from the event and not just the value, but the structure that my database would accept that value in (to match the model) - this was an array with an object that had a type and season.

The code that actually worked:

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662827840/Screenshot_2022-08-29_at_15.46.22_v8ukea.png)

From the above you can see that I am now mapping through my pollinators array (from pollinatorTypes file) and returning the type value, within an object. This structure is super important as it means that it will successfully save into my database as it follows my model design. 

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662827843/Screenshot_2022-08-29_at_15.46.13_fgzdky.png)

The above also shows that I am mapping through the seasons array (from seasonTypes file) and returning the season value, within an object. 

The first step that I took to resolve this issue was to check in Insomnia whether the database would accept me posting pollinators and seasons to it from there. I was able to get this to work, which ruled out there being an issue with how I designed my database (phew). 

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662827918/Screenshot_2022-08-29_at_15.56.12_ak6gat.png)

Another step I took in understanding the issue was to console.log the event and see what that was bringing up. From there I could see that I was not targeting the value, which is what React Select was demanding I do. 

The working/finished function:

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662827966/Screenshot_2022-08-29_at_16.07.09_iby9yh.png)

I think this was a great challenge to encounter on this project as it went back to the basics of events, of the undeniable fact that software engineering is often translating data types and restructuring them to work with different programmes/languages. I think this challenge is what really made me appreciate that I had taken that extra time to plan out my database as if I hadn’t the fix for this might not have been so simple and additional work may have been needed in my backend to get it to work, that is why I was so incredibly happy when I tried it in Insomnia and it worked, that instantly highlighted that the issue was in the frontend. It also highlighted the need to schedule time for debugging. 



## Wins

Simple, visually-pleasing and functioning site, which has responsive capabilities. I was happy to achieve mobile responsiveness as I know that most people use their mobiles nowadays to view and interact with sites. 
I used Bulma with standard CSS in order to style the project, which ensured I could quickly add in mobile responsiveness while ensuring standardisation of the styling across the site. 
I felt like the site came together really nicely, and felt like a real website when I created the icon/logo in Canva. Adding to the Login and Register pages, made it look and feel like a proper project with simple, effective branding. 

Canva Logo: 

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662828263/Screenshot_2022-08-29_at_12.37_1_fuqwur.png)

Mobile Demo:

With this and my images for the plants, I was able to really hone my skills on Cloudinary with resizing images, compressing them and cropping. This was not something I was expecting to learn, but has been a great learning piece out of this project. I find myself increasingly passionate about collecting high resolution images for my database. I believe that this really rounds things off and helps to make the site look like it has been well planned out and professional.

Navigating React Select and translating the data that is given on the frontend into the correct format that the backend needed it to be in order to save the data.

Implementing React Toastify for some stylish notification messages while using setTimeout and useNagivate in order for the user to experience a smooth flow from registering to logging in etc.




## Key Learnings

My biggest learning on this project was time management and expectations management. As with many people, I thought I could complete my backend in less than a week, and my frontend within the same timeframe. This was just not possible with having a full-time job and only being able to dedicate evenings/weekends to the project. I really appreciate that I did take the time in the initial setup of the project to set up sprints in Jira as this kept me accountable and stopped me straying for too long on things like styling or implementing stretch goals. 

Database design takes quite some time to flesh out (as seen from my very low commitment initial design through to the end result). This is time that is worth spending as it meant I did not have to make any changes to my database when working on my frontend, which I really count myself lucky for. I learnt a lot from this and when next building a project that involves a database I will always take this lesson with me.
The backend is never something I thought I would have an interest in, and this project is definitely one that has changed that perspective. I feel so much more confident with PostgreSQL, Flask & Marshmallow after this project and am really looking forward to learning about them more!

PostgreSQL is now probably my preference over MongoDB as I really benefited from having a more ‘user friendly’ interface with Table Plus to see exactly how the data was being saved and retrieved. Initially I struggled with the many-to-many relationships, however having the visual element that Table Plus provides I was able to look at my join tables and easily see how they worked together. 

Seasons:
![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662828475/Screenshot_2022-08-29_at_13.39.47_euq9nq.png)

Pollinators:
![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662828514/Screenshot_2022-08-29_at_13.39.57_a6xqwy.png)

Plants:
![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662828553/Screenshot_2022-08-29_at_13.43.42_idywwz.png)

The join tables:

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662828624/Screenshot_2022-08-29_at_13.40.19_b1im0z.png)

![App Screenshot](https://res.cloudinary.com/dlxbte5xh/image/upload/v1662828626/Screenshot_2022-08-29_at_13.40.11_e0ob92.png)

Working solo I learnt that I really miss the interaction with team members, especially when it comes to inspiration, however, I did also enjoy working solo to implement the vision I had in my mind without considering other opinions. I saw this as my opportunity to take full control and implement the styling exactly how I wanted it as I know in the future I will be working on a team so this might not be possible. From Project 3 I learnt that I loved being a Scrum master and having a team of people that you work with and feedback to you on ideas and features of the project that you are all working on gave me a lot more confidence in stand ups and presentations of projects. I really missed this aspect in this project. 
## Bugs

•Mobile responsiveness not working on title of plants (some plant names for example ‘Honeysuckle’ fall onto two lines as the text is too big)

•Deployed site is not saving new users or their plants as it should (working on this at the moment, believe there is an error with my Heroku setup)

•Toastify notifications are very generic which is not helpful for users if they register/login and have issues

•Ability to PUT (amend) on the frontend doesn’t currently exist.

## Future Improvements 

•Added functionality for amending comments and plants on the frontend

•Cloudinary upload widget so people could easily understand how to upload an image and not only have to use a link for that (they could upload from their local drive)

•Location field on plants so that users can add plants that are local to their area, this could then lend the site to have a new page for all the different continents and regions

•Carousel for the cards on the homepage and Nectar Cafe page so you can swipe through them (on mobile)

•Filter bar on All Plants page so users could easily filter which plants they would plant to attract bats in winter etc

•Search bar on All Plants page so users could easily search for plants

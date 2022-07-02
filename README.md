# Cadius Forums

The Cadius Forum is a site where gamers can come together and engage in conversation. The site contains topics and unique posts from it's users.

To visit the live version of the site (hosted by Heroku) click [here]()

## Project Board

During this project I have been using the project section of Github to manage and track my User Stories progression.

To view the Project Kanban board click [here](https://github.com/robcole-dev/cadius-forum/projects/1)


## User Stories
- As a User I can Create new topics so that I can get other peoples help or opinions
- As a User I can edit my own topics or replys so that I can correct mistakes
- As a User I can delete any of my topics or replys so that I can manage my own entries
- As a User I can create replys to topics so that i can be involved in the conversation
- As a Site Admin I can create, edit and delete topics / replys so that I can manage any bad behaviour
- As a User i can like or dislike topics / replys so that I can give feedback to other users
- As a User I can view Categories and Topics so that I can select what I want to read
- As a User I can register and account so that I can create, like / dislike Topics / replys

## UX

### Wireframes and Designs

Below are a couple of screenshots of flowcharts created for this project.

![Main-Screen](documentation/wireframes/main-screen.jpg)

![Topic-View](documentation/wireframes/topic-view.jpg)

## Features 

Below are a list of key features and future features.

### Existing Features


### Features Left to implement


## Technologies Used

During development of the site a number of programs and web based applications were used. You can find a list of the below:



## Data Model

![Models](documentation/readme/models.jpg)

- The first model is Topics. This acts like a folder of posts relating to that topic. The only fields required are ID and title.
- The second model is Posts. This is user created which then allows other users to comment on. This is link to the Topics model via the topics_id key.
- The third model is Comments. This is for when users comment on a post. This is linked to the Posts model via the post_id key.

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The site was deployed to Heroku. The steps to deploy are as follows: 
- We need to install everything in the requirements.txt file. To do this we run the following command 
 
    ```pip3 install -r requirements.txt```
- Login / signup to [Heroku](https://id.heroku.com/login)
- On the dasboard, once logged in, click New and then click Create new app
- Give the App a name and select your region, then click create app
- Click settings and then click Reveal config Vars. This is where we need to set a couple of things.
- in the Key box enter `PORT` and in the value enter `8000`
- Next we need to add 2 buildpacks. One for python and one for nodejs. Please note that they need to be in an order. python needs to be at the top of the list with nodjs below.
- Click deploy from the menu at the top, then click github.
- enter the repositry name and click search. if found the repositry will appear below, click connect.

[Link to deployed site]()

### Local Deployment

if you would like to make a clone of this repository, you can type the following command in your iDE terminal:

- `git clone `

Alternatively, if using Git pod, you can click below to create your own workspace using this repository.

[![Open in Git pod](https://gitpod.io/button/open-in-gitpod.svg)]()

Please make sure to install the requirements using ```pip3 install -r requirements.txt``` in your terminal

## Credits 

### Content


### Acknowledgments

- 
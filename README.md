## Demo
![GitHub Logo](/screenshot.png)

## Inspiration
In San Francisco, 1 out of 10 people live below the poverty line and there are 8,035 homeless people. Those people suffer from hunger, sickness, and many other ill effects. We wanted to help those people. We did the research and found out the biggest problem that they face was not a lack of help. There are plenty of food banks, charities, and homeless shelters. Rather, they didn't know about all these great services. There could be a food bank offering meals and rehabilitation, but they wouldn't know! So, we built FoodBank to help connect those in need with those services.

## What it does
FoodBank is a Twitter bot. Every certain interval, FoodBank takes tweets that contain specific keywords like #foodbank or # freefood or #foodpantry, assuming that tweets that contain these keywords have information about food being given out. FoodBank retweets those tweets and send a text message to food banks, charities, and homeless people through saved phone numbers. That way, people with and without Twitter would know of the free food giveaways and help in their area.  

## How we built it
We coded in Python. We used Tweepy, a library that allows us to access the Twitter API for looking up tweets and retweeting, as well as the Twilio API which we used to send text messages to specific phone numbers. We used a cron job so that our bot sends a retweet every certain interval.

## Challenges I ran into
Although we had internal disputes over different ideas to use the Twitter API, we all agreed that our project should help people in some shape or form. Eventually, we settled on FoodBank, to help people living in poverty. When we are building FoodBank, we had all sorts of trouble with calling the Twitter API to search tweets and retweet. However, after reading the Tweepy and Twitter API documentation multiple times we were able to solve our problems.

## Accomplishments that I'm proud of
We are extremely satisfied with being able to make our very first bot.

## What I learned
Some of us had experience with Python programming and APIs before, but some of us didn't. Needless to say, we all became better at coding in Python and calling APIs. 

## What's next for FoodBank
Currently, the Twitter bot is operational for San Francisco, but we have big hopes for expansion. To expand the scope of our project, we hope that we can add multiple geo-codes so we can reach out to food banks and churches in multiple locations. We also want to implement Deep Learning into our project so that tweets that don’t provide useful information but still have certain hashtags can be filtered out of our algorithm.

## Run Instructions
1. Download Poetry, and configure the dependencies with `poetry install`
2. Create a new file called config.py, and configure it based on the example at config.py.example.
3. Run main.

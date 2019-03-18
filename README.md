# CS172:  Information Retrieval Final Project
This project utilizes the Twitter Streaming API to collect and map geolocated tweets within 100 miles from user location.

### Team: 🐦 C://Untitled 🐦 
          Katherine Legaspi
          Kevin Frazier
          Nate Mueller

### How to run:






### Design:




 ### Part 1 - Crawler
 1. Collaborate Details: 

   Kevin Frazier: Implemented twitter stream..etc

   Katherine Legaspi: Set up Twitter API keys, basic myStreamListener, and getTitle() function that takes in a url and returns the title of the website

 2. Overview of system

    (a) Architecture

    (b) The Crawling or data collection strategy

    (c) Data Structures employed

 3. Limitations 

 4. How to deploy the crawler

 5. Screenshots

 ### Part 2 - Indexer
 1. Collaborate Details: Nate Mueller 

 2. Overview of system 

    (a) Architecture
 
    (b) Index Structure
 
    (c) Search Algorithm
 
 3. Limitations 
 
 4. How to deploy the system

 ### Part 3 - Extension
 1. Collaborate Details: Katherine Legaspi 

 We chose the Twitter geolocation extension that allows for search and display results on a map. The extension takes in user location, if browser allows, and center maps to the current location. 
 
 Each tweet relevant to the query entered by the user will be marked with a red point. When the marker is clicked, a bubble should display the username, tweet text, and the score.

 A limitation I encountered is that if multiple tweets have the same geolocation (same longitude and latitude), only one tweet is displayed.

Tools: Google Maps API

![map](map.png)
![tweet](tweetMap.png)
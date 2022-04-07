# encounter project

## Contents
* Project Brief
* Project planning
* App design
* CI/CD Pipeline

## Project Brief:
For this project we got tasked with producing an application that had four microservices that are able to interact with eachother to generate objects. 
It was also required that the application was to be created and maintained using a fully automated CI/CD pipline.

##Project Planning

While planning this project i created a risk assessment to recognise the most likely risks for the project.
![Risk assessment](https://github.com/QAEdd/encounterproj/blob/feature3/encounterpics/risk%20assessment.png)

Most of the risks that i looked at were at operational errors that can occur as for this program there is very little user input so the biggest and more likely errors that
may occur are the issues of parts of the pipline failing.

I also created a Jira board to help track the project as i was going along.
![Jira board](https://github.com/QAEdd/encounterproj/blob/feature3/encounterpics/kanbanboard.png)

## App Design

To meet this brief i created a random encounter generator for table top games such as DND. 

Service 1: This was the front end of the application and what the user sees. It is the application that sends of requests to the other services to generate the encounters.

Service 2: This Was a location generator. It randomly chose a location from a set list using random.choice() after receiving a GET request.

Service 3: This was a weather generator. It worked the same as the Location generator using random.choice and a get request.

Service 4: This was the mob generator. It used a POST request taking in what was generated from the Location service then depending on the location chosen would make the
chances of different mobs more likely.

The front end also linked to a NGINX service which listened on port 80 on the host machine and then directs traffic to port 5000 when the front end of the app is usable.

![Main page](https://github.com/QAEdd/encounterproj/blob/feature3/encounterpics/main%20page.png)
![Main page2](https://github.com/QAEdd/encounterproj/blob/feature3/encounterpics/Main%20page22.png)

A couple of examples of the application working.

## CI/CD pipeline

The main aspects of the CI/CD pipeline were:
* Jira - Project Tracking
* Git - version control
* Python - Development Enviroment
* Jenkins - CI server  
* Docker - Deployment enviroment
* Ansible - Configuration management

Version control was done using a public repository hosted on Github. Github allows for the use of the feature branch method. 

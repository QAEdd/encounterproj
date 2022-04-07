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
* Ubuntu virutal machine - Development enviroment
* Jenkins - CI server  
* Docker - Containerisation tool
* Ansible - Configuration management

###Version control 
Version control was done using a public repository hosted on Github. Github allows for the use of the feature branch method, which means i can test changes before pushing them to the main deployment.
![Feature branch](https://github.com/QAEdd/encounterproj/blob/master/encounterpics/featurebranch.png)

### Development Enviroment
The Development of this application was done on a virtual machine hosted on GCP accessed via VScode.

### CI Server

Jenkins was used as the CI server. After receving a push on the git hub repo Jenkins would then clone the repo and excecute the Jenkins script on the repo. This had 4 main stages too it. The first being a test stage where jenkins would run the unit tests that are located for each of the services. The second stage being a build and deploy which would build and push images of the program to dockerhub. The 3rd stage would then deploy these images over a docker swarm using a swarm manager and swarm worker. The 4th and final stage is where it saves the test outputs to a HTML document.

![Jenkins](https://github.com/QAEdd/encounterproj/blob/master/encounterpics/jenkins%20working.png)
Showing the successful running of the pipeline.

![Location api tests](https://github.com/QAEdd/encounterproj/blob/master/encounterpics/locaitonapitest.png)
Location api tests

![Weather api tests](https://github.com/QAEdd/encounterproj/blob/master/encounterpics/weather%20api%20tests.png)
Weather api tests

![Mob api tests](https://github.com/QAEdd/encounterproj/blob/master/encounterpics/mobapitests.png)
Mob api tests

![Front end tests](https://github.com/QAEdd/encounterproj/blob/master/encounterpics/frontendtest.png)
Front end tests

I was able to reach 100% coverage on all the testing i did. This allowed me to know the funcitons of the app worked exactly as intended.


### Containerisation tool
As mentioned earlier my project uses Docker as its containerisation tool. After the tests had been successful it would first build the images for the different services. Once complete it would then push the images to dockerhub using the credentials saved in jenkins. The use of this a this made for easier deployment and much more efficient updating of the application where you can run a rolling update causing no down time to the system.

### Configuration management
For configuration management Ansible was used where running an ansible playbook will get 4 VMs configured and ready to use and deploy the program on which works very nicely incase any of the swarm vm's go down it does not take long to configure another one.

![Ci pipeline](https://github.com/QAEdd/encounterproj/blob/master/encounterpics/cipipeline.png)
The overall structure of the pipeline

### Future improvements
Adding in more diversity in what the applcation has to offer such as a options on what sort of encounter and way of linking it to a more dnd based system. Also adding in a database so the option to save encounters would also be nice.

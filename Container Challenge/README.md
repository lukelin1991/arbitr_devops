# Container Challenge

## Introduction
For this challenge, we have provided you with some python code, the only issue is we don't want to have the overhead of this code needing an entire host. So we need it containerized, showcase your Docker and scripting skills! 

### Criteria
- Create a container that will hold the Python Code [DONE]
- Configure container to allow all python script functionality [DONE]
- Create script to interact with all TestAPI's exposed from Docker container [DONE]
- Create walkthrough documenting all of the steps taken to complete lab [DONE]

#### Bonus
- Document how to utilize script to test API functionality [DONE]
- Show optimizations in Containerization 

### Expected Results
- Python Code is fully functional within a Container [DONE]
- Applicant has created Script to interact with all API funcionality [DONE]
- Documentation on what all steps were taken [DONE]

#### Troubleshooting/Help
- If you encounter any issues with this lab, reach out to employment@arbitrsecurity.com or your HR representative and mention an issue with the "DevOps Container Challenge"

#### WALKTHROUGH Container Challenge (By Luke Lin):
- initial docker setup:
    1) create a requirements.txt (this will be where the dependencies/versions live in)
        - this requirements.txt contains the imports and dependencies as well as the current versions that are compatible (as things get updated, this will need to be adjusted over time)

    2) create dockerfile where the image will be created
        - key commands for dockerfile: FROM, WORKDIR, COPY, RUN, EXPOSE, CMD
        - FROM python:3.9-slim (it's a barebones python 3.9 version that'll work for this app)
        - WORKDIR /app
        - COPY requirements.txt . (will copy whats within requirements.txt into the docker image)
        - COPY . . (although copy . . will copy all files within the directory to docker, it is still good practice to copy requirements.txt separately, as to separate potential concerns, and it's good for optimization)
        - EXPOSE lets me use port 8000 when I specify (pick an available port per container that isn't being used)
        - CMD uvicorn is used because it is one of the dependencies of using fastAPI, host 0.0.0.0 is localhost, and port 8000 is what's opened.
    
    3) creating the interaction with api script
        - I look for the endpoints that are shown in the TestAPIs class for the routers, and create an alternate list to go through them.
        - I decided to use faker to generate random data for the username, email, and full_name which will save me time than manually creating them each time I want to add a new user.
        - I create a userlist thinking that I can use that in order to append the username of the generated user so I do not lose it, so I can have a list of users.
        - I start creating the method for the interaction which loops through the endpoints. 
            1) the first endpoint I have is /hello which is the first api route that was displayed.
            2) the second endpoint is where I needed to add a user
            3) the last endpoint I had to modify as it required the specific username that was created in the /user/add endpoint, so I had to use /user/retrieve/ instead of including the {username} in the endpoints section.
        - I first tackled the adding portion, by first creating a generate_random_data functionality using Faker that lets me return a randomly generated username, email, and full_name for interaction usage.
        - I then set if elif else statements to set request responses based on where it lands.
            1) if it landed on /user/add. it'll trigger the random data generation method and post the information into a response and set the json as the user_data generated.
            2) if it lands on /hello, it'll just say "Hello!"
            3) if it lands on /user/retrieve/, it'll go into a for loop of the username in the Userlist and pull the data from there and get the user information based on the username list and display that information.
        - The response.status_code == 200 just ensures whether the endpoint was successful or not, if it wasn't successful, it will throw a 404 error.
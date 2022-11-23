# Docker Compose

Docker-compose is a tool used to run Docker images from local machines. Docker-compose helps you manage various services in your application, such as Django and databases.


# Step 1: Installing Docker Compose

# Step 2: Building Docker Compose File to Run Django

    Create a file called docker-compose.yml at the root of your project.
    Next, open your settings.py file and add 0.0.0.0 as a value of the ALLOWED_HOSTS since Docker runs on the host (0.0.0.0). The ALLOWS_HOSTS variable holds a list of domains/hosts that can access your application.

# Step 3: Now, run each command below to build and run your Django container.
    
    sudo docker-compose build # Build your Service
    sudo docker-compose up # Runs your application


# Step 4: Finally, open your preferred web browser and navigate to url to run your API.
    
    url: http://0.0.0.0:8000/


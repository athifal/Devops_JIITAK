# Flask Web Application with CI/CD Pipeline

This project demonstrates a simple Flask web application deployed using Docker, AWS EC2, and GitHub Actions for CI/CD automation. The repository contains the following key components:

- **Web Application**: A simple Python Flask app.
- **Dockerization**: The app is containerized using Docker.
- **Deployment**: The Dockerized app is deployed on an AWS EC2 instance.
- **CI/CD Pipeline**: Automated build, push, and deployment using GitHub Actions.
### Deployed Application
[Deployed App](http://44.203.87.46)

## Project Structure

📦 Project Root  
├── `app.py`               # Flask application  
├── `requirements.txt`     # Python dependencies  
├── `Dockerfile`           # Instructions to Dockerize the app  
├── `.github/workflows`    # GitHub Actions workflow for CI/CD  
├── `README.md`            # Project documentation  

## Step-by-Step Guide

### 1. Flask Web Application

A simple Flask application (`app.py`) serves as the base for this project. Install the dependencies using the `requirements.txt` file with the following commands:

```bash
pip install -r requirements.txt
python app.py
```
### 2. Dockerization

The app is containerized using the following `Dockerfile`:

```dockerfile
FROM python:3.9-alpine
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```
### 3. Deployment on AWS EC2

#### Steps:

1. **Create an EC2 Instance**:  
   Launch an EC2 instance and SSH into it.

2. **Install Docker**:  
   Use the following commands to install Docker:

   ```bash
   sudo apt update
   sudo apt install -y docker.io
   ```
3. **Connect to Docker Hub**:  
   Log in to your Docker Hub account and pull the Docker image:

   ```bash
   docker login
   docker pull athifal/flask-app:latest
   ```
 ### 4. CI/CD Pipeline (GitHub Actions)
The GitHub Actions pipeline is defined in the `.github/workflows/ci-cd-pipeline.yml` file. It is triggered when there is a push to the master branch. The steps include:

- **Building and pushing the Docker image**: The image is built and pushed to Docker Hub.
- **Deploying on AWS EC2**: The app is deployed to an EC2 instance by logging in via SSH and executing Docker commands.

### 5. Secrets Configuration
GitHub Secrets are used to securely store credentials:

- `DOCKER_USERNAME` and `DOCKER_PASSWORD` for Docker Hub login.
- `EC2_PEM_KEY` for SSH access to the EC2 instance.

### 6. Deployment on EC2
Once the pipeline is triggered, the app is deployed on the EC2 instance by pulling the latest Docker image from Docker Hub and running it on the EC2 instance. The app will be accessible via port 80.

### How to Access the Deployed App
After the deployment, the Flask app will be running on the EC2 instance. You can access it via the EC2 public IP address on port 80 [http://44.203.87.46](http://44.203.87.46).

### Conclusion
This project demonstrates a complete CI/CD workflow for deploying a Flask app with Docker and AWS EC2, utilizing GitHub Actions for automation.
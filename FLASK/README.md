# Iris Classification AI Model Deployment

This project serves as a beginner-friendly guide to deploying an AI model using Docker. It demonstrates a simple AI model for classifying Iris flowers using the famous Iris dataset from sklearn. The model is trained using machine learning techniques and then deployed using Docker for easy distribution and usage.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Model](#model)
- [Docker Deployment](#docker-deployment)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The primary goal of this project is to provide a step-by-step tutorial for creating and deploying a machine learning model that classifies Iris flowers into one of three species: Setosa, Versicolour, and Virginica. We utilize the well-known Iris dataset from sklearn for training the model. The focus here is not only on building the AI model but also on guiding beginners through the deployment process using Docker.

## Dataset

The Iris dataset contains 150 samples of Iris flowers, each described by four features:
- Sepal length
- Sepal width
- Petal length
- Petal width

Each sample belongs to one of three species of Iris flowers:
- Iris Setosa
- Iris Versicolour
- Iris Virginica

## Model

A simple machine learning model is created using the following steps:
1. Load the Iris dataset from sklearn.
2. Split the dataset into training and testing sets.
3. Train a classifier (e.g., Random forest) on the training set.
4. Evaluate the classifier on the testing set.

## Docker Deployment

The trained model is packaged into a Docker container to ensure consistency and ease of deployment across different environments. The Docker container includes all necessary dependencies and the model itself.

### Prerequisites

1. __Docker__:

	- Ensure Docker is installed on your machine.
	- For Ubuntu or Debian Linux, use:
	```
	sudo apt install docker.io
	```
	- For Windows, download Docker from [here](https://www.docker.com/products/docker-desktop/)

2. __Python__ (Optional): Required only if you want to run the Python code locally on your machine. 
	- Install Python from the [official Python website](https://www.python.org/downloads/).

### Deployment

First, create a file named Dockerfile. This file contains all the commands needed to assemble the Docker image. Below is an overview of our project’s `Dockerfile`, along with an explanation of each step:

```
# Use the official Python image as the base image
FROM python:3.11-slim    # Use a specific version tag to ensure reproducibility

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files into the container
COPY docker-model.py requirements.txt model.pkl ./

# Install any necessary build dependencies temporarily
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python script when the container starts
CMD ["python", "docker-model.py"]

```

### Explanation of the Dockerfile

1. Base Image:
	```
	FROM python:3.11-slim
	```
	This line specifies the base image for the Docker container. In this case, it uses a slim version of Python 3.11, which is a lightweight image with the Python runtime.

2. Set Working Directory:
	```
	WORKDIR /app
	```
	This sets the working directory inside the container to `/app`. All subsequent commands will be run from this directory.

3. Copy Files:
	```
	COPY docker-model.py requirements.txt model.pkl ./
	```
	This command copies all listed files from your current directory on the host machine to the working directory (`/app`) inside the Docker container.

4. Install Dependencies:
	```
	RUN pip install --no-cache-dir -r requirements.txt
	```
	This installs the Python dependencies specified in the `requirements.txt` file. The `--no-cache-dir` option prevents pip from caching the packages, reducing the image size.

5. Command to Run:
	```
	CMD ["python", "docker-model.py"]
	```
	This specifies the command that will run when the container starts. In this case, it will run the `docker-model.py` Python script.


## Installation

### Steps

1. Clone the repository: 
	First, clone the GitHub repository to your desired location. Use the following commands:

    ```bash
    git clone https://github.com/abdur-rahman54/Docker.git
    cd Docker/iris-model
    ```
	This will download the repository and navigate into the iris-model directory, where you can proceed with the next steps.

2. Build the Docker image: 
	To build the Docker image, use the following command format:
	```
	docker build -t <image name> .
	```
	For example, to build an image named `iris-classification`:

    ```bash
    docker build -t iris-classification .
    ```
	Note: You can use any name you prefer for the image instead of `iris-classification`. Don't forget to include the dot (`.`) at the end of the command to specify the current directory as the build context.

3. Run the Docker container: 

	To run a Docker container from the Docker image, use this command format:

	```
	docker run <image name>
	```
	Since we named the image `iris-classification` in the previous step, we can use that name to run the container:

    ```bash
    docker run --rm -it iris-classification
    ```
	In this command:
	- `--rm`: Automatically removes the container when it exits. This helps to keep your system clean by removing unnecessary containers.
	- `-it`: Combines two flags, `-i` (interactive) and `-t` (pseudo-TTY). This allows you to interact with the container via the terminal.

	You should replace 'iris-classification' with your own image name if you used a different name during the build process.


## Usage
This implementation is designed for offline Docker usage on your local machine. If you wish to deploy it in a production environment or make it accessible over a network, additional configuration and setup will be required.

After running the container, you will be prompted to input the features of an iris flower.

![Initial Prompt](https://github.com/abdur-rahman54/Docker/blob/main/images/Initial%20Prompt.jpg)

Enter the four numeric features (sepal length, sepal width, petal length, petal width) separated by spaces. For example: `5.1 3.5 1.4 0.2`

The model will process the input and provide a classification result:

![Prediction Result](https://github.com/abdur-rahman54/Docker/blob/main/images/Prediction%20Result.jpg)

You can continue to input new values for additional predictions. To exit the container, simply type `exit`.

## Files

- [docker-model.py](docker-model.py): The main Python script that loads the model and handles user input.
- [requirements.txt](requirements.txt): Contains the Python dependencies required for the project.
- `model.pkl`: The pre-trained machine learning model. You can find the code in the file named [iris_model.py](iris_model.py).
- [Dockerfile](Dockerfile): Instructions to build the Docker image.
- [ai-model.py](ai-model.py): This file contains the basic version of the `docker-model.py` code.
- [demo-docker.py](demo-docker.py): This file is a simplified version of the `docker-model.py` code.

## Contributing

Contributions to this project are welcome! Whether you want to suggest improvements, report issues, or contribute code, feel free to get involved.


## License

This project is licensed under the [MIT License](../LICENSE), allowing for open collaboration and distribution of the code.
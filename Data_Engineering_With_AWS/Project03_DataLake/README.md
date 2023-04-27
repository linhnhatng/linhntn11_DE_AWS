# STEDI HUMAN BALANCE ANALYTICS

## Spark and Human Balance
As you have learned in this course Spark and AWS Glue allow you to process data from multiple sources, categorize the data, and curate it to be queried in the future for multiple purposes. In this project you will directly use the skills you have used, including some of the code you have already written.

You will go beyond that to write additional AWS Glue jobs to create curated step trainer data that can be used for machine learning.
Project Introduction: STEDI Human Balance Analytics
In this project, you'll act as a data engineer for the STEDI team to build a data lakehouse solution for sensor data that trains a machine learning model.

## Project Details

The STEDI Team has been hard at work developing a hardware STEDI Step Trainer that:

- trains the user to do a STEDI balance exercise;
- and has sensors on the device that collect data to train a machine-learning algorithm to detect steps;
- has a companion mobile app that collects customer data and interacts with the device sensors.

STEDI has heard from millions of early adopters who are willing to purchase the STEDI Step Trainers and use them.

Several customers have already received their Step Trainers, installed the mobile application, and begun using them together to test their balance. The Step Trainer is just a motion sensor that records the distance of the object detected. The app uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions.

The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a primary consideration in deciding what data can be used.

Some of the early adopters have agreed to share their data for research purposes. Only these customers’ Step Trainer and accelerometer data should be used in the training data for the machine learning model.

## Project Summary
As a data engineer on the STEDI Step Trainer team, you'll need to extract the data produced by the STEDI Step Trainer sensors and the mobile app, and curate them into a data lakehouse solution on AWS so that Data Scientists can train the learning model.

Your project work will be evaluated against this rubric. Take a moment to review the requirements of the rubric now, and while you're working on your project to make sure you're meeting all the requirements for deliverables.

## Project Environment
### AWS Environment

You'll use the data from the STEDI Step Trainer and mobile app to develop a lakehouse solution in the cloud that curates the data for the machine learning model using:

- Python and Spark
- AWS Glue
- AWS Athena
- AWS S3
On the next page, you'll find instructions for accessing a temporary AWS account you can use to complete the project. This account has a budget of $25 you should be aware of when creating resources on the AWS platform. Pay special attention to what you are creating and running and the cost of these services.

### Github Environment

You'll also need a github repository to store your SQL scripts and Python code in. You'll submit the code in this github repo for the project submission.

### Workflow Environment Configuration
You'll be creating Python scripts using AWS Glue and Glue Studio. These web-based tools and services contain multiple options for editors to write or generate Python code that uses PySpark. Remember to save any code you develop or run in these editors on AWS to a local Github Repository.

You can use any Python editor locally to work with and save code as well, but be aware that to actually test or run Glue Jobs, you'll need to submit them to your AWS Glue environment.

## Results
1. customer_landing
![image](https://user-images.githubusercontent.com/121186834/234942092-dc804b9c-1e35-4d9d-b7b5-2ef6cd358cc5.png)

2. customer_trusted
![image](https://user-images.githubusercontent.com/121186834/234942154-66165711-8be3-4a48-a4db-21e901122b90.png)

3. accelerometer_landing
![image](https://user-images.githubusercontent.com/121186834/234942135-08102ca6-5324-4aba-9da6-adb6f4d177c5.png)

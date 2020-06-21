# Retail_data-pipeline

The goal of this project was to extract data from a MySQL data base and transform the data i.e aggregate, count and also transfer some tables as they are present in the source to a PostGres data base. The purpose of doing so is to give Data analysts the data that they would be using to generate reports. The processing steps can greatly be 
changed according to the requirements rregarding what data needs to be available in target database based on source database.
I have considered the use cases like analyzing the product table and analyzing the revenue generated, revenue pending 
and analyzing order counts based on order status etc. Many such use cases might exist in the data and i have considered
a few of them. The source for the data will be mentioned in the pre requisites and acknowledgment.

# Motivation
The purpose of this project was to get some experience with docker, Google Cloud Platform, data processing 
using pandas and connecting to databases and pushing data to data base using python.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine or on a remote server like Google Cloud Platform for development and testing purposes. The instructions will be same regardless of developing on your local machine or server.


### Prerequisites

#### Data
The data has been cloned from [retail_db](https://github.com/dgadiraju/retail_db)
Make sure to clone the data from the github link.
#### Docker
Make sure docker is installed in your server.


### Setting up Source (MySQL data base) and target (Postgres database)
The Source and target data bases will be setup as part two docker containers.
First make sure you have cloned the data from the above provided link and docker is installed.
Pull postgres and mysql images using the command
```
sudo docker pull mysql
```
```
sudo docker pull postgres
```
create a network using the command
```
sudo docker network create -d bridge data-pipeline-nw
```

#### Instructions to setup Source Database
create a container using the command
```
sudo docker run --name mysql_retail_db -d -e MYSQL_ROOT_PASSWORD=enter your password here -v retail_db:/retail_db --network data-pipeline-nw -p 3306:3306 mysql
```
After creating the container run the docker command below to enter the container 
```
sudo docker exec -it mysql_retail_db mysql -u root -p
```
This prompts for the password used which is used above while creating the container
After entering the container run the following commands to create database, user and build tables from a .sql script
CREATE DATABASE retail_db;
CREATE USER retail_user IDENTIFIED BY 'your password for database';
FLUSH PRIVILEGES;
USE retail_db;
SOURCE /retail_db/create_db.sql

Now the MySQL data base is up and running and tables are imported to the database in the docker container. Try to validate by running queries on these tables

#### Instructions to setup Target Database
create a container using the command
```
sudo docker run --name pg_retail_db  -e POSTGRES_PASSWORD=enter your password here -d -v /retail_db:/retail_db -p 5432:5432 postgres
```
After creating the container run the docker command below to enter the container 
```
sudo docker exec -it pg_retail_db psql -U postgres -W
```
This prompts for the password used which is used above while creating the container
After entering the container run the following commands to create database, user 
CREATE DATABASE retail_db;
CREATE USER retail_user WITH ENCRYPTED PASSWORD 'your password for db here';
GRANT ALL PRIVILEGES ON DATABASE retail_db TO retail_user;
Now the PostGres data base is up and running in the docker container. 

#### Instructions to build image from this repo and run code
clone this repo to your server or machine.
From terminal enter this repo's directory
cd retail_data-pipeline
Build the image by running the command
```
sudo docker build -t data-copier-live .
```
create a container using the command to establish the connection to MySQL db and transform the data and load into PostGres db
```
sudo docker run --name data-copier -v `pwd`:/app -it data-copier-live
```
The container runs and establishes connection to MySQL db and transorms the data and loads into the target db i.e Postgres and exits after loading the data onto the postGres db . Note that the containers of Mysql and Postgres will always be up and running unless killed . 
Edit the details in config.py to change the source db and target db details i.e db_name,db_pass,db_user etc according to the credentials that you have used to create the databases.
The data extraction and loading will be much faster if all the three containers are part of a same network.




## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

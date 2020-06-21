# Retail_data-pipeline

The goal of this project was to extract data from a MySQL data base and transform the data i.e aggregate, count
and also transfer some tables as they are present in the source to a PostGres data base. The purpose of doing so is 
to give Data analysts the data that they would be using to generate reports. The processing steps can greatly be 
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
Make sure to clone the data from the above github link.
#### Docker
Make sure docker is installed in your server.

```
Give examples
```

### Setting up Source (MySQL data base) and target (Postgres database)
The Source and target data bases will be setup as part two docker container.
First make sure you have cloned the data from the above provided link and docker is installed
#### Instructions to setup Source Database



Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

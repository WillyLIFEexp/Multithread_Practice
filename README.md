# Multithread_Practice
This is a practice for Flask API

## :hammer_and_pick: Technologies Used
- **Language**: Python
- **Testing Framework**: Pytest
- **Containerization**: Docker

## :gear: Prerequisites
- Python 3.8+
- [Docker](https://docs.docker.com/engine/install/) 

## :closed_book: Project Directory Structure
```bash
Flask_API_Practice/
├── app/             # Application source code 
│ ├── main.py        # Contains API endpoints 
├── imgs/            # The demo.gif 
├── requirements.txt # Python dependencies 
├── Dockerfile       # Docker configuration file 
└── README.md        # Documentation for the project
```

## :wrench: Setting up

* Clone the Repo
* Build the container using the following command.
    ```
    docker build -t mt_docker .
    ```
* Starting the container with port mapping and let container to run in the background.
    ```
    docker run mt_docker
    ```
* Stop the container by using the following command.
    ```
    docker stop <container-id-or-name>
    ```

## :tophat: Demonstration
![]()
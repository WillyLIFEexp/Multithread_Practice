# Multithread Practice
This is a practice for Multithread

## :hammer_and_pick: Technologies Used
- **Language**: Python
- **Containerization**: Docker

## :gear: Prerequisites
- Python 3.8+
- [Docker](https://docs.docker.com/engine/install/) 

## :closed_book: Project Directory Structure
```bash
Flask_API_Practice/
├── app/             # Folder for source code 
│ ├── main.py        # Contains application
├── imgs/            # The demo.gif 
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
![](https://github.com/WillyLIFEexp/Multithread_Practice/blob/create_file/imgs/demo_1.gif)

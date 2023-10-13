# Host Details Service

This is a simple web service that displays the server's hostname along with the current date and time.

## Features

- Web service built with Flask
- Displays the server's hostname
- Shows the current date and time

## Docker Image

You can pull the Docker image for this service from Docker Hub: [winzux/host-details-service](https://hub.docker.com/r/winzux/host-details-service).

## Usage

### Run using Docker

```bash
docker run -p 8080:8080 winzux/host-details-service
```

After running the above command, access the service by navigating to `http://localhost:8080` in your web browser.

### Build from Source

First, clone the repository:

```
git clone https://github.com/fitsula/host-details-service.git
cd host-details-service
```

Build the Docker image:

```
docker build -t host-details-service .
```

And then run:

```
docker run -p 8080:8080 host-details-service
```

## Contributions

Feel free to submit pull requests, report bugs, or suggest new features by creating a new issue.


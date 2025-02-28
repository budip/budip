# BP Chat

BP Chat is a simple real-time chat application built using Node.js, Express, and WebSockets (Socket.io). It allows users to communicate in a live chatroom.

## Features

- Real-time messaging with WebSockets (Socket.io)
- Simple and clean UI
- Dockerized setup for easy deployment
- Lightweight and efficient

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- [Node.js](https://nodejs.org/) (LTS recommended)
- [Docker](https://www.docker.com/) (if using Docker for deployment)

### Clone the repository

```sh
git clone https://github.com/yourusername/bp-chat.git
cd bp-chat
```

### Install dependencies

```sh
npm install
```

## Running the Application

### Without Docker

```sh
node server.js
```

The application will be accessible at `http://localhost:3000`

### With Docker

```sh
docker-compose up --build
```

The application will be accessible at `http://localhost:3000`

## Project Structure

```
BP Chat
├── Dockerfile
├── docker-compose.yml
├── node_modules
├── package.json
├── public
│   ├── index.html
│   ├── script.js
│   └── styles.css
└── server.js
```

## Usage

1. Open `http://localhost:3000` in a browser.
2. Enter a username (if applicable) and join the chat.
3. Start sending messages in real time.

## Deployment

To deploy using Docker, you can push the image to a container registry and run it on any cloud provider:

```sh
docker build -t bp-chat .
docker run -p 3000:3000 bp-chat
```

## License

This project is licensed under the MIT License.

---

**Author:** Budi Prasetya - bpchen@gmail.com

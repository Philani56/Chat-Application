# Chat Application
 
This is a basic text-based chat application implemented in Python. It allows two users to exchange messages in real-time using the command line interface. The application follows a simple client-server model for message exchange.

## Features

Real-time messaging between two users
Command line interface for ease of use
Simple client-server architecture

## Requirements

Python 3.x

## How to Use

1. Clone the repository to your local machine:
   
- https://github.com/Philani56/Chat-Application

2. Navigate to the project directory:

- cd chat-application

3. Start the server by running the following command:

- python server.py

4. Once the server is running, open another terminal window/tab and navigate to the project directory.

5. Start the client by running the following command:

python client.py

Follow the prompts to enter your username and start messaging.

The client and server will exchange messages in real-time until either user quits the application.

## Architecture
The application follows a basic client-server model. The server listens for incoming connections from clients and facilitates message exchange between them. Each client connects to the server and sends messages, which are then relayed to the other connected client(s).

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests with your improvements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.




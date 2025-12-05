# Socket Programming Assignment

## Overview
This assignment demonstrates client-server communication using Python sockets. The implementation includes a robust server that can handle multiple clients simultaneously and a feature-rich client with interactive capabilities.

## Files
- `server.py` - Multi-threaded socket server
- `client.py` - Interactive socket client
- `README.md` - This documentation

## Features

### Server Features
- **Multi-client support**: Handles multiple clients simultaneously using threading
- **Error handling**: Robust error handling and graceful shutdown
- **Command processing**: Built-in commands for clients
- **Connection logging**: Detailed logging of client connections and messages
- **Graceful shutdown**: Proper cleanup of resources

### Client Features
- **Interactive mode**: Real-time chat with the server
- **Demo mode**: Automated demonstration of features
- **Simple test mode**: Quick connection test
- **Error handling**: Connection error handling and recovery

### Available Commands
When connected to the server, clients can use these commands:
- `time` - Get current server time
- `echo [message]` - Echo a message back
- `calc [expression]` - Simple calculator (e.g., `calc 5+3`)
- `clients` - Get number of active clients
- `help` - Show available commands
- `quit` - Disconnect from server

## How to Run

### Method 1: Using VS Code
1. **Start the Server:**
   - Open VS Code terminal
   - Navigate to the project directory
   - Run: `python server.py`

2. **Start the Client:**
   - Open a new VS Code terminal (Terminal → New Terminal)
   - Run: `python client.py`
   - Choose your preferred mode (Interactive/Demo/Test)

### Method 2: Using Command Prompt
1. **Terminal 1 (Server):**
   ```bash
   cd "d:\AI ML"
   python server.py
   ```

2. **Terminal 2 (Client):**
   ```bash
   cd "d:\AI ML"
   python client.py
   ```

## Example Usage

### Server Output:
```
==================================================
[SERVER] Socket Programming Assignment
[SERVER] Started at 2025-10-31 10:30:15
[SERVER] Listening on 0.0.0.0:5001
==================================================
[SERVER] New client connected: ('127.0.0.1', 52341)
[CLIENT 1]: Hello from client!
[CLIENT 1]: time
[CLIENT 1]: calc 15+25
```

### Client Output:
```
==================================================
[CLIENT] Socket Programming Assignment Client
[CLIENT] Connected to server at 127.0.0.1:5001
[CLIENT] Connection established at 2025-10-31 10:30:16
==================================================
[SERVER]: Welcome to Socket Server! You are client #1

[CLIENT] Interactive mode started!
[CLIENT] Type 'help' for available commands or 'quit' to exit
--------------------------------------------------

[YOU]: Hello from client!
[SERVER]: Message received by server at 10:30:16: Hello from client!

[YOU]: time
[SERVER]: Current server time: 2025-10-31 10:30:18

[YOU]: calc 15+25
[SERVER]: Calculation result: 15+25 = 40
```

## Technical Details

### Network Configuration
- **Host**: `0.0.0.0` (server listens on all interfaces)
- **Port**: `5001` (configurable)
- **Protocol**: TCP (SOCK_STREAM)
- **Buffer Size**: 1024 bytes

### Architecture
- **Server**: Multi-threaded architecture using Python's `threading` module
- **Client**: Single-threaded with user interaction
- **Communication**: Text-based protocol with UTF-8 encoding

### Error Handling
- Connection timeouts and failures
- Socket binding errors
- Client disconnections
- Keyboard interrupts (Ctrl+C)
- Invalid command handling

## Assignment Requirements Met
1. ✅ Basic socket creation and binding
2. ✅ Server listening for connections
3. ✅ Client-server communication
4. ✅ Message sending and receiving
5. ✅ Proper connection closure
6. ✅ Error handling
7. ✅ Multiple client support (bonus)
8. ✅ Interactive features (bonus)
9. ✅ Command processing (bonus)
10. ✅ Documentation and comments

## Testing
Run both programs to test:
1. Basic connectivity
2. Message exchange
3. Multiple clients (run multiple client instances)
4. Command processing
5. Error handling (disconnect server while client is running)

## Notes
- The server can handle multiple clients simultaneously
- Each client gets a unique ID
- The server logs all client activities
- Both programs handle Ctrl+C gracefully
- Port 5001 can be changed if needed
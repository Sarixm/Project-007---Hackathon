
import os

# ...existing code...

server_port = os.getenv('SERVER_PORT', 5000)
ai_server_port = os.getenv('AI_SERVER_PORT', 5001)

# Example usage
print(f"Server is running on port {server_port}")
print(f"AI Server is running on port {ai_server_port}")

# ...existing code...
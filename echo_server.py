import asyncio
import socket
import logging 

async def echo(connection: socket, loop : asyncio.AbstractEventLoop) -> None:
    buffer = b''

    # to detect exception we need use try/except below but it will not work concurrently well
    # I mean if one person get exception, everyone will lose connection with server
    # To provide concurrency with ability to close connection we can use signals
    try:
        while True:
                while buffer[-2:] != b'\r\n':
                    data = await loop.sock_recv(connection, 1024)
                    if not data:
                        break
                    else:
                        buffer = buffer + data

                if buffer[:-2] == b'quit':
                    raise Exception("Connection closed")
                
                print(f"All the data is: {buffer[:-2]}")
                await loop.sock_sendall(connection, buffer)
                buffer = b''
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close

async def listen_for_connections(server_socket : socket, loop: asyncio.AbstractEventLoop) -> None:
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Got a connection from {address}")
        asyncio.create_task(echo(connection, loop))

async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    await listen_for_connections(server_socket, asyncio.get_event_loop())

asyncio.run(main())

# Output, works fine with 2 concurrent users: 
"""
Got a connection from ('127.0.0.1', 54407)
All the data is: b'testing1'
Got a connection from ('127.0.0.1', 54447)
All the data is: b'testing2'
All the data is: b'testing11'
All the data is: b'testing22'
"""
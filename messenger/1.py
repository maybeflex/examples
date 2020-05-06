import asyncio
from asyncio import transports
from typing import Optional


class ServerProtocol(asyncio.Protocol):
    login: str = None
    server: 'Server'
    transport: transports.Transport

    def __init__(self, server: 'Server'):
        self.server = server

    def connection_lost(self, exception):
        self.server.clients.remove(self)
        print('Клиент вышел')

    def data_received(self, data: bytes):
        print(data)
        decoded = data.decode()
        if self.login is not None:
            self.send_message(decoded)
        else:
            if decoded.startswith("login:"):
                self.login = decoded.replace("login:", "").replace("\r\n", "")
                for user in self.server.clients:
                    if user.login == self.login and user != self:
                        self.transport.write(f'Логин {self.login} занят, попробуйте другой\n'.encode())
                        self.transport.close()
                self.transport.write(
                    f"Привет, {self.login}!\n".encode()
                )
                self.send_history()
                print(self.server.history)
            else:
                self.transport.write('Неправильный логин\n'.encode())

    def connection_made(self, transport: transports.Transport):
        self.server.clients.append(self)
        self.transport = transport
        print('Пришел новый клиент')

    def send_message(self, content: str):
        message = f"{self.login}:{content}\n"
        self.write_history(message)

        for user in self.server.clients:
            user.transport.write(message.encode())

    def send_history(self):
        if len(self.server.history) > 0:
            self.transport.write(f"Last messages >>>\n{(''.join(self.server.history))}".encode())

    def write_history(self, message: str):
        if len(self.server.history) < 10:
            self.server.history.append(message)
        else:
            self.server.history.append(message)
            self.server.history.pop(0)


class Server:
    clients: list
    history: list

    def __init__(self):
        self.clients = []
        self.history = []

    def build_protocol(self):
        return ServerProtocol(self)

    async def start(self):
        loop = asyncio.get_running_loop()

        coroutine = await loop.create_server(
            self.build_protocol,
            '127.0.0.1',
            8888
        )
        print('Server is on')

        await coroutine.serve_forever()


process = Server()

try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print('Серевер остановлен вручную')

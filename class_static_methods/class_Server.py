class Data:
    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip


class Server:
    IP = 0

    def __new__(cls, *args, **kwargs):
        cls.IP += 1
        return super().__new__(cls)

    def __init__(self):
        self.ip = Server.IP
        self.buffer = []
        self.router = None

    def send_data(self, data: Data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        b = self.buffer[:]
        self.buffer.clear()
        return b

    def get_ip(self):
        return self.ip


class Router:
    def __init__(self):
        self.servers = {}  # список серверов
        self.buffer = []  # список для хранения принятых от серверов пакетов (объектов класса Data)

    def link(self, server: Server) -> None:
        self.servers[server.ip] = server
        server.router = self  # сервер указывает на экземпляр класса Router, значит server подключен

    def unlink(self, server: Server) -> None:
        if server.ip in self.servers:
            del self.servers[server.ip]

    def send_data(self):
        for d in self.buffer:
            if d.ip in self.servers:
                self.servers.get(d.ip).buffer.append(d)
        self.buffer.clear()


router = Router()
sv_from = Server()
print("sv_from ip", sv_from.get_ip())
sv_from2 = Server()
print("sv_from2 ip", sv_from2.get_ip())
router.link(sv_from)
router.link(sv_from2)
print("router--", router.servers.items(), router.buffer)
router.link(Server())
router.link(Server())
print("router--", router.servers.items(), router.buffer)
sv_to = Server()
print("sv_to ip", sv_to.get_ip())
router.link(sv_to)
print("router--", router.servers.items(), router.buffer)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
print(sv_from.ip, "->", sv_to.get_ip(), "--->", router.servers.keys(), router.buffer)
sv_from2.send_data(Data("Hello2", sv_to.get_ip()))
print(sv_from2.ip, "->", sv_to.get_ip(), "--->", router.servers.keys(), router.buffer)
sv_to.send_data(Data("Hi", sv_from.get_ip()))
print(sv_to.ip, "->", sv_from.get_ip(), "--->", router.servers.keys(), router.buffer)
print("Router", "data:", router.buffer, "servers", router.servers)
router.send_data()
print("Router", "data:", router.buffer, "servers", router.servers)
print("ip 1 :", sv_from.buffer)
print("ip 5 :", sv_to.buffer)
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"
assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"

from local_game import Game
import socket

TCP_IP = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 1024


class RemoteGame(Game):

    def __init__(self):
        self.name = raw_input('Please fill your name: ')
        self.serv = raw_input('Connect to remote server? (y/N) ')
        self.remote = None
        if self.serv.lower().startswith('y'):
            self.remote = raw_input('Enter remote IP: ') or '127.0.0.1'
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.remote, TCP_PORT))
            self.write_to_other_player = self.s.send
        else:
            my_ip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
            print 'Waiting for someone to login (%s)' % my_ip
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.s.bind((TCP_IP, TCP_PORT))
            self.s.listen(1)
            self.conn, addr = self.s.accept()
            self.write_to_other_player = self.conn.send

    def each_turn(self, i):
        return raw_input("Rock, Paper, Scissors? ")

    def run(self):
        self.other_score = 0
        self.my_score = 0
        if self.remote:
            print self.s.recv(BUFFER_SIZE)
            self.write_to_other_player(self.name)
        else:
            self.conn.send('Welcome to %s game zone\n' % self.name)
            self.other_name = self.conn.recv(BUFFER_SIZE)
        for i in xrange(5):
            if self.remote:
                self.write_to_other_player(self.normalize(self.each_turn(i)))
                print 'Waiting for response'
                print self.s.recv(BUFFER_SIZE)
            else:
                print 'Waiting for %s to response' % self.other_name
                other = self.conn.recv(BUFFER_SIZE)
                my = self.normalize(self.each_turn(i))
                result = '~' * 10
                result += self.fight(my, other).format(p1=self.name, p2=self.other_name)
                result += '~' * 10
                result += "\n{p1}: {s1}\n{p2}: {s2}".format(p1=self.name, p2=self.other_name, s1=self.my_score, s2=self.other_score)
                print result
                self.write_to_other_player(result)
        if self.remote:
            print self.s.recv(BUFFER_SIZE)
        else:
            print self.winner()
            self.conn.send(self.winner())


if __name__ == '__main__':
    a = RemoteGame()
    a.run()
    a.s.close()

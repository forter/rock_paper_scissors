from remote_game import RemoteGame


class ImplementedGame(RemoteGame):
    @staticmethod
    def each_turn():
        return 'rock'


if __name__ == '__main__':
    a = ImplementedGame()
    a.run()
    a.s.close()

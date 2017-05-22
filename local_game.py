from random import choice


class Game(object):

    @staticmethod
    def fight(player1, player2):
        if player1 == player2:
            return_str = "Tie!"
        elif player1 == "Rock":
            if player2 == "Paper":
                return_str = "{p1} lose! paper covers rock"
            else:
                return_str = "{p1} win! rock smashes scissors"
        elif player1 == "Paper":
            if player2 == "Scissors":
                return_str = "{p1} lose! scissors cut paper"
            else:
                return_str = "{p1} win! paper covers rock"
        elif player1 == "Scissors":
            if player2 == "Rock":
                return_str = "{p1} lose... rock smashes scissors"
            else:
                return_str = "{p1} win! scissors cut paper"
        elif player1 == 'exit':
            return_str = "exit"
        return return_str

    @staticmethod
    def normalize(player):
        if player.lower().startswith('r'):
            return 'Rock'
        elif player.lower().startswith('p'):
            return 'Paper'
        elif player.lower().startswith('s'):
            return 'Scissors'
        else:
            print 'Invalid input'

    def run(self):
        computer_score = 0
        player_score = 0

        while True:
            computer = choice(["Rock", "Paper", "Scissors"])
            print 'Player Score: %s' % player_score
            print 'Computer Score: %s' % computer_score
            player = self.each_turn(computer)
            player = self.normalize(player)
            print self.fight(player, computer).format(p1="You", p2="Computer")

    @staticmethod
    def each_turn(computer):
        return raw_input("Rock, Paper, Scissors?")


if __name__ == '__main__':
    Game().run()

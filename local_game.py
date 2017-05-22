from random import choice


class Game(object):

    def fight(self, player1, player2):
        if player1 == player2:
            return_str = "Tie!"
        elif player1 == "Rock":
            if player2 == "Paper":
                self.other_score += 1
                return_str = "{p1} lose! paper covers rock"
            else:
                self.my_score += 1
                return_str = "{p1} win! rock smashes scissors"
        elif player1 == "Paper":
            if player2 == "Scissors":
                self.other_score += 1
                return_str = "{p1} lose! scissors cut paper"
            else:
                self.my_score += 1
                return_str = "{p1} win! paper covers rock"
        elif player1 == "Scissors":
            if player2 == "Rock":
                self.other_score += 1
                return_str = "{p1} lose... rock smashes scissors"
            else:
                self.my_score += 1
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

    def winner(self):
        if self.my_score == self.other_score:
            return 'Its a Tie!'
        elif self.my_score > self.other_score:
            return '%s wins!' % self.name
        else:
            return '%s wins!' % self.other_name

    def run(self):
        self.other_score = 0
        self.my_score = 0
        self.name = "You"
        self.other_name = "Computer"

        for _ in xrange(5):
            computer = choice(["Rock", "Paper", "Scissors"])
            print 'Player Score: %s' % self.my_score
            print 'Computer Score: %s' % self.other_score
            player = self.each_turn(computer)
            player = self.normalize(player)
            print '~' * 10
            print self.fight(player, computer).format(p1=self.name, p2=self.other_name)
            print '~' * 10
        print self.winner()

    @staticmethod
    def each_turn(computer):
        return raw_input("Rock, Paper, Scissors? ")


if __name__ == '__main__':
    Game().run()

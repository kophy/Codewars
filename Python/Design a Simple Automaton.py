class Automaton(object):

    def __init__(self):
        self.state = 1;
        self.table = {1 : {}, 2 : {}, 3 : {}};
        self.table[1][0] = 1;
        self.table[1][1] = 2;
        self.table[2][0] = 3;
        self.table[2][1] = 2;
        self.table[3][0] = 2;
        self.table[3][1] = 2;

    def read_commands(self, commands):
        for c in commands:
            self.state = self.table[self.state][int(c)];
        return self.state == 2;

my_automaton = Automaton()
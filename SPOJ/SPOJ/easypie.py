from sys import stdin, stdout


class Scores:
    prob = []
    time = []
    c = []
    teams = []
    all_teams = []
    submission = []

    def __init__(self):
        self.prob = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.time = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.c = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.teams = [[], [], [], [], [], [], [], [], []]
        self.all_teams = [[], [], [], [], [], [], [], [], []]
        self.submission = [[], [], [], [], [], [], [], [], []]
        self.submission_avg = [[], [], [], [], [], [], [], [], []]

    def update_scores(self, t):
        # select right prob
        i = self.prob.index(t[0])
        # select if the team exists on the teams
        thing_index = self.teams[i].index(t[2]) if t[2] in self.teams[i] else -1
        # select if the team exists on submission team
        thing_index_exist = self.all_teams[i].index(t[2]) if t[2] in self.all_teams[i] else -1
        # prob not solve yet
        # add the team in a list from correct prob if it doesn t exist
        if thing_index_exist == -1:
            self.all_teams[i].append(t[2])
            self.submission[i].append(1)
        # incr the number of submission on this prob
        else:
            self.submission[i][thing_index_exist] += 1
        # prob solve for the first time
        if thing_index == -1 and t[3] == 'A':
            self.submission_avg[i].append(self.submission[i][thing_index_exist])
            # add time to prob
            self.time[i] += int(t[1])
            # add c to prob
            self.c[i] += 1
            # add new team
            self.teams[i].append(t[2])

    def print_scores(self):
        # build final display
        res = ""
        listres = []
        divid = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
        timedivid = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
        for i in range(0, 9):
            if self.c[i] != 0:
                divid[i] = float(sum(self.submission_avg[i])) / float(len(self.submission_avg[i]))
                timedivid[i] = float(self.time[i])/self.c[i]
        for i in range(0, 9):
            if self.c[i] != 0:
                listres.append(self.prob[i] + ' ' + str(self.c[i]) + ' ' + str("%.2f" % divid[i]) + ' ' +
                               str("%.2f" % timedivid[i]) + '\n')
            else:
                listres.append(self.prob[i] + ' ' + str(self.c[i]) + '\n')
        res = res.join(listres)

        return res


def analyse_scores(expression):
    ext = expression.split(' ')
    return ext[2] + ' ' + ext[0] + ' ' + ext[1] + ' ' + ext[3]


def analyse_easypie(nb_line):
    scores = Scores()
    while nb_line != 0:
        expression = stdin.readline()
        c_p_t = analyse_scores(expression).replace("\n", "").split(' ')
        scores.update_scores(c_p_t)
        nb_line -= 1
    return scores.print_scores()


def easypie(nb_line):
    res = ""
    listres = []
    while nb_line != 0:
        listres.append(analyse_easypie(int(stdin.readline())))
        nb_line -= 1
    res = res.join(listres)
    stdout.write(res[:-1])

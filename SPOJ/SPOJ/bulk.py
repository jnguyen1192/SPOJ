from sys import stdin, stdout


def analyse_volume(list):
    return 'The bulk is composed of 992 units.'


def analyse_face(expression):
    list = expression.split('  ')
    face = []
    face.append(list)
    print 'V1 ' + str(list)
    return list.__str__()


def analyse_bulk(nb_line):
    listface = []

    while nb_line != 0:
        expression = stdin.readline()
        face = analyse_face(expression[:-1])
        # Stockage des faces quelque part
        listface.append(face)

        # Analyse des faces
        for i in xrange(1, int(face[0]) + 1):
            print face[i]

        nb_line -= 1
    #list face comporte toutes les faces
    return analyse_volume(listface)


def bulk(nb_line):
    res = ""
    listres = []
    while nb_line != 0:
        listres.append(analyse_bulk(int(stdin.readline())))
        nb_line -= 1
    res = res.join(listres)
    stdout.write(res[:-1])

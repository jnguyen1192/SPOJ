# -*- coding: utf-8 -*-
from stop_words import get_stop_words
import string


def countfullwords(file):
    stop_words = get_stop_words('french')
    fichier = open(file, "r")
    # lis le fichier et le stocke dans un tableau en fonction des espaces
    text = fichier.read().split()
    c = 0
    for i in text:
        # retirer les majuscules
        tmp = i.lower()
        # retirer la ponctuation
        tmp = tmp.translate(None, string.punctuation)
        # retirer les abbrevations
        tmp = tmp.replace('n’', '')
        tmp = tmp.replace('s’', '')
        tmp = tmp.replace('d’', '')
        tmp = tmp.replace('qu’', '')
        # test avec l anti dictionnaire
        if tmp.decode('utf-8') not in stop_words:
            c = c + 1
    print c
countfullwords('INPUT.txt')
import re


def hoofletter_naam(naam):
    n = re.compile('[A-Z]{1}' + '[a-z]+')

    match = n.match(naam)

    return match


def telnr_correct(nummer):
    t = re.compile('[0]{1}' + '[0-9]{9}')

    match = t.match(nummer)

    return match


def ww_nummer(wachtwoord):
    w = re.compile('[a-zA-Z]*' + '[0-9]+')

    match = w.match(wachtwoord)

    return match


def email_valid(email):
    e = re.compile('[^@]+@[^@]+\.[^@]+')

    match = e.match(email)

    return match







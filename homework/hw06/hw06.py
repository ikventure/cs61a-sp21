
passphrase = '*** PASSPHRASE HERE ***'


def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '0a482bce4722c8cced08479fda380c07ed4a3d664ee1bee9c90b6ed9'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()

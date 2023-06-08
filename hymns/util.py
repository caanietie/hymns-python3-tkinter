import sqlite3
from os.path import dirname, abspath

dbpath = abspath(dirname(__file__)+'/data/hymns.sqlite3')


def count_hymns():
    stmt = 'SELECT count(id) FROM hymns'
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        _count = cur.execute(stmt).fetchone()
    return _count[0]


hymn_count = count_hymns()


def get_titles(frm, to):
    stmt = 'SELECT id, title FROM hymns WHERE id BETWEEN ? AND ?'
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        _hymns = cur.execute(stmt, [frm, to]).fetchall()
    return _hymns


def get_hymn(id):
    stmt = 'SELECT * FROM hymns WHERE id IS ?'
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        _hymn = cur.execute(stmt, [id]).fetchone()
    return _hymn


def hashify_hymn(id):
    _hymn = get_hymn(id)
    _res = {
        'id': _hymn[0], 'title': _hymn[1], 'topic': _hymn[2],
        'chorus_type': _hymn[4], 'author': _hymn[7]
    }
    _body = _hymn[3].split('\n\n')
    if _res['chorus_type'] == 0:
        _res['chorus'] = None
        _res['stanza'] = _body
    elif _res['chorus_type'] == 1:
        _res['chorus'] = _body[-1]
        _res['stanza'] = _body[:-1]
    else:
        _res['chorus'] = []
        _res['stanza'] = []
        for i in range(0, len(_body), 2):
            _res['stanza'].append(_body[i])
            _res['chorus'].append(_body[i+1])
    return _res

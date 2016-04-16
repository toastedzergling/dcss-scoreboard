"""Defines the database models for this module."""

from sqlalchemy import TypeDecorator, MetaData, Table, Column
from sqlalchemy import String, Integer
import json
import collections
import sqlalchemy.ext.mutable
import pylru

def _store_game(key, value):
    set_player_score_data(key, value)

PLAYER_SCORE_CACHE = pylru.lrucache(1000, _store_game)



class DatabaseError(Exception):
    """Generic error for issues with the model."""

    pass


def sqlite_performance_over_safety(dbapi_con, con_record):
    """Significantly speeds up inserts but will break on crash."""
    dbapi_con.execute('PRAGMA journal_mode = MEMORY')
    dbapi_con.execute('PRAGMA synchronous = OFF')


def deque_default(obj):
    """Convert deques to lists.

    Used to persist deque data into JSON.
    """
    if isinstance(obj, collections.deque):
        return list(obj)
    raise TypeError


class _JsonEncodedDict(TypeDecorator):
    """Enables JSON storage by encoding and decoding on the fly."""

    impl = String

    def process_bind_param(self, value, dialect):
        """Dict -> JSON String."""
        return json.dumps(value, default=deque_default)

    def process_result_value(self, value, dialect):
        """JSON String -> Dict."""
        return json.loads(value)


sqlalchemy.ext.mutable.MutableDict.associate_with(_JsonEncodedDict)

_metadata = MetaData()

_games = Table('games',
               _metadata,
               Column('gid',
                      String,
                      primary_key=True),
               Column('logfile',
                      _JsonEncodedDict,
                      nullable=False), )

_log_progress = Table('log_progress',
                      _metadata,
                      Column('logfile',
                             String,
                             primary_key=True),
                      Column('lines_parsed',
                             Integer,
                             nullable=False))

_player_scores = Table('player_scores',
                       _metadata,
                       Column('name',
                              String,
                              primary_key=True),
                       Column('scoringinfo',
                              _JsonEncodedDict,
                              nullable=False))

_global_scores = Table('global_scores',
                       _metadata,
                       Column('global_scores',
                              _JsonEncodedDict,
                              nullable=False))

_engine = sqlalchemy.create_engine('sqlite:///scoredata.db', echo=False)
sqlalchemy.event.listen(_engine, 'connect', sqlite_performance_over_safety)
_metadata.create_all(_engine)
_conn = _engine.connect()


def add_game(gid, data):
    """Add a game to the database."""
    try:
        _conn.execute(_games.insert(), gid=gid, logfile=data)
    except sqlalchemy.exc.IntegrityError:
        raise DatabaseError("Duplicate game, ignoring.")


def get_log_pos(logfile):
    """Get the number of lines we've already processed."""
    pass
    # print(dir(model.log_progress.c))
    s = _log_progress.select().where(_log_progress.c.logfile == logfile)
    row = _conn.execute(s).fetchone()
    if row:
        return row.lines_parsed
    else:
        return 0


def save_log_pos(logfile, pos):
    """Save the number of lines we've processed."""
    # print("Saving log pos for", logfile, "as", pos)
    # XXX instead of this try: except:, see if
    # prefixes="OR REPLACE" works
    # http://docs.sqlalchemy.org/en/rel_1_0/core/dml.html#
    #                                       sqlalchemy.sql.expression.insert
    try:
        _conn.execute(_log_progress.insert(),
                      logfile=logfile,
                      lines_parsed=pos)
    except sqlalchemy.exc.IntegrityError:
        _conn.execute(_log_progress.update().where(
            _log_progress.c.logfile == logfile).values(lines_parsed=pos))


def players():
    """Return list of all players.

    XXX should be at least memoised if not outright replaced with something
    saner.
    """
    return [i.name for i in player_scores()]


def player_scores():
    """Return all rows in player_scores table.

    XXX should be at least memoised if not outright replaced with something
    saner.
    """
    s = _player_scores.select()
    return _conn.execute(s).fetchall()


def get_player_score_data(name):
    """Return a dict of the player's current scoring data.

    If the player doesn't exist, None is returned.
    """
    # serve result from the cache if it's there
    if name in PLAYER_SCORE_CACHE:
        return PLAYER_SCORE_CACHE[name]

    s = _player_scores.select().where(_player_scores.c.name == name)
    result = _conn.execute(s).fetchone()
    if result:
        score = result[1]
        # Update the cache
        PLAYER_SCORE_CACHE[name] = score
    else:
        score = None
    return score


def set_player_score_data(name, data):
    """Write player's scoring data to the database.

    XXX this function is the slowest part of scoring.py.
    """
    # print("Saving scoring data for", player)
    PLAYER_SCORE_CACHE[name] = data
    try:
        _conn.execute(_player_scores.insert(), name=name, scoringinfo=data)
    except sqlalchemy.exc.IntegrityError:
        _conn.execute(_player_scores.update().where(
            _player_scores.c.name == name).values(scoringinfo=data))


def games():
    """Return all games.

    Uses a lot of RAM if there are a lot of games.
    XXX fix this.
    """
    s = _games.select()
    return _conn.execute(s).fetchall()

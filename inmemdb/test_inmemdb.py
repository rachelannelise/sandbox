import sys

from inmemdb import Stack, InMemDB, DBSession


def test_db():
    """
    simple db tests
    """
    db = InMemDB()
    assert db.get_data() == {}

    db.set('x', 1)
    assert db.get_data() == {'x': 1}
    assert db.get('x') == 1
    db.set('y', 1)
    assert db.numequalto(1) == 2

    db.unset('x')
    assert db.get('x') == None


# TODO
def test_stack():
    stack = Stack()
    stack.push(1)
    pop = stack.pop()
    assert pop == 1
    assert stack.is_empty() == True

    stack.push(1)
    stack.push(2)
    assert stack.get_stack() == [1, 2]
    stack.reverse()
    assert stack.get_stack() == [2, 1]


# TODO
def test_dbsession():
    db = InMemDB()
    session = DBSession(db)
    # stdin = sys.stdin
    session.process_cmd('SET x 1')
    session.process_cmd('GET x')

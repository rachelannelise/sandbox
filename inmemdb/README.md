### How to use
From a python console:
```
>>> from inmemdb import DBSession, InMemDB
>>> db = InMemDB
>>> session = DBSession(db)
>>> session.begin()
SET x 10
GET x
END
```

To use a command outside of a transaction block:
```
>>> session.run_command()
GET x
```

### Did not get tos:
- Processing a .txt file
- Testing stdin/stdout commands
- Using subprocesses with stdin

### Testing
Install requirements with `pip install -r requirements.txt`

run `pytest .`

### Notes and Requirements:

Data Commands:
- SET
- GET
- UNSET
- NUMEQUALTO
- END

Transaction Commands:
- BEGIN
- ROLLBACK
- COMMIT

Things:
- Transactions (set of commands)
- Database (interprets commands, transactions, and stores values)
- Commands

Input: stdin
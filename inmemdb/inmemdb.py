import sys


class Stack:
    """
    An implementation of a Stack, for queueing transactions in the database
    _stack : A list that can be used LIFO or FIFO with reverse()
    """
    def __init__(self):
        self._stack = []

    def push(self, obj):
        return self._stack.append(obj)

    def pop(self):
        return self._stack.pop()

    def reverse(self):
        self._stack.reverse()

    def is_empty(self):
        return len(self._stack) == 0

    def get_stack(self):
        return self._stack

    def __len__(self):
        return len(self._stack)


class InMemDB:
    """
    Key-Value in-memory store
    """

    def __init__(self):
        self._data = {}

    def get_data(self):
        return self._data

    def get(self, var):
        return self._data.get(var)

    def set(self, var, val):
        self._data[var] = val

    # Not clear yet if unset should delete var or set it to None
    def unset(self, var):
        self._data[var] = None

    def numequalto(self, val):
        eqs = [i for i, x in enumerate(list(self._data.values())) if x == val]
        return len(eqs)

    def __repr__(self):
        return f'Data is {self._data}'


class DBSession:
    """
    A session to issue commands to the InMemDB
    Commands can be sent
    - with stdin using begin()
    - with a file using read_file()
    - as a one-line immediately committed line using run_command()

    """
    def __init__(self, db: InMemDB):
        self._stack = Stack()
        self._db = db

    def begin(self):
        # TODO use subprocesses
        for line in sys.stdin:
            if line.rstrip() == 'END':
                self.end()
                exit(0)
            elif line.rstrip() == 'ROLLBACK':
                self.rollback()
            elif line.rstrip() == 'COMMIT':
                self.commit()
            elif len(line.rstrip()) < 1:
                exit(0)
            elif line.rstrip() == 'BEGIN':
                super().__init__(db=self._db).begin()
            else:
                self._stack.push(line)
                self.commit()


    def read_file(self, file):
        # TODO
        # sys.stdin = open(file, 'r')
        # handle EOF
        pass

    def rollback(self):
        self._stack.pop()
        self.process_stack()

    def commit(self):
        self.process_stack()

    def end(self):
        self.process_stack()

    def process_cmd(self, cmd):
        cmd_split = cmd.split( )
        assert len(cmd_split) > 0
        return cmd_split

    def process_stack(self):
        for cmd in self._stack.get_stack():
            cmd_split = self.process_cmd(cmd)
            first_cmd = cmd_split[0].rstrip()
            output = " "
            if first_cmd == 'GET':
                var = cmd_split[1]
                output = self._db.get(var)
            elif first_cmd == 'SET':
                var = cmd_split[1]
                val = cmd_split[2]
                self._db.set(var, val)
            elif first_cmd == 'UNSET':
                var = cmd_split[1]
                self._db.unset(var)
            elif first_cmd == 'NUMEQUALTO':
                var = cmd_split[1]
                output = self._db.numequalto(var)
            sys.stdout.write(output)

    def run_command(self):
        for line in sys.stdin:
            self._stack.push(line)
            self.commit()
            # This only accepts one line, immediately exit stdin.
            exit(0)




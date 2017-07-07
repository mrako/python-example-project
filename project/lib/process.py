# External
import subprocess # module for running subprocesses from python
import shlex # lexical analysis for splitting command like shell

class Process:

    def __init__(self):
        pass

    def execute(self, command):
        process = subprocess.Popen(shlex.split(command),
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        out, err = process.communicate()
        if process.returncode:
            raise ProcessException(process.returncode)
        return out

class ProcessException(Exception):

    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)

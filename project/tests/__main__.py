import sys, os
from nose.core import TestProgram

sys.path.append(os.path.abspath(os.path.dirname(__file__)).rpartition(os.sep)[0].rpartition(os.sep)[0])
import project.tests
TestProgram(module=project.tests)
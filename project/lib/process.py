import subprocess

class Process:
  
  def __init__(self):
    pass
  
  def execute(self, command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()

    if process.returncode != 0:
      raise ProcessException(process.returncode)
  
    return out


class ProcessException(Exception):

  def __init__(self, value):
    self.parameter = value
  
  def __str__(self):
    return repr(self.parameter)

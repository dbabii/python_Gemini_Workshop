import os
import platform
import sys

# get basic process info
print("Process id:", os.getpid())
print("Parent process id:", os.getppid())
# get platform info
print("Machine network name:", platform.node())
print("Python version:", platform.python_version())
print("System:", platform.system())
# get Python path
print("Python module loookup path:", sys.path)
print("Command to run Python:", sys.argv)
# get user via env var
print("USERNAME environment variable:", os.environ["USER"])
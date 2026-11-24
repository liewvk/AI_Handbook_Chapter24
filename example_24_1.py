import sys
from importlib.metadata import version, PackageNotFoundError
 
print('Interpreter:', sys.executable)
print('Python:', sys.version.split()[0])
try:
    print('MCP package:', version('mcp'))
except PackageNotFoundError:
    print('MCP package not installed')


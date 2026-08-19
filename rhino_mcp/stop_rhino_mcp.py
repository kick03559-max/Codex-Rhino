#! python2
"""Stop a previously loaded RhinoMCP script before reloading an updated one."""

try:
    stop_server()
except NameError:
    pass

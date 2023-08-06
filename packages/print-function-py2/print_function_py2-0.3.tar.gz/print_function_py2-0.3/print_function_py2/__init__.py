#!/usr/bin/env python
# coding=UTF-8

"""
print_function_py2

Print function for Python 1 and Python 2.
Use print3() instead of print().
"""

def print3(*args, **kwargs) :
    """print3(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream."""
    
    try :
        sep = kwargs["sep"]
        del kwargs["sep"]
        if sep == None :
            sep = " "
        elif type(sep) != type("") :
            raise TypeError("sep must be None or a string, not "+str(type(sep)))
    except KeyError :
        sep = " "
    try :
        end = kwargs["end"]
        del kwargs["end"]
        if end == None :
            end = "\n"
        elif type(end) != type("") :
            raise TypeError("end must be None or a string, not "+str(type(end)))
    except KeyError :
        end = "\n"
    try :
        file = kwargs["file"]
        del kwargs["file"]
    except KeyError :
        import sys
        file = sys.stdout
    try :
        flush = kwargs["flush"]
        del kwargs["flush"]
    except KeyError :
        flush = 0
    for i in tuple(kwargs.keys()) :
        raise TypeError("'"+i+"' is an invalid keyword argument for print3()")
    args = list(args)
    for i in range(len(args)) :
        args[i] = str(args[i])
    args = tuple(args)
    message = ""
    for i in args :
        if message != "" :
            message = message + sep
        message = message + str(i)
    file.write(message+end)
    if flush :
        file.flush()

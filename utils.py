# -*- coding: utf-8 -*-

import sys
import ctypes
import ctypes.util

def get_libc_name():
    if sys.platform == 'win32':
        # Parses sys.version and deduces the version of the compiler
        import distutils.msvccompiler
        version = distutils.msvccompiler.get_build_version()
        if version is None:
            # This logic works with official builds of Python.
            if sys.version_info < (2, 4):
                clibname = 'msvcrt'
            else:
                clibname = 'msvcr71'
        else:
            if version <= 6:
                clibname = 'msvcrt'
            else:
                clibname = 'msvcr%d' % (version * 10)

        # If python was built with in debug mode
        import imp
        if imp.get_suffixes()[0][0] == '_d.pyd':
            clibname += 'd'

        return clibname + '.dll'
    else:
        return ctypes.util.find_library('c')

# ctypes extension: get error number
if not hasattr(ctypes, 'get_errno'):
    standard_c_lib = ctypes.cdll.LoadLibrary(get_libc_name())

    # Python 2.5 or older
    if sys.platform == 'win32':
        standard_c_lib._errno.restype = ctypes.POINTER(ctypes.c_int)
        def _where_is_errno():
            return standard_c_lib._errno()

    elif sys.platform in ('linux2', 'freebsd6'):
        standard_c_lib.__errno_location.restype = ctypes.POINTER(ctypes.c_int)
        def _where_is_errno():
            return standard_c_lib.__errno_location()

    elif sys.platform in ('darwin', 'freebsd7'):
        standard_c_lib.__error.restype = ctypes.POINTER(ctypes.c_int)
        def _where_is_errno():
            return standard_c_lib.__error()
    ctypes.get_errno = lambda: _where_is_errno().contents.value

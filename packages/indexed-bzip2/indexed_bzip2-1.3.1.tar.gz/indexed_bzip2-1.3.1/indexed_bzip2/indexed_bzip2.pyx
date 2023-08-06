"""
Cython wrapper for the BZ2Reader and ParallelBZ2Reader C++ classes.
"""

from libc.stdlib cimport malloc, free
from libc.stdio cimport SEEK_SET
from libcpp.string cimport string
from libcpp.map cimport map
from libcpp cimport bool
from cpython.buffer cimport PyObject_GetBuffer, PyBuffer_Release, PyBUF_ANY_CONTIGUOUS, PyBUF_SIMPLE
from cpython.ref cimport PyObject

import io
import os
import sys

ctypedef (unsigned long long int) size_t
ctypedef (long long int) lli


cdef extern from "BZ2Reader.hpp":
    cppclass BZ2Reader:
        BZ2Reader(string) except +
        BZ2Reader(int) except +
        BZ2Reader(PyObject*) except +

        bool eof() except +
        int fileno() except +
        bool seekable() except +
        void close() except +
        bool closed() except +
        size_t seek(lli, int) except +
        size_t tell() except +
        size_t size() except +

        size_t tellCompressed() except +
        int read(int, char*, size_t) except +
        bool blockOffsetsComplete() except +
        map[size_t, size_t] blockOffsets() except +
        map[size_t, size_t] availableBlockOffsets() except +
        void setBlockOffsets(map[size_t, size_t]) except +

cdef extern from "ParallelBZ2Reader.hpp":
    cppclass ParallelBZ2Reader:
        ParallelBZ2Reader(string, size_t) except +
        ParallelBZ2Reader(int, size_t) except +
        ParallelBZ2Reader(PyObject*, size_t) except +

        bool eof() except +
        int fileno() except +
        bool seekable() except +
        void close() except +
        bool closed() except +
        size_t seek(lli, int) except +
        size_t tell() except +
        size_t size() except +

        size_t tellCompressed() except +
        int read(int, char*, size_t) except +
        bool blockOffsetsComplete() except +
        map[size_t, size_t] blockOffsets() except +
        map[size_t, size_t] availableBlockOffsets() except +
        void setBlockOffsets(map[size_t, size_t]) except +
        void joinThreads() except +

def _isFileObject(file):
    return (
        hasattr(file, 'read') and callable(getattr(file, 'read'))
        and hasattr(file, 'seek') and callable(getattr(file, 'seek'))
        and hasattr(file, 'tell') and callable(getattr(file, 'tell'))
        and hasattr(file, 'seekable') and callable(getattr(file, 'seekable'))
    )

def _hasValidFileno(file):
    if not hasattr(file, 'fileno'):
        return False

    try:
        fileno = file.fileno()
        return isinstance(fileno, int) and fileno >= 0
    except Exception:
        return False

cdef class _IndexedBzip2File():
    cdef BZ2Reader* bz2reader
    _fileobj : object  # references counted object kept until the BZ2Reader with the pointer to this is destructed

    def __cinit__(self, file):
        """
        file : can be a file path, a file descriptor, or a file object
               with suitable read, seekable, seek, tell methods.
        """

        if isinstance(file, int):
            self.bz2reader = new BZ2Reader(<int>file)
        elif _hasValidFileno(file):
            self.bz2reader = new BZ2Reader(<int>file.fileno())
        elif _isFileObject(file):
            self._fileobj = file  # store to avoid it being garbage collected
            self.bz2reader = new BZ2Reader(<PyObject*>self._fileobj)
        elif isinstance(file, basestring) and hasattr(file, 'encode'):
            # Note that BytesIO also is an instance of basestring but fortunately has no encode method!
            self.bz2reader = new BZ2Reader(<string>file.encode())
        else:
            raise Exception("Expected file name string, file descriptor integer, or file-like object for BZ2Reader!")

    def __del__(self):
        if not self.closed():
            self.close()

    def __dealloc__(self):
        del self.bz2reader

    def close(self):
        if not self.bz2reader.closed():
            self.bz2reader.close()

    def closed(self):
        return self.bz2reader.closed()

    def fileno(self):
        return self.bz2reader.fileno()

    def seekable(self):
        return self.bz2reader.seekable()

    def readinto(self, bytes_like):
        bytes_count = 0

        cdef Py_buffer buffer
        PyObject_GetBuffer(bytes_like, &buffer, PyBUF_SIMPLE | PyBUF_ANY_CONTIGUOUS)
        try:
            bytes_count = self.bz2reader.read(-1, <char*>buffer.buf, len(bytes_like))
        finally:
            PyBuffer_Release(&buffer)

        return bytes_count

    def seek(self, offset, whence):
        return self.bz2reader.seek(offset, whence)

    def tell(self):
        return self.bz2reader.tell()

    def size(self):
        return self.bz2reader.size()

    def tell_compressed(self):
        return self.bz2reader.tellCompressed()

    def block_offsets_complete(self):
        return self.bz2reader.blockOffsetsComplete()

    def block_offsets(self):
        return <dict>self.bz2reader.blockOffsets()

    def available_block_offsets(self):
        return <dict>self.bz2reader.availableBlockOffsets()

    def set_block_offsets(self, offsets):
        return self.bz2reader.setBlockOffsets(offsets)


cdef class _IndexedBzip2FileParallel():
    cdef ParallelBZ2Reader* bz2reader
    _fileobj : object  # references counted object kept until the BZ2Reader with the pointer to this is destructed

    def __cinit__(self, file, parallelization):
        """
        file : can be a file path, a file descriptor, or a file object
               with suitable read, seekable, seek, tell methods.
        """

        if isinstance(file, int):
            self.bz2reader = new ParallelBZ2Reader(<int>file, <int>parallelization)
        elif _hasValidFileno(file):
            self.bz2reader = new ParallelBZ2Reader(<int>file.fileno(), <int>parallelization)
        elif _isFileObject(file):
            self._fileobj = file  # store to avoid it being garbage collected
            self.bz2reader = new ParallelBZ2Reader(<PyObject*>self._fileobj, <int>parallelization)
        elif isinstance(file, basestring) and hasattr(file, 'encode'):
            # Note that BytesIO also is an instance of basestring but fortunately has no encode method!
            self.bz2reader = new ParallelBZ2Reader(<string>file.encode(), <int>parallelization)
        else:
            raise Exception("Expected file name string, file descriptor integer, "
                            "or file-like object for ParallelBZ2Reader!")


    def __init__(self, *args, **kwargs):
        pass

    def __dealloc__(self):
        self.close()
        del self.bz2reader

    def close(self):
        if not self.bz2reader.closed():
            self.bz2reader.close()
        if self._fileobj:
            self._fileobj.close()

    def closed(self):
        return self.bz2reader.closed()

    def fileno(self):
        return self.bz2reader.fileno()

    def seekable(self):
        return self.bz2reader.seekable()

    def readinto(self, bytes_like):
        bytes_count = 0

        cdef Py_buffer buffer
        PyObject_GetBuffer(bytes_like, &buffer, PyBUF_SIMPLE | PyBUF_ANY_CONTIGUOUS)
        try:
            bytes_count = self.bz2reader.read(-1, <char*>buffer.buf, len(bytes_like))
        finally:
            PyBuffer_Release(&buffer)

        return bytes_count

    def seek(self, offset, whence):
        return self.bz2reader.seek(offset, whence)

    def tell(self):
        return self.bz2reader.tell()

    def size(self):
        return self.bz2reader.size()

    def tell_compressed(self):
        return self.bz2reader.tellCompressed()

    def block_offsets_complete(self):
        return self.bz2reader.blockOffsetsComplete()

    def block_offsets(self):
        return <dict>self.bz2reader.blockOffsets()

    def available_block_offsets(self):
        return <dict>self.bz2reader.availableBlockOffsets()

    def set_block_offsets(self, offsets):
        return self.bz2reader.setBlockOffsets(offsets)

    def join_threads(self):
        return self.bz2reader.joinThreads()

# Extra class because cdefs are not visible from outside but cdef class can't inherit from io.BufferedIOBase

class IndexedBzip2FileRaw(io.RawIOBase):
    def __init__(self, filename, parallelization = 1):
        self.bz2reader = _IndexedBzip2File(filename) if parallelization == 1 \
                         else _IndexedBzip2FileParallel(filename, parallelization)
        self.name = filename
        self.mode = 'rb'

        self.readinto = self.bz2reader.readinto
        self.seek     = self.bz2reader.seek
        self.tell     = self.bz2reader.tell
        self.seekable = self.bz2reader.seekable

        if hasattr(self.bz2reader, 'join_threads'):
            self.join_threads = self.bz2reader.join_threads

        # IOBase provides sane default implementations for read, readline, readlines, readall, ...

    def fileno(self):
        try:
            return self.bz2reader.fileno()
        except Exception as exception:
            raise io.UnsupportedOperation() from exception

    def close(self):
        if self.closed:
            return
        super().close()
        self.bz2reader.close()

    def readable(self):
        return True


class IndexedBzip2File(io.BufferedReader):
    def __init__(self, filename, parallelization = 1):
        fobj = IndexedBzip2FileRaw(filename, parallelization)
        self.bz2reader = fobj.bz2reader

        self.tell_compressed         = self.bz2reader.tell_compressed
        self.block_offsets           = self.bz2reader.block_offsets
        self.set_block_offsets       = self.bz2reader.set_block_offsets
        self.block_offsets_complete  = self.bz2reader.block_offsets_complete
        self.available_block_offsets = self.bz2reader.available_block_offsets
        self.size                    = self.bz2reader.size

        if hasattr(self.bz2reader, 'join_threads'):
            self.join_threads = self.bz2reader.join_threads

        # Most of the calls like close, seekable, name, mode ... are forwarded to the given raw object
        # by BufferedReader or more specifically _BufferedIOMixin
        super().__init__(fobj, buffer_size=1024**2)


def open(filename, parallelization = 1):
    """
    filename: can be a file path, a file descriptor, or a file object
              with suitable read, seekable, seek, and tell methods.
    """
    return IndexedBzip2File(filename, parallelization)


__version__ = '1.3.1'

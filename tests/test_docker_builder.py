import os
import sys
from os.path import join, realpath, dirname

tests_path = dirname(realpath(__file__))
lib_path = realpath(join(tests_path, '../lib/'))
valid_file_path = realpath(join(tests_path, './fixture/builder.yaml'))
empty_file_path = realpath(join(tests_path, './fixture/empty.yaml'))

#
sys.path.insert(0, lib_path)
valid_fd = os.open(valid_file_path, os.O_RDONLY)
empty_fd = os.open(empty_file_path, os.O_RDONLY)

#
from docker_builder import __version__
from docker_builder import LineReader
from docker_builder import Builder
from docker_builder import get_image_id


# http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
def which(program):

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

# Test
assert __version__ == '0.2'

# Test ReadLine
valid_reader = LineReader(valid_fd)
empty_reader = LineReader(empty_fd)
assert valid_reader.fileno() is valid_fd
assert empty_reader.fileno() is empty_fd

empty_lines = empty_reader.readlines()
valid_lines = valid_reader.readlines()
assert empty_lines is None
assert valid_lines is not None
assert type(valid_lines) is list
assert len(valid_lines) > 1

# Tests Builder
empty_builder = Builder(empty_file_path)
valid_builder = Builder(valid_file_path)
assert empty_builder.config is None
assert valid_builder.config is not None
assert type(valid_builder.config) is dict

# Test
empty_image_id = get_image_id('')
valid_image_id = get_image_id('Successfully built' + ' 123')
assert empty_image_id is False
assert valid_image_id == '123'

#
if which('docker'):
    assert True
else:
    pass

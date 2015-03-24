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

# TODO: more tests

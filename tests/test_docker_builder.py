import sys
from os.path import join, realpath, dirname

lib_path = realpath(join(dirname(realpath(__file__)), '../lib/'))

#
sys.path.insert(0, lib_path)

from docker_builder import __version__

assert __version__ == '0.2'

# TODO: more tests

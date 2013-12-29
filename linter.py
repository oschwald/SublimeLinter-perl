#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Gregory Oschwald
# Copyright (c) 2013 Gregory Oschwald
#
# License: MIT
#

"""This module exports the Perl plugin class."""

from SublimeLinter.lint import Linter, util


class Perl(Linter):

    """Provides an interface to perl -c."""

    syntax = ('modernperl', 'perl')
    cmd = 'perl -c'
    regex = r'(?P<message>.+?) at .+? line (?P<line>\d+)(, near "(?P<near>.+?)")?'
    error_stream = util.STREAM_STDERR

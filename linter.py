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
    executable = 'perl'
    base_cmd = ('perl -c')
    regex = r'(?P<message>.+?) at .+? line (?P<line>\d+)(, near "(?P<near>.+?)")?'
    error_stream = util.STREAM_STDERR

    def cmd(self):
        """
        Return the command line to execute.

        Overridden so we can add include paths based on the 'include_dirs'
        settings.

        """

        full_cmd = self.base_cmd

        settings = self.get_view_settings()

        include_dirs = settings.get('include_dirs', [])

        if include_dirs:
            full_cmd += ' ' . join([' -I ' + shlex.quote(include) for include in include_dirs])

        return full_cmd

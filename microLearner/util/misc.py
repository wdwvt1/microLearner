#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2014--, microLearner development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

import click


class AliasedGroup(click.Group):
    ''' Alias for commands.

    This implements a subclass of click.Group that accepts a prefix
    for a command. If there were a (sub)command called "push", it would
    accept "pus" as an alias (so long as it was unique).
    '''
    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx)
                   if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail('Too many matches: %s' % ', '.join(sorted(matches)))


class MultiParamType(click.ParamType):
    def __init__(self, name=None, func=None):
        if name is not None:
            self.name = ' '.join('Multiple', func.__name__)
        else:
            self.name = name
        self.func = func

    def convert(self, value, param, ctx):
        try:
            values = [i for i in value.split(',') if i]
            if self.func is None:
                return values
            else:
                return [self.func(i) for i in values]
        except ValueError:
            self.fail('%s is not a valid method setting' % value, param, ctx)

multi_int = MultiParamType(func=int)

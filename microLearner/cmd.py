#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2014--, microLearner development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------


from __future__ import print_function
from microLearner.util.misc import AliasedGroup
import click
from sklearn import preprocessing

CONTEXT_SETTINGS = dict(token_normalize_func=lambda x: x.lower())


def print_pkg_info(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()


@click.group(cls=AliasedGroup, context_settings=CONTEXT_SETTINGS)
@click.option('--info', is_flag=True, is_eager=True,
              expose_value=False,
              callback=print_pkg_info,
              help='Print package information.')
@click.pass_context
def microLearner(ctx):
    pass


@microLearner.command()
@click.argument('method', nargs=1, default='StandardScaler',
                # specify legal choices for the methods; anything not
                # listed here will be not allowed.
                type=click.Choice(['StandardScaler',
                                   'MinMaxScaler']))
@click.option('-i', '--input_table', type=str, help='Input feature table.')
def preprocess(method, input_table, **kwargs):
    click.echo('Running command %s %s' % (method, input_table))
    if False:
        getattr(preprocessing, method)()
    else:
        pass

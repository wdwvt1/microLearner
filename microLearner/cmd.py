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
from sklearn import preprocessing
import click
import pandas as pd
import numpy as np


CONTEXT_SETTINGS = dict(token_normalize_func=lambda x: x.lower())


@click.group(cls=AliasedGroup, context_settings=CONTEXT_SETTINGS)
@click.option('-v', '--verbose', count=True)
@click.version_option()   # add --version option
@click.pass_context
def microLearner(ctx, verbose):
    pass


@microLearner.command()
@click.argument('method', nargs=1, default='StandardScaler',
                required=True,
                # specify legal choices for the methods; anything not
                # listed here will be not allowed.
                type=click.Choice(['StandardScaler',
                                   'MinMaxScaler']))
@click.option('-i', '--input_table', type=click.File('r'),
              # required=True,
              help='Input feature table.')
@click.option('-o', '--output_table', type=click.File('w'),
              # required=True,
              help='Output feature table.')
@click.option('--feature_range', nargs=2, type=float)
@click.pass_context
def preprocess(ctx, method, input_table, output_table, **kwargs):
    if ctx.parent.params['verbose'] > 0:
        click.echo("Running...")
        click.echo(kwargs)
    if True:
        scaler = getattr(preprocessing, method)(**kwargs)
        i = pd.read_table(input_table)
        print(i)
        o = pd.DataFrame(scaler.fit_transform(np.array(i)), columns=i.columns)
        print(o)
        o.to_csv(output_table, sep='\t')
        # output_table.write(out)
    else:
        print(ctx.parent.params)
        pass

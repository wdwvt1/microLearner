#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2014--, microLearner development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------
from __future__ import print_function
from pandas import DataFrame


class Instances(DataFrame):
    '''
    '''
    def __init__(self, features, outcome):
        self.features = features
        self.outcome = outcome

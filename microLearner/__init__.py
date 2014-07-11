#!/usr/bin/env python
from __future__ import print_function

# ----------------------------------------------------------------------------
# Copyright (c) 2014--,  STREAz development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

__credits__ = "microLearner development team"
__version__ = "1.0.0-dev"

# Naming principles:
# 1) unique (google it)
# 2) easy to remember and pronounce

# SNEAd, SNEAk, SURA,  STREsS
# SENSE           SEarch Ncrna Structured Element
# STREgA 	  STructured Rna Element Annotation
# STREAm 	  STructured Rna Element Annotation
# STREAk 	  STructured Rna Element Annotation

# the double colons and indentation are for rst literal.
title = r"""
::

     ____     _____    ____    U _____ u    _       _____
    / __"| u |_ " _|U |  _"\ u \| ___"|/U  /"\  u  |"_  /u
   <\___ \/    | |   \| |_) |/  |  _|"   \/ _ \/   U / //
    u___) |   /| |\   |  _ <    | |___   / ___ \   \/ /_
    |____/>> u |_|U   |_| \_\   |_____| /_/   \_\  /____|
     )(  (__)_// \\_  //   \\_  <<   >>  \\    >>  _//<<,-
    (__)    (__) (__)(__)  (__)(__) (__)(__)  (__)(__) (_/
   ========== STructrual RNA Element Annotation ==========
"""

art = r"""

"""

if __doc__ is None:
    __doc__ = title + art
else:
    __doc__ = title + art + __doc__

from numpy.testing import Tester
test = Tester().test

if __name__ == '__main__':
    print(title)
    print(art)

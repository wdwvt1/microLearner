Machine Learning Package for Microbiome
=======================================
|Build Status|


``preprocess`` is the subcommand of ``microLearner``. ``MinMaxScaler`` is the argument
to the subcommand. ``--range``, ``-o`` and ``-i`` are the options. The options for the command is insensitive to the letter cases.

``microLearner preprocess MinMaxScaler --range 0 1 -i microLearner/data/otus.txt -o /tmp/foo.txt``

``microLearner preprocess MinMaxScaler --Range 0 1 -i microLearner/data/otus.txt -o /tmp/foo.txt``


.. |Build Status| image:: https://travis-ci.org/RNAer/microLearner.svg?branch=master
   :target: https://travis-ci.org/RNAer/microLearner

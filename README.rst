Machine Learning Package for Microbiome
=======================================
|Build Status|


``preprocess`` is the subcommand of ``microLearner``. ``MinMaxScaler`` is the argument
to the subcommand. ``--min``, ``--max`` and ``-i`` are the options. The options for the command is insensitive to the letter cases.

``microLearner preprocess MinMaxScaler --min 0 --max 1 -i otus.txt``
``microLearner preprocess MinMaxScaler --MIN 0 --MAX 1 -i otus.txt``


.. |Build Status| image:: https://travis-ci.org/RNAer/microLearner.svg?branch=master
   :target: https://travis-ci.org/RNAer/microLearner

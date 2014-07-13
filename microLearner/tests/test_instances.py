#!/usr/bin/env python

from microLearner.instances import Instances
from unittest import TestCase, main


class InstancesTests(TestCase):
    def setUp(self):
        self.a1 = Instances('a', 'b')


if __name__ == "__main__":
    main()

Contributing to microLearner
======================

microLearner is an open source software package, and we welcome community contributions. You can find the source code and test code for microLearner under public revision control in the microLearner git repository.

This document will help you get started with contributing to microLearner. You should read this whole document before considering submitting code to microLearner. This will save time for both you and the microLearner developers.

Type of Submissions
-------------------

Some of the types of contributions we're interested in are new features (big or small, but for big ones it's generally a good idea to ask us if we're interested in including it before starting development), bug fixes, and documentation updates, additions, and fixes.

When considering submitting a new feature to microLearner, you should begin by posting an issue to the [microLearner issue tracker](https://github.com/RNAer/microLearner/issues). The information that you include in that post will differ based on the type of contribution. Your contribution will also need to be fully tested (discussed further below).

* For new features, you'll want to describe why the functionality that you are proposing to add is relevant. For it to be relevant, it should be demonstrably useful to microLearner users. This typically means that a new analytic method is implemented (you should describe why it's useful, ideally including a link to a paper that uses this method), or an existing method is enhanced (your implementation matches the performance of the pre-existing method while reducing runtime, memory consumption, etc, or it improves performance over the pre-existing method). We will request benchmark results comparing your method to the pre-existing methods (which would also be required for publication of your method) so pointing to a paper or other document containing benchmark results, or including benchmark results in your issue, will speed up the process.

* For bug fixes, you should provide a detailed description of the bug so other developers can reproduce it. We take bugs in microLearner very seriously. Bugs can be related to errors in code, documentation, or tests. Errors in documentation or tests are usually updated in the next major release of microLearner. Errors in code that could result in incorrect results or inability to access certain functionality may result in a new minor release of microLearner.

 You should include the following information in your bug report:

 1. The exact command or function call that you issue to create the bug.
 2. A link to all necessary input files for reproducing the bug. These files should only be as large as necessary to create the bug. For example, if you have an input file with 10,000 data points but the error only arises due to one of them, create a new input file with a few data points including that one, run the command that was giving you problems, and verify that you still get an error. Then post that command and link to the trimmed input file. This is *extremely* useful to other developer, and it is likely that if you don't provide this information you'll get a response asking for it. Often this process helps you to better understand the bug as well.

* For documentation additions, you should first post an issue describing what you propose to add, where you'd like to add it in the documentation, and a description of why you think it's an important addition. For documentation improvements and fixes, you should post an issue describing what is currently wrong or missing, and how you propose to address it. For more information about building and contributing to microLearner's documentation, see [this guide](doc/README.md).

When you post your issue, the microLearner developers will respond to let you know if we agree with the addition or change. It's very important that you go through this step to avoid wasting time working on a feature that we are not interested in including in microLearner.


Getting started: "help wanted"
------------------------------

Some of our issues are labeled as ``help wanted``. Working on [these issues](https://github.com/RNAer/microLearner/issues?direction=desc&labels=quick+fix%2Chelp+wanted&page=1&sort=updated&state=open) is a good way to get started with contributing to microLearner. These are usually small bugs or documentation errors that will only require one or a few lines of code to fix. Getting started by working on one of these issues will allow you to familiarize yourself with our development process before committing to a large amount of work (e.g., adding a new feature to microLearner). If you're interested in working on one of these issues, you should comment on the issue requesting that it be assigned to you.


Code Review
-----------

When you submit code to microLearner, it will be reviewed by one or more microLearner developers. These reviews are intended to confirm a few points:

* Your code is sufficiently well-tested (see Testing Guidelines below).
* Your code adheres to our Coding Guidelines (see Coding Guidelines below).
* Your code is sufficiently well-documented (see Coding Guidelines below).
* Your code provides relevant changes or additions to microLearner (Type of Submissions above).

This process is designed to ensure the quality of microLearner, and can be a very useful experience for new developers.

Particularly for big changes, if you'd like feedback on your code in the form of a code review as you work, you should request help in the issue that you created and the microLearner developers will work with you to perform regular code reviews. This can greatly reduce development time (and frustration) so we highly recommend that new developers take advantage of this rather than submitting a pull request with a massive amount of code in one chunk. That can lead to frustration when the developer thinks they are done, but the reviewer requests large amounts of changes, and it is also very hard to review.


Submitting code to microLearner
-------------------------------

microLearner is hosted on [GitHub](http://www.github.com), and we use GitHub's [Pull Request](https://help.github.com/articles/using-pull-requests) mechanism for accepting submissions. You should go through the following steps to submit code to microLearner.

1. Begin by [creating an issue](https://github.com/RNAer/microLearner/issues) describing your proposed change. This should include a description of your proposed change (is it a new feature, a bug fix, etc.), and note in the issue description that you want to work on it. Once you hear back from a maintainer that it is OK to make changes (i.e., they dont't have local edits, they agree with the change you'd like to make, and they're comfortable with you editing their code), we will assign the issue to you on GitHub.

2. [Fork](https://help.github.com/articles/fork-a-repo) the microLearner repository on the GitHub website to your GitHub account.

3. Clone your forked repository to the system where you'll be developing with ``git clone``.

4. Ensure that you have the latest version of all files (especially important if you cloned a long time ago, but you'll need to do this before submitting changes regardless). You should do this by adding microLearner as a remote repository and then pulling from that repository. You'll only need to run the ``git remote`` step one time:
   ```
   git checkout master
   git remote add upstream https://github.com/RNAer/microLearner.git
   git pull upstream master
   ```

5. Create a new topic branch that you will make your changes in with ``git checkout -b``:
   ```
   git checkout -b my-topic-branch
   ```

6. Run ``nosetests --with-doctest ; flake8 microLearner setup.py`` to confirm that the tests pass before you make any changes. (you need to install flake8 ``pip install flake8``).

7. Make your changes, add them (with ``git add``), and commit them (with ``git commit``). Don't forget to update associated scripts and tests as necessary. You should make incremental commits, rather than one massive commit at the end. Write descriptive commit messages to accompany each commit.

8. When you think you're ready to submit your code, again ensure that you have the latest version of all files in case some changed while you were working on your edits. You can do this by merging master into your topic branch:
   ```
   git checkout my-topic-branch
   git pull upstream master
   ```

9. Run ``nosetests --with-doctest ; flake8 microLearner setup.py`` to ensure that your changes did not cause anything expected to break. 

10. Once the tests pass, you should push your changes to your forked repository on GitHub using:
    ```
    git push origin my-topic-branch
    ```

11. Issue a [pull request](https://help.github.com/articles/using-pull-requests) on the GitHub website to request that we merge your branch's changes into microLearner's master branch. One of the microLearner developers will review your code at this stage. If we request changes (which is very common), *don't issue a new pull request*. You should make changes on your topic branch, and commit and push them to GitHub. Your pull request will update automatically.

12. Edit mode.

    Packages normally install under site-packages, but when you’re making changes, it makes more sense to run the package straight from the your local directory of the package. "Editable" installation creates a .pth file in site-packages that extends Python’s import path to find the package:
    ```
    pip install --editable path/to/the/package
    ```

    Once it is installed as edit mode, you can run the commands of the package. This is *really* helpful to see the effect your changes in real time.

Coding Guidelines
-----------------

We adhere to the [PEP 8](http://www.python.org/dev/peps/pep-0008/) python coding guidelines for code and documentation standards. Before submitting any code to microLearner, you should read these carefully and apply the guidelines in your code.


Testing Guidelines
------------------

All code that is added to microLearner must be unit tested, and the unit test code must be submitted in the same pull request as the library code that you are submitting. We will not merge code that is not unit tested. The PyCogent Coding Guidelines describe our [expectations for unit tests](http://pycogent.org/coding_guidelines.html?highlight=coding%20guidelines#how-should-i-test-my-code). You should review the unit test section before working on your test code.

Tests can be executed using [nose](https://nose.readthedocs.org/en/latest/) by running `nosetests --with-doctest` from the base directory of the project or from within a Python or IPython session running the following code:

``` python
>>> import microLearner
>>> microLearner.test()
# full test suite is executed
>>> microLearner.until.test()
# tests for the util module are executed
```

Note that this is possible because the lines below are added at the end of each `__init__.py` file in the package, so if you add a new module, be sure to include these lines in its `__init__.py`:

``` python
from numpy.testing import Tester
test = Tester().test
```


Documentation Guidelines
------------------------

We strive to keep microLearner's code well-documented, particularly its public-facing API. See our [documentation guide](doc/README.md) for more details on writing documentation in microLearner.

Getting help with git
=====================

If you're new to ``git``, you'll probably find [gitref.org](http://gitref.org/) helpful.

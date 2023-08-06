[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/lschoe/mpyc/master)
[![Travis CI](https://app.travis-ci.com/lschoe/mpyc.svg)](https://app.travis-ci.com/lschoe/mpyc)
[![codecov](https://codecov.io/gh/lschoe/mpyc/branch/master/graph/badge.svg)](https://codecov.io/gh/lschoe/mpyc)
[![Read the Docs](https://readthedocs.org/projects/mpyc/badge/)](https://mpyc.readthedocs.io)
[![PyPI](https://img.shields.io/pypi/v/mpyc.svg)](https://pypi.org/project/mpyc/)

# MPyC [![MPyC logo](https://raw.githubusercontent.com/lschoe/mpyc/master/images/MPyC_Logo.svg)](https://github.com/lschoe/mpyc) Secure Multiparty Computation in Python

MPyC supports secure *m*-party computation tolerating a dishonest minority of up to *t* passively corrupt parties,
where *m &ge; 1* and *0 &le; t &lt; m/2*. The underlying cryptographic protocols are based on threshold secret sharing over finite
fields (using Shamir's threshold scheme as well as pseudorandom secret sharing).

The details of the secure computation protocols are mostly transparent due to the use of sophisticated operator overloading
combined with asynchronous evaluation of the associated protocols.

See the [MPyC homepage](https://www.win.tue.nl/~berry/mpyc/) for more info and background.

Click the "launch binder" badge above to view the entire repository and try out the Jupyter notebooks from the `demos` directory
in the cloud, without any install.

## Installation:

Just run: `python setup.py install` (pure Python, no dependencies).

See `demos` for Python programs and Jupyter notebooks with lots of example code.

See [Read the Docs](https://mpyc.readthedocs.io/) for `Sphinx`-based documentation, including an overview of the `demos`,
and [GitHub Pages](https://lschoe.github.io/mpyc/) for `pydoc`-based documentation.

## Notes:

1. Python 3.6+ (Python 3.5 or lower is not sufficient).

2. Installing package [gmpy2](https://pypi.org/project/gmpy2/) is optional, but will considerably enhance the performance of `mpyc`.
As of December 12, 2021 with the release of gmpy2 2.1, installation has been simplified greatly:
`pip install gmpy2` is now supported on all major Linux/MacOS/Windows platforms via prebuilt wheels.
If you use the [conda](https://docs.conda.io/) package and environment manager, `conda install gmpy2` should do the job.

3. Use `run-all.sh` or `run-all.bat` in the `demos` directory to have a quick look at all pure Python demos.
Demos `bnnmnist.py` and `cnnmnist.py` require [NumPy](https://www.numpy.org/), demo `kmsurvival.py` requires
[pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), and [lifelines](https://pypi.org/project/lifelines/),
and demo `ridgeregression.py` (and therefore demo `multilateration.py`) even require [Scikit-learn](https://scikit-learn.org/).
Also note the example Linux shell scripts and Windows batch files in the `docs` and `tests` directories.

4. Directory `demos\.config` contains configuration info used to run MPyC with multiple parties. Also, Windows batch
file `gen.bat` shows how to generate fresh key material for SSL. To generate SSL key material of your own, first run
`pip install cryptography` (alternatively, run `pip install pyOpenSSL`, which will also install the `cryptography` package).

5. To use the [Jupyter](https://jupyter.org/) notebooks `demos\*.ipynb`, you need to have Jupyter installed,
e.g., using `pip install jupyter`. The latest version of Jupyter will come with IPython 7.x, which supports
top-level `await`. For example, instead of `mpc.run(mpc.start())` one can now simply write `await mpc.start()` anywhere in
a notebook cell, even outside a coroutine.

6. For Python 3.8+, you also get top-level `await` by running `python -m asyncio` to launch a natively async REPL.
By running `python -m mpyc` instead you even get this REPL with the MPyC runtime preloaded!

Copyright &copy; 2018-2021 Berry Schoenmakers
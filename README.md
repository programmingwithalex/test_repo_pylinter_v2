# test_repo_pylinter_v2

Copyright (c) 2021, programmingwithalex

## Description

This repo serves as a reference for the following [YouTube video](https://www.youtube.com/watch?v=rY-igT2N8zU&list=PL0dOL8Z7pG3J6t1pqRQiNarBGY-ZnIJcq&index=2).

Demonstration of how to incorporate continuous integration (CI) into a Python project using:

1. linting
2. testing

The linting is handled by a custom GitHub Action [`pylinters`](https://github.com/marketplace/actions/pylinters) written by myself. The testing is handled by pytest.

## Contents

* `.py` simplistic files to lint with the GitHub Action `pylinters` and test with `pytest`
* `tests/` directory which contains the various `pytest` tests to run
* `requirements.txt` which contains the necessary packages to run the CI

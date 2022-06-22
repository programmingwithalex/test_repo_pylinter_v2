# test_repo_pylinter_v2

Copyright (c) 2021, [programmingwithalex](https://github.com/programmingwithalex)

## Description

This repo serves as a reference for the following [YouTube video](https://www.youtube.com/watch?v=Ls6n3WZ_tyo&list=PLbn3jWIXv_ibMS6CFOKMZkOHimDB9xdU2&index=2).

Demonstration of how to incorporate continuous integration (CI) into a Python project using:

1. linting
2. testing

The linting is handled by a custom GitHub Action [`pylinter`](https://github.com/marketplace/actions/pylinter) written by myself. The testing is handled by `pytest`.

## Contents

* `.py` simplistic files to lint with the GitHub Action `pylinter` and test with `pytest`
* `tests/` directory which contains the various `pytest` tests to run
* `requirements.txt` which contains the necessary packages to run the CI

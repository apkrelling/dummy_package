from __future__ import annotations

import importlib.metadata

import dummy_package as m


def test_version():
    assert importlib.metadata.version("dummy_package") == m.__version__

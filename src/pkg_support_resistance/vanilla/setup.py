"""Setup module"""

from setuptools import setup, Extension

ext_modules = [Extension("vanilla_algo", sources=["vanilla_algo.c"])]

setup(
    name="vanilla_algo",
    ext_modules=ext_modules,
)

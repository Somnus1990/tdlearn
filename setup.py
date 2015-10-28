from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "tdbench",
    author = "Christoph Dann",
    author_email="cdann@cdann.de",
    version = "git",
    packages = ["tdlearn", "tdlearn.util"],
    ext_modules = cythonize('tdlearn/swingup_ode.pyx'),
)

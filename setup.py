from setuptools import setup, find_packages

requirements = [
    "pyglet"
]

test_requirements = [
    "pytest"
]

setup(
    author="zanaskar",
    name='src',
    packages=find_packages(),
    test_suite="tests",
    install_requires=requirements,
    test_require=test_requirements
)

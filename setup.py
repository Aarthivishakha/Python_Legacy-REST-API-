from setuptools import find_packages, setup


setup(
    name="legacy-rest-microservice",
    version="1.0.0",
    description="Legacy WSGI REST API microservice for Python 2.7",
    python_requires=">=2.7,<3.0",
    packages=find_packages(),
    test_suite="tests",
)

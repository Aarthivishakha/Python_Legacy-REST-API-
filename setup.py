from setuptools import find_packages, setup


setup(
    name="legacy-rest-microservice",
    version="1.0.0",
    description="Legacy WSGI REST API microservice for Python 3.8",
    python_requires=">=3.8,<3.9",
    packages=find_packages(),
    test_suite="tests",
)

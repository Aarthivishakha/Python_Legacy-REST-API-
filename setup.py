from setuptools import find_packages, setup


setup(
    name="legacy-rest-microservice",
    version="1.0.0",
    description="Legacy WSGI REST API microservice for Python 3.5",
    python_requires=">=3.5,<3.6",
    packages=find_packages(),
    test_suite="tests",
)

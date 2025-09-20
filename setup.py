from setuptools import setup, find_packages

setup(
    name="titanic-ds-demo",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "scikit-learn",
    ],
)

from setuptools import find_packages, setup

setup(
    name="myproject",
    version="1.0.0",
    description="Облік і аналіз оцінок студентів",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
)
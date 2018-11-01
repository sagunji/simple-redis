from distutils.core import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="SimpleRedis",
    version="0.1",
    install_requires=requirements,
    packages=["simple-redis"],
    license="Creative Commons Attribution-Noncommercial-Share Alike license",
    long_description=open("README.md").read(),
)

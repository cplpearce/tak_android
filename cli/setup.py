import os

from setuptools import setup


app_version = os.getenv("DOCKER_ANDROID_VERSION", "test-version")

with open("requirements.txt", "r") as f:
    reqs = f.read().splitlines()

setup(
    name="docker-android",
    version=app_version,
    url="https://github.com/cplpearce/tak-android",
    description="CLI for docker-android",
    author="H2A",
    author_email="clint@h2analytics.ca",
    install_requires=reqs,
    py_modules=["cli", "docker-android"],
    entry_points={"console_scripts": "docker-android=src.app:cli"}
)

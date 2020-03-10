
# setup.py

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="avery1493-Lambdata-12",
    version="2.0",
    author="Avery Quinn",
    author_email="avery.quinn1493@gmail.com",
    description="Example Module",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/Avery1493/Lambdata-12",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)
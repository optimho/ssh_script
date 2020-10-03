import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="firecontrol", # Replace with your own username
    version="0.0.1",
    author="Michael du Plessis",
    author_email="michael@duplessis.nz",
    description="This uses netmiko to enable or disable preconfigured firewall rules in the edge router",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/optimho/ssh_script",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
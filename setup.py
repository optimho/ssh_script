# A good source for information
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#py-modules


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
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.


        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    python_requires='>=3.2',
    keywords='firewall edgrouter script',
    install_requires=['netmeko==3.3.2', 'six==1.15.0'],
)
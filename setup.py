try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

with open('readme.rst') as reader:
    long_description = reader.read()
    
setup(name='resampling',
      long_description=long_description,
      version='2015.10.02',
      description="Resampling Explorations.",
      author="russell",
      platforms=['linux'],
      url='',
      author_email="necromuralist@gmail.com",
      license="MIT",
      packages=find_packages(),
      include_package_data=True,
      )

# an example last line would be cpm= cpm.main: main

# If you want to require other packages add (to setup parameters):
# install_requires = [<package>],
#version=datetime.today().strftime("%Y.%m.%d"),
# if you have an egg somewhere other than PyPi that needs to be installed as a dependency, point to a page where you can download it:
# dependency_links = ["http://<url>"]

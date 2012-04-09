from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.2'

install_requires = [
    "flask",
    "nose"
]


setup(name='WebTestRunner',
    version=version,
    description="Web-based interface for selectively executing client-side Python UnitTests",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='unittest',
    author='Jesse Thompson',
    author_email='jessejlt@gmail.com',
    url='https://github.com/jessejlt',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['WebTestRunner=webtestrunner.server:main']
    },
    test_suite="webtestrunner.tests.tests"
)

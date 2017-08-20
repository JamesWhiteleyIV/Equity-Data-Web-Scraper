from setuptools import setup, find_packages

setup(
        name='equityscraper',
        version='0.1',
        description='Web scraper that stores fundamental stock data, analyst estimates, and earnings surprises as .pkl and/or .csv',
        url='https://github.com/JamesWhiteleyIV/Equity-Data-Web-Scraper',
        author='James Whiteley IV',
        author_email='jameswhiteleyiv@gmail.com',
        license='MIT',
        classifiers=[
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            ],
        keywords='web scraper investments  pandas',
        packages=find_packages(exclude=['docs', 'tests*']),
        install_requires=['pandas', 'beautifulsoup4'] #these get installed before this package
        )

from setuptools import setup, find_packages

README = 'who is my computer talking to?'

requires = []
tests_require = [
        'pytest',
        'coverage'
        ]

setup(name='whogoesthere',
      version='0.0.1',
      description=README,
      long_description=README,
      package_dir={'': 'src'},
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Zarqizarq Project',
      packages=find_packages('source'),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points={
          'console_scripts': ['whogoesthere = whogoesthere.main:main']
      },
      )

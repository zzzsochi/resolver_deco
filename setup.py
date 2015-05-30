from setuptools import setup


setup(name='resolver_deco',
      version='1.0',
      description='Decorator for resolve function arguments',
      # long_description=README,
      classifiers=[
          "License :: OSI Approved :: BSD License",
          "Operating System :: POSIX",
          "Programming Language :: Python :: 3",
          "Topic :: Internet :: WWW/HTTP",
      ],
      author='Alexander Zelenyak',
      author_email='zzz.sochi@gmail.com',
      url='https://github.com/zzzsochi/resolver_deco',
      keywords=['dotted'],
      modules=['resolver_deco'],
      install_requires=['zope.dottedname'],
      tests_require=['pytest'],
)

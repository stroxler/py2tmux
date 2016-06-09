from setuptools import setup

setup(name='py2tmux',
      version='0.0.1',
      description='Template for python development',
      long_description="",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 2.7',
      ],
      entry_points={
          "console_scripts": [
              'py2tmux = py2tmux.cli:main',
          ]
      },
      keywords='',
      url='https://github.com/stroxler/py2tmux',
      author='Steven Troxler',
      author_email='steven.troxler@gmail.com',
      license='None yet, but feel free to copy',
      packages=['py2tmux'],
      install_requires=[
          'click', 'sh',
      ],
      include_package_data=True,
      zip_safe=False)

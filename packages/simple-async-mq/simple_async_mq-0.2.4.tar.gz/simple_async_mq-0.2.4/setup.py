from distutils.core import setup
import setuptools
setup(
  name = 'simple_async_mq',         # How you named your package folder (MyLib)
  packages = ['simple_async_mq'],   # Chose the same as "name"
  version = '0.2.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A simple async message queue client - socket-io wrapper',   # Give a short description about your library
  author = 'Oliver Kramer',                   # Type in your name
  author_email = '3520.kramer@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/3520kramer/simple-async-mq',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/3520kramer/simple-async-mq/archive/v_024.tar.gz',    # I explain this later on
  keywords = ['mq', 'async', 'client'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'asyncio',
          'python-socketio',
          'aiohttp'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.9',      #Specify which pyhton versions that you want to support
  ],
)
from distutils.core import setup
setup(
  name = 'tender',
  packages = ['tender'],
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='GNU General Public License v3.0',
  description = 'Prepare bid documents',
  author = 'Pragyan Shrestha',
  author_email = 'pragyanOne@gmail.com',
  url = 'https://github.com/pragyanone/tender',
  download_url = 'https://github.com/pragyanone/tender/archive/0.1.tar.gz',
  keywords = ['ppmo', 'bid', 'tender',],   # Keywords that define your package best
  install_requires=[
          'python-docx',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Contractors',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3.0',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
  ],
)

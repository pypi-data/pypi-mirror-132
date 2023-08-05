from setuptools import setup, find_packages

with open('README.md', encoding='utf8') as readme_file:
    readme = readme_file.read()

setup(
  author="ArtLabss",
  author_email="art@artlabs.tech",
  description="A Data Anonymization package for tabular, image and sound data",
  name="anonympy",
  version="0.1.1",
  
  packages=find_packages(exclude=['test']),
  install_requires=['faker', 'cape-privacy', 'scikit-learn', 'texttable', 'setuptools', 'numpy', 'pandas'],
  python_requires='>=3.6*',
  url='https://github.com/ArtLabss/open-data-anonimizer',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    ],
  license="BSD license",
  long_description=readme,
  long_description_content_type='text/markdown',
  keywords='anonympy',    
  zip_safe=False,
)
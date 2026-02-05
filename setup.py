import setuptools

desc = '''
      DERBI (DEutscher RegelBasierter Inflektor) is a simple rule-based automatic 
      inflection model for German based on spaCy. Applicable regardless of POS!
       '''

setuptools.setup(
    name='DERBI',
    version='1.1',
    author='Max Schmaltz',
    authors_email='schmaltzmax@gmail.com',
    description=desc,
    packages=['DERBI'],
    package_data={'DERBI': ['Router.json', 'meta/*', 'meta/automata/*', 'meta/lexicons/*']},
    include_package_data=True,
    install_requires=[
        'nltk>=3.9.2',
        'numpy>=2.0.0',
        'spacy>=3.8.0',
        'CharSplit @ git+https://github.com/dtuggener/CharSplit.git',
    ],
    python_requires='>=3.8',
)
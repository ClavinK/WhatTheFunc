from setuptools import find_packages, setup

setup(
    name="whatthefunc",
    packages=find_packages(include=['whatthefunc']),
    version='0.1.0',
    description="Python library to learn what a function/method/attribute does, explained by OpenAI's ChatGPT in layman's terms. Additional function to insert your own OpenAI API Key",
    author='ClavinK',
    author_email='ckama222@gmail.com',
    install_requires=['openai'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==8.4.2'],
    test_suite='tests'
)
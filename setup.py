from setuptools import setup

setup(
    name='DearWidgetTemplate',
    version='1.0',
    description='A useful module',
    author='Author Name',
    author_email='haqury@gmail.com',
    packages=['DearWidgetTemplate'],  # same as name
    install_requires=['pyperclip', 'PyQt5', 'sys', 'SpeachToTextWidget', 'win32api'],  # external packages as dependencies
)
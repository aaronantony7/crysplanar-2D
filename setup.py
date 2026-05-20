from setuptools import setup, find_packages

setup(
    name='crysplanar',
    version='1.5.3',
    packages=find_packages(),
    install_requires=['pygame', 'Pillow'],
    author='aaronantony7',
    author_email='aaronantony717@gmail.com',
    description='A Python module for designing generative crystal art',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aaronantony7/CRYSPLANAR',
    license='MIT',
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Artistic Software',
    ],
)
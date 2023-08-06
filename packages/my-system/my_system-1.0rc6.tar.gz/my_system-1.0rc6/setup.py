from setuptools import setup
version = '1.0rc6'
print(f'version:{version}')
with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='my_system',
    version=version,
    url='https://github.com',
    description = 'Nearly release ...',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='mc_creater',
    author_email='guoxiuchen20170402@163.com',
    license='MIT',
    packages=['system'],
    classifiers=['Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9',],
    python_requires='>=3.6',
    install_requires=['PyQt5'],
    include_package_data=True

)

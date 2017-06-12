from setuptools import setup, find_packages

setup(name='text_generator_keras',
  version='0.1',
  packages=find_packages(),
  description='Keras text generator on Google ML Engine',
  author='Maximilian Clarke',
  author_email='maximilianfc+textgen@gmail.com',
  license='MIT',
  install_requires=[
      'keras',
      'h5py'
  ],
  zip_safe=False)

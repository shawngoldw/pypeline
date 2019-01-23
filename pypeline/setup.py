import setuptools

setuptools.setup(
     name='pypeline',
     version='0.1',
     scripts=['pypeline'] ,
     author="Shawn Goldwasser",
     author_email="shawngoldw@gmail.com",
     description="ML Pipeline Package",
   long_description_content_type="text/markdown",
     url="https://github.com/shawngoldw/pypeline",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
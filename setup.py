import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='x3dpsail',  
     version='0.3',
     scripts=['x3dpsail'] ,
     author="John W Carlson",
     author_email="yottzumm@gmail.com",
     description="X3D Python Scene Access Interface Library (X3DPSAIL)",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/carlsonsolutiondesign/x3dpsail",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )

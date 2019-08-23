#Topic: PIP conda spyder
#-----------------------------
#https://packaging.python.org/tutorials/installing-packages/

#Go to Anaconda Console (open as Administrator)
pip install -–upgrade pip

pip install -–upgrade sypder

#ther packages
pip install 

#or from command prompt
#https://datatofish.com/upgrade-pip/
#run
python -m pip install -–upgrade pip

#%%%
To install the latest version of “SomeProject”:

pip install "SomeProject"
To install a specific version:

pip install "SomeProject==1.4"
To install greater than or equal to one version and less than another:

pip install "SomeProject>=1,<2"
To install a version that’s “compatible” with a certain version: [4]

pip install "SomeProject~=1.4.2"


It’s also possible to specify an exact or minimum version directly on the command line. When using comparator operators such as >, < or some other special character which get interpreted by shell, the package name and the version should be enclosed within double quotes:

python -m pip install SomePackage==1.0.4    # specific version
python -m pip install "SomePackage>=1.0.4"  # minimum version
Normally, if a suitable module is already installed, attempting to install it again will have no effect. Upgrading existing modules must be requested explicitly:

python -m pip install --upgrade SomePackage
 
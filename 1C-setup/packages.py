#Topic:Version
#-----------------------------
#libraries

import pandas as pd
pd.__version__

pd.show_versions(as_json=False)

!pip list

!pip show pandas
!pip freeze

#%%% PIP 
#!python -m pip install --upgrade pip
!pip --version
!conda update pip

#upgrade
#https://pandas.pydata.org/pandas-docs/stable/install.html
!pip install --upgrade pandas
!pip3 install --upgrade pandas
!conda update pandas

#Windows

python -c "import pandas as pd; print(pd.__version__)"
conda list | findstr pandas  # Anaconda / Conda
pip freeze | findstr pandas
pip show pandas | findstr Version
Linux

python -c "import pandas as pd; print(pd.__version__)"
conda list | grep numpy  # Anaconda / Conda
pip freeze | grep numpy  # pip

#%%% Conda https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html
#!conda update conda

#Search
!conda search scipy
!conda list
#It is best to install all packages at once, so that all of the dependencies are installed at the same time.
#To install multiple packages at once and specify the version of the package:
#!conda install scipy=0.15.0 curl=7.26.0
#To install a package for a specific Python version:
#!conda install scipy=0.15.0 curl=7.26.0 -n py34_env


#Removing packages
#Use the terminal or an Anaconda Prompt for the following steps.
#To remove a package such as SciPy in an environment such as myenv:
#!conda remove -n myenv scipy
#To remove a package such as SciPy in the current environment:
#!conda remove scipy
#To remove multiple packages at once, such as SciPy and cURL:
#!conda remove scipy curl
#To confirm that a package has been removed:
!conda list

#update packages


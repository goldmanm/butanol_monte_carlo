This repository contains data and code to accompany "Pressure-dependent kinetics of isobutanol peroxy isomers" by Mark Jacob Goldman, Nathan Wa-Wai Lee, Jesse H Kroll, William H Green.

This repository contains the outputs of the Monte Carlo calculations for runs in this work. It is made separate from the main repository since this part of the operation does not require RMG, reducing the complexity and the computational time to generate 3000+ pressure dependent mechanisms.

Docker is the recommended way to replicate the calculations.

# Structure and files in database

The structure of the folders in this repository are as followed:

* **alpha**/**beta**/**gamma**-contains the Monte Carlo output and methods to recreate the mechanisms
  * **cantherm_pdep_input_..._uncertainty_blanks.py**-contains a formatted arkane (previously known as cantherm) input file which allows uncertainties to be placed into it.
  * **generate_inputs_series.py**-python script for converted the formatted input file into thousands of different input files and running each of those individually.
  * **random_values.csv**-list of random value parameters output during the input method generation (used for finding correlations)
  * **runs_20200715**-directory containing all the Monte Carlo outputs. In each folder is a file chem.cti, which is read by Cantera to do to the calculations of branching ratios
* **Dockerfile**-file for making virtual environment in docker to run model (see instructions below)
* **environment.yml**-specifications for python environment used in code
* **make_tables.py**-script to read Monte Carlo models, create distributions of branching ratios and overall rates, and output them in LaTeX table format for the publication
* **reaction_info.csv**/**species_name_comparison.csv** - files for formatting the table using unicode species names found in the journal article.
  
# Building using Docker

A file `Dockerfile` contains instructions to generate an image with all the dependencies for simulating the results of the model. The instructions here were tested on Ubuntu 18.04 and Ubuntu 20.04, but will likely work on other linux distributions and operating systems. The instructions below reference unix terminal commands to generate the image and complete the calculations. You will first have to install the docker package. Once that is installed, change your directory to the folder with the `Dockerfile` obtained in the this repository. Then type: 

```
docker build . -t butanol_monte_carlo
```

You can then create a container from the image and then launch a terminal session with it.

```
docker container run -it butanol_monte_carlo
```

If desired, you can simulate the monte carlo models and output the tables which appear in the electronic supporting information by typing:

```
cd /home/repo_monte_carlo
python make_tables.py
```

To get values of branching ratios and overall rates at different conditions, you can modify `make_tables.py`.

# Rerunning Monte Carlo in Arkane

This repository is primarily meant to help users calculate branching ratios from the Monte Carlo runs which were already done (since running them can take upwards of a week). However if someone wants to do Monte Carlo analysis for a different network, here are steps you can follow:

1. From the original Arkane job, there should be an `output.py` file which has species and transition states formatted into python, so they can be added to an input file which does not require reading separate quantum files. Merge this information with your original Arkane input file to remove any external quantum file dependencies. 
2. Run the file to make sure there aren't differences with the original file
3. Add text to this file to indicate which parameters you want to vary. You should have an input file similar to `cantherm_pdep_input_alpha_w_uncertainty_blanks.py`, which you can use as a guide.
4. Modify `generate_inputs_serial.py` to replace the text you desire with the desired uncertainties. There may be other changes you want to modify (like folder names).
5. You will need RMG to run the Arkane jobs. To do this, you can use the docker image available at DOI 10.5281/zenodo.3858424, with one change. The RMG-Py respoistory should use the branch `goldmanm/butanol_py3_changes_montecarlo` with commit hash `b86edab785f05ddfc90be4dd4415f1a376d1dde0` instead of branch `goldmanm/butanol_py3_changes`.
6. Run `python generate_inputs_serial.py`. This step may take days. 
7. When it is done, now have the output files with Chemkin models that you can analyze how you'd like. In this work we used `ck2cti` functionality to convert from Chemkin to cantera. 


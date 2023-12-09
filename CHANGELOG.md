## Log of improvements made based on milestone and peer review feedback

#### Improvements made based on Milestone 1 feedback

- "You should state the classes for "potential". It is not an obvious classification problem (potential could also be a numeric rating) so you should state this in the introduction."
https://github.com/UBC-MDS/fifa-potential/pull/37/commits/6ca19434b5c9496ce2c04350500680e3091d04e5
Stated the target classes we created by binning the target variable 'potential'.

- "Findings from project are not linked back to the application domain." 
https://github.com/UBC-MDS/fifa-potential/pull/37/commits/6ca19434b5c9496ce2c04350500680e3091d04e5
In the discussion section, linked the findings back to the application domain.

- "The analysis notebook (.ipynb or .Qmd or *Rmd) should be in a sub-directory called something sensible, such as analysis, src, notebooks, docs, etc, to aid in the discoverability of this file, and related ones. Having too many files in the project root makes the project organization less understandable and can lead to longer activation times to productivity for collaborators (including future you!)." 
https://github.com/UBC-MDS/fifa-potential/commit/ee4f57ccc435662b4eca776baa8391c232fe75c4
This commit is where the src sub-directory was created. Other scripts were added to it subsequently.

- Re: Contributing file - "The file exists, but is not detailed enough. Please refer to the example provided in the Milestone 1 requirement's description"
https://github.com/UBC-MDS/fifa-potential/commit/7416a75ace9de51486ed870afb5b6c34cfdae00c
Improved the contributing file based on the breast cancer predictor template.

- "versions are missing from environment.yml for all R and Python packages"
"in the repository, you have a file with a .yaml extension, while in the README file you provide a code to create an environment from the file that has a .yml extension. Additional 0.5 deduction. Please be accurate and consistent, it also affected reproducibility"
https://github.com/UBC-MDS/fifa-potential/commit/50b4ef858e265b901606a6e24f9cf92a26a57563
Versions were added to the environment file

- Re: License file - "You are expected to have the CC license text in the license file"
https://github.com/UBC-MDS/fifa-potential/commit/a12154280d2e49ce79e94f88b463d19dd16c846c
Updated the license file based on breast cancer predictor template

- Re: EDA plots - "There is no legend (at least in the PDF) for the colours in the density plots).
There are no figure legends or table descriptions"
https://github.com/UBC-MDS/fifa-potential/commit/f7f481f01c90cd35c6edff0ebca34225ea209bff
The plots already had a legend but it was being cut off in the PDF, so changed the size of the plots so the legend wouldn't get cut off.

- Re: use of git issues for communication: "2 issues are not enough for Milestone 1"
https://github.com/UBC-MDS/fifa-potential/issues?q=is%3Aissue
Issues have been used consistently since milestone 1. With many issues being many comments long.

#### Improvements made based on Milestone 2 feedback

- Re: git issues: "4 issues for this release - still not enough"
https://github.com/UBC-MDS/fifa-potential/issues?q=is%3Aissue
Issues have been used consistently since milestone 1. With many issues being many comments long.

#### Improvements made based on peer review feedback

- "In the git repository, I noticed that the scripts are currenyly put under the src directory. To further enhance the project structure, maybe you can try to put all scripts into one separate script folder instead."
https://github.com/UBC-MDS/fifa-potential/commit/87f37282aa99cb2c70ec8b19c4edd674f494fc4f
Moved scripts 01 through 05 from src/ to scripts/. Updated function imports and references.

- "All the models, figures amnd tables are put into one result folder which is very nice. However, it may be better to create separate 'tables', 'figures', and 'models' under result folder to enhance project structure."
https://github.com/UBC-MDS/fifa-potential/commit/7d4b174ca5aec93dcb01811d54009f79309dd6ae
Split contents of results folder into results/figures, results/tables, and results/models. Updated references in Jupyter Book, all scripts, and Makefile

- "It was good that you tried out several models and represented the results from those models. Just curious about why the Decision Tree model was not being used given that the validation results seemed to be better, although it was overfitting. Did you try experimenting with the hyperparameters to check and see if they give better results than your SVM model?"
https://github.com/UBC-MDS/fifa-potential/commit/a6c437c2e2a3f02610e44829b70803a9d431027d
Rationalized in more detail the choice of model used for analysis after model selection phase.

- Peer Review feedback suggested a need for more detailed information for contributors.
https://github.com/UBC-MDS/fifa-potential/pull/53
Updated README to include more details on running the project for new contributors.

- "I personally find it preferable (though I acknowledge that Tiff might not include it in her repository either) to have the link to the rendered HTML also included in the 'About' section. This way, you don't have to search for it in the README first, but, is probably just my personal preference."
https://github.com/UBC-MDS/fifa-potential/commit/08523f43017200be608119de036e23e1a2286bad
The link to the rendered report was added in the README and also in the about section of the repo.

#### Improvements made based on our own judgement

- https://github.com/UBC-MDS/fifa-potential/commit/564350950d0aff584ae4268c4018c480d5abcc39
Updated Makefile for explicit filenaming in accordance with Tiff's examples


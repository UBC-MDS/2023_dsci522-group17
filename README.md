# Predicting Athletic Potential of FIFA Athletes

## Contributors:
- Jake Barnabe
- Simon Frew
- Merete Lutz
- Waleed Mahmood

## Summary
We attempt to construct a classification model using an RBF SVM classifier algorithm which uses FIFA22 player attribute ratings to classify players' potential with target classes "Low", "Medium", "Good", and "Great". 
The classes are split on the quartiles of the distribution of the FIFA22 potential ratings. 
Our model performed reasonably well on the test data with an accuracy score of 0.84, with hyperparamters C: 100 & Gamma: 0.01. 
However, we believe there is still significant room for improvement before the model is ready to be utilized by soccer clubs and coaching staffs to predict the potential of players on the field instead of on the screen. 

## Report
The final report can be found
[here](https://github.com/UBC-MDS/fifa-potential/tree/main/src/high-potential-fifa-prediction-report.html).

## Dependencies

- [Docker](https://www.docker.com/) is a container used 
to manage the software dependencies for this project.
The Docker image used for this project is based on the
`quay.io/jupyter/minimal-notebook` image.
Additional dependencies are specified int the [`Dockerfile`](Dockerfile).

## Usage

### Setup

1. [Install](https://www.docker.com/get-started/) 
and launch Docker on your computer.

2. Clone this GitHub repository.

#### Running the analysis

1. Navigate to the root of this project on your computer using the
   command line and enter the following command:

``` 
docker compose up
```

2. In the terminal, look for a URL that starts with 
`http://127.0.0.1:8888/lab?token=` 
Copy and paste that URL into your browser.

3. To run the analysis, open `src/high-potential-fifa-prediction-report.ipynb`
in the Jupyter Lab window you just launched, and under the "Kernel" menu
click "Restart Kernel and Run All Cells..."

#### Clean up

1. To shut down the container and clean up the resources, 
type `Ctrl` + `C` in the terminal
where you launched the container, and then type `docker compose rm`

## Developer notes

#### Adding a new dependency

1. Add the dependency to the `Dockerfile` file on a new branch.

2. Re-build the Docker image locally to ensure it builds and runs properly.

3. Push the changes to GitHub. A new Docker
   image will be built and pushed to Docker Hub automatically.
   It will be tagged with the SHA for the commit that changed the file.

4. Update the `docker-compose.yml` file on your branch to use the new
   container image (make sure to update the tag specifically).

5. Send a pull request to merge the changes into the `main` branch. 

#### Running the tests
Tests are run using the `pytest` command in the root of the project.
More details about the test suite can be found in the 
[`tests`](tests) directory.


## Licenses
This report is licensed under a Attribution-NonCommercial-NoDerivs 4.0 International (CC BY-NC-ND 4.0 Deed) License with the repository itself under a MIT License. The underlying dataset is licensed by a CC0 1.0 Universal (Public Domain) license. 



## References
This README file references https://github.com/ttimbers/breast_cancer_predictor_py/tree/main. 

US National Soccer Players. (2023). (rep.). How to evaluate soccer players. Retrieved from https://ussoccerplayers.com/soccer-training-tips/evaluating-players. 

Harris, C.R. et al., 2020. Array programming with NumPy. Nature, 585, pp.357–362.

McKinney, Wes. 2010. “Data Structures for Statistical Computing in Python.” In Proceedings of the 9th Python in Science Conference, edited by Stéfan van der Walt and Jarrod Millman, 51–56.

Pauli Virtanen, et al., and SciPy 1.0 Contributors. (2020) SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. Nature Methods, 17(3), 261-272.

Pedregosa, F. et al., 2011. Scikit-learn: Machine learning in Python. Journal of machine learning research, 12(Oct), pp.2825–2830.

VanderPlas et al., (2018). Altair: Interactive Statistical Visualizations for Python. Journal of Open Source Software, 3(32), 1057, https://doi.org/10.21105/joss.01057

Van Rossum, Guido, and Fred L. Drake. 2009. Python 3 Reference Manual. Scotts Valley, CA: CreateSpace.

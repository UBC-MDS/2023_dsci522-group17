FROM --platform=linux/amd64 quay.io/jupyter/minimal-notebook:python-3.11
# Comment to test trigger GitHub Workflows


# Set user to root for sudo permissions
USER root 

# Update linux
RUN apt-get update --yes && \
    apt-get upgrade --yes 

# Copy git repository contents into home container
COPY --chown=${NB_UID} . /home/jovyan/fifa-potential

WORKDIR /home/jovyan/fifa-potential

# Update conda & install environment 
RUN conda update -n base conda && \
    conda config --set solver libmamba && \ 
    conda install nb_conda_kernels=2.3.1 && \ 
    conda env create -f environment.yaml

WORKDIR /home/jovyan

# Change back to default user
USER ${NB_UID}

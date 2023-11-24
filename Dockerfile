FROM quay.io/jupyter/minimal-notebook:python-3.11

# Set user to root for sudo permissions
USER root 

# Update linux
RUN apt-get update --yes && \
    apt-get upgrade --yes 

# Copy git repository contents into home container
COPY . /home/jovyan/fifa_potential

# Update conda & install environment 
RUN conda update -n base conda && \
    conda config --set solver libmamba && \ 
    conda env create -f environment.yaml

# Change back to default user
# USER ${NB_UID}

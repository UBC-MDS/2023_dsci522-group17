FROM quay.io/jupyter/minimal-notebook:python-3.11

# Set user to root for sudo permissions
USER root 

RUN apt-get update --yes && \
    apt-get upgrade --yes 

# Copy git repository contents into container
COPY . /home/jovyan

# Change back to default user
USER ${NB_UID}

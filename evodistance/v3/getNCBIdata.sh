#!/bin/bash

mkdir ncbi
cd ncbi

# Obtain taxonomy data from NCBI
curl -O ftp://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz

# Obtain only the files we need
tar xfz taxdump.tar.gz names.dmp nodes.dmp

# Obtain categories data from NCBI
curl -O ftp://ftp.ncbi.nih.gov/pub/taxonomy/taxcat.tar.gz

# Obtain only the files we need
tar xfz taxcat.tar.gz categories.dmp

cd ..


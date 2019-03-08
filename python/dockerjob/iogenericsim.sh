#!/bin/sh
echo "starting docker job at `date`"

#To use this first make sure docker is installed and user has permissions to run docker

#goto the docker folder of the pyiome distribution and build the docker image using the command
# docker build -t mikeg64/pyio -f Dockerfile .
docker container run  -v $PWD:/home/pyio/data --rm -it mikeg64/pyio python3 pycarjob.py > out.csv

#bash ./iogenericsim_sge.sh
echo "finished at `date`"
exit 0

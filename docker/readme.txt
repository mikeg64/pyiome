docker container template for running jobs using pyiome

Build container using
docker build -t mikeg64/pyio -f Dockerfile .

Run container using
docker container run  -v $PWD:/home/pyio/data --rm -it mikeg64/pyio python3 pycarjob.py >& out.csv

This will run the job file (in this case pycarjob.py)  inside the container
This job file gets input parametes and files from the directory $PWD

the outputs may be copied to the host working directory which is $PWD



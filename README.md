# NextFlow pipeline template

Use this template to generate a repo for your own pipelines

See the example main.nf for how to structure the script.

To include scripts, eg. in python or julia - ensure they are executable and add to /bin/. 

Workflows can then be run remotely using the command: nextflow run user/repo
eg.

    nextflow run jbwdn/nextflow_template

Clean up after runs using:

    nextflow clean -f run_name
    
Modify resource usage or allocate per process in nextflow.config

See full documentation [here](https://www.nextflow.io/docs/latest/index.html).
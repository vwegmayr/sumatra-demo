# sumatra demo

First you need to install [miniconda](https://conda.io/docs/install/quick.html#linux-miniconda-install) on your system.

## Getting started
Having installed miniconda, setup and source the environment _sumatra-demo_ with

`make env && source activate sumatra-demo`

Next setup the sumatra demo project with

`make smt`

Note that the output data storage only works if you have access to the ise-squad Dropbox folder.

Finally, run a demo experiment:

`smt run .config`

You can go to the [web interface](http://192.33.91.83:9183/demo/) and check out the record.

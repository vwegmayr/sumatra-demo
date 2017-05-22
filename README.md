# sumatra demo

.. _miniconda: https://conda.io/docs/install/quick.html#linux-miniconda-install
First you need to install miniconda_ on your system.

## Getting started
Having installed miniconda, setup and source the environment _sumatra-demo_ with

.. code-block:: shell

    make env && source activate sumatra-demo

Next setup the sumatra demo project with

.. code-block:: shell

    make smt
    
    Enter sumatra project: demo
    Enter sumatra username: demo
    Enter sumatra password: demo
    Enter archive path: /full/path/to/Dropbox/ise-squad
    Enter path where Sumatra should look for output: .

Note that the output data storage only works if you have access to the ise-squad Dropbox folder.

Finally, run a demo experiment:

.. code-block:: shell

    smt run .config

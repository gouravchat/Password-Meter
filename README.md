# Monte Carlo statistical analysis 

Monte Carlo password checking, as described in the
[ACM CCS 2015 paper](http://www.eurecom.fr/~filippon/Publications/ccs15.pdf)
by Matteo Dell'Amico and Maurizio Filippone.

Copyright 2016 Symantec Corporation

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0]


## Dependencies

- install conda
- conda create -n PIM_pwdmeter python=3.6.9
- pip install -r requirements.txt

## How to Use

1. keep 80 percent passwords in .txt format (only passwords in each row) in TRAIN_DATA folder
2. keep rest in TEST_DATA folder
3. Open config.py to change ngram settings, sample size , 
4. python infer.py
5. check results in GUESS_NUMBER folder

## results explanation


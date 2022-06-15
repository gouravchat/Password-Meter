# montecarlopwd

Monte Carlo password checking, as described in the
[ACM CCS 2015 paper](http://www.eurecom.fr/~filippon/Publications/ccs15.pdf)
by Matteo Dell'Amico and Maurizio Filippone.

Copyright 2016 Symantec Corporation

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0]

## Write me to get more info!

Very limited documentation right now -- sorry!  If you want to use
this write me (matteo_dellamico@symantec.com) and I'll add docs to
help you do what you need. There's plenty of stuff to help scalability
and persist models; my plan is to write documentation if somebody is
interested in this.

## Dependencies

- conda create -n PIM_pwdmeter python=3.6.9
- pip install -r requirements.txt

## How to Use

1. keep 80 percent password in .txt format (only passwords in each row) in TRAI_DATA folder
2. keep rest in TEST_DATA folder
3. python infer.py
4. check results in GUESS_NUMBER folder

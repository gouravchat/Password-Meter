#!/usr/bin/env python3

# Copyright 2016 Symantec Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0

# standard library
import argparse
import csv
import sys
from os import path,remove
# internal imports
import backoff
import model
import ngram_chain
import pcfg
import math
import numpy as np
from config import *
import pandas as pd



def train_analysis_meter(fileName = "ML_PWD.csv"):


    print("starting analysis .....")

    with open(TRAINING_DATA, 'rt') as f:
        training = [w.strip('\r\n') for w in f]

    models = {'{}-gram'.format(i): ngram_chain.NGramModel(training, i)
          for i in range(MIN_NGRAM, MAX_NGRAM + 1)}
    models['Backoff'] = backoff.BackoffModel(training, 10)
    models['PCFG'] = pcfg.PCFG(training)
    samples = {name: list(model.sample(SAMPLE_SIZE))
           for name, model in models.items()}

    estimators = {name: model.PosEstimator(sample)
              for name, sample in samples.items()}
    modelnames = sorted(models)

    # testing analysis

    with open(TESTING_DATA, 'rt') as f:
        test_passwords = [w.strip('\r\n') for w in f]

    colnames = ['password'] + [name for name in modelnames]

    print(colnames)

    df = pd.DataFrame(columns = colnames)
    print(df)

    for password in test_passwords:
        logprobs = [models[name].logprob(password) for name in modelnames]
        estimations = [estimators[name].position(models[name].logprob(password))
                   for name in modelnames]
        estimations = list(np.log2(estimations))
        result = {'password' : password}
        for i,name in enumerate(modelnames):
            result[name] = estimations[i]
        print(result)
        df = df.append(result,ignore_index = True)
        print(df)

    print(df)

    if path.exists("new_password_analysis.csv"):
        remove("new_password_analysis.csv")

    df.to_csv("new_password_analysis.csv")

    print("analysis done ...data saved  ...plotting...")


    

if __name__ == "__main__":

    train_analysis_meter()


   

    


            



       








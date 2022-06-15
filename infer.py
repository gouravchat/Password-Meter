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
# for plotting
import seaborn as sns
import matplotlib.pyplot as plt
sns.reset_defaults()
sns.set_context(context='talk',font_scale=0.7)
plt.rcParams['image.cmap'] = 'viridis'

def plotFuncHist(df,col):
    plt.figure(figsize = (20,20))
    plt.xlabel("Guess Number",fontsize = 25)
    plt.ylabel("Counts",fontsize = 25)
    plt.xticks(fontsize = 25)
    plt.yticks(fontsize = 25)
    plt.grid()
    plt.title(col,fontsize= 20)
    try:
        sns.displot(df[col])    
    except :
        print(col + " is robust, gives stable guess number, no need to plot")
    
    fileName = GUESS_NUMBER_DATA_SAVE+ "/"+str(col)+".jpg"
    if path.exists(fileName):
        remove(fileName)
    plt.savefig(fileName)




def train_analysis_meter(fileName = None):


    print("starting analysis .....")

    print("Reading data from for training:", str(TRAINING_DATA))

    with open(TRAINING_DATA, 'rt') as f:
        training = [w.strip('\r\n') for w in f]

    print("Min gram: ",MIN_NGRAM)
    print("Max_gram: ",MAX_NGRAM)

    models = {'{}-gram'.format(i): ngram_chain.NGramModel(training, i)
          for i in range(MIN_NGRAM, MAX_NGRAM + 1)}
    models['Backoff'] = backoff.BackoffModel(training, 10)
    models['PCFG'] = pcfg.PCFG(training)
    print("All trained models : ",models)
    samples = {name: list(model.sample(SAMPLE_SIZE))
           for name, model in models.items()}

    estimators = {name: model.PosEstimator(sample)
              for name, sample in samples.items()}
    modelnames = sorted(models)

    # testing analysis

    print("Reading data from for testing:", str(TESTING_DATA))

    with open(TESTING_DATA, 'rt') as f:
        test_passwords = [w.strip('\r\n') for w in f]

    colnames = ['password'] + [name for name in modelnames]

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
    fileName = GUESS_NUMBER_DATA_SAVE + "/password_analysis.csv"
    if path.exists(fileName):
        remove(fileName)

    df.to_csv(fileName)

    print("analysis done ...data saved  ...")



def plot_guess_number_dist():

    fileName = GUESS_NUMBER_DATA_SAVE + "/password_analysis.csv"
    df = pd.read_csv(fileName)
    attacks = list(df.columns[2:])

    print("Attack models record : ", attacks)
    for attack in attacks:
        plotFuncHist(df, attack)
        git push -f 



    

if __name__ == "__main__":

    train_analysis_meter()
    plot_guess_number_dist()


   

    


            



       








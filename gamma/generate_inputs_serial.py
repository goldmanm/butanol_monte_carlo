# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import sys
sys.path.append('/home/goldmanm/repos/RMG-Py')
import numpy as np
import numpy.random as rd
import pandas as pd
from multiprocessing import Pool
from Arkane import run_arkane_python

def replace_text_with_uncertainties(input_text, lognormal_replacement_values=None,
                                    normal_replacement_values=None,
                                    switch_replacement_values=None):
    """
    takes text for a batch script with keywords for uncertainty and replaces them
    with random values.

    input_text = text to replace values
    lognormal_replacement_values = dict with key as text to replace and value as the sigma of lognormal distribution
    normal_replacement_values =  dict with key as text to replace and value as the sigmal of normal distribution
    switch_replacement_values = dict containting tuple of (string, probability) allowing weight-based categorical decisions

    Returns a tuple with the first item the input_text and the second item a list of the random values inserted.
    """
    random_list = {}
    if lognormal_replacement_values==None:
        lognormal_replacement_values = {'***u_sigma***': 0.2,
                                        '***u_ljalpha***': 0.5,
                                        '***u_negfreq***': 0.2,
                                        '***u_ilt***': 5,
                              }
    if normal_replacement_values==None:
        normal_replacement_values = {'***u_E0***': 10,
                                     '***u_ljn***': 0.15,
                                     }
    if switch_replacement_values == None:
        switch_replacement_values = {'***u_method***':[('reservoir state',.75),('modified strong collision',.25)]}
    # get all replaced values
    str_triggers = [key for keys in [lognormal_replacement_values.keys(), normal_replacement_values.keys(), switch_replacement_values.keys()] for key in keys]
    for key in str_triggers:
        random_list[key] = []
    
    
    
    for key, value in lognormal_replacement_values.items():
        while key in input_text:
            random_value = rd.lognormal(0, value)
            random_list[key].append(random_value)
            input_text=input_text.replace(key, str(random_value), 1)
            
    for key, value in normal_replacement_values.items():
        while key in input_text:
            random_value = rd.normal(0, value)
            random_list[key].append(random_value)
            input_text=input_text.replace(key, str(random_value), 1)
        
    for key, value in switch_replacement_values.items():
        # normalize cutoff values and use that to decide which string should be replaced
        cutoff_values = np.cumsum([_tuple[1] for _tuple in value])
        #normalize to one
        cutoff_values /= cutoff_values[-1]
        while key in input_text:
            random_value = rd.uniform()
            for index, cutoff_value in enumerate(cutoff_values):
                if random_value < cutoff_value:
                    random_value = value[index][0]
                    random_list[key].append(random_value)
                    input_text=input_text.replace(key, random_value, 1)
                    break
    return input_text, random_list

def generate_mech(index):
    simulation_dir = 'runs_20200715'
    path_dir = os.path.join(simulation_dir, 'run_{:04d}'.format(index))
    os.makedirs(path_dir, exist_ok=True)
    try:
        run_arkane_python(os.path.join(simulation_dir,'input_{:04d}.py'.format(index)),
                          path_dir,
                          save_rmg_libraries=False,)
        print('run {} completed without failing'.format(index))
        return True
    except Exception as e:
        print(e)
        print('run {} failed'.format(index))
        return False


if __name__ == '__main__':
    start_index, end_index = 1488, 2000
    generate_templates = False
    generate_mechs = True
    simulation_dir = 'runs_20200715'
    
    index = start_index
    rd.seed(0)
    with open('cantherm_pdep_input_gamma_w_uncertainty_blanks.py', 'r') as f:
        input_w_blanks = f.read()

    if generate_templates:
        key_list = None
        list_of_random_values = []
        while index < end_index:
            generated_text, random_values = replace_text_with_uncertainties(input_w_blanks)
            with open(os.path.join(simulation_dir, 'input_{:04d}.py'.format(index)), 'w') as f:
                f.write(generated_text)
            if key_list is None:
                # get column names based on key time
                key_list = list(random_values.keys())
                column_names = []
                for key in key_list:
                    list_len = len(random_values[key])
                    [column_names.append(key+'_'+str(item_num)) for item_num in range(list_len)]
            # flatten dictionary to list
            random_list = []
            for key in key_list:
                random_list.extend(random_values[key])
            # store values
            list_of_random_values.append(random_list)
            index += 1
        random_values_df = pd.DataFrame(data=list_of_random_values, index=range(end_index), columns=column_names)
        random_values_df.to_csv('random_values.csv')

    if generate_mechs:
        finished_correctly = []
        index = start_index
        indexes = list(range(start_index, end_index))
        for index in indexes:
            success = generate_mech(index)
            if not success:
                finished_correctly.append(index)
        pd.Series(data=finished_correctly).to_csv('successful_runs.csv')



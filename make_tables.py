import os

import numpy as np
import pandas as pd

import cantera as ct

def get_successful_simulations(directory):
    """
    given a directory, looks at runs within directory and determines whether
    the Arkane job completed successfully based on the last line of the arkane.log file
    """
    successful_runs = []
    files = os.listdir(directory)
    for file_name in files:
        file_path = os.path.join(directory, file_name)
        if os.path.isdir(file_path):
            successful_runs.append(file_name)
    return successful_runs

def get_reaction_branching(solution, initial_reactants):
    """given a solution object at a specified temperature
    and pressure, finds the reaction rates of reactions
    corresponding to the initial_reactants, in both forward
    and reverse directions.
    
    returns a pandas.Series with the reaction index as its
    index and the reaction rate constant as its product.
    
    All reactants must be specified for a match to be found."""
    reactions = solution.reactions()
    reaction_rates = {}
    for index in range(len(reactions)):
        rxn = reactions[index]
        reactants = set(rxn.reactants.keys())
        products = set(rxn.products.keys())
        if reactants == initial_reactants:
            #print(rxn)
            reaction_rates[index] = solution.forward_rate_constants[index]
        elif products == initial_reactants:
            #print(rxn)
            reaction_rates[index] = solution.reverse_rate_constants[index]
        else:
            continue
    if len(reaction_rates) == 0:
        raise Exception('No reaction branching found for {0}'.format(initial_reactants))
    return pd.Series(reaction_rates)

def get_initial_reactants(surface, species):
    if species == 'R + O2':
        if surface == 'alpha':
            initial_reactants = set(('O2','aR'))
        elif surface == 'beta':
            initial_reactants = set(('O2','bR'))
        elif surface == 'gamma':
            initial_reactants = set(('O2', 'gR'))
    elif species == 'RO2':
        if surface == 'alpha':
            initial_reactants = set(('aRO2',))
        elif surface == 'beta':
            initial_reactants = set(('bRO2',))
        elif surface == 'gamma':
            initial_reactants = set(('gRO2',))
    return initial_reactants

# object listing all the formatting things to replace in the file
replace_dict = {}
replace_dict['title'] = {'{}': 'path',
                         'primary_factor': 'factor',
                  'secondary_factor ': 'factor',
                  'factor_corr_2': '\\texttau',
                  'factor_corr ': '\\texttau ',
                         '5%': '5\%',
                         '50%': '50\%',
                         '95%': '95\%',
                         '90%': '90\%'
                        }
replace_dict['post_fix_replacements'] = {
                                        'al...': 'alpha\\ $E_0$',
                                        'ga...': 'gamma\\ $E_0$',
                                        '<=>': '\\ce{<=>}',
                                        '->': '\\ce{->}',
                                        '\\begin{table}\n': '\\begin{table}[H]\n',
                                        'performic_acid': 'performic\\_acid',
                                        'disub_c4ether': 'disub\\_c4ether',
                                        'disub_epoxy': 'disub\\_epoxy',
                                        'trisub_epoxy': 'trisub\\_epoxy',
}


replace_dict['alpha'] = {'is_reservoir_state': 'reservoir state',
                  '***u_E0***_1': 'isobutanal $E_0$',
                  '***u_E0***_2': '\textalpha R $E_0$',       
                  '***u_E0***_5': '\textalpha adduct $E_0$',
                  '***u_E0***_7': 'trisub_epoxy $E_0$',
                  '***u_E0***_9': '\textalpha RO2 $E_0$',
                  '***u_E0***_15': '\textalpha C4EtherFrom\textgamma\ $E_0$',
                  '***u_E0***_16': '\textalpha -\textbeta scissionFromAlkoxy $E_0$',
                  '***u_E0***_17': '\textalpha -\textbeta scissionFrom\textgamma\ $E_0$',
                  '***u_E0***_19': '\textalpha AdductFromRO2 $E_0$',
                  '***u_ilt***_0': '$r_{\\alpha R + O_2}$',
                  '***u_ilt***_1': '$r_{isobutanal + HO2}$',
                  '***u_ljn***_3': '\textalpha R $\langle E_{down}\rangle$ exp',
     }
replace_dict['beta'] = {'is_reservoir_state': 'reservoir state',
                        '***u_E0***_0': '\textbeta QOOH[O] $E_0$',
                        '***u_E0***_7': '\textbeta R $E_0$',
                        '***u_E0***_9': '\textbeta RO2 $E_0$',
                        '***u_E0***_11': '\textbeta-\textgamma QOOHIsom $E_0$',
                        '***u_E0***_13': '\textbeta EpoxyFrom\textalpha\ $E_0$',
                        '***u_E0***_16': '\textbeta -\textgamma HO2elimFromRO2 $E_0$',
                        '***u_E0***_17': '\textbeta -\textalpha HO2elimFromRO2 $E_0$',
                        '***u_E0***_18': '\textbeta HO2elimFrom\textalpha\ $E_0$',
                        '***u_E0***_19': '\textbeta -\textalpha QOOHIsom $E_0$',
                        '***u_E0***_21': '\textbeta Double\textbeta scission $E_0$',
                        '***u_ilt***_0': '$r_{\\beta R + O_2}$',
                        '***u_negfreq***_0': 'imaginary freq. \textbeta -\textgamma QOOHIsom',
                        '***u_negfreq***_1': 'imaginary freq. \textbeta H2OForm',
                        '***u_negfreq***_8': 'imaginary freq. \textbeta -\textalpha QOOHIsom',
                  
    
}
replace_dict['gamma'] = {'is_reservoir_state': 'reservoir state',
                        '***u_E0***_3': '\textgamma QOOH\textalpha $E_0$',
                         '***u_E0***_9': '\textgamma RO2 $E_0$',
                         '***u_E0***_10': '\textgamma QOOH\textgamma $E_0$',
                         '***u_E0***_11': '\textgamma R $E_0$',
                         '***u_E0***_15': '\textgamma AlkoxyIsom $E_0$',
                         '***u_E0***_16': '\textgamma -\textalpha QOOHIsom $E_0$',
                         '***u_E0***_17': '\textgamma -\textgamma QOOHIsom $E_0$',
                         '***u_E0***_18': '\textgamma -\textbeta QOOHIsom $E_0$',
                         '***u_E0***_19': '\textgamma HO2elimFromRO2 $E_0$',
                         '***u_E0***_21': '\textgamma H2OForm $E_0$',
                         '***u_E0***_22': '\textgamma C4EtherFrom\textalpha\ $E_0$',
                         '***u_E0***_25': '\textgamma Double\textbeta scissionFrom\textalpha\ $E_0$',
                         '***u_E0***_26': '\textgamma Double\textbeta scissionFrom\textgamma\ $E_0$',
                         '***u_E0***_29': '\textgamma AldolFrom\textalpha\ $E_0$',
                         '***u_ilt***_0': '$r_{\\gamma R + O_2}$',
                        '***u_negfreq***_3': 'imaginary freq. \textgamma -\textbeta QOOHIsom',
    
}

# more formatting things
species_conversion_df = pd.read_csv('species_name_comparison.csv', encoding = 'utf-8')
reaction_conversion_df = pd.read_csv('reaction_info.csv', encoding = 'utf-8')
cantera2paper = dict(zip(species_conversion_df['chemkin_name'], species_conversion_df['paper_name']))
cantera2paper.update(dict(zip(reaction_conversion_df['ascii_name'], reaction_conversion_df['unicode_name'])))

# now let's get the branching ratio distributions and create pandas DataFrames
species_list = ['R + O2', 'RO2']
surface_list = ['alpha', 'beta', 'gamma']
T_P_list = [(300,1e5), (600,3e5), (900,10e5)]
tables = []
total_rates = []
for species in species_list:
    for surface in surface_list:
        total_rates.append(' + '.join(get_initial_reactants(surface, species)) + ' -> products')
total_rate_tables = {}
total_rate_tables[300] = pd.DataFrame(index=total_rates, columns=['5%', '50%', '95%', 'primary_factor', 'factor_corr', 'secondary_factor', 'factor_corr_2'])
total_rate_tables[600] = pd.DataFrame(index=total_rates, columns=['5%', '50%', '95%', 'primary_factor', 'factor_corr', 'secondary_factor', 'factor_corr_2'])
total_rate_tables[900] = pd.DataFrame(index=total_rates, columns=['5%', '50%', '95%', 'primary_factor', 'factor_corr', 'secondary_factor', 'factor_corr_2'])

for surface in surface_list:
    main_dir = '{}/runs_20200715'.format(surface)
    successful_simulations = get_successful_simulations(main_dir)
    parameter_values = pd.read_csv('{}/random_values.csv'.format(surface), index_col=0, )
    successful_simulations_int = [int(s.split('_')[1]) for s in successful_simulations]
    parameter_values = parameter_values.loc[successful_simulations_int,:]
    parameter_values['is_reservoir_state'] = parameter_values['***u_method***_0'] == 'reservoir state'
    num_sims = len(successful_simulations)
    
    # get unicode reaction_names
    solution = ct.Solution(os.path.join(main_dir, successful_simulations[0], 'chem.cti'))
    rxn_names = solution.reaction_equations()
    u_rxn_names = []
    for rxn_name in rxn_names:
        rxn_name = ' ' + rxn_name + ' ' # use spaces to ensure match
        for key, value in cantera2paper.items():
            rxn_name = rxn_name.replace(' '+key+' ', ' '+value+' ')
        u_rxn_names.append(rxn_name[1:-1])
    
    for species in species_list:
        initial_reactants = get_initial_reactants(surface, species)
        for T, P in T_P_list:
            print('{}{} at {} K'.format(surface, species, T))
            branching_data = []
            for run in successful_simulations:
                run_dir = os.path.join(main_dir, run)
                cantherm_file = os.path.join(run_dir, 'chem.cti')
                solution = ct.Solution(cantherm_file)
                solution.TP = T, P
                branching = get_reaction_branching(solution, initial_reactants)
                branching_data.append(branching)
            df = pd.DataFrame(data=branching_data, index=successful_simulations_int)
            relative_df = df.divide(df.sum(1),0)
            largest_reactions = relative_df.sum().sort_values(ascending=False)
            sorted_df = relative_df.sort_values(largest_reactions.index[0], axis=0)
            index_values = (round(num_sims * .05), round(num_sims * .5), round(num_sims * .95))

            total_rate_str = ' + '.join(initial_reactants) + ' -> products'
            table_vals = [u_rxn_names[x] for x in largest_reactions.index]
            table = pd.DataFrame(index=[u_rxn_names[x] for x in largest_reactions.index], columns=['5%', '50%', '95%', 'primary_factor', 'factor_corr', 'secondary_factor', 'factor_corr_2'])
            for rxn_index in sorted_df.columns:
                rxn_name = u_rxn_names[rxn_index]
                series = relative_df[rxn_index]
                sorted_s = series.sort_values()
                table.loc[rxn_name, '5%'] = sorted_s.iloc[index_values[0]]
                table.loc[rxn_name, '50%'] = sorted_s.iloc[index_values[1]]
                table.loc[rxn_name, '95%'] = sorted_s.iloc[index_values[2]]
                # skip if highest value is less than 1%
                if sorted_s.iloc[index_values[2]] > 0.01:
                    p_corr = parameter_values.corrwith(relative_df[rxn_index], method='spearman')
                    largest_factor = p_corr.abs().sort_values().index[-1]
                    factor_value = p_corr[largest_factor]
                    table.loc[rxn_name, 'primary_factor'] = replace_dict[surface][largest_factor]
                    table.loc[rxn_name, 'factor_corr'] = factor_value
                    second_largest_factor = p_corr.abs().sort_values().index[-2]
                    factor_value = p_corr[second_largest_factor]
                    table.loc[rxn_name, 'secondary_factor'] = replace_dict[surface][second_largest_factor]
                    table.loc[rxn_name, 'factor_corr_2'] = factor_value
            tables.append(table)
            # for bulk rate analysis
            factor_value = p_corr[largest_factor]
            rate_table = total_rate_tables[T]
            total_reaction_rates = df.sum(1)
            p_corr = parameter_values.corrwith(total_reaction_rates, method='spearman')
            largest_factor = p_corr.abs().sort_values().index[-1]
            factor_value = p_corr[largest_factor]
            rate_table.loc[total_rate_str, 'primary_factor'] = replace_dict[surface][largest_factor]
            rate_table.loc[total_rate_str, 'factor_corr'] = factor_value
            largest_factor = p_corr.abs().sort_values().index[-2]
            factor_value = p_corr[largest_factor]
            rate_table.loc[total_rate_str, 'secondary_factor'] = replace_dict[surface][largest_factor]
            rate_table.loc[total_rate_str, 'factor_corr_2'] = factor_value
            rate_table.loc[total_rate_str, '5%'] = total_reaction_rates.iloc[index_values[0]]
            rate_table.loc[total_rate_str, '50%'] = total_reaction_rates.iloc[index_values[1]]
            rate_table.loc[total_rate_str, '95%'] = total_reaction_rates.iloc[index_values[2]]
for t in total_rate_tables.keys():
    tables.append(total_rate_tables[t])

# strings to place around the tables
start_string_br = """
\\begin{{table}}
	\\caption[\\text{0} {1} uncertainty {2} K]{{Branching ratio uncertainty for \\text{0} {1} at {2} K and {3} Pa.
    The median and 90\% confidence interval of the branching ratio for each pathway are shown using data from Monte carlo simulations.
    For each branch point, the two parameters with the highest correlation, \\texttau, determined using the Spearman rank correlation, are shown with their corresponding values.
    See \\ref{{ss:uncertainty}} for description of the parameter names.}}
	\\label{{t:{0}{1} uncertainty {2} K}}
    \\begin{{adjustbox}}{{width=\columnwidth,center}}
"""
start_string_total = """
\\begin{{table}}
	\\caption[total rate uncertainty {2} K]{{Overall rate uncertainty at {2} K and {3} Pa.
    The median and 90\% confidence interval of the branching ratio for each reaction are shown using data from Monte carlo simulations.
    For each path, the two parameters with the highest correlation, \\texttau, determined using the Spearman rank correlation, are shown with their corresponding values.
    See \\ref{{ss:uncertainty}} for description of the parameter names.}}
	\\label{{t:total rate uncertainty {2} K}}
    \\begin{{adjustbox}}{{width=\columnwidth,center}}
"""
end_string = """
\end{adjustbox}
\end{table}


"""

# methods to format floats
def to_latex_float(val):
    if abs(val) > 1000:
        sci_not_form = np.format_float_scientific(val, exp_digits=1, precision=1)
        sci_not_form = sci_not_form.replace('.e+', '$\\times 10^{')
        return sci_not_form.replace('e+', '$\\times 10^{')+'}$'
    elif abs(val) > 1:
        return str(int(val))
    elif abs(val) > 0.001:
        return "{:0.3f}".format(val)
    else:
        sci_not_form = np.format_float_scientific(val, exp_digits=1, precision=0)
        return sci_not_form.replace('.e-', '$\\times 10^{-')+'}$'

index = 0
tables_str = ""
for surface in surface_list:
    for species in species_list:
        for T, P in T_P_list:
            tables_str += start_string_br.format(surface, species, T, to_latex_float(P))
            table = tables[index].copy()
            # remove data with less than 1% branching at 95%
            trunc_table = table.loc[table['95%'] > 0.01,:]
            
            latex_table = trunc_table.to_latex(float_format=to_latex_float, escape=False).replace(u'γ ',r'\textgamma\ ').replace(u'α ',r'\textalpha\ ').replace(u'β ',r'\textbeta\ ')
            latex_table = latex_table.replace(u'γ',r'\textgamma ').replace(u'α',r'\textalpha ').replace(u'β',r'\textbeta ')
    
            for key, val in replace_dict['title'].items():
                latex_table = latex_table.replace(key, val)
            tables_str += latex_table
            tables_str += end_string
            index += 1
    
for T, P in T_P_list:
    rate_table = total_rate_tables[T]
    latex_table = rate_table.to_latex(float_format=to_latex_float, escape=False).replace(u'γ ',r'\textgamma\ ').replace(u'α ',r'\textalpha\ ').replace(u'β ',r'\textbeta\ ')
    latex_table = latex_table.replace(u'γ',r'\textgamma ').replace(u'α',r'\textalpha ').replace(u'β',r'\textbeta ')
    for key, val in replace_dict['title'].items():
        latex_table = latex_table.replace(key, val)
    tables_str += start_string_total.format(surface, species, T, to_latex_float(P))
    tables_str += latex_table
    tables_str += end_string

# remove inconsistencies
for key, value in replace_dict['post_fix_replacements'].items():
    tables_str = tables_str.replace(key, value)

with open('tables.tex', 'w') as f:
    f.write(tables_str)
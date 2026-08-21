"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439998, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439998, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.186104, 'e_o_k': [0.268783, 0.215027, 0.172021], 'p_i': 10, 'u_i': 1.9682},
        {'id': 1, 'e_m': 2.138129, 'e_o_k': [0.356355, 0.285084], 'p_i': 20, 'u_i': 4.1538},
        {'id': 2, 'e_m': 10.809101, 'e_o_k': [1.098486, 0.878789, 0.703031, 0.562425], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 14.163864, 'e_o_k': [2.360644, 1.888515], 'p_i': 80, 'u_i': 4.6912},
        {'id': 4, 'e_m': 1.298646, 'e_o_k': [0.115895, 0.092716, 0.074173, 0.059338, 0.047471], 'p_i': 40, 'u_i': 2.4684},
        {'id': 5, 'e_m': 11.370525, 'e_o_k': [0.924613, 0.739691, 0.591753, 0.473402, 0.378722, 0.302977], 'p_i': 40, 'u_i': 3.0218},
        {'id': 6, 'e_m': 1.323261, 'e_o_k': [0.118092, 0.094474, 0.075579, 0.060463, 0.048371], 'p_i': 20, 'u_i': 2.6468},
        {'id': 7, 'e_m': 19.545197, 'e_o_k': [1.589351, 1.271480, 1.017184, 0.813747, 0.650998, 0.520798], 'p_i': 80, 'u_i': 1.1768},
    ]
    B_BUDGET = 167.439998
    return processors, tasks, B_BUDGET

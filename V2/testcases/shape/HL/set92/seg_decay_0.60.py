"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.39999, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.39999, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.559072, 'e_o_k': [0.121242, 0.072745, 0.043647, 0.026188, 0.015713], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 1.614981, 'e_o_k': [0.338803, 0.203282, 0.121969, 0.073182, 0.043909, 0.026345], 'p_i': 20, 'u_i': 1.1622},
        {'id': 2, 'e_m': 6.358045, 'e_o_k': [1.621950, 0.973170, 0.583902], 'p_i': 40, 'u_i': 4.1752},
        {'id': 3, 'e_m': 15.550394, 'e_o_k': [3.573160, 2.143896, 1.286338, 0.771803], 'p_i': 80, 'u_i': 1.9420},
        {'id': 4, 'e_m': 0.003664, 'e_o_k': [0.001145, 0.000687], 'p_i': 10, 'u_i': 2.5093},
        {'id': 5, 'e_m': 3.875294, 'e_o_k': [0.988595, 0.593157, 0.355894], 'p_i': 80, 'u_i': 3.6510},
        {'id': 6, 'e_m': 0.722639, 'e_o_k': [0.166048, 0.099629, 0.059777, 0.035866], 'p_i': 10, 'u_i': 3.1983},
        {'id': 7, 'e_m': 7.557649, 'e_o_k': [1.736592, 1.041955, 0.625173, 0.375104], 'p_i': 40, 'u_i': 4.3627},
    ]
    B_BUDGET = 110.399990
    return processors, tasks, B_BUDGET

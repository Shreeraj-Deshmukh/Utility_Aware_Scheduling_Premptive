"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 217.855991, "H": 80, "J": 43, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.4, "seed": 1028, "set": 28, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.40"}
"""

_SPEC = '{"B": 217.855991, "H": 80, "J": 43, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.4, "seed": 1028, "set": 28, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.834237, 'e_o_k': [0.648851, 0.519081], 'p_i': 10, 'u_i': 4.4926},
        {'id': 1, 'e_m': 2.062949, 'e_o_k': [1.183659, 0.946927, 0.757542], 'p_i': 20, 'u_i': 3.2922},
        {'id': 2, 'e_m': 2.169279, 'e_o_k': [1.687217, 1.349773], 'p_i': 40, 'u_i': 3.7450},
        {'id': 3, 'e_m': 13.026985, 'e_o_k': [6.178110, 4.942488, 3.953990, 3.163192], 'p_i': 80, 'u_i': 4.8771},
        {'id': 4, 'e_m': 0.281506, 'e_o_k': [0.218949, 0.175159], 'p_i': 20, 'u_i': 4.0203},
        {'id': 5, 'e_m': 1.211718, 'e_o_k': [0.574663, 0.459730, 0.367784, 0.294227], 'p_i': 10, 'u_i': 3.4418},
        {'id': 6, 'e_m': 1.184948, 'e_o_k': [0.679888, 0.543910, 0.435128], 'p_i': 10, 'u_i': 4.8003},
        {'id': 7, 'e_m': 1.426177, 'e_o_k': [0.818299, 0.654639, 0.523711], 'p_i': 10, 'u_i': 3.9154},
    ]
    B_BUDGET = 217.855991
    return processors, tasks, B_BUDGET

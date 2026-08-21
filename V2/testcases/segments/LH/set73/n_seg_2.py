"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.599170, 'e_o_k': [0.466021, 0.372817], 'p_i': 10, 'u_i': 3.9348},
        {'id': 1, 'e_m': 4.185659, 'e_o_k': [3.255513, 2.604410], 'p_i': 20, 'u_i': 2.2078},
        {'id': 2, 'e_m': 0.147250, 'e_o_k': [0.114528, 0.091622], 'p_i': 40, 'u_i': 1.5646},
        {'id': 3, 'e_m': 1.074448, 'e_o_k': [0.835682, 0.668545], 'p_i': 80, 'u_i': 4.4075},
        {'id': 4, 'e_m': 0.209273, 'e_o_k': [0.162768, 0.130214], 'p_i': 10, 'u_i': 2.2030},
        {'id': 5, 'e_m': 0.141966, 'e_o_k': [0.110418, 0.088334], 'p_i': 80, 'u_i': 2.4770},
        {'id': 6, 'e_m': 0.313697, 'e_o_k': [0.243986, 0.195189], 'p_i': 80, 'u_i': 4.3612},
        {'id': 7, 'e_m': 1.741302, 'e_o_k': [1.354346, 1.083477], 'p_i': 20, 'u_i': 4.6337},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760006, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760006, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.592270, 'e_o_k': [0.060190, 0.048152, 0.038522, 0.030817], 'p_i': 10, 'u_i': 4.2289},
        {'id': 1, 'e_m': 0.183971, 'e_o_k': [0.030662, 0.024529], 'p_i': 20, 'u_i': 3.6434},
        {'id': 2, 'e_m': 2.483096, 'e_o_k': [0.201917, 0.161534, 0.129227, 0.103382, 0.082705, 0.066164], 'p_i': 40, 'u_i': 4.1771},
        {'id': 3, 'e_m': 1.221389, 'e_o_k': [0.124125, 0.099300, 0.079440, 0.063552], 'p_i': 80, 'u_i': 4.0903},
        {'id': 4, 'e_m': 1.538364, 'e_o_k': [0.156338, 0.125070, 0.100056, 0.080045], 'p_i': 20, 'u_i': 2.9627},
        {'id': 5, 'e_m': 0.082762, 'e_o_k': [0.008411, 0.006729, 0.005383, 0.004306], 'p_i': 80, 'u_i': 1.9286},
        {'id': 6, 'e_m': 2.417781, 'e_o_k': [0.245709, 0.196568, 0.157254, 0.125803], 'p_i': 10, 'u_i': 3.5955},
        {'id': 7, 'e_m': 5.379957, 'e_o_k': [0.480125, 0.384100, 0.307280, 0.245824, 0.196659], 'p_i': 40, 'u_i': 1.8182},
    ]
    B_BUDGET = 71.760006
    return processors, tasks, B_BUDGET

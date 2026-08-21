"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599994, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599994, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.317393, 'e_o_k': [0.025809, 0.020647, 0.016518, 0.013214, 0.010572, 0.008457], 'p_i': 10, 'u_i': 1.0975},
        {'id': 1, 'e_m': 3.055621, 'e_o_k': [0.310531, 0.248424, 0.198740, 0.158992], 'p_i': 20, 'u_i': 4.1970},
        {'id': 2, 'e_m': 1.798002, 'e_o_k': [0.146208, 0.116966, 0.093573, 0.074858, 0.059887, 0.047909], 'p_i': 40, 'u_i': 1.7417},
        {'id': 3, 'e_m': 11.258632, 'e_o_k': [1.004757, 0.803805, 0.643044, 0.514435, 0.411548], 'p_i': 80, 'u_i': 3.7063},
        {'id': 4, 'e_m': 1.184279, 'e_o_k': [0.145608, 0.116486, 0.093189], 'p_i': 20, 'u_i': 3.7708},
        {'id': 5, 'e_m': 1.216374, 'e_o_k': [0.123615, 0.098892, 0.079114, 0.063291], 'p_i': 20, 'u_i': 3.9372},
        {'id': 6, 'e_m': 1.307875, 'e_o_k': [0.160804, 0.128643, 0.102915], 'p_i': 20, 'u_i': 1.6580},
        {'id': 7, 'e_m': 35.549627, 'e_o_k': [4.370856, 3.496685, 2.797348], 'p_i': 80, 'u_i': 4.1894},
    ]
    B_BUDGET = 119.599994
    return processors, tasks, B_BUDGET

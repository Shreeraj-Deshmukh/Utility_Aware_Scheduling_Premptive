"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.737228, 'e_o_k': [0.542884, 0.325730], 'p_i': 10, 'u_i': 1.8132},
        {'id': 1, 'e_m': 1.414064, 'e_o_k': [0.296653, 0.177992, 0.106795, 0.064077, 0.038446, 0.023068], 'p_i': 20, 'u_i': 1.3118},
        {'id': 2, 'e_m': 8.894962, 'e_o_k': [1.928991, 1.157394, 0.694437, 0.416662, 0.249997], 'p_i': 40, 'u_i': 1.6432},
        {'id': 3, 'e_m': 3.992321, 'e_o_k': [1.247600, 0.748560], 'p_i': 80, 'u_i': 3.2827},
        {'id': 4, 'e_m': 0.156022, 'e_o_k': [0.033835, 0.020301, 0.012181, 0.007308, 0.004385], 'p_i': 20, 'u_i': 1.0597},
        {'id': 5, 'e_m': 0.352177, 'e_o_k': [0.089841, 0.053905, 0.032343], 'p_i': 20, 'u_i': 4.4596},
        {'id': 6, 'e_m': 5.127088, 'e_o_k': [1.178099, 0.706860, 0.424116, 0.254469], 'p_i': 40, 'u_i': 4.8824},
        {'id': 7, 'e_m': 1.297088, 'e_o_k': [0.330890, 0.198534, 0.119120], 'p_i': 10, 'u_i': 1.5609},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET

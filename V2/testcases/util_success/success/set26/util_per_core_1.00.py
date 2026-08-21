"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200005, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200005, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.379684, 'e_o_k': [0.415535, 0.332428, 0.265942], 'p_i': 10, 'u_i': 2.4333},
        {'id': 1, 'e_m': 5.119782, 'e_o_k': [0.416324, 0.333059, 0.266447, 0.213158, 0.170526, 0.136421], 'p_i': 20, 'u_i': 4.0156},
        {'id': 2, 'e_m': 1.117136, 'e_o_k': [0.090842, 0.072673, 0.058139, 0.046511, 0.037209, 0.029767], 'p_i': 40, 'u_i': 2.4270},
        {'id': 3, 'e_m': 1.565919, 'e_o_k': [0.159138, 0.127310, 0.101848, 0.081479], 'p_i': 80, 'u_i': 3.2841},
        {'id': 4, 'e_m': 18.366198, 'e_o_k': [3.061033, 2.448826], 'p_i': 40, 'u_i': 2.5593},
        {'id': 5, 'e_m': 5.970418, 'e_o_k': [0.485495, 0.388396, 0.310717, 0.248573, 0.198859, 0.159087], 'p_i': 20, 'u_i': 3.5120},
        {'id': 6, 'e_m': 12.582475, 'e_o_k': [1.278707, 1.022965, 0.818372, 0.654698], 'p_i': 40, 'u_i': 2.6086},
        {'id': 7, 'e_m': 2.863024, 'e_o_k': [0.352011, 0.281609, 0.225287], 'p_i': 10, 'u_i': 2.0046},
    ]
    B_BUDGET = 239.200005
    return processors, tasks, B_BUDGET

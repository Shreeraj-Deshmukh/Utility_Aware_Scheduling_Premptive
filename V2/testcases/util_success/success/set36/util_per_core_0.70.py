"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439972, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439972, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.921323, 'e_o_k': [0.195256, 0.156205, 0.124964, 0.099971], 'p_i': 10, 'u_i': 3.8216},
        {'id': 1, 'e_m': 1.847805, 'e_o_k': [0.227189, 0.181751, 0.145401], 'p_i': 20, 'u_i': 4.3612},
        {'id': 2, 'e_m': 16.186326, 'e_o_k': [1.644952, 1.315961, 1.052769, 0.842215], 'p_i': 40, 'u_i': 2.3108},
        {'id': 3, 'e_m': 8.733364, 'e_o_k': [0.887537, 0.710030, 0.568024, 0.454419], 'p_i': 80, 'u_i': 1.0383},
        {'id': 4, 'e_m': 0.861245, 'e_o_k': [0.143541, 0.114833], 'p_i': 20, 'u_i': 2.0614},
        {'id': 5, 'e_m': 2.781114, 'e_o_k': [0.282634, 0.226107, 0.180885, 0.144708], 'p_i': 10, 'u_i': 4.6739},
        {'id': 6, 'e_m': 0.226384, 'e_o_k': [0.023006, 0.018405, 0.014724, 0.011779], 'p_i': 10, 'u_i': 3.1717},
        {'id': 7, 'e_m': 5.156804, 'e_o_k': [0.419334, 0.335467, 0.268374, 0.214699, 0.171759, 0.137407], 'p_i': 20, 'u_i': 4.1313},
    ]
    B_BUDGET = 167.439972
    return processors, tasks, B_BUDGET

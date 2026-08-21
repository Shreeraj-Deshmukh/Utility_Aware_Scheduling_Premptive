"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.372012, 'e_o_k': [0.428754, 0.257252], 'p_i': 10, 'u_i': 2.6470},
        {'id': 1, 'e_m': 3.488332, 'e_o_k': [0.889881, 0.533928, 0.320357], 'p_i': 20, 'u_i': 4.9479},
        {'id': 2, 'e_m': 0.095964, 'e_o_k': [0.024481, 0.014688, 0.008813], 'p_i': 40, 'u_i': 2.1346},
        {'id': 3, 'e_m': 3.859529, 'e_o_k': [1.206103, 0.723662], 'p_i': 80, 'u_i': 1.3827},
        {'id': 4, 'e_m': 11.637726, 'e_o_k': [3.636789, 2.182074], 'p_i': 80, 'u_i': 3.9576},
        {'id': 5, 'e_m': 2.185253, 'e_o_k': [0.473901, 0.284341, 0.170604, 0.102363, 0.061418], 'p_i': 20, 'u_i': 4.9670},
        {'id': 6, 'e_m': 1.684152, 'e_o_k': [0.365231, 0.219138, 0.131483, 0.078890, 0.047334], 'p_i': 10, 'u_i': 4.5958},
        {'id': 7, 'e_m': 1.167163, 'e_o_k': [0.253115, 0.151869, 0.091121, 0.054673, 0.032804], 'p_i': 80, 'u_i': 1.9552},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279986, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279986, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.660399, 'e_o_k': [0.415909, 0.332727, 0.266182, 0.212945, 0.170356], 'p_i': 10, 'u_i': 3.3951},
        {'id': 1, 'e_m': 3.125700, 'e_o_k': [0.278948, 0.223158, 0.178526, 0.142821, 0.114257], 'p_i': 20, 'u_i': 2.7774},
        {'id': 2, 'e_m': 1.252560, 'e_o_k': [0.101854, 0.081483, 0.065187, 0.052149, 0.041719, 0.033376], 'p_i': 40, 'u_i': 4.2505},
        {'id': 3, 'e_m': 11.187239, 'e_o_k': [0.909709, 0.727767, 0.582214, 0.465771, 0.372617, 0.298093], 'p_i': 80, 'u_i': 1.3804},
        {'id': 4, 'e_m': 2.690966, 'e_o_k': [0.448494, 0.358795], 'p_i': 10, 'u_i': 2.4879},
        {'id': 5, 'e_m': 11.890906, 'e_o_k': [1.061183, 0.848946, 0.679157, 0.543326, 0.434660], 'p_i': 40, 'u_i': 2.1502},
        {'id': 6, 'e_m': 2.740713, 'e_o_k': [0.278528, 0.222822, 0.178258, 0.142606], 'p_i': 40, 'u_i': 4.2698},
        {'id': 7, 'e_m': 14.865341, 'e_o_k': [1.827706, 1.462165, 1.169732], 'p_i': 40, 'u_i': 3.4628},
    ]
    B_BUDGET = 215.279986
    return processors, tasks, B_BUDGET

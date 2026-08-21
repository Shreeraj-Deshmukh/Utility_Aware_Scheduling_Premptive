"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120002, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120002, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.607201, 'e_o_k': [0.061707, 0.049366, 0.039493, 0.031594], 'p_i': 10, 'u_i': 3.8239},
        {'id': 1, 'e_m': 9.110352, 'e_o_k': [0.813037, 0.650430, 0.520344, 0.416275, 0.333020], 'p_i': 20, 'u_i': 3.4110},
        {'id': 2, 'e_m': 14.977770, 'e_o_k': [1.217943, 0.974354, 0.779483, 0.623587, 0.498869, 0.399095], 'p_i': 40, 'u_i': 3.7986},
        {'id': 3, 'e_m': 22.883553, 'e_o_k': [2.813552, 2.250841, 1.800673], 'p_i': 80, 'u_i': 2.0887},
        {'id': 4, 'e_m': 0.090005, 'e_o_k': [0.008032, 0.006426, 0.005141, 0.004113, 0.003290], 'p_i': 10, 'u_i': 1.4414},
        {'id': 5, 'e_m': 13.652412, 'e_o_k': [1.678575, 1.342860, 1.074288], 'p_i': 40, 'u_i': 1.7490},
        {'id': 6, 'e_m': 38.314342, 'e_o_k': [3.419295, 2.735436, 2.188349, 1.750679, 1.400543], 'p_i': 80, 'u_i': 2.5599},
        {'id': 7, 'e_m': 15.522685, 'e_o_k': [1.577509, 1.262007, 1.009606, 0.807684], 'p_i': 80, 'u_i': 1.2480},
    ]
    B_BUDGET = 263.120002
    return processors, tasks, B_BUDGET

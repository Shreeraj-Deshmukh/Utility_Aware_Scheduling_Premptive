"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760023, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760023, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.607502, 'e_o_k': [0.143459, 0.114767, 0.091814, 0.073451, 0.058761], 'p_i': 10, 'u_i': 1.5090},
        {'id': 1, 'e_m': 1.060466, 'e_o_k': [0.086234, 0.068987, 0.055189, 0.044152, 0.035321, 0.028257], 'p_i': 20, 'u_i': 3.9781},
        {'id': 2, 'e_m': 2.552153, 'e_o_k': [0.313789, 0.251031, 0.200825], 'p_i': 40, 'u_i': 2.6834},
        {'id': 3, 'e_m': 9.000985, 'e_o_k': [1.500164, 1.200131], 'p_i': 80, 'u_i': 1.3712},
        {'id': 4, 'e_m': 0.666112, 'e_o_k': [0.059446, 0.047557, 0.038045, 0.030436, 0.024349], 'p_i': 40, 'u_i': 4.1249},
        {'id': 5, 'e_m': 1.736033, 'e_o_k': [0.141168, 0.112935, 0.090348, 0.072278, 0.057823, 0.046258], 'p_i': 40, 'u_i': 1.3639},
        {'id': 6, 'e_m': 7.617601, 'e_o_k': [0.679819, 0.543855, 0.435084, 0.348067, 0.278454], 'p_i': 80, 'u_i': 1.0001},
        {'id': 7, 'e_m': 0.546368, 'e_o_k': [0.048760, 0.039008, 0.031206, 0.024965, 0.019972], 'p_i': 10, 'u_i': 1.8994},
    ]
    B_BUDGET = 71.760023
    return processors, tasks, B_BUDGET

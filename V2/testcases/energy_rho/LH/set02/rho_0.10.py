"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 41.952, "H": 80, "J": 32, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.1, "seed": 1002, "set": 2, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.10"}
"""

_SPEC = '{"B": 41.952, "H": 80, "J": 32, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.1, "seed": 1002, "set": 2, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.355801, 'e_o_k': [0.276734, 0.221387], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 0.978019, 'e_o_k': [0.371137, 0.296909, 0.237527, 0.190022, 0.152018, 0.121614], 'p_i': 20, 'u_i': 3.2251},
        {'id': 2, 'e_m': 3.289454, 'e_o_k': [1.887392, 1.509913, 1.207931], 'p_i': 40, 'u_i': 4.0273},
        {'id': 3, 'e_m': 7.449156, 'e_o_k': [4.274106, 3.419285, 2.735428], 'p_i': 80, 'u_i': 2.2476},
        {'id': 4, 'e_m': 2.409551, 'e_o_k': [1.142741, 0.914193, 0.731354, 0.585083], 'p_i': 80, 'u_i': 1.3199},
        {'id': 5, 'e_m': 0.229718, 'e_o_k': [0.087173, 0.069738, 0.055791, 0.044633, 0.035706, 0.028565], 'p_i': 10, 'u_i': 4.7520},
        {'id': 6, 'e_m': 0.659831, 'e_o_k': [0.274799, 0.219839, 0.175871, 0.140697, 0.112558], 'p_i': 20, 'u_i': 3.4892},
        {'id': 7, 'e_m': 1.081708, 'e_o_k': [0.841328, 0.673063], 'p_i': 20, 'u_i': 1.4050},
    ]
    B_BUDGET = 41.952000
    return processors, tasks, B_BUDGET

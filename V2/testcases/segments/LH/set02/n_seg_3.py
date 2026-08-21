"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320006, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320006, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.355801, 'e_o_k': [0.204148, 0.163318, 0.130655], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 0.978019, 'e_o_k': [0.561159, 0.448927, 0.359141], 'p_i': 20, 'u_i': 4.0273},
        {'id': 2, 'e_m': 3.289454, 'e_o_k': [1.887392, 1.509913, 1.207931], 'p_i': 40, 'u_i': 2.2476},
        {'id': 3, 'e_m': 7.449156, 'e_o_k': [4.274106, 3.419285, 2.735428], 'p_i': 80, 'u_i': 1.3199},
        {'id': 4, 'e_m': 2.409551, 'e_o_k': [1.382529, 1.106023, 0.884819], 'p_i': 80, 'u_i': 3.4892},
        {'id': 5, 'e_m': 0.229718, 'e_o_k': [0.131806, 0.105444, 0.084356], 'p_i': 10, 'u_i': 1.4050},
        {'id': 6, 'e_m': 0.659831, 'e_o_k': [0.378592, 0.302873, 0.242299], 'p_i': 20, 'u_i': 3.5798},
        {'id': 7, 'e_m': 1.081708, 'e_o_k': [0.620652, 0.496522, 0.397217], 'p_i': 20, 'u_i': 2.2529},
    ]
    B_BUDGET = 88.320006
    return processors, tasks, B_BUDGET

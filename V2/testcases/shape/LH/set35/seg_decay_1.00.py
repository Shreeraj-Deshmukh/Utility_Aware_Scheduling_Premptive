"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320006, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.320006, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.153313, 'e_o_k': [0.053660, 0.053660, 0.053660, 0.053660], 'p_i': 10, 'u_i': 2.6246},
        {'id': 1, 'e_m': 0.148369, 'e_o_k': [0.034619, 0.034619, 0.034619, 0.034619, 0.034619, 0.034619], 'p_i': 20, 'u_i': 2.3478},
        {'id': 2, 'e_m': 2.270223, 'e_o_k': [1.059438, 1.059438, 1.059438], 'p_i': 40, 'u_i': 2.5491},
        {'id': 3, 'e_m': 7.275677, 'e_o_k': [2.037190, 2.037190, 2.037190, 2.037190, 2.037190], 'p_i': 80, 'u_i': 2.9783},
        {'id': 4, 'e_m': 2.680502, 'e_o_k': [1.876351, 1.876351], 'p_i': 20, 'u_i': 1.6186},
        {'id': 5, 'e_m': 1.468106, 'e_o_k': [0.342558, 0.342558, 0.342558, 0.342558, 0.342558, 0.342558], 'p_i': 40, 'u_i': 2.1935},
        {'id': 6, 'e_m': 0.569881, 'e_o_k': [0.265945, 0.265945, 0.265945], 'p_i': 20, 'u_i': 1.0173},
        {'id': 7, 'e_m': 0.303269, 'e_o_k': [0.212288, 0.212288], 'p_i': 10, 'u_i': 4.7591},
    ]
    B_BUDGET = 88.320006
    return processors, tasks, B_BUDGET

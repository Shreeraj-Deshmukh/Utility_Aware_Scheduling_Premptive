"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319993, "H": 80, "J": 20, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319993, "H": 80, "J": 20, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.361229, 'e_o_k': [0.316075, 0.189645], 'p_i': 10, 'u_i': 1.0216},
        {'id': 1, 'e_m': 1.543444, 'e_o_k': [1.102460, 0.661476, 0.396886], 'p_i': 20, 'u_i': 4.0085},
        {'id': 2, 'e_m': 5.606336, 'e_o_k': [4.004526, 2.402715, 1.441629], 'p_i': 40, 'u_i': 1.9931},
        {'id': 3, 'e_m': 2.233033, 'e_o_k': [1.595023, 0.957014, 0.574208], 'p_i': 80, 'u_i': 2.4773},
        {'id': 4, 'e_m': 0.084420, 'e_o_k': [0.054314, 0.032589, 0.019553, 0.011732], 'p_i': 80, 'u_i': 3.1022},
        {'id': 5, 'e_m': 0.994040, 'e_o_k': [0.583905, 0.350343, 0.210206, 0.126124, 0.075674, 0.045404], 'p_i': 40, 'u_i': 1.9821},
        {'id': 6, 'e_m': 3.955611, 'e_o_k': [2.825436, 1.695262, 1.017157], 'p_i': 80, 'u_i': 1.2190},
        {'id': 7, 'e_m': 3.462576, 'e_o_k': [2.227760, 1.336656, 0.801994, 0.481196], 'p_i': 80, 'u_i': 2.8489},
    ]
    B_BUDGET = 88.319993
    return processors, tasks, B_BUDGET

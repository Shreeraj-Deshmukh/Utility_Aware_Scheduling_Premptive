"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200001, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200001, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.448948, 'e_o_k': [0.147251, 0.117801, 0.094241, 0.075392], 'p_i': 10, 'u_i': 4.6704},
        {'id': 1, 'e_m': 0.187243, 'e_o_k': [0.031207, 0.024966], 'p_i': 20, 'u_i': 1.7142},
        {'id': 2, 'e_m': 18.529290, 'e_o_k': [2.278191, 1.822553, 1.458043], 'p_i': 40, 'u_i': 2.7421},
        {'id': 3, 'e_m': 22.855562, 'e_o_k': [1.858538, 1.486831, 1.189465, 0.951572, 0.761257, 0.609006], 'p_i': 80, 'u_i': 1.9194},
        {'id': 4, 'e_m': 9.469729, 'e_o_k': [1.578288, 1.262631], 'p_i': 20, 'u_i': 4.0448},
        {'id': 5, 'e_m': 7.767516, 'e_o_k': [0.955022, 0.764018, 0.611214], 'p_i': 20, 'u_i': 1.1256},
        {'id': 6, 'e_m': 0.257086, 'e_o_k': [0.026127, 0.020901, 0.016721, 0.013377], 'p_i': 10, 'u_i': 3.9028},
        {'id': 7, 'e_m': 4.184907, 'e_o_k': [0.373475, 0.298780, 0.239024, 0.191219, 0.152975], 'p_i': 20, 'u_i': 2.5194},
    ]
    B_BUDGET = 239.200001
    return processors, tasks, B_BUDGET

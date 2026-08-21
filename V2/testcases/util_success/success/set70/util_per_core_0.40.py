"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679995, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679995, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.121191, 'e_o_k': [0.186865, 0.149492], 'p_i': 10, 'u_i': 2.9208},
        {'id': 1, 'e_m': 4.546458, 'e_o_k': [0.369703, 0.295762, 0.236610, 0.189288, 0.151430, 0.121144], 'p_i': 20, 'u_i': 4.6964},
        {'id': 2, 'e_m': 10.573229, 'e_o_k': [1.299987, 1.039990, 0.831992], 'p_i': 40, 'u_i': 4.6519},
        {'id': 3, 'e_m': 3.680258, 'e_o_k': [0.613376, 0.490701], 'p_i': 80, 'u_i': 4.9020},
        {'id': 4, 'e_m': 0.623936, 'e_o_k': [0.050736, 0.040589, 0.032471, 0.025977, 0.020782, 0.016625], 'p_i': 80, 'u_i': 1.1409},
        {'id': 5, 'e_m': 3.160733, 'e_o_k': [0.282074, 0.225659, 0.180527, 0.144422, 0.115537], 'p_i': 40, 'u_i': 1.3844},
        {'id': 6, 'e_m': 4.750875, 'e_o_k': [0.423983, 0.339187, 0.271349, 0.217079, 0.173664], 'p_i': 80, 'u_i': 3.8571},
        {'id': 7, 'e_m': 0.080412, 'e_o_k': [0.013402, 0.010722], 'p_i': 20, 'u_i': 3.6185},
    ]
    B_BUDGET = 95.679995
    return processors, tasks, B_BUDGET

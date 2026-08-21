"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599995, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599995, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.401489, 'e_o_k': [0.233581, 0.186865], 'p_i': 10, 'u_i': 2.9208},
        {'id': 1, 'e_m': 5.683073, 'e_o_k': [0.462129, 0.369703, 0.295762, 0.236610, 0.189288, 0.151430], 'p_i': 20, 'u_i': 4.6964},
        {'id': 2, 'e_m': 13.216536, 'e_o_k': [1.624984, 1.299987, 1.039990], 'p_i': 40, 'u_i': 4.6519},
        {'id': 3, 'e_m': 4.600323, 'e_o_k': [0.766721, 0.613376], 'p_i': 80, 'u_i': 4.9020},
        {'id': 4, 'e_m': 0.779920, 'e_o_k': [0.063420, 0.050736, 0.040589, 0.032471, 0.025977, 0.020782], 'p_i': 80, 'u_i': 1.1409},
        {'id': 5, 'e_m': 3.950916, 'e_o_k': [0.352592, 0.282074, 0.225659, 0.180527, 0.144422], 'p_i': 40, 'u_i': 1.3844},
        {'id': 6, 'e_m': 5.938594, 'e_o_k': [0.529979, 0.423983, 0.339187, 0.271349, 0.217079], 'p_i': 80, 'u_i': 3.8571},
        {'id': 7, 'e_m': 0.100515, 'e_o_k': [0.016752, 0.013402], 'p_i': 20, 'u_i': 3.6185},
    ]
    B_BUDGET = 119.599995
    return processors, tasks, B_BUDGET

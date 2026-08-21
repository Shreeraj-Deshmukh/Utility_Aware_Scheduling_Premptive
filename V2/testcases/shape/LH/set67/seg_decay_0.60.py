"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32001, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.32001, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.811128, 'e_o_k': [1.099748, 0.659849, 0.395909, 0.237546, 0.142527], 'p_i': 10, 'u_i': 3.4311},
        {'id': 1, 'e_m': 0.050717, 'e_o_k': [0.032630, 0.019578, 0.011747, 0.007048], 'p_i': 20, 'u_i': 3.8774},
        {'id': 2, 'e_m': 2.544213, 'e_o_k': [2.226187, 1.335712], 'p_i': 40, 'u_i': 3.3220},
        {'id': 3, 'e_m': 1.179546, 'e_o_k': [1.032103, 0.619262], 'p_i': 80, 'u_i': 2.5309},
        {'id': 4, 'e_m': 1.744117, 'e_o_k': [1.245798, 0.747479, 0.448487], 'p_i': 40, 'u_i': 3.7128},
        {'id': 5, 'e_m': 0.579467, 'e_o_k': [0.507034, 0.304220], 'p_i': 20, 'u_i': 4.9574},
        {'id': 6, 'e_m': 4.549467, 'e_o_k': [3.249619, 1.949771, 1.169863], 'p_i': 80, 'u_i': 3.9330},
        {'id': 7, 'e_m': 0.342286, 'e_o_k': [0.244490, 0.146694, 0.088016], 'p_i': 40, 'u_i': 3.5882},
    ]
    B_BUDGET = 88.320010
    return processors, tasks, B_BUDGET

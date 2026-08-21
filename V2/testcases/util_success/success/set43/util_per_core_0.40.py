"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679995, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679995, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.051640, 'e_o_k': [0.005248, 0.004198, 0.003359, 0.002687], 'p_i': 10, 'u_i': 4.0574},
        {'id': 1, 'e_m': 2.466332, 'e_o_k': [0.220103, 0.176083, 0.140866, 0.112693, 0.090154], 'p_i': 20, 'u_i': 2.7090},
        {'id': 2, 'e_m': 3.747707, 'e_o_k': [0.380865, 0.304692, 0.243753, 0.195003], 'p_i': 40, 'u_i': 3.6072},
        {'id': 3, 'e_m': 4.153790, 'e_o_k': [0.337772, 0.270218, 0.216174, 0.172939, 0.138352, 0.110681], 'p_i': 80, 'u_i': 4.5999},
        {'id': 4, 'e_m': 0.386369, 'e_o_k': [0.039265, 0.031412, 0.025130, 0.020104], 'p_i': 20, 'u_i': 4.5815},
        {'id': 5, 'e_m': 4.381916, 'e_o_k': [0.356323, 0.285058, 0.228047, 0.182437, 0.145950, 0.116760], 'p_i': 20, 'u_i': 4.3913},
        {'id': 6, 'e_m': 1.777815, 'e_o_k': [0.296303, 0.237042], 'p_i': 80, 'u_i': 2.4366},
        {'id': 7, 'e_m': 10.610695, 'e_o_k': [0.862826, 0.690261, 0.552209, 0.441767, 0.353414, 0.282731], 'p_i': 40, 'u_i': 1.2704},
    ]
    B_BUDGET = 95.679995
    return processors, tasks, B_BUDGET

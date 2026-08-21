"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.330983, 'e_o_k': [3.368542, 2.694834], 'p_i': 10, 'u_i': 4.6007},
        {'id': 1, 'e_m': 0.177947, 'e_o_k': [0.074109, 0.059287, 0.047430, 0.037944, 0.030355], 'p_i': 20, 'u_i': 4.4928},
        {'id': 2, 'e_m': 2.652215, 'e_o_k': [1.006457, 0.805165, 0.644132, 0.515306, 0.412245, 0.329796], 'p_i': 40, 'u_i': 4.0915},
        {'id': 3, 'e_m': 1.218905, 'e_o_k': [0.462547, 0.370038, 0.296030, 0.236824, 0.189459, 0.151568], 'p_i': 80, 'u_i': 4.3648},
        {'id': 4, 'e_m': 3.803019, 'e_o_k': [2.957903, 2.366323], 'p_i': 80, 'u_i': 3.7706},
        {'id': 5, 'e_m': 4.578499, 'e_o_k': [1.737439, 1.389951, 1.111961, 0.889569, 0.711655, 0.569324], 'p_i': 20, 'u_i': 4.9150},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET

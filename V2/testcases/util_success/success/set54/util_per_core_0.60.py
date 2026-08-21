"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520002, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520002, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.342909, 'e_o_k': [0.057151, 0.045721], 'p_i': 10, 'u_i': 1.0785},
        {'id': 1, 'e_m': 1.857876, 'e_o_k': [0.165803, 0.132642, 0.106114, 0.084891, 0.067913], 'p_i': 20, 'u_i': 3.4086},
        {'id': 2, 'e_m': 9.450445, 'e_o_k': [1.161940, 0.929552, 0.743642], 'p_i': 40, 'u_i': 3.2935},
        {'id': 3, 'e_m': 8.848639, 'e_o_k': [0.899252, 0.719402, 0.575521, 0.460417], 'p_i': 80, 'u_i': 4.9988},
        {'id': 4, 'e_m': 0.374998, 'e_o_k': [0.033466, 0.026773, 0.021418, 0.017135, 0.013708], 'p_i': 40, 'u_i': 2.8879},
        {'id': 5, 'e_m': 31.736170, 'e_o_k': [3.225221, 2.580176, 2.064141, 1.651313], 'p_i': 80, 'u_i': 4.7528},
        {'id': 6, 'e_m': 7.746119, 'e_o_k': [0.691289, 0.553031, 0.442425, 0.353940, 0.283152], 'p_i': 80, 'u_i': 4.9914},
        {'id': 7, 'e_m': 8.921707, 'e_o_k': [0.796202, 0.636961, 0.509569, 0.407655, 0.326124], 'p_i': 40, 'u_i': 2.2427},
    ]
    B_BUDGET = 143.520002
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.263419, 'e_o_k': [0.032388, 0.025910, 0.020728], 'p_i': 10, 'u_i': 1.1011},
        {'id': 1, 'e_m': 1.008508, 'e_o_k': [0.090003, 0.072002, 0.057602, 0.046081, 0.036865], 'p_i': 20, 'u_i': 1.8110},
        {'id': 2, 'e_m': 18.402702, 'e_o_k': [1.870193, 1.496155, 1.196924, 0.957539], 'p_i': 40, 'u_i': 2.7882},
        {'id': 3, 'e_m': 22.421718, 'e_o_k': [2.278630, 1.822904, 1.458323, 1.166658], 'p_i': 80, 'u_i': 1.5962},
        {'id': 4, 'e_m': 9.887654, 'e_o_k': [0.804031, 0.643225, 0.514580, 0.411664, 0.329331, 0.263465], 'p_i': 20, 'u_i': 4.3893},
        {'id': 5, 'e_m': 1.730277, 'e_o_k': [0.154415, 0.123532, 0.098826, 0.079061, 0.063249], 'p_i': 20, 'u_i': 1.3904},
        {'id': 6, 'e_m': 6.571273, 'e_o_k': [1.095212, 0.876170], 'p_i': 20, 'u_i': 3.7533},
        {'id': 7, 'e_m': 10.937337, 'e_o_k': [1.344755, 1.075804, 0.860643], 'p_i': 40, 'u_i': 3.0100},
    ]
    B_BUDGET = 239.200001
    return processors, tasks, B_BUDGET

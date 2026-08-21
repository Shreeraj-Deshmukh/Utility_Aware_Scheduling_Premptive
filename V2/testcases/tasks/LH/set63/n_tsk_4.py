"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.664276, 'e_o_k': [0.693118, 0.554494, 0.443596, 0.354876, 0.283901], 'p_i': 10, 'u_i': 4.0082},
        {'id': 1, 'e_m': 0.037732, 'e_o_k': [0.014318, 0.011455, 0.009164, 0.007331, 0.005865, 0.004692], 'p_i': 20, 'u_i': 3.2625},
        {'id': 2, 'e_m': 4.249107, 'e_o_k': [2.438012, 1.950410, 1.560328], 'p_i': 40, 'u_i': 3.4071},
        {'id': 3, 'e_m': 10.036655, 'e_o_k': [4.179949, 3.343959, 2.675167, 2.140134, 1.712107], 'p_i': 80, 'u_i': 2.2919},
    ]
    B_BUDGET = 88.320001
    return processors, tasks, B_BUDGET

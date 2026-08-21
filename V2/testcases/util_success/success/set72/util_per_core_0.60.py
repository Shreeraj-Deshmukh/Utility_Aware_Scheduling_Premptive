"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519976, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519976, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.345659, 'e_o_k': [0.028108, 0.022486, 0.017989, 0.014391, 0.011513, 0.009210], 'p_i': 10, 'u_i': 2.8095},
        {'id': 1, 'e_m': 2.581056, 'e_o_k': [0.317343, 0.253874, 0.203100], 'p_i': 20, 'u_i': 2.2645},
        {'id': 2, 'e_m': 7.120735, 'e_o_k': [0.635477, 0.508382, 0.406705, 0.325364, 0.260291], 'p_i': 40, 'u_i': 4.9290},
        {'id': 3, 'e_m': 8.233489, 'e_o_k': [1.012314, 0.809851, 0.647881], 'p_i': 80, 'u_i': 2.8289},
        {'id': 4, 'e_m': 3.941903, 'e_o_k': [0.351788, 0.281430, 0.225144, 0.180116, 0.144092], 'p_i': 20, 'u_i': 2.4039},
        {'id': 5, 'e_m': 3.040207, 'e_o_k': [0.271318, 0.217054, 0.173643, 0.138915, 0.111132], 'p_i': 10, 'u_i': 2.7593},
        {'id': 6, 'e_m': 18.488455, 'e_o_k': [1.649969, 1.319975, 1.055980, 0.844784, 0.675827], 'p_i': 80, 'u_i': 4.9185},
        {'id': 7, 'e_m': 1.857817, 'e_o_k': [0.228420, 0.182736, 0.146189], 'p_i': 80, 'u_i': 1.9966},
    ]
    B_BUDGET = 143.519976
    return processors, tasks, B_BUDGET

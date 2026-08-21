"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119998, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119998, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.826098, 'e_o_k': [0.347471, 0.277977, 0.222381], 'p_i': 10, 'u_i': 2.8354},
        {'id': 1, 'e_m': 2.936026, 'e_o_k': [0.238748, 0.190998, 0.152799, 0.122239, 0.097791, 0.078233], 'p_i': 20, 'u_i': 4.4570},
        {'id': 2, 'e_m': 13.034360, 'e_o_k': [2.172393, 1.737915], 'p_i': 40, 'u_i': 1.7617},
        {'id': 3, 'e_m': 6.629470, 'e_o_k': [0.539086, 0.431269, 0.345015, 0.276012, 0.220810, 0.176648], 'p_i': 80, 'u_i': 3.9855},
        {'id': 4, 'e_m': 15.449703, 'e_o_k': [1.570092, 1.256073, 1.004859, 0.803887], 'p_i': 40, 'u_i': 4.2888},
        {'id': 5, 'e_m': 14.520773, 'e_o_k': [1.180781, 0.944625, 0.755700, 0.604560, 0.483648, 0.386918], 'p_i': 40, 'u_i': 4.5823},
        {'id': 6, 'e_m': 23.700184, 'e_o_k': [2.408555, 1.926844, 1.541475, 1.233180], 'p_i': 80, 'u_i': 2.7900},
        {'id': 7, 'e_m': 12.653894, 'e_o_k': [1.028973, 0.823178, 0.658542, 0.526834, 0.421467, 0.337174], 'p_i': 40, 'u_i': 1.8324},
    ]
    B_BUDGET = 263.119998
    return processors, tasks, B_BUDGET

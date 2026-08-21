"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.157215, 'e_o_k': [0.023384, 0.018707, 0.014966, 0.011973, 0.009578], 'p_i': 10, 'u_i': 4.4619},
        {'id': 1, 'e_m': 1.013271, 'e_o_k': [0.281464, 0.225171], 'p_i': 20, 'u_i': 2.5387},
        {'id': 2, 'e_m': 3.436333, 'e_o_k': [0.582035, 0.465628, 0.372502, 0.298002], 'p_i': 40, 'u_i': 1.0056},
        {'id': 3, 'e_m': 7.676692, 'e_o_k': [1.300253, 1.040202, 0.832162, 0.665729], 'p_i': 80, 'u_i': 1.2987},
        {'id': 4, 'e_m': 1.838053, 'e_o_k': [0.273390, 0.218712, 0.174969, 0.139975, 0.111980], 'p_i': 20, 'u_i': 3.5939},
        {'id': 5, 'e_m': 4.598453, 'e_o_k': [1.277348, 1.021879], 'p_i': 10, 'u_i': 1.8409},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET

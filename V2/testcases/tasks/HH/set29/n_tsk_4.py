"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.63999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.63999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.235946, 'e_o_k': [0.469014, 0.375211, 0.300169, 0.240135, 0.192108, 0.153687], 'p_i': 10, 'u_i': 3.2393},
        {'id': 1, 'e_m': 2.190617, 'e_o_k': [0.831291, 0.665033, 0.532026, 0.425621, 0.340497, 0.272397], 'p_i': 20, 'u_i': 4.1852},
        {'id': 2, 'e_m': 10.772796, 'e_o_k': [5.109050, 4.087240, 3.269792, 2.615833], 'p_i': 40, 'u_i': 4.0538},
        {'id': 3, 'e_m': 23.804367, 'e_o_k': [11.289334, 9.031467, 7.225174, 5.780139], 'p_i': 80, 'u_i': 4.3622},
    ]
    B_BUDGET = 176.639990
    return processors, tasks, B_BUDGET

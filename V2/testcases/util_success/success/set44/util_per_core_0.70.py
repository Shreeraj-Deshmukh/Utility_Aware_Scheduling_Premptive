"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439982, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439982, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.840480, 'e_o_k': [0.491919, 0.393535, 0.314828, 0.251862], 'p_i': 10, 'u_i': 4.4798},
        {'id': 1, 'e_m': 4.485615, 'e_o_k': [0.747603, 0.598082], 'p_i': 20, 'u_i': 2.0952},
        {'id': 2, 'e_m': 4.538328, 'e_o_k': [0.557991, 0.446393, 0.357114], 'p_i': 40, 'u_i': 3.6547},
        {'id': 3, 'e_m': 12.513951, 'e_o_k': [1.538601, 1.230880, 0.984704], 'p_i': 80, 'u_i': 2.4225},
        {'id': 4, 'e_m': 0.971782, 'e_o_k': [0.079022, 0.063218, 0.050574, 0.040459, 0.032367, 0.025894], 'p_i': 20, 'u_i': 3.0832},
        {'id': 5, 'e_m': 3.468687, 'e_o_k': [0.309557, 0.247645, 0.198116, 0.158493, 0.126794], 'p_i': 20, 'u_i': 3.4868},
        {'id': 6, 'e_m': 2.232751, 'e_o_k': [0.372125, 0.297700], 'p_i': 20, 'u_i': 3.8765},
        {'id': 7, 'e_m': 1.762552, 'e_o_k': [0.157296, 0.125837, 0.100669, 0.080535, 0.064428], 'p_i': 20, 'u_i': 3.4288},
    ]
    B_BUDGET = 167.439982
    return processors, tasks, B_BUDGET

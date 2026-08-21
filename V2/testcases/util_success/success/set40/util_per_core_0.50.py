"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599982, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599982, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.561503, 'e_o_k': [0.191988, 0.153590, 0.122872], 'p_i': 10, 'u_i': 1.9682},
        {'id': 1, 'e_m': 1.527235, 'e_o_k': [0.254539, 0.203631], 'p_i': 20, 'u_i': 4.1538},
        {'id': 2, 'e_m': 7.720787, 'e_o_k': [0.784633, 0.627706, 0.502165, 0.401732], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 10.117046, 'e_o_k': [1.686174, 1.348939], 'p_i': 80, 'u_i': 4.6912},
        {'id': 4, 'e_m': 0.927604, 'e_o_k': [0.082782, 0.066226, 0.052981, 0.042385, 0.033908], 'p_i': 40, 'u_i': 2.4684},
        {'id': 5, 'e_m': 8.121803, 'e_o_k': [0.660438, 0.528350, 0.422680, 0.338144, 0.270515, 0.216412], 'p_i': 40, 'u_i': 3.0218},
        {'id': 6, 'e_m': 0.945187, 'e_o_k': [0.084351, 0.067481, 0.053985, 0.043188, 0.034550], 'p_i': 20, 'u_i': 2.6468},
        {'id': 7, 'e_m': 13.960855, 'e_o_k': [1.135250, 0.908200, 0.726560, 0.581248, 0.464999, 0.371999], 'p_i': 80, 'u_i': 1.1768},
    ]
    B_BUDGET = 119.599982
    return processors, tasks, B_BUDGET

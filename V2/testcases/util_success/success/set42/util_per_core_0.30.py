"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760003, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760003, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.079365, 'e_o_k': [0.132709, 0.106167, 0.084934], 'p_i': 10, 'u_i': 3.9504},
        {'id': 1, 'e_m': 1.559520, 'e_o_k': [0.139177, 0.111341, 0.089073, 0.071258, 0.057007], 'p_i': 20, 'u_i': 2.1226},
        {'id': 2, 'e_m': 0.220745, 'e_o_k': [0.036791, 0.029433], 'p_i': 40, 'u_i': 2.4300},
        {'id': 3, 'e_m': 0.986276, 'e_o_k': [0.088018, 0.070415, 0.056332, 0.045065, 0.036052], 'p_i': 80, 'u_i': 4.3958},
        {'id': 4, 'e_m': 6.720338, 'e_o_k': [0.546476, 0.437180, 0.349744, 0.279796, 0.223836, 0.179069], 'p_i': 80, 'u_i': 4.7703},
        {'id': 5, 'e_m': 0.036686, 'e_o_k': [0.002983, 0.002387, 0.001909, 0.001527, 0.001222, 0.000978], 'p_i': 80, 'u_i': 1.8568},
        {'id': 6, 'e_m': 1.500686, 'e_o_k': [0.184511, 0.147608, 0.118087], 'p_i': 20, 'u_i': 1.8128},
        {'id': 7, 'e_m': 9.469732, 'e_o_k': [1.578289, 1.262631], 'p_i': 40, 'u_i': 1.5689},
    ]
    B_BUDGET = 71.760003
    return processors, tasks, B_BUDGET

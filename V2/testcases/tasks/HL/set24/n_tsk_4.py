"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.582593, 'e_o_k': [0.078958, 0.063166, 0.050533, 0.040426, 0.032341, 0.025873], 'p_i': 10, 'u_i': 1.4017},
        {'id': 1, 'e_m': 4.519562, 'e_o_k': [0.612526, 0.490021, 0.392017, 0.313613, 0.250891, 0.200713], 'p_i': 20, 'u_i': 2.4636},
        {'id': 2, 'e_m': 12.596412, 'e_o_k': [2.133539, 1.706831, 1.365465, 1.092372], 'p_i': 40, 'u_i': 2.5536},
        {'id': 3, 'e_m': 16.068185, 'e_o_k': [4.463385, 3.570708], 'p_i': 80, 'u_i': 3.8458},
    ]
    B_BUDGET = 110.400009
    return processors, tasks, B_BUDGET

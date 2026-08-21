"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.462267, 'e_o_k': [0.078297, 0.062638, 0.050110, 0.040088], 'p_i': 10, 'u_i': 4.2108},
        {'id': 1, 'e_m': 3.806267, 'e_o_k': [0.779973, 0.623978, 0.499183], 'p_i': 20, 'u_i': 3.3354},
        {'id': 2, 'e_m': 18.908949, 'e_o_k': [3.202735, 2.562188, 2.049751, 1.639800], 'p_i': 40, 'u_i': 1.0371},
        {'id': 3, 'e_m': 7.258899, 'e_o_k': [1.079679, 0.863743, 0.690995, 0.552796, 0.442237], 'p_i': 80, 'u_i': 1.4152},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET

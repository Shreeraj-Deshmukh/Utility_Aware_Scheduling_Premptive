"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.812825, 'e_o_k': [0.307050, 0.245640, 0.196512, 0.157210], 'p_i': 10, 'u_i': 4.1031},
        {'id': 1, 'e_m': 4.611385, 'e_o_k': [0.944956, 0.755965, 0.604772], 'p_i': 20, 'u_i': 2.8661},
        {'id': 2, 'e_m': 5.752200, 'e_o_k': [0.779583, 0.623666, 0.498933, 0.399146, 0.319317, 0.255454], 'p_i': 40, 'u_i': 2.5404},
        {'id': 3, 'e_m': 19.547463, 'e_o_k': [4.005628, 3.204502, 2.563602], 'p_i': 80, 'u_i': 1.0986},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET

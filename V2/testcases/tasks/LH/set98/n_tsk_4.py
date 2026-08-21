"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319986, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319986, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.756013, 'e_o_k': [0.666368, 0.533094, 0.426476, 0.341180, 0.272944, 0.218355], 'p_i': 10, 'u_i': 4.8035},
        {'id': 1, 'e_m': 1.219078, 'e_o_k': [0.507707, 0.406166, 0.324933, 0.259946, 0.207957], 'p_i': 20, 'u_i': 1.9119},
        {'id': 2, 'e_m': 4.552641, 'e_o_k': [3.540943, 2.832754], 'p_i': 40, 'u_i': 3.5492},
        {'id': 3, 'e_m': 3.970302, 'e_o_k': [3.088012, 2.470410], 'p_i': 80, 'u_i': 2.1494},
    ]
    B_BUDGET = 88.319986
    return processors, tasks, B_BUDGET

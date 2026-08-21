"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200012, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200012, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.553947, 'e_o_k': [0.113514, 0.090811, 0.072649], 'p_i': 10, 'u_i': 1.6802},
        {'id': 1, 'e_m': 1.797565, 'e_o_k': [0.499324, 0.399459], 'p_i': 20, 'u_i': 4.8914},
        {'id': 2, 'e_m': 2.095061, 'e_o_k': [0.283939, 0.227151, 0.181721, 0.145377, 0.116301, 0.093041], 'p_i': 40, 'u_i': 2.7135},
        {'id': 3, 'e_m': 12.004113, 'e_o_k': [1.626891, 1.301513, 1.041210, 0.832968, 0.666375, 0.533100], 'p_i': 80, 'u_i': 1.9259},
        {'id': 4, 'e_m': 1.675111, 'e_o_k': [0.283725, 0.226980, 0.181584, 0.145267], 'p_i': 40, 'u_i': 2.2208},
        {'id': 5, 'e_m': 0.416855, 'e_o_k': [0.062002, 0.049602, 0.039682, 0.031745, 0.025396], 'p_i': 40, 'u_i': 3.1305},
    ]
    B_BUDGET = 55.200012
    return processors, tasks, B_BUDGET

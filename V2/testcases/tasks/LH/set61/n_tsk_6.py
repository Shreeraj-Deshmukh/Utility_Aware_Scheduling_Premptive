"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.471759, 'e_o_k': [0.223734, 0.178987, 0.143190, 0.114552], 'p_i': 10, 'u_i': 2.3827},
        {'id': 1, 'e_m': 1.719041, 'e_o_k': [0.715926, 0.572741, 0.458193, 0.366554, 0.293243], 'p_i': 20, 'u_i': 2.9856},
        {'id': 2, 'e_m': 0.035190, 'e_o_k': [0.013354, 0.010683, 0.008547, 0.006837, 0.005470, 0.004376], 'p_i': 40, 'u_i': 4.8236},
        {'id': 3, 'e_m': 8.778294, 'e_o_k': [4.163147, 3.330518, 2.664414, 2.131531], 'p_i': 80, 'u_i': 2.2531},
        {'id': 4, 'e_m': 11.210409, 'e_o_k': [4.668780, 3.735024, 2.988019, 2.390416, 1.912332], 'p_i': 80, 'u_i': 4.0598},
        {'id': 5, 'e_m': 0.322670, 'e_o_k': [0.153028, 0.122422, 0.097938, 0.078350], 'p_i': 20, 'u_i': 4.5014},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET

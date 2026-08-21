"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359997, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359997, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.525048, 'e_o_k': [0.053359, 0.042687, 0.034149, 0.027320], 'p_i': 10, 'u_i': 4.2383},
        {'id': 1, 'e_m': 5.701457, 'e_o_k': [0.508816, 0.407053, 0.325642, 0.260514, 0.208411], 'p_i': 20, 'u_i': 1.1754},
        {'id': 2, 'e_m': 8.964537, 'e_o_k': [1.494090, 1.195272], 'p_i': 40, 'u_i': 2.9766},
        {'id': 3, 'e_m': 22.281305, 'e_o_k': [1.811842, 1.449473, 1.159579, 0.927663, 0.742130, 0.593704], 'p_i': 80, 'u_i': 4.8798},
        {'id': 4, 'e_m': 23.790266, 'e_o_k': [1.934545, 1.547636, 1.238109, 0.990487, 0.792390, 0.633912], 'p_i': 80, 'u_i': 3.7063},
        {'id': 5, 'e_m': 3.131990, 'e_o_k': [0.279509, 0.223607, 0.178886, 0.143109, 0.114487], 'p_i': 10, 'u_i': 2.9881},
        {'id': 6, 'e_m': 1.036254, 'e_o_k': [0.092479, 0.073983, 0.059186, 0.047349, 0.037879], 'p_i': 20, 'u_i': 3.8057},
        {'id': 7, 'e_m': 7.792198, 'e_o_k': [1.298700, 1.038960], 'p_i': 80, 'u_i': 1.4079},
    ]
    B_BUDGET = 191.359997
    return processors, tasks, B_BUDGET

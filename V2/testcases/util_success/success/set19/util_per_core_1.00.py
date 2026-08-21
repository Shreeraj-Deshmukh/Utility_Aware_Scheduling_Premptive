"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200002, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200002, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.656311, 'e_o_k': [0.066698, 0.053359, 0.042687, 0.034149], 'p_i': 10, 'u_i': 4.2383},
        {'id': 1, 'e_m': 7.126822, 'e_o_k': [0.636020, 0.508816, 0.407053, 0.325642, 0.260514], 'p_i': 20, 'u_i': 1.1754},
        {'id': 2, 'e_m': 11.205671, 'e_o_k': [1.867612, 1.494090], 'p_i': 40, 'u_i': 2.9766},
        {'id': 3, 'e_m': 27.851631, 'e_o_k': [2.264802, 1.811842, 1.449473, 1.159579, 0.927663, 0.742130], 'p_i': 80, 'u_i': 4.8798},
        {'id': 4, 'e_m': 29.737832, 'e_o_k': [2.418182, 1.934545, 1.547636, 1.238109, 0.990487, 0.792390], 'p_i': 80, 'u_i': 3.7063},
        {'id': 5, 'e_m': 3.914988, 'e_o_k': [0.349386, 0.279509, 0.223607, 0.178886, 0.143109], 'p_i': 10, 'u_i': 2.9881},
        {'id': 6, 'e_m': 1.295318, 'e_o_k': [0.115598, 0.092479, 0.073983, 0.059186, 0.047349], 'p_i': 20, 'u_i': 3.8057},
        {'id': 7, 'e_m': 9.740248, 'e_o_k': [1.623375, 1.298700], 'p_i': 80, 'u_i': 1.4079},
    ]
    B_BUDGET = 239.200002
    return processors, tasks, B_BUDGET

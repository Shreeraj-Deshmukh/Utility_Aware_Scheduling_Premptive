"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120007, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120007, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.264907, 'e_o_k': [0.278472, 0.222778, 0.178222], 'p_i': 10, 'u_i': 2.3179},
        {'id': 1, 'e_m': 3.583493, 'e_o_k': [0.291398, 0.233118, 0.186495, 0.149196, 0.119357, 0.095485], 'p_i': 20, 'u_i': 3.7671},
        {'id': 2, 'e_m': 3.599541, 'e_o_k': [0.292703, 0.234162, 0.187330, 0.149864, 0.119891, 0.095913], 'p_i': 40, 'u_i': 1.5472},
        {'id': 3, 'e_m': 35.846976, 'e_o_k': [4.407415, 3.525932, 2.820746], 'p_i': 80, 'u_i': 4.7454},
        {'id': 4, 'e_m': 8.558688, 'e_o_k': [0.869785, 0.695828, 0.556663, 0.445330], 'p_i': 20, 'u_i': 1.0701},
        {'id': 5, 'e_m': 3.335452, 'e_o_k': [0.338969, 0.271175, 0.216940, 0.173552], 'p_i': 20, 'u_i': 2.4073},
        {'id': 6, 'e_m': 13.630899, 'e_o_k': [1.108419, 0.886736, 0.709388, 0.567511, 0.454009, 0.363207], 'p_i': 80, 'u_i': 4.8034},
        {'id': 7, 'e_m': 9.823314, 'e_o_k': [0.876664, 0.701331, 0.561065, 0.448852, 0.359082], 'p_i': 20, 'u_i': 3.8619},
    ]
    B_BUDGET = 263.120007
    return processors, tasks, B_BUDGET

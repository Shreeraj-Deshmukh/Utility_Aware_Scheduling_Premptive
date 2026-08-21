"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.573701, 'e_o_k': [0.437139, 0.349711], 'p_i': 10, 'u_i': 3.6650},
        {'id': 1, 'e_m': 1.488704, 'e_o_k': [0.413529, 0.330823], 'p_i': 20, 'u_i': 4.7122},
        {'id': 2, 'e_m': 1.136090, 'e_o_k': [0.315581, 0.252464], 'p_i': 40, 'u_i': 2.7870},
        {'id': 3, 'e_m': 13.753139, 'e_o_k': [3.820317, 3.056253], 'p_i': 80, 'u_i': 1.7506},
        {'id': 4, 'e_m': 5.982379, 'e_o_k': [1.661772, 1.329418], 'p_i': 40, 'u_i': 4.5685},
        {'id': 5, 'e_m': 0.674012, 'e_o_k': [0.187225, 0.149780], 'p_i': 10, 'u_i': 2.7344},
        {'id': 6, 'e_m': 0.887834, 'e_o_k': [0.246621, 0.197296], 'p_i': 40, 'u_i': 1.1398},
        {'id': 7, 'e_m': 10.297741, 'e_o_k': [2.860484, 2.288387], 'p_i': 80, 'u_i': 4.8954},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET

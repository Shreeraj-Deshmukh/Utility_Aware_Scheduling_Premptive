"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399976, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399976, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.067561, 'e_o_k': [0.231515, 0.138909, 0.083345, 0.050007, 0.030004], 'p_i': 10, 'u_i': 4.6830},
        {'id': 1, 'e_m': 6.103602, 'e_o_k': [1.907376, 1.144425], 'p_i': 20, 'u_i': 2.4027},
        {'id': 2, 'e_m': 4.537756, 'e_o_k': [1.418049, 0.850829], 'p_i': 40, 'u_i': 2.7203},
        {'id': 3, 'e_m': 4.054946, 'e_o_k': [0.850678, 0.510407, 0.306244, 0.183747, 0.110248, 0.066149], 'p_i': 80, 'u_i': 2.4000},
        {'id': 4, 'e_m': 0.349178, 'e_o_k': [0.109118, 0.065471], 'p_i': 20, 'u_i': 2.9059},
        {'id': 5, 'e_m': 0.690991, 'e_o_k': [0.176273, 0.105764, 0.063458], 'p_i': 10, 'u_i': 3.1411},
        {'id': 6, 'e_m': 5.436589, 'e_o_k': [1.249216, 0.749530, 0.449718, 0.269831], 'p_i': 80, 'u_i': 3.1206},
        {'id': 7, 'e_m': 2.776704, 'e_o_k': [0.708343, 0.425006, 0.255003], 'p_i': 40, 'u_i': 4.7030},
    ]
    B_BUDGET = 110.399976
    return processors, tasks, B_BUDGET

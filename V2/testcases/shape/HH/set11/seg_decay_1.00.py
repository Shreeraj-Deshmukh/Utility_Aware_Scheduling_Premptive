"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639992, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.639992, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.067561, 'e_o_k': [0.298917, 0.298917, 0.298917, 0.298917, 0.298917], 'p_i': 10, 'u_i': 4.6830},
        {'id': 1, 'e_m': 6.103602, 'e_o_k': [4.272522, 4.272522], 'p_i': 20, 'u_i': 2.4027},
        {'id': 2, 'e_m': 4.537756, 'e_o_k': [3.176429, 3.176429], 'p_i': 40, 'u_i': 2.7203},
        {'id': 3, 'e_m': 4.054946, 'e_o_k': [0.946154, 0.946154, 0.946154, 0.946154, 0.946154, 0.946154], 'p_i': 80, 'u_i': 2.4000},
        {'id': 4, 'e_m': 0.349178, 'e_o_k': [0.244425, 0.244425], 'p_i': 20, 'u_i': 2.9059},
        {'id': 5, 'e_m': 0.690991, 'e_o_k': [0.322463, 0.322463, 0.322463], 'p_i': 10, 'u_i': 3.1411},
        {'id': 6, 'e_m': 5.436589, 'e_o_k': [1.902806, 1.902806, 1.902806, 1.902806], 'p_i': 80, 'u_i': 3.1206},
        {'id': 7, 'e_m': 2.776704, 'e_o_k': [1.295795, 1.295795, 1.295795], 'p_i': 40, 'u_i': 4.7030},
    ]
    B_BUDGET = 176.639992
    return processors, tasks, B_BUDGET

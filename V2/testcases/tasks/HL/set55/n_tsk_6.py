"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399993, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399993, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.098894, 'e_o_k': [0.860804, 0.688643], 'p_i': 10, 'u_i': 3.3617},
        {'id': 1, 'e_m': 2.272895, 'e_o_k': [0.384975, 0.307980, 0.246384, 0.197107], 'p_i': 20, 'u_i': 3.9677},
        {'id': 2, 'e_m': 2.581905, 'e_o_k': [0.349920, 0.279936, 0.223949, 0.179159, 0.143327, 0.114662], 'p_i': 40, 'u_i': 4.5134},
        {'id': 3, 'e_m': 13.579784, 'e_o_k': [2.782743, 2.226194, 1.780955], 'p_i': 80, 'u_i': 4.5874},
        {'id': 4, 'e_m': 6.350547, 'e_o_k': [1.301342, 1.041073, 0.832859], 'p_i': 80, 'u_i': 2.7347},
        {'id': 5, 'e_m': 5.023126, 'e_o_k': [1.029329, 0.823463, 0.658771], 'p_i': 80, 'u_i': 4.9671},
    ]
    B_BUDGET = 110.399993
    return processors, tasks, B_BUDGET

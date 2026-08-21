"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399997, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399997, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.914939, 'e_o_k': [0.433564, 0.346851, 0.277481, 0.221985, 0.177588], 'p_i': 10, 'u_i': 3.3568},
        {'id': 1, 'e_m': 2.637463, 'e_o_k': [0.446725, 0.357380, 0.285904, 0.228723], 'p_i': 20, 'u_i': 2.9125},
        {'id': 2, 'e_m': 0.336975, 'e_o_k': [0.045669, 0.036536, 0.029228, 0.023383, 0.018706, 0.014965], 'p_i': 40, 'u_i': 4.1129},
        {'id': 3, 'e_m': 8.908530, 'e_o_k': [1.207353, 0.965883, 0.772706, 0.618165, 0.494532, 0.395626], 'p_i': 80, 'u_i': 4.6267},
        {'id': 4, 'e_m': 5.781916, 'e_o_k': [1.606088, 1.284870], 'p_i': 80, 'u_i': 4.4310},
        {'id': 5, 'e_m': 7.383119, 'e_o_k': [1.098156, 0.878524, 0.702820, 0.562256, 0.449805], 'p_i': 40, 'u_i': 4.5357},
    ]
    B_BUDGET = 110.399997
    return processors, tasks, B_BUDGET

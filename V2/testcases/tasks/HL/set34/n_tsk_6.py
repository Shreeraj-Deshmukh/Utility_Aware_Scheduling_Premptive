"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399993, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399993, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.305521, 'e_o_k': [0.062607, 0.050085, 0.040068], 'p_i': 10, 'u_i': 2.4499},
        {'id': 1, 'e_m': 1.667370, 'e_o_k': [0.463158, 0.370527], 'p_i': 20, 'u_i': 1.6318},
        {'id': 2, 'e_m': 15.422385, 'e_o_k': [2.612193, 2.089754, 1.671803, 1.337443], 'p_i': 40, 'u_i': 3.2685},
        {'id': 3, 'e_m': 9.092490, 'e_o_k': [1.863215, 1.490572, 1.192458], 'p_i': 80, 'u_i': 2.9234},
        {'id': 4, 'e_m': 11.462298, 'e_o_k': [2.348832, 1.879065, 1.503252], 'p_i': 80, 'u_i': 3.7707},
        {'id': 5, 'e_m': 0.871698, 'e_o_k': [0.178627, 0.142901, 0.114321], 'p_i': 20, 'u_i': 1.9627},
    ]
    B_BUDGET = 110.399993
    return processors, tasks, B_BUDGET

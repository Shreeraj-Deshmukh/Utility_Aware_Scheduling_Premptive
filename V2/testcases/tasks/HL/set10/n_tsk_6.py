"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.613560, 'e_o_k': [0.091260, 0.073008, 0.058406, 0.046725, 0.037380], 'p_i': 10, 'u_i': 4.4970},
        {'id': 1, 'e_m': 0.560926, 'e_o_k': [0.114944, 0.091955, 0.073564], 'p_i': 20, 'u_i': 1.4275},
        {'id': 2, 'e_m': 10.590332, 'e_o_k': [1.435284, 1.148228, 0.918582, 0.734866, 0.587893, 0.470314], 'p_i': 40, 'u_i': 3.5743},
        {'id': 3, 'e_m': 25.380665, 'e_o_k': [4.298893, 3.439114, 2.751292, 2.201033], 'p_i': 80, 'u_i': 4.9867},
        {'id': 4, 'e_m': 1.454899, 'e_o_k': [0.197179, 0.157743, 0.126195, 0.100956, 0.080765, 0.064612], 'p_i': 20, 'u_i': 3.7777},
        {'id': 5, 'e_m': 1.116723, 'e_o_k': [0.166100, 0.132880, 0.106304, 0.085043, 0.068035], 'p_i': 20, 'u_i': 2.9102},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET

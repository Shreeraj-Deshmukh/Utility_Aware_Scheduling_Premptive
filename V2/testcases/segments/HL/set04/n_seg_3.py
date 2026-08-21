"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399985, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399985, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.929756, 'e_o_k': [0.190524, 0.152419, 0.121935], 'p_i': 10, 'u_i': 1.2748},
        {'id': 1, 'e_m': 0.056878, 'e_o_k': [0.011655, 0.009324, 0.007459], 'p_i': 20, 'u_i': 3.8825},
        {'id': 2, 'e_m': 2.623994, 'e_o_k': [0.537704, 0.430163, 0.344130], 'p_i': 40, 'u_i': 3.8582},
        {'id': 3, 'e_m': 4.474673, 'e_o_k': [0.916941, 0.733553, 0.586842], 'p_i': 80, 'u_i': 1.6137},
        {'id': 4, 'e_m': 2.349668, 'e_o_k': [0.481489, 0.385192, 0.308153], 'p_i': 20, 'u_i': 2.7253},
        {'id': 5, 'e_m': 10.542988, 'e_o_k': [2.160448, 1.728359, 1.382687], 'p_i': 40, 'u_i': 1.4714},
        {'id': 6, 'e_m': 0.342456, 'e_o_k': [0.070175, 0.056140, 0.044912], 'p_i': 10, 'u_i': 2.9160},
        {'id': 7, 'e_m': 3.346871, 'e_o_k': [0.685834, 0.548667, 0.438934], 'p_i': 20, 'u_i': 4.4871},
    ]
    B_BUDGET = 110.399985
    return processors, tasks, B_BUDGET

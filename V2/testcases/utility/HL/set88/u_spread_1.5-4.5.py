"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399989, "H": 80, "J": 29, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 110.399989, "H": 80, "J": 29, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.686544, 'e_o_k': [0.140685, 0.112548, 0.090039], 'p_i': 10, 'u_i': 3.4191},
        {'id': 1, 'e_m': 1.582739, 'e_o_k': [0.439650, 0.351720], 'p_i': 20, 'u_i': 1.5656},
        {'id': 2, 'e_m': 5.107137, 'e_o_k': [0.865030, 0.692024, 0.553619, 0.442895], 'p_i': 40, 'u_i': 2.9585},
        {'id': 3, 'e_m': 0.225789, 'e_o_k': [0.038243, 0.030595, 0.024476, 0.019581], 'p_i': 80, 'u_i': 2.6466},
        {'id': 4, 'e_m': 10.028404, 'e_o_k': [1.491612, 1.193289, 0.954632, 0.763705, 0.610964], 'p_i': 40, 'u_i': 2.9205},
        {'id': 5, 'e_m': 5.390837, 'e_o_k': [0.730608, 0.584487, 0.467589, 0.374071, 0.299257, 0.239406], 'p_i': 40, 'u_i': 4.1713},
        {'id': 6, 'e_m': 0.266387, 'e_o_k': [0.073996, 0.059197], 'p_i': 10, 'u_i': 3.6892},
        {'id': 7, 'e_m': 4.383523, 'e_o_k': [0.742467, 0.593973, 0.475179, 0.380143], 'p_i': 40, 'u_i': 2.3508},
    ]
    B_BUDGET = 110.399989
    return processors, tasks, B_BUDGET

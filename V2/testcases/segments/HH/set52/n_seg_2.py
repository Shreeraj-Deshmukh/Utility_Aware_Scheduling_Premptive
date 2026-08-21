"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640008, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640008, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.072434, 'e_o_k': [0.056338, 0.045070], 'p_i': 10, 'u_i': 2.7495},
        {'id': 1, 'e_m': 1.148168, 'e_o_k': [0.893020, 0.714416], 'p_i': 20, 'u_i': 1.5180},
        {'id': 2, 'e_m': 10.089957, 'e_o_k': [7.847744, 6.278195], 'p_i': 40, 'u_i': 2.4726},
        {'id': 3, 'e_m': 15.634448, 'e_o_k': [12.160126, 9.728101], 'p_i': 80, 'u_i': 4.1932},
        {'id': 4, 'e_m': 5.307793, 'e_o_k': [4.128283, 3.302626], 'p_i': 80, 'u_i': 2.7154},
        {'id': 5, 'e_m': 4.328363, 'e_o_k': [3.366504, 2.693204], 'p_i': 40, 'u_i': 4.3253},
        {'id': 6, 'e_m': 4.663525, 'e_o_k': [3.627186, 2.901749], 'p_i': 80, 'u_i': 1.0005},
        {'id': 7, 'e_m': 2.192726, 'e_o_k': [1.705453, 1.364363], 'p_i': 40, 'u_i': 1.9051},
    ]
    B_BUDGET = 176.640008
    return processors, tasks, B_BUDGET

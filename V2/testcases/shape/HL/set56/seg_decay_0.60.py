"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399992, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399992, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.150064, 'e_o_k': [0.451057, 0.270634, 0.162381, 0.097428, 0.058457, 0.035074], 'p_i': 10, 'u_i': 3.8590},
        {'id': 1, 'e_m': 0.276887, 'e_o_k': [0.060047, 0.036028, 0.021617, 0.012970, 0.007782], 'p_i': 20, 'u_i': 3.6983},
        {'id': 2, 'e_m': 1.036903, 'e_o_k': [0.224866, 0.134920, 0.080952, 0.048571, 0.029143], 'p_i': 40, 'u_i': 3.0670},
        {'id': 3, 'e_m': 0.261660, 'e_o_k': [0.081769, 0.049061], 'p_i': 80, 'u_i': 2.2547},
        {'id': 4, 'e_m': 12.654356, 'e_o_k': [3.954486, 2.372692], 'p_i': 80, 'u_i': 3.3628},
        {'id': 5, 'e_m': 0.168799, 'e_o_k': [0.052750, 0.031650], 'p_i': 10, 'u_i': 1.9431},
        {'id': 6, 'e_m': 2.612506, 'e_o_k': [0.566557, 0.339934, 0.203960, 0.122376, 0.073426], 'p_i': 80, 'u_i': 4.2381},
        {'id': 7, 'e_m': 3.342402, 'e_o_k': [0.852654, 0.511592, 0.306955], 'p_i': 10, 'u_i': 1.5683},
    ]
    B_BUDGET = 110.399992
    return processors, tasks, B_BUDGET

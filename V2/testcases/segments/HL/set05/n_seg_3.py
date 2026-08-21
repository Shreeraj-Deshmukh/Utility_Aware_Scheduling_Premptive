"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.789693, 'e_o_k': [0.161822, 0.129458, 0.103566], 'p_i': 10, 'u_i': 4.2289},
        {'id': 1, 'e_m': 0.245294, 'e_o_k': [0.050265, 0.040212, 0.032170], 'p_i': 20, 'u_i': 3.6434},
        {'id': 2, 'e_m': 3.310794, 'e_o_k': [0.678441, 0.542753, 0.434203], 'p_i': 40, 'u_i': 2.1879},
        {'id': 3, 'e_m': 1.628519, 'e_o_k': [0.333713, 0.266970, 0.213576], 'p_i': 80, 'u_i': 2.3607},
        {'id': 4, 'e_m': 2.051152, 'e_o_k': [0.420318, 0.336254, 0.269004], 'p_i': 20, 'u_i': 2.0600},
        {'id': 5, 'e_m': 0.110349, 'e_o_k': [0.022613, 0.018090, 0.014472], 'p_i': 80, 'u_i': 2.1803},
        {'id': 6, 'e_m': 3.223708, 'e_o_k': [0.660596, 0.528477, 0.422781], 'p_i': 10, 'u_i': 4.5157},
        {'id': 7, 'e_m': 7.173276, 'e_o_k': [1.469934, 1.175947, 0.940757], 'p_i': 40, 'u_i': 4.4957},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET

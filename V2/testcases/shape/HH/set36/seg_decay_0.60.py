"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639986, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.639986, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.942324, 'e_o_k': [0.572195, 0.343317, 0.205990, 0.123594, 0.074157], 'p_i': 10, 'u_i': 2.0085},
        {'id': 1, 'e_m': 0.718592, 'e_o_k': [0.513280, 0.307968, 0.184781], 'p_i': 20, 'u_i': 4.1252},
        {'id': 2, 'e_m': 0.754744, 'e_o_k': [0.443341, 0.266005, 0.159603, 0.095762, 0.057457, 0.034474], 'p_i': 40, 'u_i': 1.5166},
        {'id': 3, 'e_m': 4.113295, 'e_o_k': [3.599133, 2.159480], 'p_i': 80, 'u_i': 1.2517},
        {'id': 4, 'e_m': 15.892935, 'e_o_k': [10.225234, 6.135140, 3.681084, 2.208650], 'p_i': 40, 'u_i': 3.8216},
        {'id': 5, 'e_m': 3.188381, 'e_o_k': [2.277415, 1.366449, 0.819869], 'p_i': 40, 'u_i': 4.3612},
        {'id': 6, 'e_m': 1.051973, 'e_o_k': [0.676821, 0.406092, 0.243655, 0.146193], 'p_i': 10, 'u_i': 2.3108},
        {'id': 7, 'e_m': 0.692921, 'e_o_k': [0.445813, 0.267488, 0.160493, 0.096296], 'p_i': 40, 'u_i': 1.0383},
    ]
    B_BUDGET = 176.639986
    return processors, tasks, B_BUDGET

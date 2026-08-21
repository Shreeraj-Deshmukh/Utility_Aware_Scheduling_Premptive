"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.471162, 'e_o_k': [0.096550, 0.077240, 0.061792], 'p_i': 10, 'u_i': 2.0085},
        {'id': 1, 'e_m': 0.359296, 'e_o_k': [0.073626, 0.058901, 0.047121], 'p_i': 20, 'u_i': 4.1252},
        {'id': 2, 'e_m': 0.377372, 'e_o_k': [0.077330, 0.061864, 0.049491], 'p_i': 40, 'u_i': 4.4037},
        {'id': 3, 'e_m': 2.056648, 'e_o_k': [0.421444, 0.337155, 0.269724], 'p_i': 80, 'u_i': 1.7011},
        {'id': 4, 'e_m': 7.946467, 'e_o_k': [1.628374, 1.302700, 1.042160], 'p_i': 40, 'u_i': 1.8442},
        {'id': 5, 'e_m': 1.594191, 'e_o_k': [0.326678, 0.261343, 0.209074], 'p_i': 40, 'u_i': 2.3108},
        {'id': 6, 'e_m': 0.525986, 'e_o_k': [0.107784, 0.086227, 0.068982], 'p_i': 10, 'u_i': 1.0383},
        {'id': 7, 'e_m': 0.346460, 'e_o_k': [0.070996, 0.056797, 0.045437], 'p_i': 40, 'u_i': 2.0614},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET

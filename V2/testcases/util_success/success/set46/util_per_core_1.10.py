"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119982, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119982, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.471759, 'e_o_k': [0.399074, 0.319259, 0.255407, 0.204326, 0.163461], 'p_i': 10, 'u_i': 1.3568},
        {'id': 1, 'e_m': 9.383566, 'e_o_k': [0.763040, 0.610432, 0.488346, 0.390677, 0.312541, 0.250033], 'p_i': 20, 'u_i': 4.9189},
        {'id': 2, 'e_m': 19.718522, 'e_o_k': [2.003915, 1.603132, 1.282506, 1.026004], 'p_i': 40, 'u_i': 3.2179},
        {'id': 3, 'e_m': 24.063286, 'e_o_k': [4.010548, 3.208438], 'p_i': 80, 'u_i': 1.9131},
        {'id': 4, 'e_m': 3.645921, 'e_o_k': [0.448269, 0.358615, 0.286892], 'p_i': 20, 'u_i': 4.5723},
        {'id': 5, 'e_m': 0.345348, 'e_o_k': [0.035096, 0.028077, 0.022462, 0.017969], 'p_i': 10, 'u_i': 4.6120},
        {'id': 6, 'e_m': 3.023896, 'e_o_k': [0.503983, 0.403186], 'p_i': 20, 'u_i': 4.0962},
        {'id': 7, 'e_m': 4.874639, 'e_o_k': [0.812440, 0.649952], 'p_i': 40, 'u_i': 1.0986},
    ]
    B_BUDGET = 263.119982
    return processors, tasks, B_BUDGET

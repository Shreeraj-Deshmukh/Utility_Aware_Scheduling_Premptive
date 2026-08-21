"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400013, "H": 80, "J": 37, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.400013, "H": 80, "J": 37, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.488440, 'e_o_k': [0.152638, 0.091583], 'p_i': 10, 'u_i': 1.2408},
        {'id': 1, 'e_m': 0.924655, 'e_o_k': [0.212467, 0.127480, 0.076488, 0.045893], 'p_i': 20, 'u_i': 2.7274},
        {'id': 2, 'e_m': 2.288327, 'e_o_k': [0.496254, 0.297752, 0.178651, 0.107191, 0.064315], 'p_i': 40, 'u_i': 3.7398},
        {'id': 3, 'e_m': 4.657210, 'e_o_k': [1.188064, 0.712838, 0.427703], 'p_i': 80, 'u_i': 1.4758},
        {'id': 4, 'e_m': 0.144768, 'e_o_k': [0.030370, 0.018222, 0.010933, 0.006560, 0.003936, 0.002362], 'p_i': 10, 'u_i': 1.9890},
        {'id': 5, 'e_m': 0.140954, 'e_o_k': [0.035958, 0.021575, 0.012945], 'p_i': 40, 'u_i': 1.7667},
        {'id': 6, 'e_m': 4.924673, 'e_o_k': [1.256294, 0.753776, 0.452266], 'p_i': 20, 'u_i': 2.7743},
        {'id': 7, 'e_m': 3.252657, 'e_o_k': [0.747394, 0.448436, 0.269062, 0.161437], 'p_i': 10, 'u_i': 3.3191},
    ]
    B_BUDGET = 110.400013
    return processors, tasks, B_BUDGET

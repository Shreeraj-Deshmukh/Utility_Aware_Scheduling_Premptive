"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399987, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399987, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.362417, 'e_o_k': [0.495606, 0.297364, 0.178418, 0.107051, 0.064231, 0.038538], 'p_i': 10, 'u_i': 4.5134},
        {'id': 1, 'e_m': 1.818372, 'e_o_k': [0.463870, 0.278322, 0.166993], 'p_i': 20, 'u_i': 4.5874},
        {'id': 2, 'e_m': 2.018400, 'e_o_k': [0.514898, 0.308939, 0.185363], 'p_i': 40, 'u_i': 2.7347},
        {'id': 3, 'e_m': 10.977605, 'e_o_k': [2.800409, 1.680246, 1.008147], 'p_i': 80, 'u_i': 4.9671},
        {'id': 4, 'e_m': 5.439997, 'e_o_k': [1.179736, 0.707841, 0.424705, 0.254823, 0.152894], 'p_i': 80, 'u_i': 4.8761},
        {'id': 5, 'e_m': 0.284101, 'e_o_k': [0.065281, 0.039168, 0.023501, 0.014101], 'p_i': 10, 'u_i': 2.5248},
        {'id': 6, 'e_m': 1.455737, 'e_o_k': [0.454918, 0.272951], 'p_i': 40, 'u_i': 4.9532},
        {'id': 7, 'e_m': 6.094243, 'e_o_k': [1.400332, 0.840199, 0.504119, 0.302472], 'p_i': 40, 'u_i': 2.2979},
    ]
    B_BUDGET = 110.399987
    return processors, tasks, B_BUDGET

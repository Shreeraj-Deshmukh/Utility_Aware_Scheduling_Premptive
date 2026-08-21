"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.362417, 'e_o_k': [0.484102, 0.387282, 0.309825], 'p_i': 10, 'u_i': 4.5874},
        {'id': 1, 'e_m': 1.818372, 'e_o_k': [0.372617, 0.298094, 0.238475], 'p_i': 20, 'u_i': 2.7347},
        {'id': 2, 'e_m': 2.018400, 'e_o_k': [0.413607, 0.330885, 0.264708], 'p_i': 40, 'u_i': 4.9671},
        {'id': 3, 'e_m': 10.977605, 'e_o_k': [2.249509, 1.799607, 1.439686], 'p_i': 80, 'u_i': 4.8761},
        {'id': 4, 'e_m': 5.439997, 'e_o_k': [1.114753, 0.891803, 0.713442], 'p_i': 80, 'u_i': 2.5248},
        {'id': 5, 'e_m': 0.284101, 'e_o_k': [0.058218, 0.046574, 0.037259], 'p_i': 10, 'u_i': 4.9532},
        {'id': 6, 'e_m': 1.455737, 'e_o_k': [0.298307, 0.238645, 0.190916], 'p_i': 40, 'u_i': 2.2979},
        {'id': 7, 'e_m': 6.094243, 'e_o_k': [1.248820, 0.999056, 0.799245], 'p_i': 40, 'u_i': 4.0423},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET

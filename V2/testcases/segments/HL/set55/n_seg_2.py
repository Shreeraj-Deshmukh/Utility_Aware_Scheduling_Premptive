"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.362417, 'e_o_k': [0.656227, 0.524982], 'p_i': 10, 'u_i': 4.5874},
        {'id': 1, 'e_m': 1.818372, 'e_o_k': [0.505103, 0.404083], 'p_i': 20, 'u_i': 2.7347},
        {'id': 2, 'e_m': 2.018400, 'e_o_k': [0.560667, 0.448533], 'p_i': 40, 'u_i': 4.9671},
        {'id': 3, 'e_m': 10.977605, 'e_o_k': [3.049335, 2.439468], 'p_i': 80, 'u_i': 4.8761},
        {'id': 4, 'e_m': 5.439997, 'e_o_k': [1.511110, 1.208888], 'p_i': 80, 'u_i': 2.5248},
        {'id': 5, 'e_m': 0.284101, 'e_o_k': [0.078917, 0.063134], 'p_i': 10, 'u_i': 4.9532},
        {'id': 6, 'e_m': 1.455737, 'e_o_k': [0.404372, 0.323497], 'p_i': 40, 'u_i': 2.2979},
        {'id': 7, 'e_m': 6.094243, 'e_o_k': [1.692845, 1.354276], 'p_i': 40, 'u_i': 4.0423},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET

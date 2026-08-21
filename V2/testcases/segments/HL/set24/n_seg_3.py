"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400009, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400009, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.255086, 'e_o_k': [0.052272, 0.041817, 0.033454], 'p_i': 10, 'u_i': 1.4092},
        {'id': 1, 'e_m': 1.766930, 'e_o_k': [0.362076, 0.289661, 0.231729], 'p_i': 20, 'u_i': 2.7448},
        {'id': 2, 'e_m': 4.717796, 'e_o_k': [0.966761, 0.773409, 0.618727], 'p_i': 40, 'u_i': 3.9391},
        {'id': 3, 'e_m': 2.076602, 'e_o_k': [0.425533, 0.340427, 0.272341], 'p_i': 80, 'u_i': 3.4662},
        {'id': 4, 'e_m': 0.980401, 'e_o_k': [0.200902, 0.160721, 0.128577], 'p_i': 40, 'u_i': 1.1407},
        {'id': 5, 'e_m': 28.292425, 'e_o_k': [5.797628, 4.638102, 3.710482], 'p_i': 80, 'u_i': 3.5457},
        {'id': 6, 'e_m': 0.799254, 'e_o_k': [0.163782, 0.131025, 0.104820], 'p_i': 10, 'u_i': 1.4096},
        {'id': 7, 'e_m': 1.683036, 'e_o_k': [0.344884, 0.275908, 0.220726], 'p_i': 20, 'u_i': 4.8654},
    ]
    B_BUDGET = 110.400009
    return processors, tasks, B_BUDGET

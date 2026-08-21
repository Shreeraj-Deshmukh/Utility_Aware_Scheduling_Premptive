"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.39998, "H": 80, "J": 47, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.39998, "H": 80, "J": 47, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.224462, 'e_o_k': [0.340128, 0.272103], 'p_i': 10, 'u_i': 3.9801},
        {'id': 1, 'e_m': 1.637441, 'e_o_k': [0.454845, 0.363876], 'p_i': 20, 'u_i': 3.7892},
        {'id': 2, 'e_m': 2.261107, 'e_o_k': [0.628085, 0.502468], 'p_i': 40, 'u_i': 1.4880},
        {'id': 3, 'e_m': 0.027461, 'e_o_k': [0.007628, 0.006102], 'p_i': 80, 'u_i': 4.5731},
        {'id': 4, 'e_m': 1.620094, 'e_o_k': [0.450026, 0.360021], 'p_i': 10, 'u_i': 3.7064},
        {'id': 5, 'e_m': 2.906870, 'e_o_k': [0.807464, 0.645971], 'p_i': 10, 'u_i': 4.7396},
        {'id': 6, 'e_m': 0.061370, 'e_o_k': [0.017047, 0.013638], 'p_i': 10, 'u_i': 4.0832},
        {'id': 7, 'e_m': 0.799773, 'e_o_k': [0.222159, 0.177727], 'p_i': 10, 'u_i': 1.4400},
    ]
    B_BUDGET = 110.399980
    return processors, tasks, B_BUDGET

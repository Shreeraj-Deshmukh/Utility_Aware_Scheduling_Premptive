"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319995, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319995, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.244220, 'e_o_k': [0.189949, 0.151959], 'p_i': 10, 'u_i': 1.2408},
        {'id': 1, 'e_m': 0.462328, 'e_o_k': [0.359588, 0.287671], 'p_i': 20, 'u_i': 2.7274},
        {'id': 2, 'e_m': 1.144163, 'e_o_k': [0.889905, 0.711924], 'p_i': 40, 'u_i': 3.7398},
        {'id': 3, 'e_m': 2.328605, 'e_o_k': [1.811137, 1.448910], 'p_i': 80, 'u_i': 1.4758},
        {'id': 4, 'e_m': 0.072384, 'e_o_k': [0.056298, 0.045039], 'p_i': 10, 'u_i': 4.3036},
        {'id': 5, 'e_m': 0.070477, 'e_o_k': [0.054815, 0.043852], 'p_i': 40, 'u_i': 3.9596},
        {'id': 6, 'e_m': 2.462336, 'e_o_k': [1.915151, 1.532120], 'p_i': 20, 'u_i': 3.9830},
        {'id': 7, 'e_m': 1.626328, 'e_o_k': [1.264922, 1.011938], 'p_i': 10, 'u_i': 3.3191},
    ]
    B_BUDGET = 88.319995
    return processors, tasks, B_BUDGET

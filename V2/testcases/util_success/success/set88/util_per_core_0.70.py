"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.201452, 'e_o_k': [0.147720, 0.118176, 0.094541], 'p_i': 10, 'u_i': 3.5588},
        {'id': 1, 'e_m': 2.769793, 'e_o_k': [0.461632, 0.369306], 'p_i': 20, 'u_i': 1.0875},
        {'id': 2, 'e_m': 8.937490, 'e_o_k': [0.908282, 0.726625, 0.581300, 0.465040], 'p_i': 40, 'u_i': 2.9446},
        {'id': 3, 'e_m': 0.395131, 'e_o_k': [0.040156, 0.032124, 0.025700, 0.020560], 'p_i': 80, 'u_i': 2.5289},
        {'id': 4, 'e_m': 17.549708, 'e_o_k': [1.566192, 1.252954, 1.002363, 0.801891, 0.641512], 'p_i': 40, 'u_i': 2.8941},
        {'id': 5, 'e_m': 9.433965, 'e_o_k': [0.767139, 0.613711, 0.490969, 0.392775, 0.314220, 0.251376], 'p_i': 40, 'u_i': 4.5618},
        {'id': 6, 'e_m': 0.466177, 'e_o_k': [0.077696, 0.062157], 'p_i': 10, 'u_i': 3.9189},
        {'id': 7, 'e_m': 7.671165, 'e_o_k': [0.779590, 0.623672, 0.498938, 0.399150], 'p_i': 40, 'u_i': 2.1344},
    ]
    B_BUDGET = 167.440001
    return processors, tasks, B_BUDGET

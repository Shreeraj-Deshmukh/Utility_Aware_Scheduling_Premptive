"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.20001, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "segments", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.20001, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "segments", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.464878, 'e_o_k': [0.078739, 0.062992, 0.050393, 0.040315], 'p_i': 10, 'u_i': 1.2748},
        {'id': 1, 'e_m': 0.028439, 'e_o_k': [0.004817, 0.003854, 0.003083, 0.002466], 'p_i': 20, 'u_i': 3.8825},
        {'id': 2, 'e_m': 1.311997, 'e_o_k': [0.222222, 0.177777, 0.142222, 0.113778], 'p_i': 40, 'u_i': 3.8582},
        {'id': 3, 'e_m': 2.237336, 'e_o_k': [0.378953, 0.303162, 0.242530, 0.194024], 'p_i': 80, 'u_i': 1.6137},
        {'id': 4, 'e_m': 1.174834, 'e_o_k': [0.198990, 0.159192, 0.127353, 0.101883], 'p_i': 20, 'u_i': 2.7253},
        {'id': 5, 'e_m': 5.271494, 'e_o_k': [0.892868, 0.714295, 0.571436, 0.457149], 'p_i': 40, 'u_i': 1.4714},
        {'id': 6, 'e_m': 0.171228, 'e_o_k': [0.029002, 0.023202, 0.018561, 0.014849], 'p_i': 10, 'u_i': 2.9160},
        {'id': 7, 'e_m': 1.673435, 'e_o_k': [0.283441, 0.226753, 0.181402, 0.145122], 'p_i': 20, 'u_i': 4.4871},
    ]
    B_BUDGET = 55.200010
    return processors, tasks, B_BUDGET

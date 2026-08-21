"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.279536, 'e_o_k': [0.160389, 0.128312, 0.102649], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 0.807491, 'e_o_k': [0.463314, 0.370651, 0.296521], 'p_i': 20, 'u_i': 1.2645},
        {'id': 2, 'e_m': 3.179023, 'e_o_k': [1.824029, 1.459224, 1.167379], 'p_i': 40, 'u_i': 2.2756},
        {'id': 3, 'e_m': 7.775197, 'e_o_k': [4.461179, 3.568943, 2.855154], 'p_i': 80, 'u_i': 2.5093},
        {'id': 4, 'e_m': 0.001832, 'e_o_k': [0.001051, 0.000841, 0.000673], 'p_i': 10, 'u_i': 3.6510},
        {'id': 5, 'e_m': 1.937647, 'e_o_k': [1.111765, 0.889412, 0.711529], 'p_i': 80, 'u_i': 3.1983},
        {'id': 6, 'e_m': 0.361320, 'e_o_k': [0.207314, 0.165852, 0.132681], 'p_i': 10, 'u_i': 4.3627},
        {'id': 7, 'e_m': 3.778825, 'e_o_k': [2.168178, 1.734542, 1.387634], 'p_i': 40, 'u_i': 4.4103},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET

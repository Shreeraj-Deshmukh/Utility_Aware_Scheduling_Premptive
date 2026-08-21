"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400008, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400008, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.073209, 'e_o_k': [0.298114, 0.238491], 'p_i': 10, 'u_i': 3.4396},
        {'id': 1, 'e_m': 2.009822, 'e_o_k': [0.558284, 0.446627], 'p_i': 20, 'u_i': 1.7213},
        {'id': 2, 'e_m': 4.500422, 'e_o_k': [1.250117, 1.000094], 'p_i': 40, 'u_i': 2.3007},
        {'id': 3, 'e_m': 5.174123, 'e_o_k': [1.437257, 1.149805], 'p_i': 80, 'u_i': 2.4667},
        {'id': 4, 'e_m': 4.541214, 'e_o_k': [1.261448, 1.009159], 'p_i': 80, 'u_i': 2.4016},
        {'id': 5, 'e_m': 0.685731, 'e_o_k': [0.190481, 0.152385], 'p_i': 10, 'u_i': 3.4602},
        {'id': 6, 'e_m': 15.096114, 'e_o_k': [4.193365, 3.354692], 'p_i': 80, 'u_i': 3.9709},
        {'id': 7, 'e_m': 8.076896, 'e_o_k': [2.243582, 1.794866], 'p_i': 80, 'u_i': 1.7339},
    ]
    B_BUDGET = 110.400008
    return processors, tasks, B_BUDGET

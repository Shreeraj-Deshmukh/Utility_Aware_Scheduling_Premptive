"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400003, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400003, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.001859, 'e_o_k': [0.000381, 0.000305, 0.000244], 'p_i': 10, 'u_i': 1.4564},
        {'id': 1, 'e_m': 1.030212, 'e_o_k': [0.211109, 0.168887, 0.135110], 'p_i': 20, 'u_i': 1.4719},
        {'id': 2, 'e_m': 0.499974, 'e_o_k': [0.102454, 0.081963, 0.065570], 'p_i': 40, 'u_i': 1.0831},
        {'id': 3, 'e_m': 3.303812, 'e_o_k': [0.677011, 0.541609, 0.433287], 'p_i': 80, 'u_i': 3.5025},
        {'id': 4, 'e_m': 16.765688, 'e_o_k': [3.435592, 2.748474, 2.198779], 'p_i': 40, 'u_i': 4.4776},
        {'id': 5, 'e_m': 1.698548, 'e_o_k': [0.348063, 0.278451, 0.222760], 'p_i': 20, 'u_i': 3.2024},
        {'id': 6, 'e_m': 0.189483, 'e_o_k': [0.038828, 0.031063, 0.024850], 'p_i': 10, 'u_i': 1.4405},
        {'id': 7, 'e_m': 1.714886, 'e_o_k': [0.351411, 0.281129, 0.224903], 'p_i': 10, 'u_i': 3.4151},
    ]
    B_BUDGET = 110.400003
    return processors, tasks, B_BUDGET

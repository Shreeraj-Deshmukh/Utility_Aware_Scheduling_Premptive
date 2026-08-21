"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "segments", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "segments", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.622255, 'e_o_k': [1.717872, 1.374297, 1.099438, 0.879550], 'p_i': 10, 'u_i': 3.4311},
        {'id': 1, 'e_m': 0.101434, 'e_o_k': [0.048105, 0.038484, 0.030787, 0.024630], 'p_i': 20, 'u_i': 3.8774},
        {'id': 2, 'e_m': 5.088426, 'e_o_k': [2.413210, 1.930568, 1.544455, 1.235564], 'p_i': 40, 'u_i': 3.3220},
        {'id': 3, 'e_m': 2.359092, 'e_o_k': [1.118810, 0.895048, 0.716039, 0.572831], 'p_i': 80, 'u_i': 2.5309},
        {'id': 4, 'e_m': 3.488235, 'e_o_k': [1.654312, 1.323449, 1.058760, 0.847008], 'p_i': 40, 'u_i': 3.7128},
        {'id': 5, 'e_m': 1.158934, 'e_o_k': [0.549630, 0.439704, 0.351763, 0.281410], 'p_i': 20, 'u_i': 4.9574},
        {'id': 6, 'e_m': 9.098933, 'e_o_k': [4.315212, 3.452170, 2.761736, 2.209389], 'p_i': 80, 'u_i': 3.9330},
        {'id': 7, 'e_m': 0.684572, 'e_o_k': [0.324662, 0.259729, 0.207783, 0.166227], 'p_i': 40, 'u_i': 3.5882},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET

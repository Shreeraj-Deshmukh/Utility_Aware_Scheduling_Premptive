"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400003, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400003, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.930633, 'e_o_k': [0.190703, 0.152563, 0.122050], 'p_i': 10, 'u_i': 3.1458},
        {'id': 1, 'e_m': 3.264279, 'e_o_k': [0.668910, 0.535128, 0.428102], 'p_i': 20, 'u_i': 4.9683},
        {'id': 2, 'e_m': 2.777130, 'e_o_k': [0.569084, 0.455267, 0.364214], 'p_i': 40, 'u_i': 2.4718},
        {'id': 3, 'e_m': 8.264281, 'e_o_k': [1.693500, 1.354800, 1.083840], 'p_i': 80, 'u_i': 3.8875},
        {'id': 4, 'e_m': 2.998873, 'e_o_k': [0.614523, 0.491619, 0.393295], 'p_i': 80, 'u_i': 3.3599},
        {'id': 5, 'e_m': 0.395365, 'e_o_k': [0.081017, 0.064814, 0.051851], 'p_i': 40, 'u_i': 3.9269},
        {'id': 6, 'e_m': 2.545753, 'e_o_k': [0.521671, 0.417336, 0.333869], 'p_i': 10, 'u_i': 3.4836},
        {'id': 7, 'e_m': 2.761829, 'e_o_k': [0.565949, 0.452759, 0.362207], 'p_i': 40, 'u_i': 2.8974},
    ]
    B_BUDGET = 110.400003
    return processors, tasks, B_BUDGET

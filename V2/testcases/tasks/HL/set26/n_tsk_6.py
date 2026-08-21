"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.157033, 'e_o_k': [0.563394, 0.450715, 0.360572, 0.288458, 0.230766, 0.184613], 'p_i': 10, 'u_i': 2.2803},
        {'id': 1, 'e_m': 1.308705, 'e_o_k': [0.177366, 0.141893, 0.113514, 0.090811, 0.072649, 0.058119], 'p_i': 20, 'u_i': 3.9685},
        {'id': 2, 'e_m': 3.452694, 'e_o_k': [0.959082, 0.767265], 'p_i': 40, 'u_i': 1.4001},
        {'id': 3, 'e_m': 9.033558, 'e_o_k': [1.530074, 1.224059, 0.979247, 0.783398], 'p_i': 80, 'u_i': 2.1780},
        {'id': 4, 'e_m': 4.055672, 'e_o_k': [0.831080, 0.664864, 0.531891], 'p_i': 80, 'u_i': 3.8388},
        {'id': 5, 'e_m': 5.514294, 'e_o_k': [0.933993, 0.747194, 0.597755, 0.478204], 'p_i': 80, 'u_i': 1.0041},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET

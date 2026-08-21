"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400008, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400008, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.392989, 'e_o_k': [0.080531, 0.064424, 0.051540], 'p_i': 10, 'u_i': 3.6850},
        {'id': 1, 'e_m': 1.450345, 'e_o_k': [0.245655, 0.196524, 0.157219, 0.125775], 'p_i': 20, 'u_i': 3.7169},
        {'id': 2, 'e_m': 14.787038, 'e_o_k': [3.030131, 2.424105, 1.939284], 'p_i': 40, 'u_i': 3.7239},
        {'id': 3, 'e_m': 10.342252, 'e_o_k': [1.751736, 1.401389, 1.121111, 0.896889], 'p_i': 80, 'u_i': 1.9107},
        {'id': 4, 'e_m': 8.055015, 'e_o_k': [1.198092, 0.958474, 0.766779, 0.613423, 0.490739], 'p_i': 80, 'u_i': 1.7322},
        {'id': 5, 'e_m': 1.770841, 'e_o_k': [0.263393, 0.210714, 0.168571, 0.134857, 0.107886], 'p_i': 20, 'u_i': 1.5709},
    ]
    B_BUDGET = 110.400008
    return processors, tasks, B_BUDGET

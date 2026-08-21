"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440005, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440005, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.882752, 'e_o_k': [0.234416, 0.187533, 0.150026, 0.120021, 0.096017, 0.076813], 'p_i': 10, 'u_i': 3.9772},
        {'id': 1, 'e_m': 0.060026, 'e_o_k': [0.006100, 0.004880, 0.003904, 0.003123], 'p_i': 20, 'u_i': 1.4627},
        {'id': 2, 'e_m': 5.120310, 'e_o_k': [0.853385, 0.682708], 'p_i': 40, 'u_i': 4.5040},
        {'id': 3, 'e_m': 2.896673, 'e_o_k': [0.356148, 0.284919, 0.227935], 'p_i': 80, 'u_i': 4.7123},
        {'id': 4, 'e_m': 1.711718, 'e_o_k': [0.152759, 0.122207, 0.097766, 0.078213, 0.062570], 'p_i': 20, 'u_i': 4.3702},
        {'id': 5, 'e_m': 3.269547, 'e_o_k': [0.332271, 0.265817, 0.212653, 0.170123], 'p_i': 40, 'u_i': 3.7678},
        {'id': 6, 'e_m': 27.007778, 'e_o_k': [2.744693, 2.195754, 1.756603, 1.405283], 'p_i': 80, 'u_i': 3.2312},
        {'id': 7, 'e_m': 17.583424, 'e_o_k': [2.161896, 1.729517, 1.383614], 'p_i': 40, 'u_i': 3.7207},
    ]
    B_BUDGET = 167.440005
    return processors, tasks, B_BUDGET

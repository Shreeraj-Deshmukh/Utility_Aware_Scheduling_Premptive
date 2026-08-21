"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 207.551957, "H": 80, "J": 28, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.3, "seed": 1055, "set": 55, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.30"}
"""

_SPEC = '{"B": 207.551957, "H": 80, "J": 28, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.3, "seed": 1055, "set": 55, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.362417, 'e_o_k': [0.896485, 0.717188, 0.573750, 0.459000, 0.367200, 0.293760], 'p_i': 10, 'u_i': 4.5134},
        {'id': 1, 'e_m': 1.818372, 'e_o_k': [1.043328, 0.834662, 0.667730], 'p_i': 20, 'u_i': 4.5874},
        {'id': 2, 'e_m': 2.018400, 'e_o_k': [1.158098, 0.926479, 0.741183], 'p_i': 40, 'u_i': 2.7347},
        {'id': 3, 'e_m': 10.977605, 'e_o_k': [6.298626, 5.038900, 4.031120], 'p_i': 80, 'u_i': 4.9671},
        {'id': 4, 'e_m': 5.439997, 'e_o_k': [2.265586, 1.812469, 1.449975, 1.159980, 0.927984], 'p_i': 80, 'u_i': 4.8761},
        {'id': 5, 'e_m': 0.284101, 'e_o_k': [0.134736, 0.107789, 0.086231, 0.068985], 'p_i': 10, 'u_i': 2.5248},
        {'id': 6, 'e_m': 1.455737, 'e_o_k': [1.132240, 0.905792], 'p_i': 40, 'u_i': 4.9532},
        {'id': 7, 'e_m': 6.094243, 'e_o_k': [2.890224, 2.312179, 1.849743, 1.479794], 'p_i': 40, 'u_i': 2.2979},
    ]
    B_BUDGET = 207.551957
    return processors, tasks, B_BUDGET

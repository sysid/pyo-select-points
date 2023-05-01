from helper import plot_points

test = {
    'dist': 50,
    'points': {
        1: (66.111, 75.582),
        2: (62.745, 28.386),
        3: (8.642, 10.251),
        4: (64.125, 54.531),
        5: (3.152, 79.236),
        6: (7.277, 17.566),
        7: (52.563, 75.021),
        8: (17.812, 3.414),
        9: (58.513, 62.123),
        10: (38.936, 35.871),
    },
}

full = {
    'dist': 50,
    'points': {
        1: (17.175, 84.327),
        2: (55.038, 30.114),
        3: (29.221, 22.405),
        4: (34.983, 85.627),
        5: (6.711, 50.021),
        6: (99.812, 57.873),
        7: (99.113, 76.225),
        8: (13.069, 63.972),
        9: (15.952, 25.008),
        10: (66.893, 43.536),
        11: (35.970, 35.144),
        12: (13.149, 15.010),
        13: (58.911, 83.089),
        14: (23.082, 66.573),
        15: (77.586, 30.366),
        16: (11.049, 50.238),
        17: (16.017, 87.246),
        18: (26.511, 28.581),
        19: (59.396, 72.272),
        20: (62.825, 46.380),
        21: (41.331, 11.770),
        22: (31.421, 4.655),
        23: (33.855, 18.210),
        24: (64.573, 56.075),
        25: (76.996, 29.781),
        26: (66.111, 75.582),
        27: (62.745, 28.386),
        28: (8.642, 10.251),
        29: (64.125, 54.531),
        30: (3.152, 79.236),
        31: (7.277, 17.566),
        32: (52.563, 75.021),
        33: (17.812, 3.414),
        34: (58.513, 62.123),
        35: (38.936, 35.871),
        36: (24.303, 24.642),
        37: (13.050, 93.345),
        38: (37.994, 78.340),
        39: (30.003, 12.548),
        40: (74.887, 6.923),
        41: (20.202, 0.507),
        42: (26.961, 49.985),
        43: (15.129, 17.417),
        44: (33.064, 31.691),
        45: (32.209, 96.398),
        46: (99.360, 36.990),
        47: (37.289, 77.198),
        48: (39.668, 91.310),
        49: (11.958, 73.548),
        50: (5.542, 57.630),
    }
}

full2 = {
    'dist': 50,
    'points': {1: (31.487, 3.397), 2: (57.189, 4.053), 3: (25.188, 13.872), 4: (60.994, 76.828), 5: (21.735, 0.946),
               6: (27.975, 77.959), 7: (23.703, 93.899), 8: (68.679, 20.511), 9: (22.453, 93.224), 10: (7.377, 11.775),
               11: (54.193, 23.732), 12: (78.498, 58.671), 13: (40.641, 74.675), 14: (34.743, 79.203),
               15: (99.784, 53.974), 16: (43.995, 47.065), 17: (84.872, 32.03), 18: (76.402, 46.851),
               19: (90.188, 69.991),
               20: (22.23, 58.883), 21: (11.877, 64.604), 22: (2.486, 77.866), 23: (99.799, 65.378),
               24: (32.309, 5.814),
               25: (64.986, 8.961), 26: (31.044, 20.636), 27: (74.735, 19.901), 28: (84.953, 95.465),
               29: (5.364, 36.746),
               30: (50.527, 68.371), 31: (86.194, 88.184), 32: (84.159, 3.061), 33: (38.979, 48.349),
               34: (30.585, 42.691),
               35: (6.531, 35.056), 36: (48.308, 14.249), 37: (7.727, 40.714), 38: (58.519, 87.09),
               39: (67.393, 23.184),
               40: (4.208, 89.739), 41: (40.728, 89.554), 42: (87.795, 87.217), 43: (5.914, 17.697), 44: (5.93, 23.415),
               45: (90.604, 20.814), 46: (7.883, 26.039), 47: (21.568, 47.344), 48: (2.206, 68.055),
               49: (86.001, 23.108),
               50: (85.441, 38.957), 51: (73.444, 6.247), 52: (67.607, 29.003), 53: (78.209, 27.471),
               54: (58.357, 81.046),
               55: (82.178, 10.346), 56: (28.206, 50.764), 57: (85.382, 32.101), 58: (34.107, 68.218),
               59: (82.062, 11.217), 60: (57.761, 93.717), 61: (82.877, 31.546), 62: (87.53, 20.937),
               63: (57.557, 64.843),
               64: (72.721, 3.754), 65: (44.539, 19.422), 66: (82.174, 49.68), 67: (85.659, 14.618),
               68: (4.783, 49.968),
               69: (74.146, 82.793), 70: (60.202, 28.075), 71: (26.761, 69.42), 72: (64.761, 80.018),
               73: (47.025, 40.37),
               74: (81.275, 71.139), 75: (65.48, 25.461), 76: (93.072, 81.172), 77: (95.517, 31.637),
               78: (55.215, 40.147),
               79: (75.955, 89.229), 80: (29.531, 8.48), 81: (2.724, 46.297), 82: (56.463, 38.411), 83: (62.716, 18.85),
               84: (58.186, 34.441), 85: (35.788, 0.023), 86: (79.823, 38.954), 87: (97.484, 72.655),
               88: (87.483, 32.71),
               89: (84.183, 21.32), 90: (13.667, 41.655), 91: (34.314, 0.728), 92: (23.783, 45.109),
               93: (61.481, 40.634),
               94: (78.09, 30.989), 95: (19.4, 92.502), 96: (92.537, 3.097), 97: (37.16, 70.524), 98: (70.576, 28.016),
               99: (89.001, 82.238), 100: (48.206, 8.888), 101: (1.371, 39.179), 102: (13.86, 38.073),
               103: (50.771, 40.158), 104: (78.615, 4.787), 105: (50.903, 23.443), 106: (1.597, 77.97),
               107: (45.148, 93.618), 108: (36.283, 10.85), 109: (4.603, 33.583), 110: (65.757, 1.319),
               111: (94.783, 2.492), 112: (30.018, 56.72), 113: (7.242, 98.308), 114: (6.47, 75.873),
               115: (42.147, 37.964), 116: (42.775, 57.04), 117: (62.44, 66.846), 118: (62.246, 65.509),
               119: (69.582, 20.094), 120: (44.426, 57.318), 121: (7.993, 14.766), 122: (18.405, 5.275),
               123: (93.763, 12.965), 124: (12.265, 65.482), 125: (92.146, 90.098), 126: (33.138, 79.385),
               127: (54.179, 0.02), 128: (95.829, 90.873), 129: (98.555, 67.397), 130: (57.15, 33.223),
               131: (66.367, 10.116), 132: (4.551, 94.21), 133: (16.25, 71.599), 134: (37.784, 90.661),
               135: (2.677, 82.816), 136: (71.02, 63.968), 137: (51.566, 73.013), 138: (55.074, 32.021),
               139: (0.906, 33.973), 140: (39.128, 78.308), 141: (39.851, 78.757), 142: (95.693, 95.888),
               143: (32.024, 43.29), 144: (96.457, 57.044), 145: (50.212, 32.347), 146: (81.584, 31.951),
               147: (19.833, 75.78), 148: (32.124, 35.05), 149: (86.542, 83.09), 150: (90.378, 75.501),
               151: (99.952, 54.205), 152: (0.18, 20.466), 153: (68.484, 38.301), 154: (72.162, 43.708),
               155: (37.132, 77.623), 156: (84.614, 23.318), 157: (66.445, 84.434), 158: (86.513, 98.019),
               159: (11.09, 69.74), 160: (56.782, 97.267), 161: (69.239, 42.297), 162: (70.067, 57.167),
               163: (47.424, 45.543), 164: (56.109, 65.03), 165: (50.483, 31.899), 166: (14.463, 83.953),
               167: (74.655, 32.224), 168: (12.693, 66.509), 169: (87.466, 29.738), 170: (16.138, 10.473),
               171: (46.647, 40.037), 172: (93.93, 56.48), 173: (57.06, 63.697), 174: (38.08, 61.014),
               175: (90.7, 59.405),
               176: (81.042, 55.203), 177: (55.161, 79.663), 178: (58.287, 78.143), 179: (68.943, 72.214),
               180: (2.858, 15.707), 181: (59.628, 90.758), 182: (77.753, 69.061), 183: (35.799, 0.142),
               184: (99.832, 49.753), 185: (67.87, 9.358), 186: (17.193, 48.512), 187: (12.089, 28.25),
               188: (37.478, 63.092), 189: (44.598, 37.246), 190: (52.863, 49.604), 191: (0.84, 49.053),
               192: (38.601, 37.201), 193: (63.599, 50.346), 194: (96.199, 66.091), 195: (37.422, 62.735),
               196: (47.091, 56.845), 197: (77.694, 14.475), 198: (40.734, 96.084), 199: (21.147, 29.8),
               200: (6.876, 69.797)}}

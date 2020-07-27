
# coding=utf8

modelChemistry = 'CCSD(T)-F12/cc-pVTZ-F12//B3LYP/CBSB7'
useHinderedRotors = True
useBondCorrections = False

species(label = 'aOOHbalkene',
    E0 = (
        ***u_E0***-257.233,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(90.0317, 'amu')),
        NonlinearRotor(
            inertia = ([58.5208, 220.798, 265.309], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([257.491, 320.223, 437.353, 549.589, 607.728, 713.412, 939.453, 983.153, 996.518, 1023.73, 1045.16, 1080.06, 1165.23, 1281.77, 1312.52, 1354.16, 1424.5, 1441.97, 1453.24, 1709.53, 3051.26, 3136.57, 3171.12, 3224.07, 3787.1, 3838.71], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.865227, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-3.30244, -10.593, -2.86958, 0.077152, 0.101446],
                    [6.47957, -2.62952, -2.94653, 0.0400083, 0.21474],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (7.25144, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-8.19212, -6.93264, -13.3307, -0.327246, 0.597786],
                    [3.51461, 8.83716, -6.02019, -1.40613, 0.126518],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.87043, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-4.46214, -6.84434, -0.40349, 0.42967, 0.188659],
                    [-6.00225, 0.883883, 1.61462, 0.462874, -0.0231973],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (7.79504, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-1.14815, -2.84698, -2.82698, -1.35585, -0.0703014],
                    [-0.605051, -3.23702, 1.85718, -0.0812629, 0.323479],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 2,
    structure = SMILES('OOC(O)C=C'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'OH',
    E0 = (28.4187, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(17.0027, 'amu')),
        LinearRotor(inertia=(0.90166, 'amu*angstrom^2'), symmetry=1),
        HarmonicOscillator(frequencies=([3719.11], 'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    structure = SMILES('[OH]'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'ibutanal',
    E0 = (
        ***u_E0***-225.137,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(72.0575, 'amu')),
        NonlinearRotor(
            inertia = ([67.5563, 123.992, 171.092], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([269.321, 342.5, 402.416, 641.624, 795.744, 917.809, 928.63, 946.947, 976.782, 1133.5, 1158.42, 1204.52, 1309.9, 1356.8, 1409.48, 1412.97, 1436.79, 1492.33, 1497.51, 1511.78, 1516.17, 1821.51, 2854.63, 2987.5, 3037.24, 3049.34, 3099.98, 3109.82, 3113.74, 3123.59], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.88822, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0561389, -0.0363091, -4.80587, 0.035679, -0.0343592],
                    [0.0247882, 0.0156983, -0.0270546, 0.0220617, 0.0131048],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.90774, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (12272.6, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (6.95111, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.355836, -0.917331, -2.64256, 0.0186916, -0.0249643],
                    [0.505618, -1.10506, 0.702449, 0.042892, -0.125139],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    structure = SMILES('O=CC(C)C'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'aR',
    E0 = (
        ***u_E0***-114.612,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(73.0653, 'amu')),
        NonlinearRotor(
            inertia = ([64.8913, 143.774, 189.065], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([261.857, 350.564, 414.843, 500.938, 684.141, 830.206, 936.735, 944.011, 972.516, 1106.59, 1129.25, 1180.28, 1200.02, 1274.58, 1344.22, 1351.17, 1399.13, 1422.74, 1457.81, 1497.35, 1499.15, 1509.89, 1521.98, 2985.33, 3005.1, 3010.66, 3062.56, 3069.29, 3077.17, 3083.77, 3091.3, 3767.07], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.98054, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (12268.4, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.96048, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (14158.1, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.408158, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [1.97557, -6.84552, -3.52822, 1.65988, 0.229909],
                    [-0.659497, 0.4254, 0.701523, -0.879831, 0.238906],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (7.40315, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-1.11597, 0.207475, -3.95806, 0.108777, -0.121279],
                    [-1.22064, -0.157371, 0.544275, 0.0991051, -0.152781],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    structure = SMILES('CC(C)[CH]O'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'performic_acid',
    E0 = (
        -301.613,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(62.0004, 'amu')),
        NonlinearRotor(
            inertia = ([24.6504, 66.9352, 91.5857], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([345.991, 848.935, 892.101, 1002.7, 1146.85, 1365.63, 1497.92, 1803.75, 3084.64, 3552.77], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (5.98303, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-4.5477, -31.6031, -3.8018, 0.691414, 0.958034],
                    [-2.66453, -5.18627, 1.18802, 1.37715, 0.709481],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.739725, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-6.4187, -3.17743, -1.07798, -0.40043, -0.0453182],
                    [0.357222, 0.359361, 0.18248, 0.0918069, 0.0143392],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    structure = SMILES('OOC=O'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'disub_c4ether',
    E0 = (
        ***u_E0***-328.806,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(88.0524, 'amu')),
        NonlinearRotor(
            inertia = ([96.3307, 151.65, 218.331], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([114.503, 265.593, 326.69, 445.323, 554.757, 711.166, 857.648, 893.745, 935.537, 963.993, 993.826, 1097.75, 1128.97, 1147.96, 1169.52, 1185.15, 1256.23, 1282.07, 1326.45, 1345.29, 1404.61, 1421.63, 1460.66, 1504.02, 1505.69, 1539.93, 3027.2, 3033.86, 3046.79, 3054.31, 3082.31, 3098.45, 3100.35, 3809.53], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.94616, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (11163.3, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.871339, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-4.09781, -4.2384, -2.60554, 0.0386657, 0.0159963],
                    [-7.59597, 2.16361, 0.881012, -0.0646185, -0.0856098],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 2,
    structure = SMILES('OC1OCC(C)1'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'aQOOHb',
    E0 = (
        ***u_E0***-239.806,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([125.972, 282.182, 344.149], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([158.672, 279.729, 322.316, 336.683, 445.222, 522.818, 633.868, 795.679, 838.184, 909.249, 946.236, 983.131, 999.758, 1049.99, 1110.69, 1207.57, 1288.1, 1311.08, 1331.15, 1384.57, 1403.26, 1415.24, 1472.87, 1475.11, 1478.1, 1491.81, 1506.01, 2969.62, 2978.28, 2997.76, 3042.47, 3046.54, 3097.38, 3136.94, 3805.29, 3828.64], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.88424, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0116458, -0.00851126, -1.04622, 0.00598859, -0.00712817],
                    [-0.00264115, -0.00556034, -0.279939, 0.00557522, -0.0177938],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.81562, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0168744, 0.00518582, -1.00197, 0.00405355, 0.0381895],
                    [0.024021, 0.0162927, 0.119721, -0.00865612, 0.0119365],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (32.0162, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.00242769, -5.20625, 0.0449287, 0.0246984, -0.396694],
                    [-0.67052, -0.481428, 0.302878, -0.389611, 0.673677],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.682802, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-1.27482, -1.11631, -2.6239, 0.17892, 0.37],
                    [0.194942, -2.57006, 1.57222, 0.579472, -0.256617],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (5.70403, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-6.90354, -3.15167, -7.64009, 0.450424, 0.735851],
                    [-0.874591, 3.5657, -0.799112, -0.9434, 0.220044],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.759891, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-15.2028, 4.75917, -1.61321, -0.942045, 0.892201],
                    [-6.76634, 5.93591, -1.08857, -1.63814, 1.4105],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    structure = SMILES('OOC(O)[C](C)C'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'H',
    E0 = (211.794, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(1.00783, 'amu')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    structure = SMILES('[H]'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'aadduct',
    E0 = (
        ***u_E0***-259.643,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([96.02, 517.706, 589.212], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([36.9864, 63.9992, 78.6639, 121.079, 141.47, 229.387, 312.854, 347.966, 410.959, 650.597, 677.189, 802.257, 924.369, 941.463, 956.453, 978.376, 1137.38, 1164.17, 1198.47, 1205.86, 1304.11, 1363.28, 1410.78, 1417.94, 1439.06, 1492.82, 1498.79, 1511.74, 1516.59, 1568.92, 1772, 2967.07, 2989.12, 3042.06, 3051.89, 3107, 3114.66, 3118.72, 3125.77, 3331.59], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.66339, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (12135.5, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.64602, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (9917.83, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    structure = SMILES('OC(O)C(O)C[CH2]'),
    molecularWeight = (105.11, 'g/mol'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),    #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'ibutenol',
    E0 = (
        ***u_E0***-192.771,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(72.0575, 'amu')),
        NonlinearRotor(
            inertia = ([60.415, 134.931, 189.106], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([266.605, 273.676, 360.058, 448.874, 583.561, 817.418, 849.082, 977.192, 1015.73, 1047.49, 1104.54, 1172.81, 1201.01, 1317.78, 1391.69, 1418.66, 1429.15, 1479.03, 1493.2, 1500.32, 1508.41, 1773.69, 3009.39, 3016.95, 3047.95, 3052.54, 3097.16, 3137.25, 3152.2, 3895.04], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.9945, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (10526.5, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.97371, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (4763.43, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.375121, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.447, -5.93738, -1.28329, 0.323354, -0.0403791],
                    [0.0149421, 0.0212545, 0.00463222, -0.00272066, 0.00269864],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    structure = SMILES('CC(C)=CO'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'trisub_epoxy',
    E0 = (
        ***u_E0***-337.779,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(88.0524, 'amu')),
        NonlinearRotor(
            inertia = ([90.1114, 166.987, 201.665], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([223.05, 283.149, 362.446, 400.597, 532.379, 551.453, 692.773, 794.744, 914.792, 958.511, 1002.83, 1042.59, 1123.24, 1150.51, 1165.24, 1260.64, 1307.27, 1374.3, 1418.08, 1431, 1472.45, 1481.88, 1490.46, 1505.81, 1524.31, 3037.43, 3045.53, 3096.77, 3104.43, 3120.54, 3122.72, 3130.35, 3836.69], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.98628, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0120909, -0.0162932, -2.88503, 0.0335141, 0.00223636],
                    [-0.00675956, -0.0237039, -0.330621, -0.000334559, 0.00842816],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (3.03538, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (9112.12, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.871924, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-4.61082, -0.445028, -0.162812, -0.30709, -0.00374357],
                    [3.74167, -1.06677, -1.52635, 0.33858, -0.0125998],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 2,
    structure = SMILES('CC1(C)OC1O'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'aQOOH[O]',
    E0 = (
        ***u_E0***-194.582,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([107.408, 302.018, 330.657], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([213.765, 267.057, 338.453, 358.032, 453.017, 568.716, 635.197, 838.16, 929.71, 951.735, 980.706, 1005.67, 1013.09, 1073.31, 1096.44, 1169.91, 1194.06, 1220.52, 1294.6, 1364.45, 1378.27, 1419.91, 1439.68, 1452.04, 1515.08, 1515.76, 1527.78, 1537.52, 2900.78, 3054.99, 3056.98, 3091.05, 3129.09, 3130.84, 3144.21, 3147.54, 3857.33], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.89062, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (11739.2, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.72713, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (11739.2, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (28.16, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [0.075855, -0.653293, -8.12501, 0.124308, 0.00481959],
                    [-2.96514, -1.56339, 2.27981, 0.524347, -0.0747834],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.87574, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-6.82153, -3.08415, -0.00938933, -2.14103, 1.08339],
                    [-2.91832, 1.84555, -1.90203, 0.787481, 1.63255],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (6.70808, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-13.1513, -2.25182, -7.19141, 0.0882609, -0.296329],
                    [4.94271, -0.465415, -1.79427, 0.3047, 0.265423],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    structure = SMILES('OOC([O])C(C)C'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'ipropyl',
    E0 = (78.892, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(43.0548, 'amu')),
        NonlinearRotor(
            inertia = ([13.4796, 60.8049, 68.0038], 'amu*angstrom^2'),
            symmetry = 2,
        ),
        HarmonicOscillator(
            frequencies = ([356.818, 392.9, 886.537, 942.7, 948.58, 1032.71, 1150.99, 1182.08, 1373.64, 1414.54, 1419.14, 1475.03, 1484.1, 1485.65, 1497.6, 2942.59, 2947.02, 3022.39, 3024.68, 3093.16, 3094.08, 3174.67], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.41732, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.00534336, -0.00168993, -0.695299, -0.00296174, 0.0144027],
                    [0.0173173, -0.00563888, 0.522882, -0.0138542, -0.0117925],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.41715, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.00534336, -0.00168993, -0.695299, -0.00296174, 0.0144027],
                    [0.0173173, -0.00563888, 0.522882, -0.0138542, -0.0117925],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    structure = SMILES('C[CH]C'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'aRO2',
    E0 = (
        ***u_E0***-280.352,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([109.596, 294.731, 322.38], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([203.396, 271.691, 333.208, 362.121, 443.736, 610.762, 650.657, 811.041, 836.723, 943.052, 953.706, 979.401, 1068.8, 1135.68, 1175.93, 1208.96, 1227.89, 1273.47, 1335.46, 1359.16, 1400.44, 1410.56, 1425.57, 1475.34, 1497.44, 1501.84, 1511.95, 1526.81, 3020.78, 3038.15, 3041.99, 3051.97, 3104.36, 3115.12, 3118.66, 3127.28, 3779.04], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.70329, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (11324.2, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.88813, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0166632, 0.0351443, -6.42061, -0.0339526, 0.032109],
                    [0.0162712, -0.0534413, 0.249651, -0.0444743, 0.0371104],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (29.1293, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.228187, -1.10361, -8.42689, -0.0911091, 0.220529],
                    [-2.9247, -2.27719, 3.32263, 0.224114, 0.0237221],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.630389, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-11.392, -3.4019, -2.75988, 0.955952, 1.21551],
                    [4.72519, -3.50816, 0.927512, 1.28296, -0.0298812],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (5.65032, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-9.13561, -1.53382, -1.335, 0.894626, 0.261718],
                    [4.13364, -3.60089, -0.0392582, 0.143705, 0.554344],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    structure = SMILES('[O]OC(O)C(C)C'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'O2',
    E0 = (
        -7.71678,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(31.9898, 'amu')),
        LinearRotor(inertia=(11.6246, 'amu*angstrom^2'), symmetry=2),
        HarmonicOscillator(frequencies=([1647.57], 'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    structure = SMILES('[O][O]'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'formic_acid',
    E0 = (
        -388.183,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(46.0055, 'amu')),
        NonlinearRotor(
            inertia = ([6.48155, 41.9361, 48.4176], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([635.209, 1056.92, 1136.37, 1315.31, 1416.62, 1843.17, 3055.06, 3751.69], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.782705, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-10.1529, -24.6372, -0.658504, 0.555442, -0.072251],
                    [-0.00247328, 0.00166718, -0.00411729, -0.000537326, 0.00174],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    structure = SMILES('OC=O'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'propene',
    E0 = (***u_E0***+13.5795, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(42.047, 'amu')),
        NonlinearRotor(
            inertia = ([10.754, 54.4504, 62.0929], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([428.285, 590.161, 927.526, 944.169, 952.167, 1032.95, 1074.81, 1193.78, 1332.05, 1414.2, 1454.3, 1486.41, 1500.73, 1719.42, 3024.51, 3068.34, 3103.78, 3131.95, 3139.22, 3219.87], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.26569, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0280319, 0.0230521, -4.32867, -0.0105886, 0.0348881],
                    [-0.0625506, -0.0312973, 0.218109, -0.0243042, -0.0564601],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    structure = SMILES('CC=C'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'aQOOHg',
    E0 = (
        ***u_E0***-215.637,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([108.251, 298.682, 324.325], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([218.615, 301.217, 347.771, 377.435, 465.961, 559.521, 635.336, 704.267, 860.282, 939.06, 964.371, 999.222, 1024.6, 1089.21, 1103.32, 1172.26, 1199.51, 1275.79, 1318.85, 1349.13, 1392.31, 1420.93, 1462.09, 1474.31, 1475.29, 1515.86, 1519.62, 3003.73, 3053.34, 3114.76, 3128.1, 3139.24, 3154.77, 3269.43, 3837.14, 3878.15], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.88062, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (11921.3, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (1.51936, 'amu*angstrom^2'),
            symmetry = 2,
            fourier = (
                [
                    [0.42853, -4.97876, -0.242324, 0.419454, -0.378456],
                    [0.883437, 0.851976, 0.280672, -0.729048, 0.0282063],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (28.7716, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-3.49483, -0.82242, -9.40608, -0.202232, -0.140568],
                    [-4.62352, -2.71105, 2.4583, 0.684636, 0.437269],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.878024, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-7.01376, -11.7291, -0.459596, 0.36951, -0.506873],
                    [7.15972, -2.19461, -1.94739, 1.00392, -0.38238],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (6.65047, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-10.9907, -5.16987, -12.3581, -1.70464, 0.963806],
                    [5.76042, 4.16221, -2.37765, -1.87072, -0.623299],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.877481, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.07774, -6.99902, -0.636487, 0.317483, 0.163866],
                    [-4.84065, 0.210645, 1.51796, 0.539394, 0.0157578],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    structure = SMILES('OOC(O)C(C)[CH2]'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'ibut_peroxyacid',
    E0 = (
        ***u_E0***-403.847,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(104.047, 'amu')),
        NonlinearRotor(
            inertia = ([102.863, 307.792, 321.557], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([250.456, 282.671, 311.436, 445.507, 502.528, 688.257, 782.529, 896.294, 947.275, 971.361, 987.628, 1028.47, 1138.97, 1142.25, 1206.81, 1234.66, 1345.7, 1413.7, 1423.84, 1437.51, 1509.33, 1514.25, 1527.08, 1537.37, 1669.21, 1883.24, 3057.82, 3060.06, 3105.11, 3136.53, 3138.32, 3144.24, 3151.37, 3674.49], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.82506, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.019161, -0.0648524, -6.43947, -0.0451348, 0.0652753],
                    [0.0983832, 0.0107088, 0.788015, 0.0864975, -0.0683473],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.84932, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (12204.2, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (7.12801, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-17.82, -26.6917, -2.57164, 2.95761, 0.527096],
                    [-3.09391, 0.331439, 2.13509, 0.743824, -0.961251],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (25.5027, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-1.98558, -0.533541, -0.0560004, -0.0408061, -0.0030522],
                    [-0.231862, -0.0893396, 0.0383969, 0.0166717, 0.00640862],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.830441, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-9.68523, -3.72198, -0.826831, -0.332061, 0.00270339],
                    [0.162455, 0.206059, 0.0770687, 0.0131142, 0.00569279],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    structure = SMILES('OOC(=O)C(C)C'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'HO2',
    E0 = (4.09903, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(32.9977, 'amu')),
        NonlinearRotor(
            inertia = ([0.811985, 14.9938, 15.8058], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(frequencies=([1168.22, 1433.56, 3624.29], 'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    structure = SMILES('O[O]'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(label = 'CH3',
    E0 = (137.961, 'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(15.0235, 'amu')),
        NonlinearRotor(
            inertia = ([1.7691, 1.77012, 3.53921], 'amu*angstrom^2'),
            symmetry = 6,
        ),
        HarmonicOscillator(
            frequencies = ([502.388, 1422.47, 1426.99, 3120.37, 3309.5, 3310.43], 'cm^-1'),
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    structure = SMILES('[CH3]'),
    energyTransferModel = SingleExponentialDown(alpha0=(***u_ljalpha****250,'cm^-1'), T0=(300,'K'), n=***u_ljn***+0.85),  #From Antonov 2016 for butanol in helium.
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,'angstrom'), epsilon=(318.27557,'cm^-1')),)

species(
    label = "bath_gas",
    #structure = SMILES("N#N"),
    E0 = (0,'kJ/mol'),
    molecularWeight = (28.0062,"g/mol"),
    collisionModel = TransportData(sigma=(***u_sigma****4.63691,"angstrom"), epsilon=(318.27557,'cm^-1')),
    energyTransferModel = None,
)

thermo('aOOHbalkene', 'NASA')
thermo('OH', 'NASA')
thermo('ibutanal', 'NASA')
thermo('aR', 'NASA')
thermo('performic_acid', 'NASA')
thermo('disub_c4ether', 'NASA')
thermo('aQOOHb', 'NASA')
thermo('H', 'NASA')
thermo('aadduct', 'NASA')
thermo('trisub_epoxy', 'NASA')
thermo('ibutenol', 'NASA')
thermo('aQOOH[O]', 'NASA')
thermo('ipropyl', 'NASA')
thermo('aRO2', 'NASA')
thermo('O2', 'NASA')
thermo('formic_acid', 'NASA')
thermo('propene', 'NASA')
thermo('aQOOHg', 'NASA')
thermo('ibut_peroxyacid', 'NASA')
thermo('HO2', 'NASA')
thermo('CH3', 'NASA')

transitionState(label = 'aEpoxyFromb',
    E0 = (
        ***u_E0***-207.388,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([126.886, 284.828, 334.458], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([102.803, 174.619, 183.23, 259.739, 307.211, 354.685, 431.893, 491.986, 636.908, 794.144, 936.587, 949.157, 980.269, 990.311, 1050.23, 1073.98, 1127.95, 1216.25, 1309.89, 1319.5, 1369.05, 1405.47, 1413.5, 1455.75, 1464.53, 1472.67, 1488.53, 1506.54, 2990.68, 2998.13, 3005.07, 3053.25, 3057.88, 3130.04, 3159.49, 3743.16, 3815.86], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.93634, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (3252.58, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.81527, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0414306, 0.00391428, -1.57253, -0.00189899, -0.0660056],
                    [0.0486007, 0.00869661, -0.455389, -0.000139203, 0.00551847],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.809824, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-15.4893, -1.29351, -2.28896, -0.519002, -0.199475],
                    [-0.479078, -1.23882, 1.30764, -0.41539, -0.34272],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.81389, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-14.2862, 1.47145, -2.52974, 1.12214, -0.532258],
                    [10.6589, -8.19425, 3.16117, -2.57616, 1.62871],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-563.942,
        'cm^-1',
    ),)
reaction(
    label = 'aEpoxyFromb',
    reactants = ['aQOOHb'],
    products = ['trisub_epoxy', 'OH'],
    transitionState = 'aEpoxyFromb',
    tunneling = 'Eckart',
)

transitionState(label = 'aHejection',
    E0 = (
        ***u_E0***-152.697,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([106.775, 293.407, 333.786], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([209.226, 288.836, 341.209, 376.954, 458.042, 523.154, 608.278, 672.133, 775.058, 870.874, 941.433, 950.306, 976.116, 998.384, 1111.23, 1119.95, 1153.57, 1199.98, 1339.18, 1363.22, 1403.38, 1424.72, 1493.55, 1498.03, 1500.52, 1507.3, 1521.36, 1697.29, 3032.53, 3035.6, 3061.65, 3100.87, 3103.2, 3112.79, 3114.46, 3591.06], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.8717, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0381376, 0.0182554, -5.86835, -0.0297165, 0.0169255],
                    [-0.0717275, 0.0343337, -0.191143, 0.0537626, -0.0341576],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.74497, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (13834.7, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (27.7128, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-1.69376, 0.913715, -6.98592, 0.110134, 0.00735734],
                    [1.17302, -0.314841, 0.218627, -0.348076, -0.163293],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (7.25932, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-11.2467, -23.7549, -2.07781, 2.42616, 0.828526],
                    [-4.17587, 3.20849, -0.795373, 0.920327, -0.713775],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.827206, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-9.56264, -3.71561, -0.654544, -0.287613, 0.0104807],
                    [0.244162, 0.93656, -0.304691, -0.187755, 0.0141688],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-1034.37,
        'cm^-1',
    ),
)
reaction(
    label = 'aHejection',
    reactants = ['aQOOH[O]'],
    products = ['ibut_peroxyacid', 'H'],
    transitionState = 'aHejection',
    tunneling = 'Eckart',
)

transitionState(label = 'aC4EtherFromg',
    E0 = (
        ***u_E0***-150.419,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([117.073, 272.543, 344.282], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([70.0397, 178.357, 232.645, 299.029, 336.989, 400.28, 467.192, 500.503, 553.515, 621.988, 804.015, 853.907, 923.572, 940.067, 978.009, 1081.99, 1101.56, 1113.96, 1150.39, 1170.78, 1257.8, 1316.03, 1362.92, 1372.53, 1412.58, 1450.42, 1484.43, 1503.88, 1505.38, 3002.16, 3038.17, 3078.22, 3107.36, 3109.87, 3157.82, 3265.29, 3777.05, 3822.28], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.90777, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (12457.2, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.737346, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-12.6752, -1.38671, 1.09967, -1.01478, -0.0586466],
                    [11.6386, -8.76568, 1.19399, 0.827566, -1.23398],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.767906, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-14.7121, -1.86158, -3.95961, 0.30808, 0.0591607],
                    [-6.84879, 1.97033, -0.15024, -0.543022, -0.288272],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-734.692,
        'cm^-1',
    ),
)
reaction(
    label = 'aC4EtherFromg',
    reactants = ['aQOOHg'],
    products = ['disub_c4ether', 'OH'],
    transitionState = 'aC4EtherFromg',
    tunneling = 'Eckart',
)

transitionState(label = 'a-bscissionFromAlkoxy',
    E0 = (
        ***u_E0***-179.799,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([147.681, 280.62, 310.899], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([207.42, 240.211, 262.278, 383.289, 426.935, 466.405, 572.317, 863.349, 924.402, 931.346, 936.696, 946.811, 956.413, 1042.16, 1146.86, 1161.04, 1205.66, 1309.5, 1368.19, 1374.69, 1413.91, 1416.35, 1474.93, 1487.94, 1491.26, 1509.81, 1553.24, 2948.81, 3013.75, 3018.95, 3082.6, 3095.89, 3114.08, 3128.67, 3141.16, 3792.06], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.75614, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0837494, -0.0222853, -5.01634, 0.0183924, -0.0723318],
                    [0.107768, 0.0377329, -0.349244, 0.03609, 0.0761584],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.91393, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0583511, -0.0903397, -4.69449, 0.0586976, -0.0254456],
                    [0.12886, 0.00885545, -0.171631, 0.00149271, 0.104905],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (11.5788, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-4.19221, -16.4028, -2.00312, 0.776432, -0.309218],
                    [8.94153, 3.0401, -4.28669, -0.388114, 0.181502],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (38.2223, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-1.62976, -2.40225, -4.67687, -0.24062, -0.0139783],
                    [1.46996, 1.22853, -0.474431, -0.0937522, -0.188626],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.412496, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-9.68208, -1.50045, 0.217269, -0.103207, 0.0384099],
                    [10.3233, -5.92064, 0.436018, -0.0781665, -0.0273912],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-377.086,
        'cm^-1',
    ),
)
reaction(
    label = 'a-bscissionFromAlkoxy',
    reactants = ['aQOOH[O]'],
    products = ['ipropyl', 'performic_acid'],
    transitionState = 'a-bscissionFromAlkoxy',
    tunneling = 'Eckart',
)

transitionState(label = 'a-bscissionFromg',
    E0 = (
        ***u_E0***-80.5461,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([152.152, 272.628, 318.137], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([194.24, 236.895, 272.231, 357.042, 479.424, 500.437, 530.353, 553.947, 608.66, 659.183, 856.117, 902.738, 941.359, 985.072, 999.066, 1056.41, 1136.22, 1162.57, 1279.32, 1290.27, 1393.62, 1434.38, 1443.76, 1460.28, 1466.67, 1474.52, 1577.73, 3087.56, 3111.25, 3161.05, 3189.8, 3245.68, 3263.18, 3279.31, 3836.38, 3919.65], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.90138, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0140642, 0.0139576, -0.526241, -0.0230466, -0.00374363],
                    [0.0198516, -0.0202211, 0.525326, 0.00115604, -0.00125852],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (38.589, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [2.92386, -5.50892, -4.01036, -1.27895, -0.188126],
                    [1.20397, -0.516438, -0.4117, -0.492601, -0.0618737],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.870421, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.71764, -11.3099, -0.701109, 0.158159, -0.0858062],
                    [6.70038, -1.97056, -1.75763, 0.83517, -0.301571],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (4.5653, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-14.6666, -5.46549, -13.4356, -0.51206, -0.120413],
                    [1.74475, 11.9714, -5.35626, -1.65764, 0.0202362],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.879955, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-4.28183, -7.04387, -0.967512, 0.182637, 0.177603],
                    [-5.86342, -0.633332, 1.48009, 0.603995, 0.0933508],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-463.064,
        'cm^-1',
    ),
)
reaction(
    label = 'a-bscissionFromg',
    reactants = ['aQOOHg'],
    products = ['aOOHbalkene', 'CH3'],
    transitionState = 'a-bscissionFromg',
    tunneling = 'Eckart',
)

transitionState(label = 'aHO2elimFromAlkoxy',
    E0 = (
        ***u_E0***-141.449,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([138.558, 268.631, 322.166], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([109.163, 198.367, 269.094, 317.221, 351.266, 427.366, 495.967, 618.462, 816.861, 937.127, 950.837, 971.263, 978.101, 1079.81, 1149.24, 1174.25, 1210.93, 1313.66, 1339.37, 1349.46, 1402.54, 1414.78, 1419.02, 1447.92, 1496.87, 1502.56, 1509.43, 1522.57, 2974.7, 3001.57, 3039.07, 3047.65, 3099.03, 3107.07, 3114.26, 3129.96, 3739.81], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.70256, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0682609, 0.0315315, -6.57385, -0.0206087, -0.0382532],
                    [-0.00259932, 0.0117228, 0.2637, 0.0213851, 0.0013316],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.6651, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0188758, 0.00327947, -6.71263, 0.0135948, 0.0270924],
                    [0.0221379, -0.0246674, 0.260115, -0.0252229, 0.0501362],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (35.5233, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [2.66483, -2.04672, -9.56381, -0.025678, -0.113269],
                    [-1.04855, -1.81129, -4.1965, 0.123745, 0.0794538],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.704978, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-8.1197, -15.505, 0.390714, 1.54727, -0.127832],
                    [-0.612256, 1.55013, 0.352129, -1.32992, -0.163279],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-558.14,
        'cm^-1',
    ),
)
reaction(
    label = 'aHO2elimFromAlkoxy',
    reactants = ['aQOOH[O]'],
    products = ['ibutanal', 'HO2'],
    transitionState = 'aHO2elimFromAlkoxy',
    tunneling = 'Eckart',
)

transitionState(label = 'aAdductFromRO2',
    E0 = (
        ***u_E0***-232.357,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([135.226, 269.419, 298.627], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([110.275, 194.946, 281.672, 351.055, 409.66, 519.829, 579.248, 667.058, 732.869, 814.481, 938.033, 956.02, 976.748, 986, 1041.69, 1153.86, 1161.37, 1214.64, 1294.7, 1320.46, 1347.15, 1380.69, 1410.01, 1431.58, 1497.94, 1502.27, 1512.54, 1521.45, 1599.11, 1875.6, 2975.62, 3012.94, 3043.74, 3050.93, 3105.51, 3112.33, 3119.15, 3131.31], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.58285, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.00521574, 0.0113194, -5.89413, 0.00387859, 0.0232897],
                    [0.0400969, 0.0215173, -0.265162, 0.0158591, 0.0272878],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.72805, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.00316105, 0.0449751, -5.74893, -0.0134113, 0.0296967],
                    [-0.0341791, 0.00499989, -0.211575, 0.0306649, -0.0520245],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (34.6669, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [1.51362, -3.22421, -6.83025, 0.401228, -0.198104],
                    [-0.25324, 0.950969, 0.352174, -0.416768, -0.243186],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-851.697,
        'cm^-1',
    ),
)
reaction(
    label = 'aAdductFromRO2',
    reactants = ['aRO2'],
    products = ['aadduct'],
    transitionState = 'aAdductFromRO2',
    tunneling = 'Eckart',
)

transitionState(label = 'aHO2elimFromRO2',
    E0 = (
        ***u_E0***-148.364,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([183.191, 242.043, 313.002], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([110.349, 154.398, 225.601, 244.583, 271.653, 347.649, 423.077, 550.641, 579.536, 668.033, 833.077, 901.194, 976.661, 1015.79, 1032.97, 1129.43, 1165.87, 1228.31, 1274.49, 1306.71, 1331.75, 1376.84, 1413.93, 1429.01, 1491.35, 1500.87, 1505.59, 1514.12, 1589.92, 1643.49, 3028.98, 3035.17, 3087.49, 3092.62, 3104.76, 3131.79, 3189.08, 3835.64], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.93948, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (7711.14, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.99913, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0678511, -0.0852014, -5.06861, 0.0772134, 0.0389066],
                    [0.0466309, 0.0155243, -0.604689, 0.037557, 0.0316809],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.611264, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-2.69352, -13.1967, 0.0522179, 0.243816, 0.0480028],
                    [-7.22492, 3.75229, -1.19733, -0.183586, 0.0775098],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-919.308,
        'cm^-1',
    ),
)
reaction(
    label = 'aHO2elimFromRO2',
    reactants = ['aRO2'],
    products = ['ibutenol', 'HO2'],
    transitionState = 'aHO2elimFromRO2',
    tunneling = 'Eckart',
)

transitionState(label = 'aHO2elimFromb',
    E0 = (
        ***u_E0***-170.399,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([132.709, 300.211, 344.816], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([114.263, 149.925, 291.504, 333.842, 356.854, 411.06, 471.821, 593.071, 816.705, 912.346, 957.173, 971.354, 1009.07, 1046.23, 1068.52, 1211.33, 1251.5, 1331.03, 1368.22, 1370.1, 1409.64, 1418.77, 1473.92, 1477.52, 1493.39, 1494.54, 1548.91, 3006.17, 3011.41, 3045.57, 3048.48, 3113.4, 3145.56, 3146.08, 3611.74, 3748.8], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.76284, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0310844, -0.00570696, -1.41008, -0.00698825, 0.0137655],
                    [0.0512381, 0.0155604, -0.275479, 0.000720651, 0.0431242],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.90242, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.060768, -0.00520966, -2.60394, 0.0254367, -0.0348589],
                    [0.0223141, 0.0268882, 0.379605, 0.0111455, 0.0190074],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.8524, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-17.7143, -2.26034, -0.853268, -0.378347, -0.155364],
                    [-11.8452, 3.17438, 0.617441, 0.650788, 0.273519],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (10.0859, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-7.23045, -4.20279, -2.93657, -0.261873, 0.139196],
                    [2.98931, 2.95238, -2.36176, -0.523988, 0.0972299],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.870838, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-2.7314, -18.5771, -0.988972, 2.9949, -0.946688],
                    [-4.51726, 1.25044, -1.96818, -1.96181, -0.622196],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-402.639,
        'cm^-1',
    ),
)
reaction(
    label = 'aHO2elimFromb',
    reactants = ['aQOOHb'],
    products = ['ibutenol', 'HO2'],
    transitionState = 'aHO2elimFromb',
    tunneling = 'Eckart',
)

transitionState(label = 'a-bQOOHIsom',
    E0 = (
        ***u_E0***-156.365,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([167.37, 219.763, 270.184], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([113.099, 226.553, 257.687, 262.693, 315.293, 450.572, 579.565, 585.365, 656.42, 795.199, 936.158, 944.769, 958.912, 969.211, 985.066, 1096.85, 1119.59, 1156.17, 1224.73, 1255.15, 1310.14, 1344.62, 1405.64, 1416.85, 1438.69, 1482.4, 1486.44, 1502.49, 1506.96, 1727.99, 3002.95, 3010.74, 3068.17, 3073.66, 3080.03, 3108.95, 3112.33, 3808.73], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (3.02495, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0309163, -0.0180088, -5.42765, 0.017305, -0.029637],
                    [-0.111589, 0.00109363, 0.973834, -0.0137077, -0.118682],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.8967, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.120598, 0.0573516, -7.2423, -0.0516097, 0.109466],
                    [0.159147, 0.00901551, -0.194564, 0.00563625, 0.12392],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.879202, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-3.89238, -5.55144, -2.11574, 0.143384, 0.0574998],
                    [-7.36439, 2.95289, 0.236388, -0.300403, -0.0593762],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-1953.26,
        'cm^-1',
    ),
)
reaction(
    label = 'a-bQOOHIsom',
    reactants = ['aRO2'],
    products = ['aQOOHb'],
    transitionState = 'a-bQOOHIsom',
    tunneling = 'Eckart',
)

transitionState(label = 'a-bAlkoxyIsom',
    E0 = (
        ***u_E0***-99.3869,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([114.393, 292.834, 338.015], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([122.396, 199.05, 318.675, 329.027, 352.687, 509.202, 578.751, 655.259, 860.484, 922.947, 941.076, 961.104, 978.292, 1000.02, 1073.1, 1076.51, 1125.54, 1222.18, 1272.86, 1322.45, 1382.63, 1398.98, 1405.34, 1422.95, 1481.41, 1486.02, 1500.02, 1506.05, 1920.5, 3014.13, 3022, 3075.38, 3086.86, 3094.1, 3121.13, 3142.25, 3743.01], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.79664, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.090602, 0.0613425, -4.91969, -0.0362368, 0.107169],
                    [-0.0320009, 0.0556285, -0.0199946, 0.0427924, -0.0351845],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.95941, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (11192.3, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (6.30002, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-15.9795, -0.154559, -9.74836, 0.312289, 0.296957],
                    [8.5584, 0.885306, -1.8454, -0.553334, -0.633926],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.883112, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.80336, -7.81219, -0.155698, 0.70751, 0.243159],
                    [-7.30676, 1.52294, 2.09613, 0.382396, -0.201481],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-1899.09,
        'cm^-1',
    ),
)
reaction(
    label = 'a-bAlkoxyIsom',
    reactants = ['aQOOHb'],
    products = ['aQOOH[O]'],
    transitionState = 'a-bAlkoxyIsom',
    tunneling = 'Eckart',
)

transitionState(label = 'a-gQOOHIsom',
    E0 = (
        ***u_E0***-175.7,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([130.451, 224.101, 279.196], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([110.741, 242.629, 264.023, 325.245, 402.202, 480.248, 481.581, 590.487, 604.731, 727.372, 839.824, 897.055, 933.658, 956.419, 982.387, 993.039, 1049.75, 1103.92, 1137.71, 1158.11, 1184.1, 1290.48, 1314.05, 1341.19, 1379.81, 1407.44, 1427.48, 1467.7, 1502.72, 1505.55, 1565.91, 3043.28, 3057.56, 3094.33, 3099.6, 3108.42, 3130.4, 3188.95, 3765.89], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.89935, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.0196208, 0.00695754, -6.63374, 0.0165441, -0.0152383],
                    [0.0353596, -0.0117486, 0.211818, -0.0131717, 0.0569697],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.879087, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-11.8872, -1.28635, -0.960015, -0.68915, -0.318331],
                    [-7.20814, 1.73647, 2.25552, -0.0639089, -0.0107267],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-1620.49,
        'cm^-1',
    ),
)
reaction(
    label = 'a-gQOOHIsom',
    reactants = ['aRO2'],
    products = ['aQOOHg'],
    transitionState = 'a-gQOOHIsom',
    tunneling = 'Eckart',
)

transitionState(label = 'a-gAlkoxyIsom',
    E0 = (
        ***u_E0***-129.003,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([104.434, 300.703, 316.261], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([136.369, 223.9, 323.375, 361.251, 442.038, 477.191, 600.185, 633.188, 746.788, 855.992, 927.745, 945.08, 950.896, 976.739, 1015.51, 1029.98, 1109.11, 1143.48, 1169.53, 1186.06, 1287.44, 1302.92, 1351.98, 1375.04, 1421.96, 1441.37, 1462.42, 1508.37, 1512.55, 1709.86, 3019.18, 3037.28, 3040.54, 3081.58, 3086.1, 3088.31, 3168.35, 3625.92], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (2.90129, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [0.00988811, 0.0129183, -7.46067, 0.0156907, 0.00775912],
                    [-0.0530157, -0.00916455, 0.201273, -0.00704052, -0.0345641],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (7.83757, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-10.1642, -6.87662, -11.5055, -0.167705, 0.359694],
                    [6.71119, 3.07803, -2.44772, -0.815656, -0.429932],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.886744, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-6.37722, -7.94463, -0.387257, 0.635603, 0.199731],
                    [-5.69094, 0.568579, 2.05676, 0.478495, -0.165075],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-1881.06,
        'cm^-1',
    ),
)
reaction(
    label = 'a-gAlkoxyIsom',
    reactants = ['aQOOHg'],
    products = ['aQOOH[O]'],
    transitionState = 'a-gAlkoxyIsom',
    tunneling = 'Eckart',
)

transitionState(label = 'aDoublebscission',
    E0 = (
        ***u_E0***-126.258,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([122.242, 309.106, 403.728], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([65.2546, 105.302, 174.876, 260.989, 275.22, 305.007, 390.651, 404.352, 454.817, 518.661, 604.135, 764.066, 882.168, 942.189, 971.481, 1034.49, 1049.98, 1100.06, 1146.11, 1188.12, 1232.57, 1263.32, 1309.06, 1396.3, 1417.18, 1440.48, 1490.71, 1507.87, 1515.29, 3042.01, 3094.58, 3113.69, 3116.52, 3140.7, 3145.92, 3246.48, 3795.21, 3806.21], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (0.839755, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-10.8497, -8.9497, 0.33454, 0.446295, 0.247068],
                    [7.40949, -1.09604, -0.856527, 0.726692, 0.104591],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (0.798657, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-5.71601, -1.44166, 0.664542, -0.256599, 0.0748653],
                    [-4.32334, 2.86681, -0.321223, 0.0389991, 0.0624977],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (2.76151, 'amu*angstrom^2'),
            symmetry = 3,
            fourier = (
                [
                    [-0.0308912, 0.084572, -4.64889, -0.0512308, 0.0349302],
                    [-0.0621818, 0.0207915, 0.249188, 0.020484, -0.0628059],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-916.757,
        'cm^-1',
    ),
)
reaction(
    label = 'aDoublebscission',
    reactants = ['aQOOHg'],
    products = ['propene', 'formic_acid', 'OH'],
    transitionState = 'aDoublebscission',
    tunneling = 'Eckart',
)

transitionState(label = 'aAlkoxyIsom',
    E0 = (
        ***u_E0***-189.932,
        'kJ/mol',
    ),
    modes = [
        IdealGasTranslation(mass=(105.055, 'amu')),
        NonlinearRotor(
            inertia = ([112.161, 276.525, 369.402], 'amu*angstrom^2'),
            symmetry = 1,
        ),
        HarmonicOscillator(
            frequencies = ([95.6631, 240.848, 257.483, 310.488, 344.758, 394.382, 457.94, 522.414, 643.943, 743.65, 818.479, 896.381, 904.414, 923.651, 985.063, 1006.17, 1095.64, 1130.67, 1157.16, 1164.2, 1223.59, 1314.72, 1358.56, 1397.96, 1415.01, 1477.49, 1494.35, 1499.63, 1511.26, 2577.42, 2679.62, 2925.22, 3037.5, 3042.9, 3092.59, 3099.5, 3138.41, 3576.91], 'cm^-1'),
        ),
        HinderedRotor(
            inertia = (49.5656, 'amu*angstrom^2'),
            symmetry = 1,
            fourier = (
                [
                    [-0.617948, 0.466932, -13.8684, -0.636883, 0.149652],
                    [3.04884, 3.39491, -4.24072, -0.568851, -0.398113],
                ],
                'kJ/mol',
            ),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (11.7328, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (13398.2, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
        HinderedRotor(
            inertia = (10.5487, 'amu*angstrom^2'),
            symmetry = 3,
            barrier = (15377.6, 'J/mol'),
            quantum = True,
            semiclassical = True,
        ),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 2,
    frequency = (
        ***u_negfreq****-138.269,
        'cm^-1',
    ),
)
reaction(
    label = 'aAlkoxyIsom',
    reactants = ['aRO2'],
    products = ['aQOOH[O]'],
    transitionState = 'aAlkoxyIsom',
    tunneling = 'Eckart',
)

transitionState(
    label = 'aRO2Form',
    spinMultiplicity = 2,
    opticalIsomers = 2,
)
reaction(
    label = 'aRO2Form',
    reactants = ['aR', 'O2'],
    products = ['aRO2'],
    transitionState = 'aRO2Form',
    kinetics = Arrhenius(A=(***u_ilt****4.29702e-13,'cm^3/(molecule*s)'), n=0.395835, Ea=(-582.4,'K'), T0=(1,"K")),
)

transitionState(
    label = 'aAdductSplit',
    spinMultiplicity = 2,
    opticalIsomers = 2,
)
reaction(
    label = 'aAdductSplit',
    reactants = ['ibutanal', 'HO2'],
    products = ['aadduct'],
    transitionState = 'aAdductSplit',
    kinetics = Arrhenius(A=(***u_ilt****1.75e-11,'cm^3/(molecule*s)'), n=0.35126, Ea=(0.0,'K'), T0=(1,"K")),
)

network(
    label = 'C4H9O3',
    isomers = ['aQOOHb', 'aQOOH[O]', 'aQOOHg', 'aRO2', 'aadduct'],
    reactants = [['aR', 'O2']],
    bathGas = {'bath_gas': 1.0}
)
pressureDependence(
    'C4H9O3',
    Tmin=(180.0,'K'), Tmax=(1500.0,'K'), Tcount=20,
    Pmin=(0.01,'bar'), Pmax=(100.0,'bar'), Pcount=20,
    maximumGrainSize = (0.5,'kcal/mol'),
    minimumGrainCount = 200,
    method = '***u_method***',
    #method = 'reservoir state',
    #method = 'modified strong collision',
    interpolationModel = ('chebyshev', 10, 8),
    activeKRotor = True, 
    activeJRotor = True,
    rmgmode = False,
)

import itertools


class AlphaFactory:

    def __init__(self):

        self.lookbacks = [
            5,
            10,
            20,
            50,
            100,
            200
        ]

        self.vol_windows = [
            10,
            20,
            60
        ]

    def generate(self):

        alphas = []

        # Momentum family

        for lb in self.lookbacks:

            alphas.append({

                "type":
                "momentum",

                "lookback":
                lb

            })

        # Mean reversion family

        for lb in self.lookbacks:

            alphas.append({

                "type":
                "mean_reversion",

                "lookback":
                lb

            })

        # Breakout family

        for lb in self.lookbacks:

            alphas.append({

                "type":
                "breakout",

                "lookback":
                lb

            })

        # Combo family

        for combo in itertools.product(
            self.lookbacks,
            self.vol_windows
        ):

            alphas.append({

                "type":
                "momentum_vol",

                "lookback":
                combo[0],

                "vol":
                combo[1]

            })

        return alphas
from pathlib import Path


OUTPUT_DIR = Path(
    "outputs"
)

OUTPUT_DIR.mkdir(
    exist_ok=True
)


class ExportPipeline:

    def run(
        self,
        alpha_data,
        research,
        risk
    ):

        alpha_data[
            "alpha_universe"
        ].to_csv(

            OUTPUT_DIR /
            "alpha_universe.csv"

        )

        alpha_data[
            "ranking"
        ].to_csv(

            OUTPUT_DIR /
            "alpha_ranking.csv",

            index=False

        )

        research.to_csv(

            OUTPUT_DIR /
            "research_results.csv",

            index=False

        )

        risk[
            "mc_summary"
        ].to_csv(

            OUTPUT_DIR /
            "monte_carlo_summary.csv",

            index=False

        )
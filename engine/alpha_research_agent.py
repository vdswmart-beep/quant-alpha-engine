from engine.alpha_llm_generator import (
    AlphaLLMGenerator
)


class AlphaResearchAgent:

    def __init__(self):

        self.generator = (
            AlphaLLMGenerator()
        )

    def generate_ideas(
        self,
        n=100
    ):

        return self.generator.generate_batch(
            n
        )
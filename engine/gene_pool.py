import json
from pathlib import Path


class GenePool:

    def __init__(self):

        self.path = Path(
            "research/gene_pool.json"
        )

        if not self.path.exists():

            self.path.write_text("[]")

    def add(self, alpha):

        genes = self.load()

        genes.append(alpha)

        self.path.write_text(
            json.dumps(
                genes,
                indent=4
            )
        )

    def load(self):

        return json.loads(
            self.path.read_text()
        )
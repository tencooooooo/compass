from __future__ import annotations

from typing import Any

from api.services.data_loader import REPO_ROOT
from lab.experiments.experiment_registry import ExperimentRegistry
from lab.experiments.experiment_report import ExperimentReport
from lab.experiments.experiment_runner import ExperimentRunner


class ExperimentEngine:
    """Runs reproducible Compass baseline-vs-candidate experiments."""

    @classmethod
    def run(cls) -> dict[str, Any]:
        registry = ExperimentRegistry()
        runner = ExperimentRunner()
        definitions = registry.definitions()
        results = [runner.run(definition) for definition in definitions]
        outputs = ExperimentReport().write(results)
        registry_path = registry.save_results(results)
        return {
            "success": True,
            "experiments": len(results),
            "outputs": outputs,
            "registry": str(registry_path.relative_to(REPO_ROOT)),
        }


if __name__ == "__main__":
    print(ExperimentEngine.run())

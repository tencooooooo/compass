from __future__ import annotations

from typing import Any

from api.services.data_loader import REPO_ROOT
from lab.experiments.candidate_replay import CandidateReplay
from lab.experiments.experiment_registry import ExperimentRegistry
from lab.experiments.experiment_report import ExperimentReport
from lab.experiments.experiment_runner import ExperimentRunner


class ExperimentEngine:
    """Runs reproducible Compass baseline-vs-candidate experiments."""

    @classmethod
    def run(cls) -> dict[str, Any]:
        # スコアリング候補ルールのメトリクスをスナップショットから再生成してから比較する。
        # データ未復元の環境(ローカルのmainブランチ等)でもエンジン全体は止めない。
        try:
            replay = CandidateReplay().run()
        except Exception as error:  # noqa: BLE001 - リプレイ失敗は実験全体の失敗にしない
            replay = {"success": False, "reason": str(error)}
        registry = ExperimentRegistry()
        runner = ExperimentRunner()
        definitions = registry.definitions()
        results = [runner.run(definition) for definition in definitions]
        outputs = ExperimentReport().write(results)
        registry_path = registry.save_results(results)
        return {
            "success": True,
            "experiments": len(results),
            "replay": replay,
            "outputs": outputs,
            "registry": str(registry_path.relative_to(REPO_ROOT)),
        }


if __name__ == "__main__":
    print(ExperimentEngine.run())

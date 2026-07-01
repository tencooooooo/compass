from pathlib import Path


class PromptManager:
    """Loads Compass prompts without binding agents to a specific AI provider."""

    def __init__(self, prompt_root: Path | None = None):
        self.prompt_root = prompt_root or Path(__file__).resolve().parents[1] / "prompts"

    def load_prompt(self, prompt_name: str, fallback: str = "") -> str:
        path = self.prompt_root / prompt_name
        if not path.exists():
            return fallback
        return path.read_text(encoding="utf-8")

    def build_agent_prompt(self, agent_name: str, task: str, context_summary: str = "") -> str:
        base = self.load_prompt("agent_prompt.md", "You are a Compass agent. Use only provided Compass context.")
        return "\n\n".join(
            part
            for part in [
                base,
                f"Agent: {agent_name}",
                f"Task: {task}",
                f"Context Summary: {context_summary}" if context_summary else "",
            ]
            if part
        )

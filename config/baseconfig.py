from dataclasses import dataclass

@dataclass(frozen=True)
class ProjectConfig:
    NAME: str = "NormBot"
    SLUG: str = "normbot"
    VERSION: str = "0.0.0.1 beta"
    DESCRIPTION: str = "A Security-First, Self-Hosted AI Agent"
    AUTHOR: str = "nonesubham"

@dataclass(frozen=True)
class BOTConfig:
    COMMAND_PREFIX: str = "normbot"
    PREFIX_SEPARATOR: str = ":" 


bot_config = BOTConfig()
project_config = ProjectConfig()
# Config & Logging Template

A minimal, language‑agnostic template focused on application configuration and structured logging. The Python reference implementation uses Pydantic for typed config and YAML for config files, plus a simple logging helper.

## Features
- YAML‑based configuration loaded from one or more files.
- Typed validation with Pydantic and clear error messages.
- Simple logging setup via the provided helper.
- Custom exceptions for common config failure modes.

## Project structure
- 'backend/config/models.py' — Pydantic models for typed configuration.
- 'backend/config/load_config.py' — YAML loading, merging, and validation.
- 'backend/core/logging/get_logger.py' — Logger factory using config.
- 'backend/resources/config/application.yml' — Default config example.
- 'backend/config/exceptions.py' — Config exceptions.

## Quick start

1) Define configuration in YAML:
```yaml
# backend/resources/config/application.yml
app_name: App
app_version: 1.0.0
logging:
  level: INFO
  format: "%(asctime)s [%(levelname)s] - %(name)s - %(message)s"
```

2) Load config and get a logger:
```python
from config import load_config
from core.logging.get_logger import get_logger

cfg = load_config()  # reads from defaults like 'backend/resources/config/application.yml'
logger = get_logger(cfg.logging, __name__)

logger.info(f"Starting {cfg.app_name} v{cfg.app_version}")
```

## Validation and errors
- Missing file: raises 'ConfigFileNotFoundException'.
- Invalid data: prints detailed validation errors and raises 'ConfigException'.

## Extending
- Add fields to 'BaseConfig' and/or new Pydantic models in 'backend/config/models.py'.
- Reference new sections from your YAML under the same keys.

## Requirements
- Python 3.10+  
- Dependencies: PyYAML, Pydantic

## License
Use freely as a starting point for projects that need consistent configuration and logging.

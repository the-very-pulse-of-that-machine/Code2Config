# Code2Config

> **Automated parameter extraction and real-time visualization suite.**

**Code2Config** is a refactoring tool designed for developers who build with AI. It identifies scattered hard-coded constants, refactors them into a unified dynamic configuration interface, and deploys a local web dashboard for real-time parameter tuning.

---

## 🚀 Quick Start

### 1. Triggering the Tool
In your AI-integrated terminal (e.g., Claude Code, Cursor), use the keyword:
> **UseCode2Config**

Or provide a prompt:
> *"I need to visually tune the parameters of this project."*

### 2. Execution Steps
1. **Backup**: Always back up your project folder before starting the refactoring.
2. **Automated Workflow**: The AI will execute Phase 1 (Analysis), Phase 2 (Injection), and Phase 3 (Deployment) sequentially.
3. **Launch Dashboard**:
   ```bash
   python ui_bridge.py
   ```
    Frontend of dashboard will be launched at 127.0.0.1:8000 if default
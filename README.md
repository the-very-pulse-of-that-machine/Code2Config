# Code2Config

> **Automated parameter extraction and real-time visualization suite.**

**Code2Config** is a refactoring tool designed for developers who build with AI. It identifies scattered hard-coded constants, refactors them into a unified dynamic configuration interface, and deploys a local web dashboard for real-time parameter tuning.

---
## 👁️ What the OUTPUT looks like

**Your code, visualized.** The tool analyzes your codebase and transforms abstract variables into an **interactive dashboard**. 
- **Auto-Discovery**: It finds your "magic numbers" and builds the UI for them.
- **Semantic Sync**: Each UI component is labeled based on the variable's actual function in your project.
- **Live Link**: Any adjustment on the dashboard propagates directly back into your `program` files.


![html](/asset/html.png)

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


---

## 🧠 Design Philosophy: 

We believe that **tuning a system should be as intuitive as playing an instrument.** Most codebases are black boxes where logic and parameters are tangled together. Code2Config acts as a dictionary of all members of a project, where you get concise explanation as well as fast manipulation

### The Three-Stage Process (Our Pipeline):

1. **Extraction (De-coding)**: 
   Instead of just searching for numbers, we perform a **Semantic Scan** performed by agent. We identify which constants actually drive your system's behavior and translate their purpose into "Plain English" causal relationships.
   
2. **Injection (Config Refactoring)**: 
   We don't rewrite your logic; we **liberate it**. By replacing hard-coded values with dynamic hooks, we create a "Hot-Reloading" tunnel that allows parameters to flow in and out of your program while it's still running.

3. **Manifestation (UI Generation)**: 
   The final dashboard isn't a template—it's a **Mirror**. The UI is dynamically constructed from the "Mental Map" of your specific project, ensuring that every slider you see has a direct, documented impact on your code.


![arch](/asset/arch.png)

---
## 📝 TODO / Roadmap

### 🟢 Phase 1: Core Enhancement (Stability)
- [ ] **Multi-Language Hooks**: Expand the refactoring engine to support C++ (Header-only) and JavaScript parameter injection.
- [ ] **Enhanced Syntax Validation**: Automatically run static analysis tools (e.g., `ruff` or `flake8`) post-injection to ensure original code style remains intact.
- [ ] **Automatic Type Inference**: Use type hints to automatically assign precise Web UI controls (e.g., `bool` to toggles, `int` to integer steppers).

### 🟡 Phase 2: User Experience (The "Intuitive" Part)
- [ ] **UI Layout Editor**: Allow users to custom group or reorder parameters via a drag-and-drop interface on the web dashboard.
- [ ] **Preset System**: Save current parameter states as "Snapshots," enabling one-click switching between different experimental configurations.
- [ ] **Mobile Optimization**: Optimize the interface for touch, enabling remote parameter control via smartphones or tablets.

### 🔴 Phase 3: AI Intelligence (Advanced)
- [ ] **Self-Tuning Suggestions**: Implement a feedback loop where AI suggests optimal parameter ranges based on program output.
- [ ] **Natural Language Search**: Add a search bar that supports descriptive queries (e.g., typing *"Make it faster"* automatically locates the `MAX_SPEED` slider).
- [ ] **One-Click Revert**: Add a safety command to automatically remove injected hooks and revert the project to its original hard-coded state.
---
#### Built by 91mrqiao.
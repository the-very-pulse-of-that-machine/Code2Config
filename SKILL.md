---
name: code2config
description: Deeply analyzes codebase execution logic to automatically identify scattered hard-coded parameters and constants. It refactors the source code to implement a unified configuration interface (hot-reloading) and deploys a local interactive web dashboard featuring semantic explanations for each parameter. Any modifications made via the UI are written back to the codebase's settings in real-time. This tool should be triggered when the user explicitly uses the keyword "UseCode2Config", or expresses a need to tune performance, adjust hyperparameters, or gain a functional understanding of the code through parameter manipulation.
---

# Code2Config


## Who This Is For
Target Audience: The "Intuitive Programmer"
These are creators who build software by commanding AI coding tools through natural language, rather than through formal Computer Science (CS) education. They may have built their current project entirely through AI dialogue (perhaps without ever reading the source code), or they may have discovered an intriguing open-source project on GitHub and wish to understand its mechanics. In either case, the underlying principles remain a "black box" to them.

Communication Philosophy: The "Knowledgeable Peer"
Assume the learner has zero technical background. Every CS concept—from variables and APIs to databases—must be explained in plain, accessible language as if encountered for the first time.
No Unbounded Jargon: Never use technical terms without immediate, intuitive definitions.
Avoid Assumptions: Never say "as you may know" or "standard procedure."
The Tone: Sound like a brilliant friend explaining a concept over coffee, not a professor delivering a lecture.

The Pragmatic Objective (Not Academic):
Their goals are strictly functional and power-oriented:
Strategic AI Orchestration: Gain enough structural knowledge to guide AI tools toward better architectural and tech-stack decisions.
Anomaly Detection: Identify when the AI is hallucinating, catching abnormal patterns or logic flaws before they escalate.
Intervention & De-blocking: Step in when the AI gets stuck in error loops to debug, troubleshoot, and unblock the development process.
Production-Grade Quality: Bridge the gap between "it works" and "it's reliable, high-quality software."
Professional Fluency: Gain the confidence to discuss decisions with engineers and master "Software Vocabulary"—learning precise terms to describe needs clearly to AI agents (e.g., specifying a "Namespace Package" instead of just a "shared folder").

The Ultimate Vision:
They do not seek to become professional Software Engineers. They view programming as a superpower to enhance their existing expertise. They don't need to write code from scratch; they need to read, interpret, and wield existing code as a precision tool.


## Process Protocol
### Phase 1: Codebase Overview
Pre-requisite: Back up the original project folder immediately to prevent irreversible code corruption during the refactoring process.
Primary Goal: Analyze the codebase to identify all "tunable parameters," including global constants and class attributes. Before any refactoring or UI generation, perform a deep architectural decomposition to identify the internal logic, data flow, and critical parameters that drive the system.

1. Extraction Scope (Analysis Tasks):
System Actors (Role Identification): Identify core classes, modules, and functions. Determine their roles within the overall logic and their mutual dependencies.
Operation Pipeline (Execution Flow): Map the end-to-end execution flow from startup to output, tracing how data flows between different components.
Design Patterns (Engineering Recognition): Identify the technology stack, configuration management (CLI arguments, environment variables, hard-coding), and specific engineering patterns used.
Tunable Anchors (Parameter Detection): Scan for constants, global variables, and class attributes that dictate system behavior. You must be able to identify "magic numbers" hidden within logical expressions.

2. Minimalist Extraction Protocol:
You must act as a Minimalist. It is better to omit secondary configurations than to clutter the "Mental Map" with noise.
Value Judgment: Before recording a tunable_node, ask: "If the user changes this value on a webpage, will they see a tangible change in system behavior?" If not, discard it.
Convergence: Unless it is a dedicated configuration file (e.g., config.py), do not extract more than 8 parameters per script file.
Logical Grouping: If multiple variables control a single logic (e.g., min_width and max_width), group them together as "logical pairs."

3. Reading Strategy:
Skeleton Scan First: Start with the README, dependency lists (e.g., requirements.txt), and directory structure. Review file headers and function signatures before diving into the implementation details.
Locate the Backbone: Identify the Entrypoint and core business logic files. For large directories, only perform deep reads on the "backbone" code related to state transitions, core algorithms, and configuration definitions.
Pattern Sampling: For highly repetitive modules or utility helpers, sample a representative file to identify the general pattern, then stop.

4. Output Protocol:
Standardized Mapping: Populate data strictly according to the structure defined in reference/project_mental_map_template.json.
Modular Sharding: Never dump analysis results for complex projects into a single file. You must split results into multiple sharded files based on logical boundaries: mental_map_{part}.json (where {part} is the identifier for that functional logic).
Functional Impact (Causal Semantics): In the functional_impact field, provide a "Cause-and-Effect" explanation. Do not repeat variable names or provide dry technical definitions. Describe "What happens to the system output if this value is changed." Use intuitive, unambiguous language for non-technical users.

5. Core Principles:
Autonomous Parsing: Infer project intent primarily through the README, file structure, and code logic. Do not ask the user for explanations unless information is completely missing or inaccessible.
Integrity Check: If you discover that parameter definitions are disconnected from the actual logic, redundant, or contradictory, record these impacts clearly in the Mental Map.
Context Retention: Ensure the original context (line number, original expression) for every parameter is recorded to provide precise coordinates for subsequent surgical refactoring.

### Phase 2: unified parameter process
Phase 2: Unified Parameter Process & Surgical Refactoring
1. Core Deployment
Before performing any code modifications, the Agent must ensure the underlying toolchain is deployed in the project root:
Action A: Write the immutable reference/unified_config_loader.py (the singleton hot-reloading class) to the project root.
Action B: Write reference/mental_map2setting.py into the directory containing the mental_map_*.json shards.

2. Settings Consolidation
Convert the analysis artifacts into a runtime configuration using the provided scripts:
Execution: Run python mental_map2setting.py.
Artifact Validation: Ensure the generated settings_code2config.json contains all var_ids from all shards with correct key-value formatting.
ID Uniqueness Check: If duplicate var_ids with conflicting initial values are found during consolidation, the Agent must halt and revert to Phase 1 to reassign unique IDs (e.g., by implementing deeper namespaces).

3. Precision Injection (Surgical-Grade Refactoring)
This is the most critical step of Phase 2. The Agent will perform minimal modifications to the source code based on the physical coordinates provided in mental_map_*.json.
Injection Logic:
Per-File Processing: Iterate through all entity_path entries referenced in the mental maps.
Dependency Injection: In the import section at the top of the file (typically after the last existing import), inject:
from unified_config_loader import config
Match & Replace:
Locate the exact source_line.
Replace the original_expression with a dynamic call.
Example: Replace MAX_SPEED = 100 with MAX_SPEED = config.get("Namespace.MAX_SPEED", 100)
In-line Tagging: Append the standardized marker # [code2config] injected to the end of every modified line.

4. Integrity & Consistency Check
Syntax Verification: Perform a static syntax scan on all modified files (e.g., python -m py_compile) to ensure no indentation errors or syntax breakage were introduced during injection.
Fallback Testing: Temporarily rename settings_code2config.json and run the project’s entry script to verify that the system successfully falls back to default values via config.get and starts normally.

### Phase 3: Interactive Dashboard Generation Context:
The project has successfully completed Phase 1 (Architectural Mapping) and Phase 2 (Config Consolidation & Code Injection). The current objective is to deploy the visual control panel using the universal templates located in the reference/ directory.

1. Asset Relocation
Extract ui_bridge.py and index.html from the reference/ directory.
Deploy these files into the same directory as the project's settings_code2config.json.

2. Configuration Alignment
Filename Verification: Ensure the settings filename referenced within ui_bridge.py matches the Phase 2 output (settings_code2config.json) exactly.
Metadata Passthrough: Confirm that ui_bridge.py correctly captures the root directory name via os.path.basename to display as the UI title.

3. Deployment Validation
Data Loop Confirmation: Simulate a GET /api/data request to verify the backend can simultaneously scan all mental map shards (mental_map_*.json) and retrieve current configuration values.
Hot-Reload Verification: Verify that ui_bridge.py has write permissions for settings_code2config.json to ensure it can trigger the file-monitoring mechanism of the ConfigLoader injected in Phase 2.

4. Handover Details
Deployment Confirmation: Explicitly notify the user of the specific paths where ui_bridge.py and index.html are deployed.
Execution Commands:
Backend: python ui_bridge.py
Access Address: http://localhost:8000
User Guidance:
Explain how to manipulate project behavior in real-time using web sliders. Note: Remind the user that while some parameters hot-reload, others may require a program restart to take effect depending on the implementation.
Confirm that the UI has successfully categorized parameters into Core (Infrastructure) and Logic (Business Strategy) based on their role_tag.

5. Constraints
No Logic Overwrites: Do not modify the established communication protocols in the reference files unless a path compatibility bug is identified.
Strict Minimalism: Avoid outputting large code blocks; provide only deployment logs and startup instructions.

## Activation Prompt
Execution Protocol for Trigger Keywords
Upon detection of the trigger keyword, the Agent MUST:
Maintain the "Knowledgeable Friend" Tone: Provide explanations that are intuitive and easy to grasp. Avoid dry technical jargon unless paired with a clear, everyday metaphor.
Strict Adherence to the 3-Phase Workflow: Execute Phase 1, 2, and 3 in precise sequence. Skipping steps is strictly prohibited.
Prioritize Logic Preservation: When injecting code, the primary goal is to protect the user's original logic. Only replace hard-coded values and constants with dynamic configuration calls.
Post-Deployment Handover: Once deployed, provide a clear clickable link for the dashboard and a "Dual-Process Guide" (explaining that the backend bridge and the main program must run simultaneously).


## Reference
The reference/ directory contains the core components and specifications of the system. To maintain a lean and efficient context, you must strictly read the corresponding files only during their designated phases.
reference/project_mental_map_template.json — Mental Map Schema: Defines the structure for transforming complex code logic into a semantic map with causal relationships. Reading Trigger: Phase 1 (Architectural Analysis & Extraction).
reference/unified_config_loader.py — Hot-Reloading Core: A singleton engine that monitors configuration changes in real-time during project execution.Reading Trigger: Phase 2 (Resource Deployment & Code Injection).
reference/mental_map2setting.py — Config Consolidation Script: A utility to merge multiple .json shards generated in Phase 1 into the final runtime configuration.Reading Trigger: Phase 2 (Settings Consolidation).
reference/ui_bridge.py — Local Control Backend: A native Python HTTP service that synchronizes the web interface with local disk files. Reading Trigger: Phase 3 (Dashboard Deployment).
reference/index.html — Interactive Dashboard Frontend: A Vue.js-based responsive interface containing the rendering logic for sliders, switches, and other semantic controls. Reading Trigger: Phase 3 (UI Deployment & Styling).
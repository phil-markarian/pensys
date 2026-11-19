# Research notes

- Keep general notes in `research/NN-topic.md`. Give each proposed or implemented tool its own `research/_tools/<tool-name>/` folder with a README. Keep downloaded references under `research/_references/` and cloned repositories under `research/_repos/`. Link related notes and tool designs with relative paths.
- Write for personal projects and team deployments. Keep the general design provider- and framework-neutral. Use Cloudflare, AWS, Google Cloud, Azure, and self-managed setups as relevant examples. Include other providers where they illustrate a distinct pattern.
- Start a technical note with a short explanation and an editable Mermaid overview. Follow it with detailed examples, each with its own heading and Mermaid block. Stack alternative paths vertically as separate previews. Prefer short left-to-right paths within each block and use legible arrows in light and dark themes.
- Store reusable Mermaid sources as `.mmd` files under `research/_references/diagrams/` and add them to its index. Link to the source directly below each preview. Edit the canonical source, then run `./tool sync_diagrams` to refresh linked previews.
- Label actors, traffic direction, controls, decisions, and boundaries where relevant. Use a colon in explanatory labels such as `Reachability: who can connect?`. Identify the typical control owner and the evidence a reviewer should record when the topic calls for it.
- In tool diagrams, name who or what produces each input, the artifact the tool reads, and the output it writes. Label optional inputs and identify downstream consumers where relevant.
- Put current official documentation immediately below the relevant diagram or explanation. Verify links when adding or updating them. Identify community observations as such and distinguish their claims from project conclusions.
- Mark material proposals, source claims that could not be verified, and unimplemented interfaces with a bold status label and a footnote. Identify agreed design decisions separately from implemented behavior.
- Keep prose concise and retain existing examples and references when expanding a note. Verify relative links and Mermaid block structure after edits. Check rendered diagrams when a compatible preview is available.

# Design review

- Evaluate the user's plans and ideas critically. Check assumptions, compare viable options, and explain tradeoffs that could change the decision. State disagreements directly and propose a better approach when the evidence supports one.
- Ground feedback in the project's goals and available evidence. Flag uncertainty and suggest a concrete way to resolve it when it matters. Agree when the proposal holds up.

# Tool entry points

- Put standalone Python scripts in `scripts/` and expose each as `./tool <filename_without_extension> [args...]`. Use descriptive names and supply `--help` on each script. The dispatcher discovers scripts by filename and forwards arguments and exit status.
- Keep the same thin dispatch model for Pensys packages. Group public commands under `pensys internal`, `pensys external`, or `pensys evidence` as appropriate. Route named commands to independently runnable entry points and keep analysis logic in the owning package.

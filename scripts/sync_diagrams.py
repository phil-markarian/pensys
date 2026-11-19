"""Refresh inline Mermaid previews from their linked canonical sources."""

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"
LIBRARY = (RESEARCH / "_references" / "diagrams").resolve()
MERMAID_FENCE = re.compile(r"^```mermaid[^\S\n]*$", re.MULTILINE)
INDEX_LINK = re.compile(r"\]\(([^)\n]+\.mmd)\)")
PREVIEW = re.compile(
    r"(^```mermaid[^\S\n]*\n)((?:(?!^```[^\S\n]*$).)*)(^```[^\S\n]*\n"
    r"\n\[Mermaid source\]\(([^)\n]+)\)$)",
    re.MULTILINE | re.DOTALL,
)


def refresh(document: Path) -> str:
    def replace(match: re.Match[str]) -> str:
        source = (document.parent / match[4]).resolve()
        if not source.is_relative_to(LIBRARY) or source.suffix != ".mmd":
            raise ValueError(f"{document.relative_to(ROOT)}: invalid Mermaid source {match[4]}")
        try:
            body = source.read_text(encoding="utf-8")
        except OSError as error:
            raise ValueError(f"{document.relative_to(ROOT)}: {error}") from error
        if not body.strip() or re.search(r"^```[^\S\n]*$", body, re.MULTILINE):
            raise ValueError(f"{source.relative_to(ROOT)}: expected unfenced Mermaid source")
        if not body.endswith("\n"):
            body += "\n"
        return match[1] + body + match[3]

    current = document.read_text(encoding="utf-8")
    if len(MERMAID_FENCE.findall(current)) != len(PREVIEW.findall(current)):
        raise ValueError(f"{document.relative_to(ROOT)}: Mermaid preview needs a source link")
    return PREVIEW.sub(replace, current)


def check_index() -> None:
    index = LIBRARY / "README.md"
    listed = set(INDEX_LINK.findall(index.read_text(encoding="utf-8")))
    sources = {path.relative_to(LIBRARY).as_posix() for path in LIBRARY.rglob("*.mmd")}
    problems = [f"unindexed source: {path}" for path in sorted(sources - listed)]
    problems.extend(f"missing indexed source: {path}" for path in sorted(listed - sources))
    if problems:
        raise ValueError("\n".join(problems))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report stale previews without editing")
    args = parser.parse_args()
    documents = sorted(
        path for path in ROOT.rglob("*.md")
        if not {".git", "_repos"}.intersection(path.relative_to(ROOT).parts)
    )
    updates = {}
    try:
        if args.check:
            check_index()
        for document in documents:
            updated = refresh(document)
            if updated != document.read_text(encoding="utf-8"):
                updates[document] = updated
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")

    for document, updated in updates.items():
        if not args.check:
            document.write_text(updated, encoding="utf-8")
        status = "Stale" if args.check else "Updated"
        print(f"{status}: {document.relative_to(ROOT)}")
    if not updates:
        print("Mermaid previews are in sync.")
    return int(args.check and bool(updates))


if __name__ == "__main__":
    raise SystemExit(main())

"""Generate docs/spine-{light,dark}.svg for the profile README.

The verification spine: OpenGATE gating the tools, and the same pattern
shipped in products and distilled into reference repos.
Hand-tuned layout; run from the repo root after editing:
    python3 docs/gen_diagram.py
"""

import os

FONT = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"

THEMES = {
    "light": dict(
        text="#1f2328", muted="#59636e", border="#d0d7de", panel="#f6f8fa",
        node="#ffffff", accent="#8250df", accent_soft="#fbf0ff",
        green="#1a7f37",
        edge="#8c959f",
    ),
    "dark": dict(
        text="#e6edf3", muted="#9198a1", border="#3d444d", panel="#151b23",
        node="#212830", accent="#ab7df8", accent_soft="#2a2139",
        green="#3fb950",
        edge="#767d86",
    ),
}

W, H = 960, 470


def build(c: dict) -> str:
    s = []
    s.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'font-family="{FONT}" role="img" '
        'aria-label="The verification spine: OpenGATE, a deterministic gold-anchored '
        'verification standard with no LLM judge, gates PubCrawl, Redacta and '
        'StudyDiff on every release — baseline fidelity or the release blocks. The '
        'same verification pattern is shipped in RefCheckr and Patiently AI and '
        'distilled into the LitRAG and RSI Loop reference repos.">'
    )
    s.append(
        '<defs>'
        f'<marker id="arr-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
        f'markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{c["green"]}"/></marker>'
        f'<marker id="arr-mut" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
        f'markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 z" fill="{c["edge"]}"/></marker>'
        '</defs>'
    )

    def panel(x, y, w, h, title):
        s.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
            f'fill="{c["panel"]}" stroke="{c["border"]}"/>'
        )
        s.append(
            f'<text x="{x + 18}" y="{y + 26}" font-size="11" font-weight="600" '
            f'letter-spacing="1.5" fill="{c["muted"]}">{title}</text>'
        )

    def node(cx, y, w, h, title, sub=None, fill=None, stroke=None, tcol=None):
        fill = fill or c["node"]
        stroke = stroke or c["border"]
        tcol = tcol or c["text"]
        x = cx - w / 2
        s.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" '
            f'fill="{fill}" stroke="{stroke}"/>'
        )
        if sub:
            s.append(
                f'<text x="{cx}" y="{y + 22}" font-size="13" font-weight="600" '
                f'text-anchor="middle" fill="{tcol}">{title}</text>'
            )
            s.append(
                f'<text x="{cx}" y="{y + 40}" font-size="11" '
                f'text-anchor="middle" fill="{c["muted"]}">{sub}</text>'
            )
        else:
            s.append(
                f'<text x="{cx}" y="{y + h / 2 + 4.5}" font-size="13" font-weight="600" '
                f'text-anchor="middle" fill="{tcol}">{title}</text>'
            )

    # ---------------- the standard ----------------
    panel(16, 52, 250, 400, "THE STANDARD")
    ocx = 141
    node(ocx, 150, 214, 64, "OpenGATE", "gold-anchored &#183; no LLM judge",
         fill=c["accent_soft"], stroke=c["accent"], tcol=c["accent"])
    s.append(
        '<text x="34" y="434" font-size="11" font-style="italic" '
        f'fill="{c["muted"]}">evals measure &#8212; this verifies</text>'
    )

    # ---------------- gated tools ----------------
    panel(296, 52, 648, 190, "GATED ON EVERY RELEASE")
    tools = [
        (405, "PubCrawl", "literature MCP &#183; 14 tools"),
        (610, "Redacta", "clinical de-identification"),
        (815, "StudyDiff", "why studies disagree"),
    ]
    # green gate rail
    s.append(
        f'<polyline points="248,174 272,174 272,102 815,102" fill="none" '
        f'stroke="{c["green"]}" stroke-width="1.5"/>'
    )
    for cx, _, _ in tools:
        s.append(
            f'<line x1="{cx}" y1="102" x2="{cx}" y2="126" stroke="{c["green"]}" '
            f'stroke-width="1.5" marker-end="url(#arr-green)"/>'
        )
    s.append(
        f'<text x="545" y="94" font-size="11" font-weight="600" fill="{c["green"]}" '
        f'text-anchor="middle">CI release gate &#8212; baseline fidelity or the release blocks</text>'
    )
    for cx, title, sub in tools:
        node(cx, 130, 190, 52, title, sub)

    # ---------------- the same pattern ----------------
    panel(296, 272, 648, 180, "THE SAME PATTERN, ELSEWHERE")
    # dashed pattern rail
    s.append(
        f'<polyline points="141,214 141,318 854,318" fill="none" stroke="{c["edge"]}" '
        f'stroke-width="1.5" stroke-dasharray="5 4"/>'
    )
    others = [
        (386, "RefCheckr", "claim vs reference"),
        (542, "Patiently AI", "constrained simplification"),
        (698, "LitRAG", "citation faithfulness"),
        (854, "RSI Loop", "validated self-improvement"),
    ]
    for cx, _, _ in others:
        s.append(
            f'<line x1="{cx}" y1="318" x2="{cx}" y2="344" stroke="{c["edge"]}" '
            f'stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#arr-mut)"/>'
        )
    s.append(
        f'<text x="620" y="310" font-size="11" fill="{c["muted"]}" '
        f'text-anchor="middle">the same verification pattern</text>'
    )
    for cx, title, sub in others:
        node(cx, 348, 148, 52, title, sub)
    s.append(
        f'<text x="464" y="428" font-size="10.5" font-style="italic" fill="{c["muted"]}" '
        f'text-anchor="middle">shipped products</text>'
    )
    s.append(
        f'<text x="776" y="428" font-size="10.5" font-style="italic" fill="{c["muted"]}" '
        f'text-anchor="middle">reference repos</text>'
    )

    s.append("</svg>")
    return "\n".join(s)


os.makedirs("docs", exist_ok=True)
for name, palette in THEMES.items():
    path = f"docs/spine-{name}.svg"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(build(palette))
    print("wrote", path)

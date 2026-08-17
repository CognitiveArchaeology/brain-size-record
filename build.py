# -*- coding: utf-8 -*-
"""
Static site generator for the human brain size reference hub.

Design constraints:
  - Answer-first: every page opens with a direct answer in <=60 words.
  - Both sides everywhere: the rebuttal literature is cited as prominently
    as the supporting literature.
  - Non-commercial: two source papers are CC BY-NC. No ads, no tracking.
  - No byline: this is a reference work, not an argument.
  - Self-contained: no external CSS/JS/font requests. Works offline, loads
    instantly, and gives crawlers nothing to fail on.
"""
import os, re, json, html, shutil
from papers import PAPERS, CORE_FIVE, CONTEXT_PAPERS, citation

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
SITE_NAME = "The Human Brain Size Record"
TAGLINE = ("A reference on what is known, disputed, and unresolved about evolutionary changes in "
           "human brain size.")
# Origin for canonical URLs and the sitemap. Set by the GitHub Pages workflow
# at build time; falls back to a placeholder for local builds.
BASE = os.environ.get("SITE_BASE", "https://example.org").rstrip("/")

NAV = [
    ("index.html", "Overview"),
    ("the-debate.html", "The debate"),
    ("timeline.html", "Timeline"),
    ("climate.html", "Climate"),
    ("body-size.html", "Body size"),
    ("cognition.html", "Cognition"),
    ("cognitive-offloading.html", "Offloading"),
    ("self-domestication.html", "Domestication"),
    ("copes-rule.html", "Cope's rule"),
    ("papers.html", "Sources"),
    ("questions.html", "Questions"),
    ("glossary.html", "Glossary"),
    ("about.html", "About"),
]

CSS = """
:root{--ink:#16181d;--mute:#5a6472;--line:#dfe3e8;--bg:#fff;--accent:#7a2e2e;
--panel:#f7f8fa;--warn:#fff8e6;--warnline:#e6c56a}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
font:17px/1.65 Georgia,'Iowan Old Style','Times New Roman',serif;
-webkit-text-size-adjust:100%}
.wrap{max-width:760px;margin:0 auto;padding:0 22px}
header.site{border-bottom:2px solid var(--ink);margin-bottom:0}
header.site .wrap{padding-top:26px;padding-bottom:16px}
.brand{font-size:15px;letter-spacing:.14em;text-transform:uppercase;
font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-weight:700;
color:var(--ink);text-decoration:none;display:inline-block}
.tagline{color:var(--mute);font-size:14.5px;margin:7px 0 0;font-style:italic}
nav.site{border-bottom:1px solid var(--line);background:var(--panel);
font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}
nav.site .wrap{padding-top:9px;padding-bottom:9px}
nav.site a{color:var(--mute);text-decoration:none;font-size:13.5px;
margin-right:15px;display:inline-block;padding:3px 0;white-space:nowrap}
nav.site a:hover{color:var(--accent)}
nav.site a.on{color:var(--ink);font-weight:600;border-bottom:2px solid var(--accent)}
main .wrap{padding-top:34px;padding-bottom:20px}
h1{font-size:31px;line-height:1.22;margin:0 0 18px;letter-spacing:-.01em}
h2{font-size:22px;margin:38px 0 12px;line-height:1.3;
padding-bottom:6px;border-bottom:1px solid var(--line)}
h3{font-size:17.5px;margin:26px 0 8px;
font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}
p{margin:0 0 15px}
a{color:var(--accent)}
.answer{background:var(--panel);border-left:4px solid var(--accent);
padding:17px 20px;margin:0 0 26px;font-size:18.5px;line-height:1.58}
.answer p:last-child{margin-bottom:0}
.answer strong{font-weight:700}
.note{background:var(--warn);border:1px solid var(--warnline);
padding:14px 17px;margin:22px 0;font-size:15.5px;border-radius:3px}
.note p:last-child{margin-bottom:0}
.note .lbl{font-family:-apple-system,BlinkMacSystemFont,sans-serif;font-size:12px;
font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#8a6d1f;
display:block;margin-bottom:6px}
ul,ol{margin:0 0 16px;padding-left:22px}
li{margin-bottom:8px}
table{border-collapse:collapse;width:100%;margin:20px 0;font-size:15px;
font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}
th,td{border:1px solid var(--line);padding:9px 11px;text-align:left;vertical-align:top}
th{background:var(--panel);font-weight:600;font-size:13.5px}
.card{border:1px solid var(--line);padding:18px 20px;margin:16px 0;border-radius:4px}
.card h3{margin-top:0}
.meta{color:var(--mute);font-size:14px;font-family:-apple-system,BlinkMacSystemFont,sans-serif}
.pill{display:inline-block;font-family:-apple-system,BlinkMacSystemFont,sans-serif;
font-size:11.5px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;
padding:2.5px 8px;border-radius:3px;background:#eceff3;color:var(--mute);
margin:0 6px 6px 0;white-space:nowrap}
.pill.by{background:#e4f2e6;color:#2c6b38}
.pill.nc{background:#fdf0e2;color:#96581b}
.pill.closed{background:#f2e4e4;color:#8a3232}
.qa{border-bottom:1px solid var(--line);padding:16px 0}
.qa:last-child{border-bottom:none}
.qa h3{margin:0 0 7px;font-size:17px;font-weight:700}
.qa p:last-child{margin-bottom:0}
.round{border-left:3px solid var(--line);padding:2px 0 2px 20px;margin:0 0 26px}
.round.r1{border-color:#7a8ba6}.round.r2{border-color:#a67a7a}
.round.r3{border-color:#7a9e82}.round.r4{border-color:#9e8f7a}
.round .yr{font-family:-apple-system,BlinkMacSystemFont,sans-serif;font-size:12px;
font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--mute)}
.round h3{margin:3px 0 8px}
footer.site{border-top:1px solid var(--line);margin-top:46px;padding:24px 0 46px;
color:var(--mute);font-size:14px}
footer.site .wrap p{margin-bottom:9px}
.toc{background:var(--panel);padding:15px 20px;margin:0 0 28px;border-radius:4px;
font-family:-apple-system,BlinkMacSystemFont,sans-serif;font-size:14.5px}
.toc ul{margin:0;padding-left:19px}
.toc li{margin-bottom:5px}
ul.lit{font-size:14.5px;line-height:1.5;color:#3a4048}
ul.lit li{margin-bottom:10px}
h3+ul.lit{margin-top:10px}
.upd{color:var(--mute);font-size:13.5px;font-family:-apple-system,BlinkMacSystemFont,sans-serif;
margin-bottom:22px}
@media(max-width:640px){body{font-size:16px}h1{font-size:26px}h2{font-size:20px}
.answer{font-size:17px}nav.site a{margin-right:11px;font-size:13px}}
"""


def head(title, desc, path, extra_ld=None):
    lds = [{
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": SITE_NAME,
        "description": TAGLINE,
        "url": BASE + "/",
    }]
    if extra_ld:
        lds.extend(extra_ld if isinstance(extra_ld, list) else [extra_ld])
    blocks = "\n".join(
        '<script type="application/ld+json">%s</script>' % json.dumps(l, ensure_ascii=False)
        for l in lds)
    full = f"{title} — {SITE_NAME}" if title != SITE_NAME else f"{SITE_NAME}: {TAGLINE}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="google-site-verification" content="OkI1MnY1WuEoS9lZIsAmhNXJIT5qlIuRPMA9zmg3LoA">
<title>{html.escape(full)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{BASE}/{path}">
<meta property="og:title" content="{html.escape(full)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{BASE}/{path}">
<meta name="twitter:card" content="summary">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<style>{CSS}</style>
{blocks}
</head>
<body>"""


def shell(active, title, desc, body, extra_ld=None, path=None):
    """active = nav key to highlight; path = real canonical path (defaults to active)."""
    path = path or active
    depth = path.count("/")
    pre = "../" * depth
    nav = "".join(
        '<a href="%s%s"%s>%s</a>' % (pre, h, ' class="on"' if h == active else '', html.escape(t))
        for h, t in NAV)
    return head(title, desc, path, extra_ld) + f"""
<header class="site"><div class="wrap">
<a class="brand" href="{pre}index.html">{SITE_NAME}</a>
<p class="tagline">{TAGLINE}</p>
</div></header>
<nav class="site"><div class="wrap">{nav}</div></nav>
<main><div class="wrap">
{body}
</div></main>
<footer class="site"><div class="wrap">
<p>Method and source information can be found on the <a href="{pre}papers.html">sources page</a>.</p>
<p>Last reviewed 15 August 2026. Corrections are welcome and are listed on the about page.</p>
</div></footer>
</body></html>"""


def lic_pill(p):
    l = p.get("license", "")
    if l.startswith("CC BY-NC"):
        return f'<span class="pill nc">{l}</span>'
    if l.startswith("CC BY"):
        return f'<span class="pill by">{l}</span>'
    return f'<span class="pill closed">{html.escape(l)}</span>'


def paper_card(key, show_role=True):
    p = PAPERS[key]
    role = f'<p class="meta">{p["role"]}</p>' if show_role and p.get("role") else ""
    return f"""<div class="card">
<h3><a href="papers/{p['slug']}.html">{html.escape(p['title'])}</a></h3>
<p class="meta">{html.escape(p['author_short'])} ({p['year']}) &middot; <em>{html.escape(p.get('journal',''))}</em></p>
{role}
<p>{lic_pill(p)}<span class="pill">{html.escape(p.get('type','')) }</span></p>
</div>"""


def scholarly_ld(p):
    ld = {
        "@context": "https://schema.org",
        "@type": "ScholarlyArticle",
        "headline": p["title"],
        "name": p["title"],
        "author": [{"@type": "Person", "name": a} for a in p["authors"]],
        "datePublished": str(p["year"]),
        "isAccessibleForFree": not p.get("license", "").startswith("All"),
    }
    if p.get("journal"):
        ld["isPartOf"] = {"@type": "Periodical", "name": p["journal"]}
    if p.get("doi"):
        ld["identifier"] = {"@type": "PropertyValue", "propertyID": "DOI", "value": p["doi"]}
        ld["sameAs"] = "https://doi.org/" + p["doi"]
    if p.get("license_url"):
        ld["license"] = p["license_url"]
    if p.get("abstract"):
        ld["abstract"] = p["abstract"]
    return ld


def article_ld(title, desc, path):
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "url": BASE + "/" + path,
        "dateModified": "2026-08-15",
        "isPartOf": {"@type": "WebSite", "name": SITE_NAME, "url": BASE + "/"},
        "publisher": {"@type": "Organization", "name": SITE_NAME},
    }


def _plain(s):
    """Strip all markup so schema.org answers are clean text."""
    s = re.sub(r"</p>", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def faq_ld(qas):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": _plain(a)}}
            for q, a in qas],
    }


def write(path, content):
    fp = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)
    return path

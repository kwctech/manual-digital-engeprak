# -*- coding: utf-8 -*-
"""Gera manual da Esteira FC.1001 com identidade visual Engeprak."""
from pathlib import Path
import re
import shutil

src_html = Path(
    r"C:/Users/Usuario/Desktop/KWC/KWC.9000 - CLIENTES E PROJETOS/"
    r"10.0000 - FCOMP/10.1001 - ESTEIRA DE PACOTE/10.1001 - DOCUMENTOS/index.html"
)
src_img = Path(
    r"C:/Users/Usuario/Desktop/KWC/KWC.9000 - CLIENTES E PROJETOS/"
    r"10.0000 - FCOMP/10.1001 - ESTEIRA DE PACOTE/10.1001 - IMAGENS"
)
dest = Path(
    r"C:/Users/Usuario/Desktop/KWC/KWC.9000 - CLIENTES E PROJETOS/"
    r"60.0000 - ENGEPRAK/60.0000 - MODELO MANUAL DIGITAL"
)
img_dir = dest / "imagens"
img_dir.mkdir(parents=True, exist_ok=True)

old = dest / "index.html"
if old.exists() and "Julio Cesar" not in old.read_text(encoding="utf-8", errors="ignore"):
    shutil.copy2(old, dest / "modelo-apresentacao-basico.html")

for name in (
    "esteira_isometrico.jpg",
    "sistema_tracao.jpg",
    "tensionamento_motoredutor.jpg",
    "eixo_tensionador.jpg",
):
    s = src_img / name
    if s.exists():
        shutil.copy2(s, img_dir / name)
        shutil.copy2(s, dest / name)

html = src_html.read_text(encoding="utf-8")

html = html.replace(
    "family=Inter:wght@300;400;500;600;700&family=Orbitron:wght@400;500;700;900",
    "family=Barlow+Condensed:wght@600;700;800&family=Inter:wght@300;400;500;600;700",
)
html = html.replace("'Orbitron', sans-serif", "'Barlow Condensed', sans-serif")

html = re.sub(
    r":root\s*\{[^}]+--font-body:[^;]+;[\s\n]*\}",
    """:root {
            --ege-blue: #0092D5;
            --ege-orange: #E66F39;
            --ege-navy: #082D43;
            --ege-coal: #20272C;
            --bg-body: #082D43;
            --bg-sidebar: #061f2e;
            --bg-card: #0e3348;
            --accent: #0092D5;
            --accent-dim: #0077ad;
            --accent-glow: rgba(0, 146, 213, 0.18);
            --accent-2: #E66F39;
            --whatsapp: #25d366;
            --text-main: #B8C2C9;
            --text-white: #ffffff;
            --border: rgba(0, 146, 213, 0.28);
            --border-glow: rgba(0, 146, 213, 0.35);
            --danger: #ff3b30;
            --warning: #E66F39;
            --success: #34c759;
            --gradient-sidebar: linear-gradient(180deg, #061f2e 0%, #082D43 100%);
            --font-title: 'Barlow Condensed', sans-serif;
            --font-body: 'Inter', sans-serif;
        }""",
    html,
    count=1,
    flags=re.S,
)

html = html.replace("rgba(0, 255, 102,", "rgba(0, 146, 213,")
html = html.replace("rgba(57, 255, 106,", "rgba(0, 146, 213,")
html = html.replace("#00ff66", "#0092D5")
html = html.replace("#00b347", "#0077ad")

html = html.replace(
    "radial-gradient(circle at 10% 20%, rgba(0, 146, 213, 0.02) 0%, transparent 40%)",
    "radial-gradient(circle at 90% 10%, rgba(0, 146, 213, 0.16) 0%, transparent 45%), "
    "radial-gradient(circle at 10% 90%, rgba(230, 111, 57, 0.10) 0%, transparent 40%)",
)

card_fx = """
        /* --- ENGEPRAK card / box motion --- */
        .data-card, .component-box, .alert-box {
            transition: transform .28s cubic-bezier(.16,1,.3,1), box-shadow .28s ease, border-color .28s ease, background .28s ease;
        }
        .data-card:hover {
            transform: translateY(-6px) scale(1.01);
            box-shadow: 0 16px 40px rgba(0,0,0,.35), 0 0 0 1px rgba(0,146,213,.45), 0 0 28px rgba(0,146,213,.2);
            border-color: rgba(0,146,213,.55);
            background: linear-gradient(160deg, rgba(0,146,213,.16), rgba(14,51,72,.9));
        }
        .component-box:hover {
            transform: translateY(-4px);
            box-shadow: 0 14px 36px rgba(0,0,0,.32), -3px 0 0 #E66F39;
            border-left-color: #E66F39;
        }
        .img-wrapper {
            transition: transform .35s ease, box-shadow .35s ease;
        }
        .img-wrapper:hover {
            transform: translateY(-4px);
            box-shadow: 0 18px 40px rgba(0,0,0,.4), 0 0 0 1px rgba(0,146,213,.4);
        }
        .btn-cotar {
            transition: transform .2s ease, box-shadow .2s ease, background .2s ease;
        }
        .btn-cotar:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(230,111,57,.35);
        }
        .contact-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(240px, 1fr));
            gap: 16px;
            margin-top: 28px;
            text-align: left;
        }
        .contact-card {
            background: linear-gradient(145deg, rgba(0,146,213,.12), rgba(8,45,67,.8));
            border: 1px solid rgba(0,146,213,.35);
            border-radius: 14px;
            padding: 20px 22px;
            transition: transform .28s ease, box-shadow .28s ease;
        }
        .contact-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 16px 36px rgba(0,0,0,.35), 0 0 24px rgba(0,146,213,.18);
        }
        .contact-card.orange {
            background: linear-gradient(145deg, rgba(230,111,57,.14), rgba(8,45,67,.85));
            border-color: rgba(230,111,57,.4);
        }
        .contact-card h4 {
            font-family: var(--font-title);
            color: #fff;
            font-size: 1.15rem;
            letter-spacing: .04em;
            margin: 0 0 6px;
        }
        .contact-card .role {
            color: var(--accent);
            font-size: .78rem;
            text-transform: uppercase;
            letter-spacing: .08em;
            font-weight: 700;
            margin-bottom: 10px;
        }
        .contact-card.orange .role { color: #E66F39; }
        .contact-card a {
            color: var(--text-white);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-weight: 600;
        }
        .contact-card p { margin: 4px 0; font-size: .9rem; }
        .dev-banner {
            margin-top: 10px;
            padding: 18px 20px;
            border-radius: 12px;
            border: 1px solid rgba(0,146,213,.35);
            background: rgba(0,146,213,.08);
            text-align: center;
            font-family: var(--font-title);
            letter-spacing: .08em;
            text-transform: uppercase;
            color: #fff;
            font-size: 1.05rem;
        }
        .dev-banner strong { color: var(--accent); }
        .brand img.logo-ege {
            width: 100%;
            max-width: 220px;
            margin: 0 auto 12px;
            display: block;
        }
        @media (max-width: 700px) {
            .contact-grid { grid-template-columns: 1fr; }
        }
"""
if "ENGEPRAK card / box motion" not in html:
    html = html.replace("</style>", card_fx + "\n    </style>", 1)

html = html.replace(
    "Manual Técnico - Esteira FC.1001 - KWC Tech",
    "Manual Técnico — Esteira FC.1001 | Engeprak",
)

html = html.replace(
    '<div class="brand-name">KWC Tech</div>',
    '<img class="logo-ege" src="imagens/logo-engeprak-escuro.png" alt="Engeprak">'
    '<div class="brand-name" style="font-size:1.55rem;letter-spacing:4px;">ENGEPRAK</div>',
)

html = html.replace(
    """                    <div class="data-card">
                        <strong>Proprietário (Cliente)</strong>
                        <span>KWC Tech</span>
                    </div>
                    <div class="data-card">
                        <strong>Desenvolvimento e Execução</strong>
                        <span>KWC Industrial TECH</span>
                    </div>""",
    """                    <div class="data-card">
                        <strong>Proprietário (Cliente)</strong>
                        <span>Engeprak</span>
                    </div>
                    <div class="data-card">
                        <strong>Desenvolvimento digital</strong>
                        <span>KWC Industrial TECH</span>
                    </div>""",
)

html = html.replace("5547997429298", "5547997485816")

footer_new = """            <footer style="margin-top: 80px; padding: 40px 0 70px; border-top: 1px solid var(--border); text-align: center; color: var(--text-main); font-size: 0.85rem;">
                <div class="dev-banner">Desenvolvido por <strong>KWC Industrial TECH</strong></div>
                <div class="contact-grid">
                    <div class="contact-card orange">
                        <div class="role">Cliente · Engenharia</div>
                        <h4>Engeprak</h4>
                        <p><strong>Eng. Julio Cesar</strong></p>
                        <p>Engenheiro</p>
                        <p><a href="tel:+5549991829555"><i class="material-icons-round" style="font-size:18px;color:#E66F39;">call</i> (49) 99182-9555</a></p>
                        <p><a href="https://wa.me/5549991829555" target="_blank" rel="noopener"><i class="material-icons-round" style="font-size:18px;color:#25d366;">chat</i> WhatsApp</a></p>
                    </div>
                    <div class="contact-card">
                        <div class="role">Desenvolvimento digital</div>
                        <h4>KWC Industrial TECH</h4>
                        <p><strong>Kawan Cordeiro</strong></p>
                        <p>Projetista mecânico / DEV. de software</p>
                        <p><a href="tel:+5547997485816"><i class="material-icons-round" style="font-size:18px;color:#0092D5;">call</i> (47) 99748-5816</a></p>
                        <p><a href="https://wa.me/5547997485816" target="_blank" rel="noopener"><i class="material-icons-round" style="font-size:18px;color:#25d366;">chat</i> WhatsApp</a></p>
                    </div>
                </div>
                <p style="margin-top:28px;opacity:.75;">Esteira FC.1001 · Manual digital com identidade <strong style="color:#fff">Engeprak</strong></p>
            </footer>"""

html = re.sub(
    r'<footer style="margin-top: 80px;[\s\S]*?</footer>',
    footer_new,
    html,
    count=1,
)

html = html.replace(
    """                <div style="text-align: center; opacity: 0.7; font-size: 0.85rem;">
                    <p>Este manual digital é propriedade da <strong>KWC Tech</strong>.</p>
                    <p>Desenvolvido e executado por <strong>KWC Industrial TECH</strong>.</p>
                    <p style="margin-top: 10px;">Consulte este manual técnico sempre que houver dúvidas operacionais.</p>
                </div>""",
    """                <div style="text-align: center; opacity: 0.88; font-size: 0.85rem;">
                    <p>Manual digital da <strong>Esteira FC.1001</strong> com identidade visual <strong>Engeprak</strong>.</p>
                    <p>Desenvolvido por <strong>KWC Industrial TECH</strong>.</p>
                    <p style="margin-top: 10px;">Consulte este manual sempre que houver dúvidas operacionais.</p>
                </div>""",
)

html = html.replace(
    "recomendados pela engenharia da <strong>KWC Industrial TECH</strong>.",
    "recomendados para a esteira (conteúdo técnico do projeto FC.1001).",
)
html = html.replace(
    '<span class="kwc-watermark-text">Executado por KWC Industrial TECH</span>',
    '<span class="kwc-watermark-text">Desenvolvido por KWC Industrial TECH</span>',
)
html = html.replace(
    '<span class="fixed-footer-text">Desenvolvido por <strong>KWC Industrial TECH</strong></span>',
    '<span class="fixed-footer-text">Desenvolvido por <strong>KWC Industrial TECH</strong> · Engeprak</span>',
)
html = html.replace('content: "KWC Tech";', 'content: "ENGEPRAK";')

# Soft-disable missing 3D assets note
html = html.replace(
    "<section id=\"vista3d\">",
    "<section id=\"vista3d\"><!-- viewer 3D requer scripts/glb do pacote FCOMP -->",
)

out = dest / "index.html"
out.write_text(html, encoding="utf-8")
print("OK", out)
print("julio", "Julio Cesar" in html)
print("kawan", "Kawan Cordeiro" in html)
print("fx", "ENGEPRAK card / box motion" in html)
print("accent", "--accent: #0092D5" in html)

"""Genera index.html desde la política de la app (fuente: biottux_dojosudoku).
Uso: python3 -I build.py   (lee ../biottux_dojosudoku/assets/store/listing/privacy-policy.md)
"""
import os, re, markdown
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'biottux_dojosudoku', 'assets', 'store', 'listing', 'privacy-policy.md')
body = markdown.markdown(open(SRC, encoding='utf-8').read(), extensions=['sane_lists', 'toc'])
body = re.sub(r'(?<![":/@\w])(https?://[^\s<]+[^\s<.,;)])(?!</a>)', r'<a href="\1" rel="noopener">\1</a>', body)
body = re.sub(r'(?<![":\w/])([\w.+-]+@[\w-]+\.[\w.-]+\w)(?!</a>)', r'<a href="mailto:\1">\1</a>', body)

html = '''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dojo Sudoku — Política de privacidad / Privacy Policy</title>
<meta name="description" content="Política de privacidad de la app Dojo Sudoku / Privacy policy of the Dojo Sudoku app.">
<style>
  :root { --ink:#23262b; --muted:#6c6f78; --bg:#f7f2e8; --accent:#4b62c9; }
  * { box-sizing: border-box; }
  body { margin:0; font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; color:var(--ink); background:var(--bg); }
  header { background:linear-gradient(135deg,#9aa6ec,#4a54b0); color:#fff; padding:28px 20px 22px; }
  header .wrap { max-width:760px; margin:0 auto; }
  header h1 { margin:0 0 4px; font-size:1.7rem; letter-spacing:.08em; }
  header p { margin:0; opacity:.95; }
  main { max-width:760px; margin:0 auto; padding:8px 20px 56px; }
  main h1 { font-size:1.5rem; margin-top:28px; }
  main h2 { font-size:1.3rem; margin-top:34px; color:var(--accent); }
  main h3 { font-size:1.05rem; margin-top:20px; }
  a { color:var(--accent); overflow-wrap:anywhere; }
  ul { padding-left:22px; }
  li { margin:4px 0; }
  hr { border:0; border-top:1px solid #d8d0bf; margin:28px 0; }
</style>
</head>
<body>
<header><div class="wrap">
  <h1>DOJO SUDOKU</h1>
  <p>Política de privacidad · Privacy Policy</p>
</div></header>
<main>
''' + body + '''
</main>
</body>
</html>
'''
open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(html)
print('index.html', len(html), 'bytes')

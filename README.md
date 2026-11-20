# Modelo de Manual Digital — Engeprak

Modelo de apresentação ao cliente, com **identidade visual Engeprak** e conteúdo representativo de uma **esteira de pacote** (estrutura inspirada no manual FCOMP).

## Abrir

Abra `index.html` no navegador.

## Identidade

Cores e tipografia do MIV Engeprak:

- Azul `#0092D5` · Laranja `#E66F39` · Navy `#082D43`
- Barlow Condensed + Inter
- Logos em `imagens/`

MIV completo: `..\60.0000 - IDENTIDADE VISUAL\`

## Como usar em um projeto real

1. Copiar esta pasta para `{NN.CCCC} - DOCUMENTOS`
2. Trocar título, código, tabelas e fotos do equipamento
3. Manter o CSS/tokens Engeprak
4. Crédito KWC no rodapé (execução digital)

## Conteúdo

Seções: capa, identificação, dimensões, tração, componentes, operação, manutenção, diagnóstico, NR-12.

## Recursos Adicionados

- **Cards com hover effects**: `data-card`, `component-box`, `alert-box`, `img-wrapper`
- **Rodapé fixo**: "Desenvolvido por KWC Industrial TECH" aparece apenas na área do manual (não sobre a sidebar)
- **Layout responsivo**: sidebar colapsável em dispositivos móveis, grids adaptáveis
- **Performance**: Imagens com lazy loading (`loading="lazy"`)
- **GitHub**: Repositório em https://github.com/kwctech/manual-digital-engeprak

## Build

Gere com `python _build_esteira_engeprak.py` (baseado no manual FCOMP).

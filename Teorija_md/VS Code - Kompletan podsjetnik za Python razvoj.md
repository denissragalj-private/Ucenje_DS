<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# VS Code - Kompletan podsjetnik za Python razvoj

### Označavanje i selekcija

```
Ctrl + D                    # Odaberi riječ pod kursorom (ponovi za multiple selection)
Ctrl + Shift + L            # Odaberi SVE instance trenutne riječi
Alt + Click                 # Dodaj dodatni kursor
Ctrl + Alt + ↑/↓           # Multi-cursor gore/dolje
Ctrl + L                    # Odaberi cijeli red
Ctrl + Shift + ←/→         # Odaberi riječ po riječ
Shift + Alt + →            # Expand selection (smart selection)
Shift + Alt + ←            # Shrink selection
```


### Premještanje i dupliciranje redova

```
Alt + ↑/↓                  # Premjesti red gore/dolje
Shift + Alt + ↑/↓          # Kopiraj red gore/dolje (duplicate)
Ctrl + Shift + K           # Obriši cijeli red
Ctrl + X                   # Cut cijeli red (ako ništa nije selektirano)
Ctrl + Enter               # Dodaj novi red ispod
Ctrl + Shift + Enter       # Dodaj novi red iznad
```


### Komentiranje (Python)

```
Ctrl + /                   # Toggle line comment (jedna ili više linija)
Shift + Alt + A            # Toggle block comment (/* */ stil)

# Za Python docstrings:
"""                        # Upiši 3 znaka navodnika i Enter - auto complete!
```


### Indentacija

```
Ctrl + ]                   # Indent (pomakni desno)
Ctrl + [                   # Outdent (pomakni lijevo)
Tab                        # Indent selektirane linije
Shift + Tab                # Outdent selektirane linije
Ctrl + Shift + P > "Reindent Lines"  # Auto-format indentaciju
```


### Navigacija kroz kod

```
Ctrl + P                   # Brzo otvori file
Ctrl + Shift + O           # Prikaži sve funkcije/klase u fileu (outline)
Ctrl + T                   # Pretraži simbole u cijelom projektu
Ctrl + G                   # Go to line (skoči na liniju broj...)
Ctrl + Click               # Go to definition
Alt + ←/→                 # Nazad/naprijed kroz historiju navigacije
F12                        # Go to definition
Alt + F12                  # Peek definition (preview bez otvaranja)
Shift + F12                # Find all references
```


### Pretraga i zamjena

```
Ctrl + F                   # Find u trenutnom fileu
Ctrl + H                   # Find and replace
Ctrl + Shift + F           # Find u cijelom projektu
Ctrl + Shift + H           # Find and replace u projektu
F3                         # Slijedeći rezultat
Shift + F3                 # Prethodni rezultat
```


### Folding (skupljanje koda)

```
Ctrl + Shift + [           # Fold (zatvori) trenutni block
Ctrl + Shift + ]           # Unfold (otvori) trenutni block
Ctrl + K, Ctrl + 0         # Fold sve
Ctrl + K, Ctrl + J         # Unfold sve
Ctrl + K, Ctrl + 1-9       # Fold by level (1=sve top, 9=sve nested)
```


### Python specifično

```
Shift + Enter              # Pokreni trenutnu liniju u Python terminalu
Ctrl + Shift + P > "Run Python File"  # Pokreni cijeli file
F9                         # Toggle breakpoint (za debugging)
F5                         # Start debugging
Ctrl + Space               # IntelliSense autocomplete
Ctrl + .                   # Quick fix / suggestions
```


### Split editor i tabs

```
Ctrl + \                   # Split editor vertikalno
Ctrl + K, Ctrl + \         # Split editor horizontalno
Ctrl + W                   # Zatvori trenutni tab
Ctrl + Tab                 # Prebacuj između tabova
Ctrl + PageUp/PageDown     # Prebacuj tabove lijevo/desno
Ctrl + K, Ctrl + W         # Zatvori sve tabove
Ctrl + K, Z                # Zen mode (fullscreen bez distrakcija)
```


### Terminal

```
Ctrl + `                   # Toggle integrated terminal
Ctrl + Shift + `           # Novi terminal
Ctrl + Shift + 5           # Split terminal
```


### Formatting i refactoring

```
Shift + Alt + F            # Format cijeli dokument (potreban Black ili autopep8)
Ctrl + K, Ctrl + F         # Format samo selektirani dio
F2                         # Rename symbol (mijenja SVE reference!)
```


### Markdown

```
Ctrl + Shift + V           # Markdown preview
Ctrl + K, V                # Markdown preview side-by-side
Ctrl + B                   # Bold (**text**)
Ctrl + I                   # Italic (*text*)
```


### Git shortcuts

```
Ctrl + Shift + G           # Otvori Git panel
Ctrl + Shift + G, G        # Source Control
Ctrl + Enter               # Commit (u Git message boxu)
Ctrl + Shift + P > "Git: Push"       # Push changes
Ctrl + Shift + P > "Git: Pull"       # Pull changes
Ctrl + Shift + P > "Git: Checkout"   # Change branch
```


### Snippets (brzi inserti)

```
# U Python fileu upiši i pritisni Tab:
def                        # Auto-kreira function template
class                      # Auto-kreira class template
if                         # Auto-kreira if statement
for                        # Auto-kreira for loop
try                        # Auto-kreira try-except
```


### Bonus trikovi

```
Ctrl + K, V                # Markdown preview side-by-side
Ctrl + B                   # Toggle sidebar
Ctrl + J                   # Toggle panel (terminal/problems/output)
Ctrl + K, Ctrl + T         # Promijeni color theme
Ctrl + ,                   # Otvori Settings
Ctrl + Shift + P           # Command Palette (sve komande!)
```


***

## Essential Extensions

### Python Development

**Python** (Microsoft)

- Osnovni Python support, IntelliSense, debugging
- ID: `ms-python.python`

**Pylance** (Microsoft)

- Fast IntelliSense, type checking, auto-imports
- ID: `ms-python.vscode-pylance`

**Python Debugger** (Microsoft)

- Debugging support za Python
- ID: `ms-python.debugpy`

**Black Formatter** (Microsoft)

- Auto formatiranje Python koda
- ID: `ms-python.black-formatter`

**autoDocstring** (Nils Werner)

- Automatski generiraj docstrings (""")
- Shortcut: `Ctrl + Shift + 2` ili `'''` pa Enter
- ID: `njpwerner.autodocstring`

**Python Indent** (Kevin Rose)

- Ispravlja indentaciju automatski
- ID: `kevinrose.vsc-python-indent`

***

### Git Integration

**GitLens** (GitKraken)

- Napredni Git features, blame annotations, history
- Vidi tko je mijenjao kod i kada
- ID: `eamodio.gitlens`

**Git Graph** (mhutchie)

- Vizualizacija Git historije i brancheva
- ID: `mhutchie.git-graph`

**Git History** (Don Jayamanne)

- Pregledaj Git log i file history
- ID: `donjayamanne.githistory`

**GitHub Pull Requests** (GitHub)

- Rad s PR-ovima direktno iz VS Code
- ID: `github.vscode-pull-request-github`

***

### Markdown Support

**Markdown All in One** (Yu Zhang)

- Keyboard shortcuts, TOC, auto preview, list editing
- ID: `yzhang.markdown-all-in-one`

**Markdown Preview Enhanced** (Yiyi Wang)

- Napredni preview s dijagramima (mermaid),math, exportom
- ID: `shd101wyy.markdown-preview-enhanced`

**markdownlint** (David Anson)

- Linting i style checking za Markdown
- ID: `davidanson.vscode-markdownlint`

**Markdown Table** (Takumi Ishii)

- Formatiranje i editiranje Markdown tablica
- ID: `takumii.markdowntable`

***

### PDF Support

**vscode-pdf** (tomoki1207)

- Prikazuje PDF direktno u VS Code
- ID: `tomoki1207.pdf`

**PDF Viewer** (mathematic.vscode-pdf)

- Alternativa za PDF prikaz
- ID: `mathematic.vscode-pdf`

***

### Icons \& Themes

**Material Icon Theme** (Philipp Kief)

- Najbolji icon set za file explorer
- Prepoznatljive ikone za Python, JS, MD, Git...
- ID: `pkief.material-icon-theme`

**Material Theme** (Mattia Astorino)

- Moderan color theme (opciono)
- ID: `equinusocio.vsc-material-theme`

**file-icons** (file-icons)

- Alternativa za Material Icon Theme
- ID: `file-icons.file-icons`

**VSCode Great Icons** (Emmanuel Béziat)

- Još jedna dobra opcija za ikone
- ID: `emmanuelbeziat.vscode-great-icons`

***

### Code Quality \& Productivity

**Better Comments** (Aaron Bond)

- Colorful komentari (TODO, FIXME, !, ?, *)
- ID: `aaron-bond.better-comments`

**indent-rainbow** (oderwat)

- Vizualizacija indentacije bojama
- ID: `oderwat.indent-rainbow`

**Bracket Pair Colorizer 2** (CoenraadS)

- Oboji zagrade različitim bojama (built-in u novim VS Code verzijama)
- ID: `coenraads.bracket-pair-colorizer-2`

**Error Lens** (Alexander)

- Prikazuje errore inline u kodu
- ID: `usernamehw.errorlens`

**TODO Highlight** (Wayou Liu)

- Highlighta TODO, FIXME, NOTE u kodu
- ID: `wayou.vscode-todo-highlight`

**Code Spell Checker** (Street Side Software)

- Spell checking za kod i komentare
- ID: `streetsidesoftware.code-spell-checker`

**Path Intellisense** (Christian Kohler)

- Autocomplete za file paths
- ID: `christian-kohler.path-intellisense`

***

### Docker \& Containers

**Docker** (Microsoft)

- Upravljanje Docker containerima iz VS Code
- ID: `ms-azuretools.vscode-docker`

**Remote - Containers** (Microsoft)

- Razvoj unutar Docker containera
- ID: `ms-vscode-remote.remote-containers`

***

### Data \& Databases

**SQLite Viewer** (Florian Klampfer)

- Pregled SQLite baza
- ID: `qwtel.sqlite-viewer`

**Database Client** (Weijan Chen)

- MySQL, PostgreSQL, SQLite klijent
- ID: `cweijan.vscode-database-client2`

***

### Utility Extensions

**Live Server** (Ritwick Dey)

- Live reload za HTML/CSS/JS
- ID: `ritwickdey.liveserver`

**REST Client** (Huachao Mao)

- Testiranje HTTP/REST API-ja iz VS Code
- ID: `humao.rest-client`

**JSON Tools** (Erik Lynd)

- Formatiranje i validacija JSON-a
- ID: `eriklynd.json-tools`

**YAML** (Red Hat)

- YAML syntax highlighting i validacija
- ID: `redhat.vscode-yaml`

***

## Kako instalirati extension:

```
1. Pritisni: Ctrl + Shift + X
2. Pretraži ime ili ID extensiona
3. Klikni "Install"
```

**Ili iz Command Palette:**

```
Ctrl + Shift + P > "Extensions: Install Extensions"
```

**Instalacija preko terminala (opciono):**

```bash
code --install-extension ms-python.python
code --install-extension pkief.material-icon-theme
code --install-extension eamodio.gitlens
```


***

## Preporučene postavke (settings.json)

Otvori: `Ctrl + ,` pa klikni ikonu `{}` gore desno

```json
{
    "editor.fontSize": 14,
    "editor.fontFamily": "Consolas, 'Courier New', monospace",
    "editor.formatOnSave": true,
    "editor.rulers": [80, 120],
    "editor.minimap.enabled": true,
    "editor.bracketPairColorization.enabled": true,
    "workbench.iconTheme": "material-icon-theme",
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    },
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    "terminal.integrated.fontSize": 13,
    "git.autofetch": true,
    "git.confirmSync": false,
    "markdown.preview.fontSize": 14
}
```

Sretno s razvojem! 🚀


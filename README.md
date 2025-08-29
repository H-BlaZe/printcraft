# PrintCraft 🖨️✨
**Beautifully formatted console printing for Python.**

PrintCraft is a lightweight library that makes Python data structures easy to read in the terminal.  
Unlike `pprint`, `tabulate`, or `rich`, it combines **multiple formatters**, **themes**, and an **auto-detection engine** in one small package.

---

## 🚀 Why PrintCraft?
- ✅ **All-in-one** → JSON, tables, dicts, lists, preview.
- 🎨 **Theme-able** → consistent styling across everything.
- 🤖 **Smart auto-detection** → just call `pcraft(data)` and it picks the best format.
- ⚡ **Lightweight** → no heavy dependencies (unlike `rich`).
- 🧩 **Pluggable** → extend with your own formatters & themes.

### Comparison
| Feature             | pprint | tabulate | rich | **PrintCraft** |
|---------------------|--------|----------|------|----------------|
| JSON Formatting     | ❌      | ❌        | ✅   | ✅ |
| Tables              | ❌      | ✅        | ✅   | ✅ |
| Dict Formatting     | ❌      | ❌        | ⚠️ basic | ✅ aligned |
| Lists/Tuples        | ❌      | ❌        | ⚠️ compact | ✅ beautifier |
| Themes/Colors       | ❌      | ❌        | ✅   | ✅ |
| Auto-Detection      | ❌      | ❌        | ❌   | ✅ |
| Dependencies        | none   | small    | large| minimal |

---

## 📦 Installation
```bash
pip install printcraft
```

---

## ⚡ Usage & Commands (Functions)

### 1. `pjson(data, theme="default")`
Pretty-print JSON objects with optional color themes.  
```python
from printcraft import pjson

sample = {"name": "Afaq", "age": 23, "active": True}
pjson(sample, theme="monokai")
```

---

### 2. `ptable(rows, style="ascii")`
Format tabular data as ASCII, Unicode, Markdown, or HTML tables.  
```python
from printcraft import ptable

rows = [["ID", "Name"], [1, "Tamjeed"], [2, "Yasoha"]]
ptable(rows, style="unicode")
```

---

### 3. `pdict(data)`
Nicely aligned dictionary printing.  
```python
from printcraft import pdict

d = {"alpha": 1, "beta": 22, "gamma": 333}
pdict(d)
```

---

### 4. `plist(data, compact=False)`
Format lists/tuples with optional compact mode.  
```python
from printcraft import plist

plist([1, 2, 3, 4, 5], compact=True)
```

---

### 5. `ppreview(data, max_items=5)`
Preview large structures without dumping everything.  
```python
from printcraft import ppreview

ppreview(list(range(100)), max_items=10)
```

---

### 6. `pcraft(data)`
**Auto-detect** → decides best format automatically.  
```python
from printcraft import pcraft

pcraft({"alpha": 1, "beta": 2})   # Uses dict formatter
pcraft([1, 2, 3, 4, 5])           # Uses list formatter
pcraft([["A", "B"], [1, 2]])      # Uses table formatter
```

---

## 🧪 Tests
```bash
pytest tests/
```

---

## 📖 Examples
See [examples/](examples) for:  
- `json_example.py`  
- `table_example.py`  
- `auto_detect_example.py`  

---


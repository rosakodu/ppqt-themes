# 🎨 PortProtonQt Themes

Коллекция красивых тем для [PortProtonQt](https://github.com/Linux-Gaming/PortProtonQt) — Linux-лаунчера для Windows-игр через Proton/Wine.

## 📦 Доступные темы

### Темы из Omarchy / популярных цветовых схем

| Тема | Стиль |
|------|-------|
| **Nord** | Арктическая сине-серая палитра |
| **Catppuccin** | Пастельная уютная палитра (Mocha) |
| **Miasma** | Органическая оливково-зеленая палитра |
| **Tokyo Night** | Неоновые ночные огни Токио |
| **Rose Pine** | Мягкая пастельная палитра Rosé Pine |
| **Kanagawa** | Японская волна — глубокие сине-фиолетовые тона |
| **Everforest** | Уютная природная зеленая палитра |

### Тематические темы

| Тема | Стиль |
|------|-------|
| **Steam Classic 2004** | Ретро-стиль VGUI Steam лаунчера 2004 года |
| **Steam Modern** | Современный интерфейс Steam Client |
| **Hannah Montana** | Яркая розово-фиолетовая эстетика HML |

## 🚀 Установка

### Ручная установка

1. Скопируйте папку нужной темы в:
   ```
   ~/.local/share/PortProtonQt/themes/
   ```
2. Перезапустите PortProtonQt
3. Выберите тему в настройках

### Пример

```bash
git clone https://github.com/rosakodu/ppqt-themes.git
cp -r ppqt-themes/nord ~/.local/share/PortProtonQt/themes/
cp -r ppqt-themes/catppuccin ~/.local/share/PortProtonQt/themes/
```

## 📁 Структура темы

```
theme-name/
├── styles.py          # Палитра цветов, анимации, стили
├── metainfo.ini       # Метаданные (название, автор)
└── images/
    └── screenshots/   # Скриншоты-превью темы
```

## 🎨 Источники палитр

- [Nord](https://www.nordtheme.com/) — Arctic, north-bluish color palette
- [Catppuccin](https://github.com/catppuccin/catppuccin) — Soothing pastel theme
- [Miasma](https://github.com/xero/miasma.nvim) — Dark, organic color scheme by xero
- [Tokyo Night](https://github.com/enkia/tokyo-night-vscode-theme) — Night city lights theme
- [Rosé Pine](https://rosepinetheme.com/) — All natural pine, faux fur and a bit of soho vibes
- [Kanagawa](https://github.com/rebelot/kanagawa.nvim) — Dark theme inspired by Katsushika Hokusai
- [Everforest](https://github.com/sainnhe/everforest) — Green-based warm color scheme
- [Omarchy Themes](https://omarchythemes.com/) — Community themes for Omarchy

## 📝 Лицензия

MIT

## 👤 Автор

**rosakodu** — [GitHub](https://github.com/rosakodu)

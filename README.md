# 🎨 PortProtonQt Themes

Коллекция красивых тем для [PortProtonQt](https://github.com/Linux-Gaming/PortProtonQt) — Linux-лаунчера для Windows-игр через Proton/Wine.

## 📦 Доступные темы

### Темы из Omarchy / популярных цветовых схем

| Тема | Вариант | Стиль |
|------|---------|-------|
| **Nord** | Dark / Light | Арктическая сине-серая палитра |
| **Catppuccin** | Mocha (Dark) / Latte (Light) | Пастельная уютная палитра |
| **Miasma** | Dark | Органическая оливково-зеленая палитра |
| **Tokyo Night** | Dark / Light | Неоновые ночные огни Токио |
| **Rose Pine** | Dark / Dawn (Light) | Мягкая пастельная палитра |
| **Dracula** | Dark | Классическая фиолетовая палитра Дракулы |
| **Kanagawa** | Dark | Японская волна — синие и фиолетовые тона |
| **Everforest** | Dark / Light | Природная зеленая палитра |

### Тематические темы

| Тема | Вариант | Стиль |
|------|---------|-------|
| **Steam Classic 2004** | Dark | Ретро-стиль VGUI Steam лаунчера 2004 года |
| **Steam Modern** | Dark | Современный интерфейс Steam Client |
| **Hannah Montana** | Dark | Яркая розово-фиолетовая эстетика HML |

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
- [Dracula](https://draculatheme.com/) — Dark theme for everything
- [Kanagawa](https://github.com/rebelot/kanagawa.nvim) — Dark theme inspired by Katsushika Hokusai
- [Everforest](https://github.com/sainnhe/everforest) — Green-based warm color scheme
- [Omarchy Themes](https://omarchythemes.com/) — Community themes for Omarchy

## 📝 Лицензия

MIT

## 👤 Автор

**rosakodu** — [GitHub](https://github.com/rosakodu)

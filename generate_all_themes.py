import os

BASE_DIR = "/home/rosakodu/Projects/PortProtonQt Themes"
AUTHOR = "rosakodu"
AUTHOR_LINK = "https://github.com/rosakodu/ppqt-themes"

def create_theme(folder, metainfo_data, styles_code):
    theme_path = os.path.join(BASE_DIR, folder)
    os.makedirs(theme_path, exist_ok=True)
    
    meta_content = f"""[Metainfo]
dark_variant = {metainfo_data['dark_variant']}
light_variant = {metainfo_data['light_variant']}
name_en = {metainfo_data['name_en']}
name_ru = {metainfo_data['name_ru']}
author = {AUTHOR}
author_link = {AUTHOR_LINK}
description_en = {metainfo_data['description_en']}
description_ru = {metainfo_data['description_ru']}
"""
    with open(os.path.join(theme_path, "metainfo.ini"), "w", encoding="utf-8") as f:
        f.write(meta_content)
        
    with open(os.path.join(theme_path, "styles.py"), "w", encoding="utf-8") as f:
        f.write(styles_code.strip() + "\n")
    print(f"Updated theme: {folder}")

def make_styles(inherits, bg, bg_darker, surface, surface_elevated, surface_hover, card_bg, text, text_muted, disabled_text, border, accent, accent_dark, accent_blue, grad_colors, bg_gradient_stops, font="Inter", r_small="8px", r_large="14px", r_card="18px", preloader_style="pulse", anim_type="gradient"):
    nav_inactive = text_muted
    separator = border
    scrollbar_bg = bg_darker
    scrollbar_handle = surface_hover
    slider_handle = accent
    slider_groove_bg = surface
    border_subtle = "rgba(255, 255, 255, 0.05)"
    border_input = accent
    border_light = border
    border_faint = "rgba(255, 255, 255, 0.08)"
    border_focus = accent
    checkbox_unchecked = surface
    checkbox_hover = surface_elevated
    combo_disabled_bg = bg_darker
    combo_disabled_border = surface
    overlay = "rgba(0,0,0,0.85)"
    detail_overlay = "rgba(0,0,0,0.5)"
    cover_frame_bg = surface

    grad_list_str = ",\n        ".join([f'{{"position": {p}, "color": "{c}"}}' for p, c in grad_colors])
    bg_stops_str = ",\n            ".join([f'stop:{p} {c}' for p, c in bg_gradient_stops])
    detail_grad_str = ",\n    ".join([f'{{"position": {p}, "color": "{c}"}}' for p, c in bg_gradient_stops])

    return f'''THEME_INHERITS = "{inherits}"

color_accent = "{accent}"
color_accent_dark = "{accent_dark}"
color_accent_blue = "{accent_blue}"
color_preloader = "{accent}"
color_bg = "{bg}"
color_bg_darker = "{bg_darker}"
color_surface = "{surface}"
color_surface_elevated = "{surface_elevated}"
color_surface_hover = "{surface_hover}"
color_card_bg = "{card_bg}"
color_text = "{text}"
color_text_muted = "{text_muted}"
color_disabled_text = "{disabled_text}"
color_border = "{border}"

color_nav_inactive = "{nav_inactive}"
color_separator = "{separator}"
color_scrollbar_bg = "{scrollbar_bg}"
color_scrollbar_handle = "{scrollbar_handle}"
color_slider_handle = "{slider_handle}"
color_slider_groove_bg = "{slider_groove_bg}"
color_border_subtle = "{border_subtle}"
color_border_input = "{border_input}"
color_border_light = "{border_light}"
color_border_faint = "{border_faint}"
color_border_focus = "{border_focus}"
color_checkbox_unchecked_bg = "{checkbox_unchecked}"
color_checkbox_hover_bg = "{checkbox_hover}"
color_combo_disabled_bg = "{combo_disabled_bg}"
color_combo_disabled_border = "{combo_disabled_border}"
color_overlay = "{overlay}"
color_detail_overlay = "{detail_overlay}"
color_cover_frame_bg = "{cover_frame_bg}"

LIBRARY_WIDGET_STYLE = f"""
    QWidget {{{{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            {bg_stops_str});
        border-radius: 0px;
    }}}}
"""

SOURCE_CORNER = {{
    "ribbon_color": "{surface}",
    "ribbon_fold_color": "#00000096",
    "size_ratio": 0.28,
    "min_size": 54,
    "min_widget_size": 4,
}}

font_family = "{font}"
border_radius_small = "{r_small}"
border_radius_large = "{r_large}"
border_radius_card = "{r_card}"

LIBRARY_LAYOUT_MODE = "grid"
DETAIL_PAGE_LAYOUT_MODE = "full"
DETAIL_PAGE_BG_MODE = "gradient"

DETAIL_PAGE_GRADIENT = [
    {detail_grad_str}
]

PRELOADER = {{
    "style": "{preloader_style}",
    "pulse_count": 3,
    "pulse_max_radius": 42,
    "pulse_speed": 2.2,
    "pulse_color": color_accent,
    "dots_count": 8,
    "dots_radius": 36,
    "dots_dot_size": 5,
    "dots_speed": 3.0,
    "dots_color": color_accent,
    "wave_width": 80,
    "wave_amplitude": 15,
    "wave_speed": 2.5,
    "wave_line_width": 3,
    "wave_color": color_accent,
}}

GAME_CARD_ANIMATION = {{
    "detail_page_animation_type": "fade",
    "default_border_width": 2,
    "hover_border_width": 6,
    "focus_border_width": 8,
    "pulse_min_border_width": 6,
    "pulse_max_border_width": 8,
    "thickness_anim_duration": 250,
    "pulse_anim_duration": 800,
    "gradient_anim_duration": 3000,
    "gradient_start_angle": 360,
    "gradient_end_angle": 0,
    "card_animation_type": "{anim_type}",
    "fill_color": color_accent,
    "fill_alpha": 90,
    "stripe_color": color_accent,
    "stripe_alpha": 255,
    "glow_base_alpha": 120,
    "glow_pulse_alpha": 80,
    "default_scale": 1.0,
    "hover_scale": 1.05,
    "focus_scale": 1.03,
    "scale_anim_duration": 200,
    "thickness_easing_curve": "OutBack",
    "thickness_easing_curve_out": "InBack",
    "scale_easing_curve": "OutBack",
    "scale_easing_curve_out": "InBack",
    "gradient_colors": [
        {grad_list_str}
    ],
    "detail_page_fade_duration": 350,
    "detail_page_slide_duration": 500,
    "detail_page_bounce_duration": 400,
    "detail_page_fade_duration_exit": 350,
    "detail_page_slide_duration_exit": 500,
    "detail_page_bounce_duration_exit": 400,
    "detail_page_easing_curve": "OutCubic",
    "detail_page_easing_curve_exit": "InCubic",
}}

ICON_COLORS = {{
    "tray_portproton": color_accent,
    "*_hover": color_text,
    "*_pressed": color_accent,
    "*_focused": color_accent,
}}
'''

# 1. Nord
create_theme("nord",
    {"dark_variant": "nord", "light_variant": "nord", "name_en": "Nord", "name_ru": "Nord", "description_en": "Arctic, dark bluish-gray color palette theme.", "description_ru": "Тема в арктической темно-синей палитре Nord."},
    make_styles("standart", "#2e3440", "#242933", "#3b4252", "#434c5e", "#4c566a", "#3b4252", "#eceff4", "#d8dee9", "#4c566a", "#4c566a", "#88c0d0", "#5e81ac", "#81a1c1", [(0, "#88c0d0"), (0.5, "#81a1c1"), (1, "#88c0d0")], [(0, "#1b1f27"), (0.5, "#2e3440"), (1, "#3b4252")], r_card="18px")
)

# 2. Catppuccin
create_theme("catppuccin",
    {"dark_variant": "catppuccin", "light_variant": "catppuccin", "name_en": "Catppuccin", "name_ru": "Catppuccin", "description_en": "Soothing pastel theme (Mocha variant).", "description_ru": "Пастельная тёмная тема Catppuccin (Mocha)."},
    make_styles("standart", "#1e1e2e", "#181825", "#313244", "#45475a", "#585b70", "#313244", "#cdd6f4", "#a6adc8", "#585b70", "#45475a", "#cba6f7", "#b4befe", "#89b4fa", [(0, "#cba6f7"), (0.5, "#89b4fa"), (1, "#cba6f7")], [(0, "#11111b"), (0.5, "#1e1e2e"), (1, "#313244")], r_card="18px")
)

# 3. Miasma
create_theme("miasma",
    {"dark_variant": "miasma", "light_variant": "miasma", "name_en": "Miasma", "name_ru": "Miasma", "description_en": "Organic dark olive Miasma theme by xero.", "description_ru": "Органическая тёмно-оливковая тема Miasma."},
    make_styles("standart", "#222222", "#1a1a1a", "#2c2c2c", "#333333", "#3c3c3c", "#2c2c2c", "#c2c2b0", "#8a8a7a", "#666666", "#444444", "#78824b", "#5f875f", "#c9a554", [(0, "#78824b"), (0.5, "#bb7744"), (1, "#c9a554")], [(0, "#181818"), (0.5, "#22251d"), (1, "#2a2e22")], r_card="18px", preloader_style="wave")
)

# 4. Tokyo Night
create_theme("tokyo-night", 
    {"dark_variant": "tokyo-night", "light_variant": "tokyo-night", "name_en": "Tokyo Night", "name_ru": "Tokyo Night", "description_en": "Vibrant Tokyo Night city aesthetic theme.", "description_ru": "Тёмная тема в стиле ночных огней Токио."},
    make_styles("standart", "#1a1b26", "#16161e", "#24283b", "#292e42", "#343b58", "#24283b", "#c0caf5", "#a9b1d6", "#565f89", "#3b4261", "#7aa2f7", "#3d59a1", "#7dcfff", [(0, "#7aa2f7"), (0.5, "#bb9af7"), (1, "#7aa2f7")], [(0, "#13141c"), (0.5, "#1a1b26"), (1, "#24283b")], r_card="18px")
)

# 5. Rosé Pine
create_theme("rose-pine", 
    {"dark_variant": "rose-pine", "light_variant": "rose-pine", "name_en": "Rosé Pine", "name_ru": "Rosé Pine", "description_en": "Soothing all-natural pine pastel theme.", "description_ru": "Уютная тёмно-пастельная тема Rosé Pine."},
    make_styles("standart", "#191724", "#1f1d2e", "#26233a", "#2a2837", "#393552", "#26233a", "#e0def4", "#908caa", "#6e6a86", "#393552", "#c4a7e7", "#9ccfd8", "#31748f", [(0, "#c4a7e7"), (0.5, "#ebbcba"), (1, "#c4a7e7")], [(0, "#12101d"), (0.5, "#191724"), (1, "#26233a")], r_card="18px", preloader_style="dots")
)

# 6. Dracula
create_theme("dracula", 
    {"dark_variant": "dracula", "light_variant": "dracula", "name_en": "Dracula", "name_ru": "Dracula", "description_en": "Famous dark purple theme for PortProtonQt.", "description_ru": "Легендарная тёмно-фиолетовая тема Dracula."},
    make_styles("standart", "#282a36", "#21222c", "#44475a", "#4d5066", "#6272a4", "#44475a", "#f8f8f2", "#bfbfb9", "#6272a4", "#44475a", "#bd93f9", "#ff79c6", "#8be9fd", [(0, "#bd93f9"), (0.33, "#ff79c6"), (0.66, "#8be9fd"), (1, "#bd93f9")], [(0, "#191a21"), (0.5, "#282a36"), (1, "#383a59")], r_card="18px")
)

# 7. Kanagawa
create_theme("kanagawa", 
    {"dark_variant": "kanagawa", "light_variant": "kanagawa", "name_en": "Kanagawa", "name_ru": "Kanagawa", "description_en": "Dark theme inspired by Katsushika Hokusai artworks.", "description_ru": "Эстетичная тёмная тема в японском стиле Kanagawa."},
    make_styles("standart", "#1f1f28", "#16161d", "#2a2a37", "#363646", "#54546d", "#2a2a37", "#dcd7ba", "#c8c093", "#727169", "#363646", "#7e9cd8", "#957fb8", "#7fb4ca", [(0, "#7e9cd8"), (0.5, "#957fb8"), (1, "#7e9cd8")], [(0, "#15151c"), (0.5, "#1f1f28"), (1, "#2a2a37")], r_card="18px", preloader_style="wave")
)

# 8. Everforest
create_theme("everforest", 
    {"dark_variant": "everforest", "light_variant": "everforest", "name_en": "Everforest", "name_ru": "Everforest", "description_en": "Warm, natural green forest palette theme.", "description_ru": "Уютная природная зелёная тема Everforest."},
    make_styles("standart", "#2d353b", "#272e33", "#343f44", "#3d484d", "#475258", "#343f44", "#d3c6aa", "#9da9a0", "#7a8478", "#475258", "#a7c080", "#83c092", "#7fbbb3", [(0, "#a7c080"), (0.5, "#83c092"), (1, "#a7c080")], [(0, "#1e2529"), (0.5, "#2d353b"), (1, "#343f44")], r_card="18px", preloader_style="dots")
)

# 9. Hannah Montana
create_theme("hannah-montana", 
    {"dark_variant": "hannah-montana", "light_variant": "hannah-montana", "name_en": "Hannah Montana", "name_ru": "Ханна Монтана", "description_en": "Vibrant pink-purple Hannah Montana aesthetic theme.", "description_ru": "Яркая розово-фиолетовая тема в стиле Ханны Монтаны."},
    make_styles("standart", "#1e0a2e", "#150720", "#2d1545", "#3a1d58", "#4a2570", "#2d1545", "#f5e6ff", "#c9a8e8", "#6b4d8a", "#3a1d58", "#ff69b4", "#da70d6", "#87ceeb", [(0, "#ff69b4"), (0.33, "#da70d6"), (0.66, "#87ceeb"), (1, "#ff69b4")], [(0, "#12041d"), (0.5, "#1e0a2e"), (1, "#301748")], font="Inter", r_card="18px")
)

# 10. Steam Classic 2004 (Stripe / Square borders)
create_theme("steam-2004", 
    {"dark_variant": "steam-2004", "light_variant": "steam-2004", "name_en": "Steam Classic 2004", "name_ru": "Классический Steam 2004", "description_en": "Classic 2004 VGUI olive-green Steam launcher aesthetic theme.", "description_ru": "Классическая оливково-зеленая эстетика Steam 2004 (VGUI)."},
    make_styles("standart", "#4c5844", "#3d4837", "#586650", "#64745c", "#6e8064", "#434e3c", "#e1ebd9", "#a8b89e", "#68785c", "#2f362a", "#849874", "#5a6850", "#a4ba92", [(0, "#849874"), (0.5, "#a4ba92"), (1, "#849874")], [(0, "#333b2e"), (0.5, "#4c5844"), (1, "#586650")], font="Tahoma", r_small="2px", r_large="4px", r_card="2px", anim_type="stripe")
)

# 11. Steam Modern (Stripe / Square borders without rounded animation corners)
create_theme("steam-modern", 
    {"dark_variant": "steam-modern", "light_variant": "steam-modern", "name_en": "Steam Modern", "name_ru": "Новый Steam", "description_en": "Modern Steam Client desktop aesthetic theme.", "description_ru": "Современная темно-синяя эстетика клиента Steam."},
    make_styles("standart", "#171d25", "#10151c", "#1e2633", "#283548", "#314159", "#1e2633", "#f3f3f3", "#96a5b7", "#4a596e", "#2a374d", "#1a9fff", "#0078d4", "#66c0f4", [(0, "#1a9fff"), (0.5, "#66c0f4"), (1, "#1a9fff")], [(0, "#0e1218"), (0.5, "#171d25"), (1, "#1e2633")], font="Inter", r_small="4px", r_large="6px", r_card="4px", anim_type="stripe")
)

print("UPDATED STEAM MODERN WITH RECTANGULAR STRIPE ANIMATION BORDERS!")

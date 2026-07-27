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
    print(f"Created theme: {folder}")

def make_styles(inherits, bg, bg_darker, surface, surface_elevated, surface_hover, card_bg, text, text_muted, disabled_text, border, accent, accent_dark, accent_blue, grad_colors, font="Inter", r_small="8px", r_large="14px", r_card="12px", preloader_style="pulse", is_light=False):
    nav_inactive = text_muted
    separator = border
    scrollbar_bg = bg_darker
    scrollbar_handle = surface_hover
    slider_handle = accent
    slider_groove_bg = surface
    border_subtle = "rgba(255, 255, 255, 0.05)" if not is_light else "rgba(0, 0, 0, 0.05)"
    border_input = accent
    border_light = border
    border_faint = "rgba(255, 255, 255, 0.08)" if not is_light else "rgba(0, 0, 0, 0.08)"
    border_focus = accent
    checkbox_unchecked = surface
    checkbox_hover = surface_elevated
    combo_disabled_bg = bg_darker
    combo_disabled_border = surface
    overlay = "rgba(0,0,0,0.85)"
    detail_overlay = "rgba(0,0,0,0.5)"
    cover_frame_bg = surface

    grad_list_str = ",\n        ".join([f'{{"position": {p}, "color": "{c}"}}' for p, c in grad_colors])

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
        background-color: {bg};
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
    {{"position": 0, "color": "{bg}"}},
    {{"position": 1, "color": "{bg}"}},
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
    "card_animation_type": "gradient",
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

# 1. Tokyo Night
create_theme("tokyo-night", 
    {"dark_variant": "tokyo-night", "light_variant": "tokyo-night-light", "name_en": "Tokyo Night", "name_ru": "Tokyo Night", "description_en": "Vibrant Tokyo Night city aesthetic theme.", "description_ru": "Тёмная тема в стиле ночных огней Токио."},
    make_styles("standart", "#1a1b26", "#16161e", "#24283b", "#292e42", "#343b58", "#24283b", "#c0caf5", "#a9b1d6", "#565f89", "#3b4261", "#7aa2f7", "#3d59a1", "#7dcfff", [(0, "#7aa2f7"), (0.5, "#bb9af7"), (1, "#7aa2f7")])
)

# 2. Tokyo Night Light
create_theme("tokyo-night-light", 
    {"dark_variant": "tokyo-night", "light_variant": "tokyo-night-light", "name_en": "Tokyo Night Light", "name_ru": "Tokyo Night Светлая", "description_en": "Light variant of Tokyo Night theme.", "description_ru": "Светлая тема в стиле Tokyo Night."},
    make_styles("standart-light", "#d5d6db", "#c8c8cf", "#c8c8cf", "#b8b8c0", "#a8a8b0", "#c8c8cf", "#343b58", "#565f89", "#9699a3", "#b8b8c0", "#34548a", "#343b58", "#34548a", [(0, "#34548a"), (0.5, "#5a4a78"), (1, "#34548a")], is_light=True)
)

# 3. Rosé Pine
create_theme("rose-pine", 
    {"dark_variant": "rose-pine", "light_variant": "rose-pine-dawn", "name_en": "Rosé Pine", "name_ru": "Rosé Pine", "description_en": "Soothing all-natural pine pastel theme.", "description_ru": "Уютная тёмно-пастельная тема Rosé Pine."},
    make_styles("standart", "#191724", "#1f1d2e", "#26233a", "#2a2837", "#393552", "#26233a", "#e0def4", "#908caa", "#6e6a86", "#393552", "#c4a7e7", "#9ccfd8", "#31748f", [(0, "#c4a7e7"), (0.5, "#ebbcba"), (1, "#c4a7e7")], r_small="10px", r_large="16px", r_card="14px", preloader_style="dots")
)

# 4. Rosé Pine Dawn
create_theme("rose-pine-dawn", 
    {"dark_variant": "rose-pine", "light_variant": "rose-pine-dawn", "name_en": "Rosé Pine Dawn", "name_ru": "Rosé Pine Dawn", "description_en": "Light variant of Rosé Pine theme.", "description_ru": "Светлая пастельная тема Rosé Pine Dawn."},
    make_styles("standart-light", "#faf4ed", "#fffaf3", "#f2e9e1", "#e4dfde", "#d7d1cc", "#f2e9e1", "#575279", "#797593", "#9893a5", "#dfdad9", "#907aa9", "#56949f", "#286983", [(0, "#907aa9"), (0.5, "#d7827e"), (1, "#907aa9")], r_small="10px", r_large="16px", r_card="14px", preloader_style="dots", is_light=True)
)

# 5. Dracula
create_theme("dracula", 
    {"dark_variant": "dracula", "light_variant": "dracula", "name_en": "Dracula", "name_ru": "Dracula", "description_en": "Famous dark purple theme for PortProtonQt.", "description_ru": "Легендарная тёмно-фиолетовая тема Dracula."},
    make_styles("standart", "#282a36", "#21222c", "#44475a", "#4d5066", "#6272a4", "#44475a", "#f8f8f2", "#bfbfb9", "#6272a4", "#44475a", "#bd93f9", "#ff79c6", "#8be9fd", [(0, "#bd93f9"), (0.33, "#ff79c6"), (0.66, "#8be9fd"), (1, "#bd93f9")])
)

# 6. Kanagawa
create_theme("kanagawa", 
    {"dark_variant": "kanagawa", "light_variant": "kanagawa", "name_en": "Kanagawa", "name_ru": "Kanagawa", "description_en": "Dark theme inspired by Katsushika Hokusai artworks.", "description_ru": "Эстетичная тёмная тема в японском стиле Kanagawa."},
    make_styles("standart", "#1f1f28", "#16161d", "#2a2a37", "#363646", "#54546d", "#2a2a37", "#dcd7ba", "#c8c093", "#727169", "#363646", "#7e9cd8", "#957fb8", "#7fb4ca", [(0, "#7e9cd8"), (0.5, "#957fb8"), (1, "#7e9cd8")], r_small="6px", r_large="12px", r_card="10px", preloader_style="wave")
)

# 7. Everforest
create_theme("everforest", 
    {"dark_variant": "everforest", "light_variant": "everforest-light", "name_en": "Everforest", "name_ru": "Everforest", "description_en": "Warm, natural green forest palette theme.", "description_ru": "Уютная природная зелёная тема Everforest."},
    make_styles("standart", "#2d353b", "#272e33", "#343f44", "#3d484d", "#475258", "#343f44", "#d3c6aa", "#9da9a0", "#7a8478", "#475258", "#a7c080", "#83c092", "#7fbbb3", [(0, "#a7c080"), (0.5, "#83c092"), (1, "#a7c080")], preloader_style="dots")
)

# 8. Everforest Light
create_theme("everforest-light", 
    {"dark_variant": "everforest", "light_variant": "everforest-light", "name_en": "Everforest Light", "name_ru": "Everforest Светлая", "description_en": "Light warm green Everforest theme.", "description_ru": "Светлая природная зеленая тема Everforest."},
    make_styles("standart-light", "#fdf6e3", "#f4f0d9", "#efebd4", "#e5dfc8", "#d8d3ba", "#efebd4", "#5c6a72", "#829181", "#a6b0a0", "#e0dcc7", "#8da101", "#35a77c", "#3a94c5", [(0, "#8da101"), (0.5, "#35a77c"), (1, "#8da101")], preloader_style="dots", is_light=True)
)

# 9. Hannah Montana
create_theme("hannah-montana", 
    {"dark_variant": "hannah-montana", "light_variant": "hannah-montana", "name_en": "Hannah Montana", "name_ru": "Ханна Монтана", "description_en": "Vibrant pink-purple Hannah Montana aesthetic theme.", "description_ru": "Яркая розово-фиолетовая тема в стиле Ханны Монтаны."},
    make_styles("standart", "#1e0a2e", "#150720", "#2d1545", "#3a1d58", "#4a2570", "#2d1545", "#f5e6ff", "#c9a8e8", "#6b4d8a", "#3a1d58", "#ff69b4", "#da70d6", "#87ceeb", [(0, "#ff69b4"), (0.33, "#da70d6"), (0.66, "#87ceeb"), (1, "#ff69b4")], font="Inter", r_small="12px", r_large="20px", r_card="16px")
)

print("RE-GENERATED ALL 9 THEMES CORRECTLY!")

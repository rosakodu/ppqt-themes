THEME_INHERITS = "standart"

# === Catppuccin Mocha Core Palette ===
color_accent = "#cba6f7"        # Mauve
color_accent_dark = "#b4befe"   # Lavender
color_accent_blue = "#89b4fa"   # Blue
color_preloader = "#cba6f7"
color_bg = "#1e1e2e"            # Base
color_bg_darker = "#181825"     # Mantle
color_surface = "#313244"       # Surface0
color_surface_elevated = "#45475a" # Surface1
color_surface_hover = "#585b70"  # Surface2
color_card_bg = "#313244"
color_text = "#cdd6f4"          # Text
color_text_muted = "#a6adc8"    # Subtext0
color_disabled_text = "#585b70"
color_border = "#45475a"        # Surface1

# === Widget & Navigation Colors ===
color_nav_inactive = "#a6adc8"
color_separator = "#45475a"
color_scrollbar_bg = "#181825"
color_scrollbar_handle = "#585b70"
color_slider_handle = "#cba6f7"
color_slider_groove_bg = "#313244"
color_border_subtle = "rgba(205, 214, 244, 0.05)"
color_border_input = "#cba6f7"
color_border_light = "#45475a"
color_border_faint = "rgba(205, 214, 244, 0.08)"
color_border_focus = "#cba6f7"
color_checkbox_unchecked_bg = "#313244"
color_checkbox_hover_bg = "#45475a"
color_combo_disabled_bg = "#181825"
color_combo_disabled_border = "#313244"
color_overlay = "rgba(30, 30, 46, 0.9)"
color_detail_overlay = "rgba(30, 30, 46, 0.6)"
color_cover_frame_bg = "rgba(49, 50, 68, 0.85)"

# === Flat Background Style (No Gradients) ===
LIBRARY_WIDGET_STYLE = f"""
    QWidget {{
        background-color: {color_bg};
        border-radius: 0px;
    }}
"""

SOURCE_CORNER = {
    "ribbon_color": "#313244",
    "ribbon_fold_color": "#00000096",
    "size_ratio": 0.28,
    "min_size": 54,
    "min_widget_size": 4,
}

font_family = "Inter"
border_radius_small = "10px"
border_radius_large = "16px"
border_radius_card = "14px"

LIBRARY_LAYOUT_MODE = "grid"
DETAIL_PAGE_LAYOUT_MODE = "full"
DETAIL_PAGE_BG_MODE = "gradient"

DETAIL_PAGE_GRADIENT = [
    {"position": 0, "color": color_bg},
    {"position": 1, "color": color_bg},
]

PRELOADER = {
    "style": "pulse",
    "pulse_count": 3,
    "pulse_max_radius": 42,
    "pulse_speed": 2.2,
    "pulse_color": color_accent,
}

GAME_CARD_ANIMATION = {
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
        {"position": 0, "color": "#cba6f7"},
        {"position": 0.33, "color": "#89b4fa"},
        {"position": 0.66, "color": "#f5c2e7"},
        {"position": 1, "color": "#cba6f7"},
    ],
    "detail_page_fade_duration": 350,
    "detail_page_slide_duration": 500,
    "detail_page_bounce_duration": 400,
    "detail_page_fade_duration_exit": 350,
    "detail_page_slide_duration_exit": 500,
    "detail_page_bounce_duration_exit": 400,
    "detail_page_easing_curve": "OutCubic",
    "detail_page_easing_curve_exit": "InCubic",
}

ICON_COLORS = {
    "tray_portproton": color_accent,
    "*_hover": color_text,
    "*_pressed": color_accent,
    "*_focused": color_accent,
}

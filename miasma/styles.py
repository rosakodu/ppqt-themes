THEME_INHERITS = "standart"

# === Official Miasma Palette (by xero / omarchytheme.com) ===
color_accent = "#78824b"        # Olive Green (miasma accent)
color_accent_dark = "#5f875f"   # Green (color2)
color_accent_blue = "#c9a554"   # Gold (color6)
color_preloader = "#78824b"
color_bg = "#222222"            # Background
color_bg_darker = "#1a1a1a"     # Darker Base
color_surface = "#2c2c2c"       # Surface
color_surface_elevated = "#333333" # Elevated Surface
color_surface_hover = "#3c3c3c"  # Hover Surface
color_card_bg = "#2c2c2c"
color_text = "#c2c2b0"          # Foreground (exact miasma)
color_text_muted = "#8a8a7a"    # Muted Text (warm tint)
color_disabled_text = "#666666" # color0
color_border = "#444444"        # Border

# === Widget & Navigation Colors ===
color_nav_inactive = "#8a8a7a"
color_separator = "#444444"
color_scrollbar_bg = "#1a1a1a"
color_scrollbar_handle = "#685742"  # Brown (color1)
color_slider_handle = "#78824b"
color_slider_groove_bg = "#2c2c2c"
color_border_subtle = "rgba(194, 194, 176, 0.05)"
color_border_input = "#78824b"
color_border_light = "#444444"
color_border_faint = "rgba(194, 194, 176, 0.08)"
color_border_focus = "#78824b"
color_checkbox_unchecked_bg = "#2c2c2c"
color_checkbox_hover_bg = "#333333"
color_combo_disabled_bg = "#1a1a1a"
color_combo_disabled_border = "#2c2c2c"
color_overlay = "rgba(34, 34, 34, 0.9)"
color_detail_overlay = "rgba(34, 34, 34, 0.6)"
color_cover_frame_bg = "rgba(44, 44, 44, 0.85)"

# === Flat Background Style (No Gradients) ===
LIBRARY_WIDGET_STYLE = f"""
    QWidget {{
        background-color: {color_bg};
        border-radius: 0px;
    }}
"""

SOURCE_CORNER = {
    "ribbon_color": "#2c2c2c",
    "ribbon_fold_color": "#00000096",
    "size_ratio": 0.28,
    "min_size": 54,
    "min_widget_size": 4,
}

font_family = "Inter"
border_radius_small = "6px"
border_radius_large = "12px"
border_radius_card = "10px"

LIBRARY_LAYOUT_MODE = "grid"
DETAIL_PAGE_LAYOUT_MODE = "full"
DETAIL_PAGE_BG_MODE = "gradient"

DETAIL_PAGE_GRADIENT = [
    {"position": 0, "color": color_bg},
    {"position": 1, "color": color_bg},
]

PRELOADER = {
    "style": "wave",
    "wave_width": 80,
    "wave_amplitude": 15,
    "wave_speed": 2.5,
    "wave_line_width": 3,
    "wave_color": color_accent,
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
    "hover_scale": 1.04,
    "focus_scale": 1.02,
    "scale_anim_duration": 200,
    "thickness_easing_curve": "OutBack",
    "thickness_easing_curve_out": "InBack",
    "scale_easing_curve": "OutBack",
    "scale_easing_curve_out": "InBack",
    "gradient_colors": [
        {"position": 0, "color": "#78824b"},
        {"position": 0.33, "color": "#bb7744"},
        {"position": 0.66, "color": "#c9a554"},
        {"position": 1, "color": "#78824b"},
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

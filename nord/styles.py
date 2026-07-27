THEME_INHERITS = "standart"

# === Nord Core Palette ===
color_accent = "#88c0d0"        # Nord8 (Frost)
color_accent_dark = "#5e81ac"   # Nord10 (Frost Dark)
color_accent_blue = "#81a1c1"   # Nord9 (Frost Blue)
color_preloader = "#88c0d0"
color_bg = "#2e3440"            # Nord0 (Polar Night)
color_bg_darker = "#242933"     # Darker Polar Night
color_surface = "#3b4252"       # Nord1 (Polar Night Light)
color_surface_elevated = "#434c5e" # Nord2
color_surface_hover = "#4c566a"  # Nord3
color_card_bg = "#3b4252"
color_text = "#eceff4"          # Nord6 (Snow Storm)
color_text_muted = "#d8dee9"    # Nord4
color_disabled_text = "#4c566a"
color_border = "#4c566a"        # Nord3

# === Widget & Navigation Colors ===
color_nav_inactive = "#d8dee9"
color_separator = "#4c566a"
color_scrollbar_bg = "#242933"
color_scrollbar_handle = "#4c566a"
color_slider_handle = "#88c0d0"
color_slider_groove_bg = "#3b4252"
color_border_subtle = "rgba(236, 239, 244, 0.05)"
color_border_input = "#88c0d0"
color_border_light = "#4c566a"
color_border_faint = "rgba(236, 239, 244, 0.08)"
color_border_focus = "#88c0d0"
color_checkbox_unchecked_bg = "#3b4252"
color_checkbox_hover_bg = "#434c5e"
color_combo_disabled_bg = "#242933"
color_combo_disabled_border = "#3b4252"
color_overlay = "rgba(46, 52, 64, 0.9)"
color_detail_overlay = "rgba(46, 52, 64, 0.6)"
color_cover_frame_bg = "rgba(59, 66, 82, 0.85)"

# === Flat Background Style (No Gradients) ===
LIBRARY_WIDGET_STYLE = f"""
    QWidget {{
        background-color: {color_bg};
        border-radius: 0px;
    }}
"""

SOURCE_CORNER = {
    "ribbon_color": "#3b4252",
    "ribbon_fold_color": "#00000096",
    "size_ratio": 0.28,
    "min_size": 54,
    "min_widget_size": 4,
}

font_family = "Inter"
border_radius_small = "8px"
border_radius_large = "14px"
border_radius_card = "12px"

LIBRARY_LAYOUT_MODE = "grid"
DETAIL_PAGE_LAYOUT_MODE = "full"
DETAIL_PAGE_BG_MODE = "gradient"

DETAIL_PAGE_GRADIENT = [
    {"position": 0, "color": color_bg},
    {"position": 1, "color": color_bg},
]

PRELOADER = {
    "style": "dots",
    "dots_count": 8,
    "dots_radius": 36,
    "dots_dot_size": 5,
    "dots_speed": 3.0,
    "dots_color": color_accent,
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
    "gradient_anim_duration": 2500,
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
        {"position": 0, "color": "#88c0d0"},
        {"position": 0.33, "color": "#81a1c1"},
        {"position": 0.66, "color": "#b48ead"},
        {"position": 1, "color": "#88c0d0"},
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

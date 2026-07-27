THEME_INHERITS = "standart-light"

# === Nord Light Core Palette ===
color_accent = "#5e81ac"        # Nord10 (Frost Dark)
color_accent_dark = "#4c566a"   # Nord3
color_accent_blue = "#5e81ac"
color_preloader = "#5e81ac"
color_bg = "#eceff4"            # Nord6 (Snow Storm)
color_bg_darker = "#e5e9f0"     # Nord5
color_surface = "#e5e9f0"       # Nord5
color_surface_elevated = "#d8dee9" # Nord4
color_surface_hover = "#d8dee9"
color_card_bg = "#e5e9f0"       
color_text = "#2e3440"          # Nord0 (Polar Night)
color_text_muted = "#4c566a"    # Nord3
color_disabled_text = "#a3be8c"
color_border = "#d8dee9"        # Nord4

# === Widget & Navigation Colors ===
color_nav_inactive = "#4c566a"
color_separator = "#d8dee9"
color_scrollbar_bg = "#eceff4"
color_scrollbar_handle = "#d8dee9"
color_slider_handle = "#5e81ac"
color_slider_groove_bg = "#d8dee9"
color_border_subtle = "rgba(46, 52, 64, 0.05)"
color_border_input = "#5e81ac"
color_border_light = "#d8dee9"
color_border_faint = "rgba(46, 52, 64, 0.08)"
color_border_focus = "#5e81ac"
color_checkbox_unchecked_bg = "#e5e9f0"
color_checkbox_hover_bg = "#d8dee9"
color_combo_disabled_bg = "#e5e9f0"
color_combo_disabled_border = "#d8dee9"
color_overlay = "rgba(236, 239, 244, 0.9)"
color_detail_overlay = "rgba(236, 239, 244, 0.6)"
color_cover_frame_bg = "rgba(229, 233, 240, 0.85)"

# === Flat Background Style (No Gradients) ===
LIBRARY_WIDGET_STYLE = f"""
    QWidget {{
        background-color: {color_bg};
        border-radius: 0px;
    }}
"""

SOURCE_CORNER = {
    "ribbon_color": "#e5e9f0",
    "ribbon_fold_color": "#00000040",
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
        {"position": 0, "color": "#5e81ac"},
        {"position": 0.5, "color": "#81a1c1"},
        {"position": 1, "color": "#5e81ac"},
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

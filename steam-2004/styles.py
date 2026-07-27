THEME_INHERITS = "standart"

# === Steam 2004 Olive-Green Core Palette ===
color_accent = "#849874"        # Vintage Steam Green Accent
color_accent_dark = "#5a6850"   # Darker Steam Olive
color_accent_blue = "#a4ba92"   # Highlighted Green
color_preloader = "#849874"
color_bg = "#4c5844"            # Classic Steam Olive Background
color_bg_darker = "#3d4837"     # Darker Panel Background
color_surface = "#586650"       # Button/Surface Background
color_surface_elevated = "#64745c" # Raised Surface
color_surface_hover = "#6e8064"  # Hover Surface
color_card_bg = "#434e3c"       # Card Background
color_text = "#e1ebd9"          # Light Off-White/Green Text
color_text_muted = "#a8b89e"    # Muted Olive Text
color_disabled_text = "#68785c"
color_border = "#2f362a"        # Deep Olive Border

# === Widget & Navigation Colors ===
color_nav_inactive = "#a8b89e"
color_separator = "#3d4837"
color_scrollbar_bg = "#3d4837"
color_scrollbar_handle = "#6e8064"
color_slider_handle = "#849874"
color_slider_groove_bg = "#3d4837"
color_border_subtle = "rgba(225, 235, 217, 0.05)"
color_border_input = "#849874"
color_border_light = "#68785c"
color_border_faint = "rgba(225, 235, 217, 0.08)"
color_border_focus = "#a4ba92"
color_checkbox_unchecked_bg = "#3d4837"
color_checkbox_hover_bg = "#586650"
color_combo_disabled_bg = "#3d4837"
color_combo_disabled_border = "#4c5844"
color_overlay = "rgba(76, 88, 68, 0.95)"
color_detail_overlay = "rgba(76, 88, 68, 0.6)"
color_cover_frame_bg = "rgba(61, 72, 55, 0.85)"

# === Flat Background Style (Classic VGUI Solid) ===
LIBRARY_WIDGET_STYLE = f"""
    QWidget {{
        background-color: {color_bg};
        border-radius: 0px;
    }}
"""

SOURCE_CORNER = {
    "ribbon_color": "#3d4837",
    "ribbon_fold_color": "#00000096",
    "size_ratio": 0.28,
    "min_size": 54,
    "min_widget_size": 4,
}

font_family = "Tahoma"
border_radius_small = "2px"
border_radius_large = "4px"
border_radius_card = "4px"

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
    "default_border_width": 1,
    "hover_border_width": 4,
    "focus_border_width": 6,
    "pulse_min_border_width": 4,
    "pulse_max_border_width": 6,
    "thickness_anim_duration": 200,
    "pulse_anim_duration": 800,
    "gradient_anim_duration": 2500,
    "gradient_start_angle": 360,
    "gradient_end_angle": 0,
    "card_animation_type": "stripe",
    "fill_color": color_accent,
    "fill_alpha": 90,
    "stripe_color": color_accent,
    "stripe_alpha": 255,
    "glow_base_alpha": 120,
    "glow_pulse_alpha": 80,
    "default_scale": 1.0,
    "hover_scale": 1.03,
    "focus_scale": 1.02,
    "scale_anim_duration": 150,
    "thickness_easing_curve": "Linear",
    "thickness_easing_curve_out": "Linear",
    "scale_easing_curve": "Linear",
    "scale_easing_curve_out": "Linear",
    "gradient_colors": [
        {"position": 0, "color": "#849874"},
        {"position": 0.5, "color": "#a4ba92"},
        {"position": 1, "color": "#849874"},
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

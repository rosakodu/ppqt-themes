THEME_INHERITS = "standart-light"

# === Catppuccin Latte Core Palette ===
color_accent = "#8839ef"        # Latte Mauve
color_accent_dark = "#7287fd"   # Latte Lavender
color_accent_blue = "#1e66f5"   # Latte Blue
color_preloader = "#8839ef"
color_bg = "#eff1f5"            # Latte Base
color_bg_darker = "#e6e9ef"     # Latte Mantle
color_surface = "#e6e9ef"
color_surface_elevated = "#ccd0da" # Latte Surface0
color_surface_hover = "#bcc0cc"
color_card_bg = "#e6e9ef"
color_text = "#4c4f69"          # Latte Text
color_text_muted = "#6c6f85"    # Latte Subtext0
color_disabled_text = "#9ca0b0"
color_border = "#ccd0da"        # Latte Surface1

# === Widget & Navigation Colors ===
color_nav_inactive = "#6c6f85"
color_separator = "#ccd0da"
color_scrollbar_bg = "#eff1f5"
color_scrollbar_handle = "#bcc0cc"
color_slider_handle = "#8839ef"
color_slider_groove_bg = "#ccd0da"
color_border_subtle = "rgba(76, 79, 105, 0.05)"
color_border_input = "#8839ef"
color_border_light = "#ccd0da"
color_border_faint = "rgba(76, 79, 105, 0.08)"
color_border_focus = "#8839ef"
color_checkbox_unchecked_bg = "#e6e9ef"
color_checkbox_hover_bg = "#ccd0da"
color_combo_disabled_bg = "#e6e9ef"
color_combo_disabled_border = "#ccd0da"
color_overlay = "rgba(239, 241, 245, 0.9)"
color_detail_overlay = "rgba(239, 241, 245, 0.6)"
color_cover_frame_bg = "rgba(230, 233, 239, 0.85)"

# === Flat Background Style (No Gradients) ===
LIBRARY_WIDGET_STYLE = f"""
    QWidget {{
        background-color: {color_bg};
        border-radius: 0px;
    }}
"""

SOURCE_CORNER = {
    "ribbon_color": "#e6e9ef",
    "ribbon_fold_color": "#00000040",
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
        {"position": 0, "color": "#8839ef"},
        {"position": 0.5, "color": "#1e66f5"},
        {"position": 1, "color": "#ea76cb"},
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

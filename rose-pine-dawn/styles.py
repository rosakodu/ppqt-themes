THEME_INHERITS = "standart-light"

color_accent = "#907aa9"
color_accent_dark = "#56949f"
color_accent_blue = "#286983"
color_preloader = "#907aa9"
color_bg = "#faf4ed"
color_bg_darker = "#fffaf3"
color_surface = "#f2e9e1"
color_surface_elevated = "#e4dfde"
color_surface_hover = "#d7d1cc"
color_card_bg = "#f2e9e1"
color_text = "#575279"
color_text_muted = "#797593"
color_disabled_text = "#9893a5"
color_border = "#dfdad9"

color_nav_inactive = "#797593"
color_separator = "#dfdad9"
color_scrollbar_bg = "#fffaf3"
color_scrollbar_handle = "#d7d1cc"
color_slider_handle = "#907aa9"
color_slider_groove_bg = "#f2e9e1"
color_border_subtle = "rgba(0, 0, 0, 0.05)"
color_border_input = "#907aa9"
color_border_light = "#dfdad9"
color_border_faint = "rgba(0, 0, 0, 0.08)"
color_border_focus = "#907aa9"
color_checkbox_unchecked_bg = "#f2e9e1"
color_checkbox_hover_bg = "#e4dfde"
color_combo_disabled_bg = "#fffaf3"
color_combo_disabled_border = "#f2e9e1"
color_overlay = "rgba(0,0,0,0.85)"
color_detail_overlay = "rgba(0,0,0,0.5)"
color_cover_frame_bg = "#f2e9e1"

LIBRARY_WIDGET_STYLE = f"""
    QWidget {{
        background-color: #faf4ed;
        border-radius: 0px;
    }}
"""

SOURCE_CORNER = {
    "ribbon_color": "#f2e9e1",
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
    {"position": 0, "color": "#faf4ed"},
    {"position": 1, "color": "#faf4ed"},
]

PRELOADER = {
    "style": "dots",
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
        {"position": 0, "color": "#907aa9"},
        {"position": 0.5, "color": "#d7827e"},
        {"position": 1, "color": "#907aa9"}
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

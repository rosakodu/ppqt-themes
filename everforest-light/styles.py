THEME_INHERITS = "standart-light"

color_accent = "#8da101"
color_accent_dark = "#35a77c"
color_accent_blue = "#3a94c5"
color_preloader = "#8da101"
color_bg = "#fdf6e3"
color_bg_darker = "#f4f0d9"
color_surface = "#efebd4"
color_surface_elevated = "#e5dfc8"
color_surface_hover = "#d8d3ba"
color_card_bg = "#efebd4"
color_text = "#5c6a72"
color_text_muted = "#829181"
color_disabled_text = "#a6b0a0"
color_border = "#e0dcc7"

color_nav_inactive = "#829181"
color_separator = "#e0dcc7"
color_scrollbar_bg = "#f4f0d9"
color_scrollbar_handle = "#d8d3ba"
color_slider_handle = "#8da101"
color_slider_groove_bg = "#efebd4"
color_border_subtle = "rgba(0, 0, 0, 0.05)"
color_border_input = "#8da101"
color_border_light = "#e0dcc7"
color_border_faint = "rgba(0, 0, 0, 0.08)"
color_border_focus = "#8da101"
color_checkbox_unchecked_bg = "#efebd4"
color_checkbox_hover_bg = "#e5dfc8"
color_combo_disabled_bg = "#f4f0d9"
color_combo_disabled_border = "#efebd4"
color_overlay = "rgba(0,0,0,0.85)"
color_detail_overlay = "rgba(0,0,0,0.5)"
color_cover_frame_bg = "#efebd4"

LIBRARY_WIDGET_STYLE = f"""
    QWidget {{
        background-color: #fdf6e3;
        border-radius: 0px;
    }}
"""

SOURCE_CORNER = {
    "ribbon_color": "#efebd4",
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
    {"position": 0, "color": "#fdf6e3"},
    {"position": 1, "color": "#fdf6e3"},
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
        {"position": 0, "color": "#8da101"},
        {"position": 0.5, "color": "#35a77c"},
        {"position": 1, "color": "#8da101"}
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

THEME_INHERITS = "standart"

color_accent = "#78824b"
color_accent_dark = "#5f875f"
color_accent_blue = "#c9a554"
color_preloader = "#78824b"
color_bg = "#222222"
color_bg_darker = "#1a1a1a"
color_surface = "#2c2c2c"
color_surface_elevated = "#333333"
color_surface_hover = "#3c3c3c"
color_card_bg = "#2c2c2c"
color_text = "#c2c2b0"
color_text_muted = "#8a8a7a"
color_disabled_text = "#666666"
color_border = "#444444"

color_nav_inactive = "#8a8a7a"
color_separator = "#444444"
color_scrollbar_bg = "#1a1a1a"
color_scrollbar_handle = "#3c3c3c"
color_slider_handle = "#78824b"
color_slider_groove_bg = "#2c2c2c"
color_border_subtle = "rgba(255, 255, 255, 0.05)"
color_border_input = "#78824b"
color_border_light = "#444444"
color_border_faint = "rgba(255, 255, 255, 0.08)"
color_border_focus = "#78824b"
color_checkbox_unchecked_bg = "#2c2c2c"
color_checkbox_hover_bg = "#333333"
color_combo_disabled_bg = "#1a1a1a"
color_combo_disabled_border = "#2c2c2c"
color_overlay = "rgba(0,0,0,0.85)"
color_detail_overlay = "rgba(0,0,0,0.5)"
color_cover_frame_bg = "#2c2c2c"

LIBRARY_WIDGET_STYLE = f"""
    QWidget {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #181818,
            stop:0.5 #22251d,
            stop:1 #2a2e22);
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
border_radius_small = "8px"
border_radius_large = "14px"
border_radius_card = "18px"
border_radius_badge = "6px"

LIBRARY_LAYOUT_MODE = "grid"
DETAIL_PAGE_LAYOUT_MODE = "full"
DETAIL_PAGE_BG_MODE = "gradient"

DETAIL_PAGE_GRADIENT = [
    {"position": 0, "color": "#181818"},
    {"position": 0.5, "color": "#22251d"},
    {"position": 1, "color": "#2a2e22"}
]

PRELOADER = {
    "style": "wave",
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
        {"position": 0, "color": "#78824b"},
        {"position": 0.5, "color": "#bb7744"},
        {"position": 1, "color": "#c9a554"}
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

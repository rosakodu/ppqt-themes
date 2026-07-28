THEME_INHERITS = "standart"

color_accent = "#1a9fff"
color_accent_dark = "#0078d4"
color_accent_blue = "#66c0f4"
color_preloader = "#1a9fff"
color_bg = "#171d25"
color_bg_darker = "#10151c"
color_surface = "#1e2633"
color_surface_elevated = "#283548"
color_surface_hover = "#314159"
color_card_bg = "#1e2633"
color_text = "#f3f3f3"
color_text_muted = "#96a5b7"
color_disabled_text = "#4a596e"
color_border = "#2a374d"

color_nav_inactive = "#96a5b7"
color_separator = "#2a374d"
color_scrollbar_bg = "#10151c"
color_scrollbar_handle = "#314159"
color_slider_handle = "#1a9fff"
color_slider_groove_bg = "#2a374d"
color_border_subtle = "rgba(255, 255, 255, 0.05)"
color_border_input = "#1a9fff"
color_border_light = "#2a374d"
color_border_faint = "rgba(255, 255, 255, 0.08)"
color_border_focus = "#1a9fff"
color_checkbox_unchecked_bg = "#1e2633"
color_checkbox_hover_bg = "#283548"
color_combo_disabled_bg = "#10151c"
color_combo_disabled_border = "#1e2633"
color_overlay = "rgba(0,0,0,0.85)"
color_detail_overlay = "rgba(0,0,0,0.5)"
color_cover_frame_bg = "#1e2633"

LIBRARY_WIDGET_STYLE = f"""
    QWidget {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #0e1218,
            stop:0.5 #171d25,
            stop:1 #1e2633);
        border-radius: 0px;
    }}
"""

SOURCE_CORNER = {
    "ribbon_color": "#1e2633",
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
    {"position": 0, "color": "#0e1218"},
    {"position": 0.5, "color": "#171d25"},
    {"position": 1, "color": "#1e2633"}
]

PRELOADER = {
    "style": "pulse",
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
        {"position": 0, "color": "#1a9fff"},
        {"position": 0.5, "color": "#66c0f4"},
        {"position": 1, "color": "#1a9fff"}
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

# === Button Icons & Dynamic State Colors ===
ICON_COLORS = {
    "*_hover": color_text,
    "*_pressed": color_text,
    "*_focused": color_text,
    "*_disabled": color_disabled_text,
}

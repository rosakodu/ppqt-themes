THEME_INHERITS = "standart"

color_accent = "#c5003c"
color_accent_dark = "#880425"
color_accent_blue = "#55ead4"
color_preloader = "#c5003c"
color_bg = "#0f0508"
color_bg_darker = "#060102"
color_surface = "#1d0a0f"
color_surface_elevated = "#280e15"
color_surface_hover = "#36131c"
color_card_bg = "#1d0a0f"
color_text = "#ffffff"
color_text_accent_hover = "#0f0508"
color_text_muted = "#e4356a"
color_disabled_text = "#880425"
color_border = "#c5003c"

color_nav_inactive = "#e4356a"
color_separator = "#c5003c"
color_scrollbar_bg = "#060102"
color_scrollbar_handle = "#36131c"
color_slider_handle = "#c5003c"
color_slider_groove_bg = "#880425"
color_border_subtle = "rgba(197, 0, 60, 0.2)"
color_border_input = "#c5003c"
color_border_light = "#c5003c"
color_border_faint = "rgba(197, 0, 60, 0.15)"
color_border_focus = "#55ead4"
color_checkbox_unchecked_bg = "#1d0a0f"
color_checkbox_hover_bg = "#280e15"
color_combo_disabled_bg = "#060102"
color_combo_disabled_border = "#1d0a0f"
color_overlay = "rgba(0,0,0,0.85)"
color_detail_overlay = "rgba(0,0,0,0.5)"
color_cover_frame_bg = "#1d0a0f"

LIBRARY_WIDGET_STYLE = f"""
    QWidget {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #060102,
            stop:0.4 #0f0508,
            stop:0.7 #1d0a0f,
            stop:1 #280e15);
        border-radius: 0px;
    }}
"""

SOURCE_CORNER = {
    "ribbon_color": "#c5003c",
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
    {"position": 0, "color": "#060102"},
    {"position": 0.4, "color": "#0f0508"},
    {"position": 0.7, "color": "#1d0a0f"},
    {"position": 1, "color": "#280e15"}
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
    "default_border_width": 3,
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
        {"position": 0, "color": "#c5003c"},
        {"position": 0.5, "color": "#880425"},
        {"position": 1, "color": "#c5003c"}
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
    "*_hover": color_bg,
    "*_pressed": color_bg_darker,
    "*_focused": color_bg,
    "*_disabled": color_disabled_text,
}

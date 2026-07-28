THEME_INHERITS = "standart"

color_accent = "#7e9cd8"
color_accent_dark = "#957fb8"
color_accent_blue = "#7fb4ca"
color_preloader = "#7e9cd8"
color_bg = "#1f1f28"
color_bg_darker = "#16161d"
color_surface = "#2a2a37"
color_surface_elevated = "#363646"
color_surface_hover = "#54546d"
color_card_bg = "#2a2a37"
color_text = "#dcd7ba"
color_text_muted = "#c8c093"
color_disabled_text = "#727169"
color_border = "#363646"

color_nav_inactive = "#c8c093"
color_separator = "#363646"
color_scrollbar_bg = "#16161d"
color_scrollbar_handle = "#54546d"
color_slider_handle = "#7e9cd8"
color_slider_groove_bg = "#363646"
color_border_subtle = "rgba(255, 255, 255, 0.05)"
color_border_input = "#7e9cd8"
color_border_light = "#363646"
color_border_faint = "rgba(255, 255, 255, 0.08)"
color_border_focus = "#7e9cd8"
color_checkbox_unchecked_bg = "#2a2a37"
color_checkbox_hover_bg = "#363646"
color_combo_disabled_bg = "#16161d"
color_combo_disabled_border = "#2a2a37"
color_overlay = "rgba(0,0,0,0.85)"
color_detail_overlay = "rgba(0,0,0,0.5)"
color_cover_frame_bg = "#2a2a37"

LIBRARY_WIDGET_STYLE = f"""
    QWidget {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #15151c,
            stop:0.5 #1f1f28,
            stop:1 #2a2a37);
        border-radius: 0px;
    }}
"""

SOURCE_CORNER = {
    "ribbon_color": "#2a2a37",
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
    {"position": 0, "color": "#15151c"},
    {"position": 0.5, "color": "#1f1f28"},
    {"position": 1, "color": "#2a2a37"}
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
        {"position": 0, "color": "#7e9cd8"},
        {"position": 0.5, "color": "#957fb8"},
        {"position": 1, "color": "#7e9cd8"}
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

# === Custom Combobox Style Overrides ===
COMBOBOX_STYLE = f"""
    QComboBox {{
        background: {color_surface};
        border: {border_medium} transparent;
        border-radius: {border_radius_small};
        padding-left: 12px;
        height: 34px;
        color: {color_text};
        font-family: '{font_family}';
        font-size: {font_size_normal};
        min-width: 120px;
        combobox-popup: 0;
    }}
    QComboBox:on {{
        background: {color_bg};
        border: {border_medium} {color_accent};
        border-bottom-style: none;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
        border-bottom-left-radius: 0px;
        border-bottom-right-radius: 0px;
    }}
    QComboBox:hover {{
        border: {border_medium} {color_accent};
        background: {color_accent};
        color: {color_bg};
    }}
    /* Focus state */
    QComboBox:focus {{
        border: {border_medium} {color_accent};
        background-color: {color_accent};
        color: {color_bg};
    }}
    QComboBox:disabled {{
        background: {color_combo_disabled_bg};
        border: {border_medium} {color_combo_disabled_border};
        color: {color_combo_disabled_text};
    }}
    QComboBox::drop-down {{
        subcontrol-origin: padding;
        subcontrol-position: center right;
        border-left: {border_thin} {color_border_faint};
        padding: 12px;
        height: 12px;
        width: 12px;
    }}
    /* List when combobox is open */
    QComboBox QAbstractItemView {{
        outline: none;
        background: {color_surface};
        border: {border_medium} {color_accent};
        border-top-style: none;
        border-top-left-radius: 0px;
        border-top-right-radius: 0px;
        border-bottom-left-radius: 10px;
        border-bottom-right-radius: 10px;
    }}
    QComboBox:editable {{
        background: {color_surface};
        color: {color_text};
    }}
    QComboBox::drop-down:editable:focus {{
        background: {color_accent};
        border-top-left-radius: 0px;
        border-top-right-radius: 10px;
        border-bottom-left-radius: 0px;
        border-bottom-right-radius: 10px;
    }}
    QListView {{
        background: {color_surface};
    }}
    QListView::item {{
        padding: 7px 7px 7px 12px;
        margin: 3px;
        min-height: 24px;
        border-radius: {border_radius_small};
        color: {color_text};
    }}
    QListView::item:hover {{
        background: {color_bg};
    }}
    QListView::item:selected {{
        background: {color_bg};
    }}
    /* Selection in list when item is focused */
    QListView::item:focus {{
        background: {color_accent};
        color: {color_bg};
    }}
"""

SETTINGS_TABLE_COMBOBOX_STYLE = f"""
    QComboBox#settingsTableCombo:hover,
    QComboBox#settingsTableCombo:focus {{
        background: {color_surface};
        border: {border_medium} {color_accent};
        color: {color_accent};
    }}
"""
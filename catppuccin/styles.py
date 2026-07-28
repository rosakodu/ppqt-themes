THEME_INHERITS = "standart"

color_accent = "#cba6f7"
color_accent_dark = "#b4befe"
color_accent_blue = "#89b4fa"
color_preloader = "#cba6f7"
color_bg = "#1e1e2e"
color_bg_darker = "#181825"
color_surface = "#313244"
color_surface_elevated = "#45475a"
color_surface_hover = "#585b70"
color_card_bg = "#313244"
color_text = "#cdd6f4"
color_text_muted = "#a6adc8"
color_disabled_text = "#585b70"
color_border = "#45475a"

color_nav_inactive = "#a6adc8"
color_separator = "#45475a"
color_scrollbar_bg = "#181825"
color_scrollbar_handle = "#585b70"
color_slider_handle = "#cba6f7"
color_slider_groove_bg = "#45475a"
color_border_subtle = "rgba(255, 255, 255, 0.05)"
color_border_input = "#cba6f7"
color_border_light = "#45475a"
color_border_faint = "rgba(255, 255, 255, 0.08)"
color_border_focus = "#cba6f7"
color_checkbox_unchecked_bg = "#313244"
color_checkbox_hover_bg = "#45475a"
color_combo_disabled_bg = "#181825"
color_combo_disabled_border = "#313244"
color_overlay = "rgba(0,0,0,0.85)"
color_detail_overlay = "rgba(0,0,0,0.5)"
color_cover_frame_bg = "#313244"

LIBRARY_WIDGET_STYLE = f"""
    QWidget {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #11111b,
            stop:0.5 #1e1e2e,
            stop:1 #313244);
        border-radius: 0px;
    }}
"""

SOURCE_CORNER = {
    "ribbon_color": "#313244",
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
    {"position": 0, "color": "#11111b"},
    {"position": 0.5, "color": "#1e1e2e"},
    {"position": 1, "color": "#313244"}
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
        {"position": 0, "color": "#cba6f7"},
        {"position": 0.5, "color": "#89b4fa"},
        {"position": 1, "color": "#cba6f7"}
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
    # Main action & status icons
    "tray_portproton": color_accent,
    "badge_portproton": color_accent,
    "menu": color_accent,
    "addgame": color_accent,
    "play": color_accent,
    "stop": color_accent_dark,
    "apply": color_accent,
    "check": color_accent,
    "desktop": color_accent_blue,
    "update": color_accent_blue,
    "star": color_accent,
    "settings": color_accent,
    "edit": color_accent,
    "folder": color_accent_blue,
    "search": color_accent,
    
    # Navigation row (top row - arrows)
    "back": color_accent,
    "down": color_accent,
    "up": color_accent,
    "dpad_left": color_accent,
    "dpad_right": color_accent,
    
    # Keyboard shortcut badges (bottom row)
    "key_enter": color_accent,
    "key_backspace": color_accent,
    "key_e": color_accent,
    "key_context": color_accent,
    "key_f11": color_accent,
    "key_f5": color_accent,
    "key_+": color_accent,
    "key_left": color_accent,
    "key_right": color_accent,
    
    # Gamepad controller buttons (Xbox & PlayStation)
    "xbox_a": color_accent,
    "xbox_b": color_accent,
    "xbox_x": color_accent,
    "xbox_y": color_accent,
    "xbox_lb": color_accent,
    "xbox_lt": color_accent,
    "xbox_rb": color_accent,
    "xbox_rt": color_accent,
    "xbox_start": color_accent,
    "xbox_view": color_accent,
    "xbox_xbox": color_accent,
    "ps_circle": color_accent,
    "ps_cross": color_accent,
    "ps_square": color_accent,
    "ps_triangle": color_accent,
    "ps_l1": color_accent,
    "ps_l2": color_accent,
    "ps_r1": color_accent,
    "ps_r2": color_accent,
    "ps_options": color_accent,
    "ps_share": color_accent,
    "ps_ps": color_accent,

    # Dynamic states
    "*_hover": color_accent,
    "*_pressed": color_accent_dark,
    "*_focused": color_accent_blue,
    "*_disabled": color_disabled_text,
}

# Easy AVR USB Keyboard Firmware Keymapper
# Copyright (C) 2013-2017 David Howland
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Keyboard definition for the KBD75 custom keyboard."""

import easykeymap.templates.ATmega32U4_16MHz_TKL as firmware
from easykeymap.ioports import *
from easykeymap.helper import make_matrix_config

description = "KBD75"
unique_id = "KBD75_001"
cfg_name = "kbd75"

teensy = False
hw_boot_key = False

num_rows = 6
num_cols = 16

strobe_cols = False
strobe_low = True

matrix_hardware, matrix_strobe, matrix_sense = make_matrix_config(
    strobe_cols=strobe_cols,
    strobe_low=strobe_low,
    rows=[D0, D1, D2, D3, D5, B7],
    cols=[F0, F1, E6, C7, C6, F5, D4, B1, B0, B5, B4, D7, D6, B3, F4, F6],
    device=firmware.device
)

num_leds = 1
num_ind = 0
num_bl_enab = 2

led_definition = [
]

led_hardware = [
#       Port    Pin    Direction
    ( REF_PORTB, 6, LED_DRIVER_PULLUP )
]

backlighting = False

bl_modes = [
    ( 0, ),
    ( 1, )
]

KMAC_key = None

keyboard_definition = [
    [((4, 4), (0, 0), 'HID_KEYBOARD_SC_ESCAPE'),
     ((4, 4), (0, 1), 'HID_KEYBOARD_SC_F1'),
     ((4, 4), (0, 2), 'HID_KEYBOARD_SC_F2'),
     ((4, 4), (0, 3), 'HID_KEYBOARD_SC_F3'),
     ((4, 4), (0, 4), 'HID_KEYBOARD_SC_F4'),
     ((4, 4), (0, 5), 'HID_KEYBOARD_SC_F5'),
     ((4, 4), (0, 6), 'HID_KEYBOARD_SC_F6'),
     ((4, 4), (0, 7), 'HID_KEYBOARD_SC_F7'),
     ((4, 4), (0, 8), 'HID_KEYBOARD_SC_F8'),
     ((4, 4), (0, 9), 'HID_KEYBOARD_SC_F9'),
     ((4, 4), (0, 10), 'HID_KEYBOARD_SC_F10'),
     ((4, 4), (0, 11), 'HID_KEYBOARD_SC_F11'),
     ((4, 4), (0, 12), 'HID_KEYBOARD_SC_F12'),
     ((4, 4), (0, 13), 'HID_KEYBOARD_SC_PRINT_SCREEN'),
     ((4, 4), (0, 14), 'HID_KEYBOARD_SC_SCROLL_LOCK'),
     ((4, 4), (0, 15), 'HID_KEYBOARD_SC_PAUSE')],

    [((4, 4), (1, 0), 'HID_KEYBOARD_SC_GRAVE_ACCENT_AND_TILDE'),
     ((4, 4), (1, 1), 'HID_KEYBOARD_SC_1_AND_EXCLAMATION'),
     ((4, 4), (1, 2), 'HID_KEYBOARD_SC_2_AND_AT'),
     ((4, 4), (1, 3), 'HID_KEYBOARD_SC_3_AND_HASHMARK'),
     ((4, 4), (1, 4), 'HID_KEYBOARD_SC_4_AND_DOLLAR'),
     ((4, 4), (1, 5), 'HID_KEYBOARD_SC_5_AND_PERCENTAGE'),
     ((4, 4), (1, 6), 'HID_KEYBOARD_SC_6_AND_CARET'),
     ((4, 4), (1, 7), 'HID_KEYBOARD_SC_7_AND_AND_AMPERSAND'),
     ((4, 4), (1, 8), 'HID_KEYBOARD_SC_8_AND_ASTERISK'),
     ((4, 4), (1, 9), 'HID_KEYBOARD_SC_9_AND_OPENING_PARENTHESIS'),
     ((4, 4), (1, 10), 'HID_KEYBOARD_SC_0_AND_CLOSING_PARENTHESIS'),
     ((4, 4), (1, 11), 'HID_KEYBOARD_SC_MINUS_AND_UNDERSCORE'),
     ((4, 4), (1, 12), 'HID_KEYBOARD_SC_EQUAL_AND_PLUS'),
     ((4, 4), (1, 13), 'HID_KEYBOARD_SC_DELETE'),
     ((4, 4), (1, 14), 'HID_KEYBOARD_SC_BACKSPACE'),
     ((4, 4), (1, 15), 'HID_KEYBOARD_SC_HOME')],

    [((6, 4), (2, 0), 'HID_KEYBOARD_SC_TAB'),
     ((4, 4), (2, 2), 'HID_KEYBOARD_SC_Q'),
     ((4, 4), (2, 3), 'HID_KEYBOARD_SC_W'),
     ((4, 4), (2, 4), 'HID_KEYBOARD_SC_E'),
     ((4, 4), (2, 5), 'HID_KEYBOARD_SC_R'),
     ((4, 4), (2, 6), 'HID_KEYBOARD_SC_T'),
     ((4, 4), (2, 7), 'HID_KEYBOARD_SC_Y'),
     ((4, 4), (2, 8), 'HID_KEYBOARD_SC_U'),
     ((4, 4), (2, 9), 'HID_KEYBOARD_SC_I'),
     ((4, 4), (2, 10), 'HID_KEYBOARD_SC_O'),
     ((4, 4), (2, 11), 'HID_KEYBOARD_SC_P'),
     ((4, 4), (2, 12), 'HID_KEYBOARD_SC_OPENING_BRACKET_AND_OPENING_BRACE'),
     ((4, 4), (2, 13), 'HID_KEYBOARD_SC_CLOSING_BRACKET_AND_CLOSING_BRACE'),
     ((6, 4), (2, 14), 'HID_KEYBOARD_SC_BACKSLASH_AND_PIPE'),
     ((4, 4), (2, 15), 'HID_KEYBOARD_SC_PAGE_UP')],

    [((7, 4), (3, 0), 'HID_KEYBOARD_SC_CAPS_LOCK'),
     ((4, 4), (3, 2), 'HID_KEYBOARD_SC_A'),
     ((4, 4), (3, 3), 'HID_KEYBOARD_SC_S'),
     ((4, 4), (3, 4), 'HID_KEYBOARD_SC_D'),
     ((4, 4), (3, 5), 'HID_KEYBOARD_SC_F'),
     ((4, 4), (3, 6), 'HID_KEYBOARD_SC_G'),
     ((4, 4), (3, 7), 'HID_KEYBOARD_SC_H'),
     ((4, 4), (3, 8), 'HID_KEYBOARD_SC_J'),
     ((4, 4), (3, 9), 'HID_KEYBOARD_SC_K'),
     ((4, 4), (3, 10), 'HID_KEYBOARD_SC_L'),
     ((4, 4), (3, 11), 'HID_KEYBOARD_SC_SEMICOLON_AND_COLON'),
     ((4, 4), (3, 12), 'HID_KEYBOARD_SC_APOSTROPHE_AND_QUOTE'),
     ((9, 4), (3, 13), 'HID_KEYBOARD_SC_ENTER'),
     ((4, 4), (3, 15), 'HID_KEYBOARD_SC_PAGE_DOWN')],

    [((9, 4), (4, 0), 'HID_KEYBOARD_SC_LEFT_SHIFT'),
     ((4, 4), (4, 2), 'HID_KEYBOARD_SC_Z'),
     ((4, 4), (4, 3), 'HID_KEYBOARD_SC_X'),
     ((4, 4), (4, 4), 'HID_KEYBOARD_SC_C'),
     ((4, 4), (4, 5), 'HID_KEYBOARD_SC_V'),
     ((4, 4), (4, 6), 'HID_KEYBOARD_SC_B'),
     ((4, 4), (4, 7), 'HID_KEYBOARD_SC_N'),
     ((4, 4), (4, 8), 'HID_KEYBOARD_SC_M'),
     ((4, 4), (4, 9), 'HID_KEYBOARD_SC_COMMA_AND_LESS_THAN_SIGN'),
     ((4, 4), (4, 10), 'HID_KEYBOARD_SC_DOT_AND_GREATER_THAN_SIGN'),
     ((4, 4), (4, 11), 'HID_KEYBOARD_SC_SLASH_AND_QUESTION_MARK'),
     ((7, 4), (4, 13), 'HID_KEYBOARD_SC_RIGHT_SHIFT'),
     ((4, 4), (4, 14), 'HID_KEYBOARD_SC_UP_ARROW'),
     ((4, 4), (4, 15), 'HID_KEYBOARD_SC_END')],

    [((5, 4), (5, 0), 'HID_KEYBOARD_SC_LEFT_CONTROL'),
     ((5, 4), (5, 1), 'HID_KEYBOARD_SC_LEFT_GUI'),
     ((5, 4), (5, 3), 'HID_KEYBOARD_SC_APPLICATION'),
     ((25, 4), (5, 6), 'HID_KEYBOARD_SC_SPACE'),
     ((4, 4), (5, 10), 'HID_KEYBOARD_SC_RIGHT_ALT'),
     ((4, 4), (5, 11), 'HID_KEYBOARD_SC_RIGHT_GUI'),
     ((4, 4), (5, 12), 'HID_KEYBOARD_SC_RIGHT_CONTROL'),
     ((4, 4), (5, 13), 'HID_KEYBOARD_SC_LEFT_ARROW'),
     ((4, 4), (5, 14), 'HID_KEYBOARD_SC_DOWN_ARROW'),
     ((4, 4), (5, 15), 'HID_KEYBOARD_SC_RIGHT_ARROW')]
]

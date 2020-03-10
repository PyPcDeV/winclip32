from datetime import datetime
from time import time

ANSI_STD_TEXT = 1
ANSI_MSL_TEXT = 4
ANCII_DIF_TEXT = 5
BIT8_DOS_TEXT = 7
UNICODE_STD_TEXT = 13
ANSI_DSP_TEXT = 129
HBITMAP_GDI_STD_OBJECT = 2
HBITMAP_GDI_DSP_OBJECT = 130
BITMAPINFO_STD_STRUCTURE = 8
METAFILEPICT_STD_STRUCTURE = 3
METAFILEPICT_DSP_STRUCTURE = 131
TIFF_STD_IMAGE = 6
HPALETTE_GDI_STD_OBJECT = 9
PENDATA_STD_DATA = 10
RIFF_STD_AUDIO = 11
WAVE_STD_AUDIO = 12
HENHMETAFILE_STD_HANDLE = 14
HENHMETAFILE_DSP_HANDLE = 142
DROPFILES_STD_LIST = 15
DWORD_STD_LCID = 16
BITMAPV5HEADER_STD_STRUCTURE = 17
STIME_MARK = "stime"
DTTIME_MARK = "dttime"
NUMERIC_MARK = "numeric"

clipboard_formats_str = ['ansi_std_text',
                            'ansi_msl_text',
                            'ascii_dif_text',
                            '8bit_dos_text',
                            'unicode_std_text',
                            'ansi_dsp_text',
                            'hbitmap_gdi_std_object',
                            'hbitmap_gdi_dsp_object',
                            'bitmapinfo_std_structure',
                            'metafilepict_std_structure',
                            'metafilepict_dsp_structure',
                            'tiff_std_image',
                            'hpalette_gdi_std_object',
                            'pendata_std_data',
                            'riff_std_audio',
                            'wave_std_audio',
                            'henhmetafile_std_handle',
                            'henhmetafile_dsp_handle',
                            'dropfiles_std_list',
                            'dword_std_lcid',
                            'bitmapv5header_std_structure']
clipboard_formats_int = [1,
                            4,
                            5,
                            7,
                            13,
                            129,
                            2,
                            130,
                            8,
                            3,
                            131,
                            6,
                            9,
                            10,
                            11,
                            12,
                            14,
                            142,
                            15,
                            16,
                            17]

marks = [NUMERIC_MARK, STIME_MARK, DTTIME_MARK]

from winclip32.errors import *

ERROR = 0
try:
    import win32clipboard
except:
    ERROR = 1

if ERROR:
    raise something_went_wrong





def get_clipboard_formats_info():
    # information got from https://www.codeproject.com/Reference/1091137/Windows-Clipboard-Formats
    print("| DATA TYPE                    | FORMATS KEYS                                          | ABOUT")
    print("|------------------------------|-------------------------------------------------------|------------------------------------------------")
    print("| ANSI text                    | format: 1 or 'ansi_std_text'                          | standart text")
    print("|                              |                                                       |")
    print("| ANSI text                    | format: 4 or 'ansi_msl_text'                          | Microsoft Symbolic Link")
    print("|                              |                                                       |")
    print("| ASCII text                   | format: 5 or 'ascii_dif_text'                         | Software Arts Data Interchange Format")
    print("|                              |                                                       |")
    print("| 8-bit DOS text               | format: 7 or '8bit_dos_text'                          | stardart text")
    print("|                              |                                                       |")
    print("| UNICODE text                 | format: 13 or 'unicode_std_text'                      | stardart text")
    print("|                              |                                                       |")
    print("| ANSI text                    | format: 129 or 'ansi_dsp_text'                        | standart text")
    print("|                              |                                                       |")
    print("| HBITMAP (GDI) object         | format: 2 or 'hbitmap_gdi_std_object'                 | Handle to a bitmap (GDI object)")
    print("|                              |                                                       |")
    print("| HBITMAP (GDI) object         | format: 130 or 'hbitmap_gdi_dsp_object'               | Handle to a bitmap (GDI object)")
    print("|                              |                                                       |")
    print("| BITMAPINFO structure         | format: 8 or 'bitmapinfo_std_structure'               | Structure followed by bitmap bits")
    print("|                              |                                                       |")
    print("| METAFILEPICT picture         | format: 3 or 'metafilepict_std_structure'             | Windows-Format Metafiles picture")
    print("|                              |                                                       |")
    print("| METAFILEPICT picture         | format: 131 or 'metafilepict_dsp_structure'           | Windows-Format Metafiles picture")
    print("|                              |                                                       |")
    print("| TIFF image                   | format: 6 or 'tiff_std_image'                         | TIFF image")
    print("|                              |                                                       |")
    print("| HPALETTE                     | format: 9 or 'hpalette_gdi_std_object'                | Handle to a color palette (GDI object)")
    print("|                              |                                                       |")
    print("| PENDATA extension data       | format: 10 or 'pendata_std_data'                      | Windows 3.1 pen extension data")
    print("|                              |                                                       |")
    print("| RIFF audio                   | format: 11 or 'riff_std_audio'                        | Resource Interchange File Format (RIFF) audio")
    print("|                              |                                                       |")
    print("| WAVE audio                   | format: 12 or 'wave_std_audio'                        | WAVE audio")
    print("|                              |                                                       |")
    print("| HENHMETAFILE handle          | format: 14 or 'henhmetafile_std_handle'               | Enhanced-Format Metafiles handle")
    print("|                              |                                                       |")
    print("| HENHMETAFILE handle          | format: 142 or 'henhmetafile_dsp_handle'              | Enhanced-Format Metafiles handle")
    print("|                              |                                                       |")
    print("| DROPFILES list               | format: 15 or 'dropfiles_std_list'                    | List of file names")
    print("|                              |                                                       |")
    print("| DWORD (LCID)                 | format: 16 or 'dword_std_lcid'                        | LCID for ansi_std_text to unicode_std_text conversion")
    print("|                              |                                                       |")
    print("| BITMAPV5HEADER structure     | format: 17 or 'bitmapv5header_std_structure'          | Structure followed by bitmap bits")
    print("|                              |                                                       |")
    print("| another data                 | format: int                                           | another data")

def get_clipboard_data(format):
    ERROR = 0
    try:
        assert type(format) is int or type(format) is str
    except:
        ERROR = 1

    if ERROR:
        raise unknown_clipboard_format_given(type(format).__name__)
    clipboarddata = None
    ERROR = 0
    if format in clipboard_formats_int:
        try:
            win32clipboard.OpenClipboard()
            clipboarddata = win32clipboard.GetClipboardData(format)
            win32clipboard.CloseClipboard()
        except:
            ERROR = 1

        if ERROR:
            win32clipboard.CloseClipboard()
            raise clipboard_format_is_not_available(format)
    elif format in clipboard_formats_str:
        try:
            win32clipboard.OpenClipboard()
            clipboarddata = win32clipboard.GetClipboardData(clipboard_formats_int[clipboard_formats_str.index(format)])
            win32clipboard.CloseClipboard()
        except:
            ERROR = 1

        if ERROR:
            raise clipboard_format_is_not_available(format)
    else:
        raise unknown_clipboard_format_given(format)

    return clipboarddata

def is_clipboard_format_available(format):
    ERROR = 0
    try:
        assert type(format) is str or type(format) is int
    except:
        ERROR = 1
    if ERROR:
        raise unknown_clipboard_format_given(format)

    if type(format) is str:
        if format not in clipboard_formats_str:
            raise unknown_clipboard_format_given(format)
        else:
            return bool(win32clipboard.IsClipboardFormatAvailable(
                clipboard_formats_int[clipboard_formats_str.index(format)]))
    else:
        return bool(win32clipboard.IsClipboardFormatAvailable(format))


def set_clipboard_data(format, data):
    ERROR = 0
    try:
        assert type(format) is str or type(format) is int
    except:
        ERROR = 1
    if ERROR:
        raise unknown_clipboard_format_given(format)
    ERROR = 0
    if type(format) is int:
        try:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(format, data)
            win32clipboard.CloseClipboard()
        except:
            ERROR = 1


    elif type(format) is str:
        try:
            win32clipboard.OpenClipboard()
            win32clipboard.SetClipboardData(clipboard_formats_int[clipboard_formats_str.index(format)], data)
            win32clipboard.CloseClipboard()
        except:
            ERROR = 1

    if ERROR:
        win32clipboard.CloseClipboard()
        raise invalid_clipboard_format_or_data_given


def count_clipboard_formats():
    try:
        return win32clipboard.CountClipboardFormats()
    except:
        return 0

def empty_clipboard():
    ERROR = 0
    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.CloseClipboard()
    except:
        ERROR = 1
    if ERROR:
        raise something_went_wrong

class Recorder:
    def __init__(self, format=13, mark=None):
        self.format = format
        self.mark = mark
        self.recording = {"0000-00-00 00:00:00": ""}
        self.last_record = time()
        self.started = 0
        if type(format) is not str and type(format) is not int:
            raise invalid_format_type(format)
        elif mark not in marks and mark != None:
            raise invalid_mark(mark)

        if type(format) is str:
            if format not in clipboard_formats_str:
                raise unknown_clipboard_format_given(format)
            else:
                self.format = clipboard_formats_int[clipboard_formats_str.index(format)]

        self.mark = mark

        if self.mark == "numeric":
            self.n = 1
            self.recording = {0:""}
        elif self.mark == "stime":
            self.recording = {"0":""}
        elif self.mark is None:
            self.recording = [""]

    def record(self, record_interval=0.1):
        if not self.started:
            empty_clipboard()
            self.started = 1

        if time() - self.last_record >= record_interval:
            if is_clipboard_format_available(self.format):
                data = get_clipboard_data(self.format)
                if self.mark == None:
                    if self.recording[-1] != data:
                        self.recording.append(data)
                elif self.mark == "numeric":
                    if self.recording[self.n-1] != data:
                        self.recording[self.n] = data
                        self.n += 1
                elif self.mark == "stime":
                    if self.recording[list(self.recording.keys())[-1]] != data:
                        self.recording[str(time())] = data
                elif self.mark == "dttime":
                    if self.recording[list(self.recording.keys())[-1]] != data:
                        self.recording[str(datetime.now())] = data


            self.last_update = time()

    def get_recording(self):
        return self.recording

    def clear_recorder(self):
        self.started = 0
        if self.mark == None:
            self.recording = []
        elif self.mark == "numeric":
            self.recording = {0:""}
            self.n = 1
        elif self.mark == "stime":
            self.recording = {"0":""}
        else:
            self.recording = {"0000-00-00 00:00:00": ""}

    def set_format(self, format):
        self.__init__(format, self.mark)

    def set_mark(self, mark):
        self.__init__(self.format, mark)






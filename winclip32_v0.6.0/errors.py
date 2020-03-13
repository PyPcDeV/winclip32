class invalid_clipboard_format_given(Exception):
    def __init__(self, f):
        Exception.__init__(self, "Invalid clipboard format given. Require int or str, but got '%s'" % f)

class unknown_clipboard_format_given(Exception):
    def __init__(self, f):
        if type(f) is int:
            Exception.__init__(self, "Unknown clipboard format given: %s. Try winclip32.get_clipboard_formats_info()" % f)
        else:
            Exception.__init__(self, "Unknown clipboard format given: '%s'. Try winclip32.get_clipboard_formats_info()" % f)

class clipboard_format_is_not_available(Exception):
    def __init__(self, f):
        if type(f) is int:
            Exception.__init__(self, "%s format is not available, try another format: winclip32.get_clipboard_formats_info()" % f)
        else:
            Exception.__init__(self, "'%s' format is not available, try another format: winclip32.get_clipboard_formats_info()" % f)

class something_went_wrong(Exception):
    def __init__(self):
        Exception.__init__(self, "Something went wrong")

class invalid_clipboard_format_or_data_given(Exception):
    def __init__(self):
        Exception.__init__(self, "Invalid clipboard format or data given")

class invalid_mark(Exception):
    def __init__(self, m):
        Exception.__init__(self, "Invalid mark: %s. Marks: winclip32.HUMERIC_MARK, winclip32.STIME_MARK, winclip32.DTTIME_MARK" % m)

class invalid_format_type(Exception):
    def __init__(self, f):
        Exception.__init__(self, "Invalid format type. Require int or str, but got %s" % f)





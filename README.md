** THE CODE IS NO LONGER MAINTAINED, PLEASE USE OTHER LIBRARIES**
This is a small library for _windows OS_ to work with _clipboard data storage_. winclip32 is based on _pywin32_ module.
https://github.com/PyPcDeV/winclip32

## _**Installation**_
**Only Windows OS**  

**_`pip install winclip32`_**


## _**Code Examples**_

#### _**Example 1**_
`import winclip32`  
`winclip32.set_clipboard_data("unicode_std_text", "Python is beautiful!!!")`  
`print(winclip32.get_clipboard_data("unicode_std_text"))  # >>> Python is beautiful!!!`
#### _**Example 2**_
`import winclip32`  
`winclip32.set_clipboard_data("unicode_std_text", "Python is beautiful!!!")`  
`print(winclip32.is_clipboard_format_available("bitmapinfo_std_structure"))  # >>> False`  
`print(winclip32.is_clipboard_format_available(13))  # >>> True`
#### _**Example 3**_
`import winclip32`   
`winclip32.get_clipboard_formats_info()  # >>> ...`

## _**API**_


_winclip32.get_clipboard_formats_info()_ >> print all informations about winclip32 clipboard formats

_winclip32.get_clipboard_data(**_format_**)_ >> **_format_**: **_str_** / **_int_**; return data or error if something went wrong

_winclip32.set_clipboard_data(**_format_**, **_data_**)_ >> **_format_**: _**str**_ / _**int**_; _**data**_: **_int_**/_**str**_/_**unicode**_/any _**object**_ that supports the **_buffer interface_**; return data or error if something went wrong

_winclip32.is_clipboard_format_available(**_format_**)_ >> **_format_**: _**str**_ / _**int**_; return True if format is available, False if not, and error if something went wrong

_winclip32.count_clipboard_formats()_ >> return the number of different formats currently on the clipboard.

_winclip32.empty_clipboard()_ >> empty the clipboard

_winclip32.Recorder(**_format_**=13, **_mark_**=None)_ >> **_format_**: _**str**_ / _**int**_; _**mark**_: _**str**_; create a recorder for clipboard changes

_winclip32.Recorder().record(**_record_interval_**=0.1)_ >> **_record_interval_**: _**int**_; record the clipboard changes and add them to the recording list or dict

_winclip32.Recorder().get_recording()_ >> return the recorded list or dict

_winclip32.Recorder().clear_recorder()_ >> clear the recording list or dict. use this for new records

_winclip32.Recorder().set_format(**_format_**)_ >> **_format_**: **_str_** / **_int_**; set the main record format

_winclip32.Recorder().set_mark(**_mark_**)_ >> **_mark_**: **_str_**; set the main record mark  



### __**Constants**__
* winclip32.ANSI_STD_TEXT
* winclip32.ANSI_MSL_TEXT
* winclip32.ANCII_DIF_TEXT
* winclip32.BIT8_DOS_TEXT
* winclip32.UNICODE_STD_TEXT
* winclip32.ANSI_DSP_TEXT
* winclip32.HBITMAP_GDI_STD_OBJECT
* winclip32.HBITMAP_GDI_DSP_OBJECT
* winclip32.BITMAPINFO_STD_STRUCTURE
* winclip32.METAFILEPICT_STD_STRUCTURE
* winclip32.METAFILEPICT_DSP_STRUCTURE
* winclip32.TIFF_STD_IMAGE
* winclip32.HPALETTE_GDI_STD_OBJECT
* winclip32.PENDATA_STD_DATA 
* winclip32.RIFF_STD_AUDIO
* winclip32.WAVE_STD_AUDIO
* winclip32.HENHMETAFILE_STD_HANDLE
* winclip32.HENHMETAFILE_DSP_HANDLE 
* winclip32.DROPFILES_STD_LIST
* winclip32.DWORD_STD_LCID
* winclip32.BITMAPV5HEADER_STD_STRUCTURE
* winclip32.NUMERIC_MARK
* winclip32.STIME_MARK
* winclip32.DTTIME_MARK

## _**Update v0.6.0a. --Recorder update--**_
* Added Recorder() - record the clipboard changes and add them to the list or dict.
    * _winclip32.Recorder(**_format_**=13, **_mark_**=None)_ >> **_format_**: _**str**_ / _**int**_; _**mark**_: _**str**_; create a recorder for clipboard changes 
     
    * _winclip32.Recorder().record(**_record_interval_**=0.1)_ >> **_record_interval_**: _**int**_; record the clipboard changes and add them to the recording list or dict  
    
    * _winclip32.Recorder().get_recording()_ >> return the recorded list or dict
    
    * _winclip32.Recorder().clear_recorder()_ >> clear the recording list or dict. use this for new records
    
    * _winclip32.Recorder().set_format(**_format_**)_ >> **_format_**: **_str_** / **_int_**; set the main record format
    
    * _winclip32.Recorder().set_mark(**_mark_**)_ >> **_mark_**: **_str_**; set the main record mark
      
* Added mark-constants
    * winclip32.NUMERIC_MARK
    * winclip32.STIME_MARK
    * winclip32.DTTIME_MARK
    
* Added new errors
    * winclip32.invalid_mark(m)
    * winclip32.invalid_format_type(f)
    
    
## _**Update v0.5.4**_
- Renamed   
    * winclip32.get_clipboad_data_types_info() to winclip32.get_clipboard_formats_info()
    * winclip32.get_clipboard_data(type_key) to winclip32.get_clipboard_data(format) 
    * winclip32.set_clipboard_data(type_key, data) to winclip32.set_clipboard_data(format, data)
    * winclip32.is_clipboard_data_type_available(type_key) to winclip32.is_clipboard_format_available(format)
    * winclip32.count_clipboard_data_types() to winclip32.count_clipboard_formats()
    
    
- Added format constants
    * winclip32.ANSI_STD_TEXT
    * winclip32.ANSI_MSL_TEXT
    * winclip32.ANCII_DIF_TEXT
    * winclip32.BIT8_DOS_TEXT
    * winclip32.UNICODE_STD_TEXT
    * winclip32.ANSI_DSP_TEXT
    * winclip32.HBITMAP_GDI_STD_OBJECT
    * winclip32.HBITMAP_GDI_DSP_OBJECT
    * winclip32.BITMAPINFO_STD_STRUCTURE
    * winclip32.METAFILEPICT_STD_STRUCTURE
    * winclip32.METAFILEPICT_DSP_STRUCTURE
    * winclip32.TIFF_STD_IMAGE
    * winclip32.HPALETTE_GDI_STD_OBJECT
    * winclip32.PENDATA_STD_DATA 
    * winclip32.RIFF_STD_AUDIO
    * winclip32.WAVE_STD_AUDIO
    * winclip32.HENHMETAFILE_STD_HANDLE
    * winclip32.HENHMETAFILE_DSP_HANDLE 
    * winclip32.DROPFILES_STD_LIST
    * winclip32.DWORD_STD_LCID
    * winclip32.BITMAPV5HEADER_STD_STRUCTURE


- Renamed errors. Current:
    * winclip32.invalid_clipboard_format_given(f)
    * winclip32.unknown_clipboard_format_given(f)
    * winclip32.clipboard_format_is_not_available(f)
    * winclip32.something_went_wrong
    * winclip32.invalid_clipboard_format_or_data_given

    






import sys

if sys.version_info < (3, 7):
    from ._colorbar import ColorBar
    from ._hoverlabel import Hoverlabel
    from ._legendgrouptitle import Legendgrouptitle
    from ._marker import Marker
    from ._stream import Stream
    from ._textfont import Textfont
    from ._xbins import XBins
    from ._ybins import YBins
    from . import colorbar
    from . import hoverlabel
    from . import legendgrouptitle
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [".colorbar", ".hoverlabel", ".legendgrouptitle"],
        [
            "._colorbar.ColorBar",
            "._hoverlabel.Hoverlabel",
            "._legendgrouptitle.Legendgrouptitle",
            "._marker.Marker",
            "._stream.Stream",
            "._textfont.Textfont",
            "._xbins.XBins",
            "._ybins.YBins",
        ],
    )

import sys

if sys.version_info < (3, 7):
    from ._visible import VisibleValidator
    from ._unselected import UnselectedValidator
    from ._uirevision import UirevisionValidator
    from ._uid import UidValidator
    from ._texttemplatesrc import TexttemplatesrcValidator
    from ._texttemplate import TexttemplateValidator
    from ._textsrc import TextsrcValidator
    from ._textpositionsrc import TextpositionsrcValidator
    from ._textposition import TextpositionValidator
    from ._textfont import TextfontValidator
    from ._text import TextValidator
    from ._subplot import SubplotValidator
    from ._stream import StreamValidator
    from ._showlegend import ShowlegendValidator
    from ._selectedpoints import SelectedpointsValidator
    from ._selected import SelectedValidator
    from ._realsrc import RealsrcValidator
    from ._real import RealValidator
    from ._opacity import OpacityValidator
    from ._name import NameValidator
    from ._mode import ModeValidator
    from ._metasrc import MetasrcValidator
    from ._meta import MetaValidator
    from ._marker import MarkerValidator
    from ._line import LineValidator
    from ._legendrank import LegendrankValidator
    from ._legendgrouptitle import LegendgrouptitleValidator
    from ._legendgroup import LegendgroupValidator
    from ._imagsrc import ImagsrcValidator
    from ._imag import ImagValidator
    from ._idssrc import IdssrcValidator
    from ._ids import IdsValidator
    from ._hovertextsrc import HovertextsrcValidator
    from ._hovertext import HovertextValidator
    from ._hovertemplatesrc import HovertemplatesrcValidator
    from ._hovertemplate import HovertemplateValidator
    from ._hoveron import HoveronValidator
    from ._hoverlabel import HoverlabelValidator
    from ._hoverinfosrc import HoverinfosrcValidator
    from ._hoverinfo import HoverinfoValidator
    from ._fillcolor import FillcolorValidator
    from ._fill import FillValidator
    from ._customdatasrc import CustomdatasrcValidator
    from ._customdata import CustomdataValidator
    from ._connectgaps import ConnectgapsValidator
    from ._cliponaxis import CliponaxisValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._visible.VisibleValidator",
            "._unselected.UnselectedValidator",
            "._uirevision.UirevisionValidator",
            "._uid.UidValidator",
            "._texttemplatesrc.TexttemplatesrcValidator",
            "._texttemplate.TexttemplateValidator",
            "._textsrc.TextsrcValidator",
            "._textpositionsrc.TextpositionsrcValidator",
            "._textposition.TextpositionValidator",
            "._textfont.TextfontValidator",
            "._text.TextValidator",
            "._subplot.SubplotValidator",
            "._stream.StreamValidator",
            "._showlegend.ShowlegendValidator",
            "._selectedpoints.SelectedpointsValidator",
            "._selected.SelectedValidator",
            "._realsrc.RealsrcValidator",
            "._real.RealValidator",
            "._opacity.OpacityValidator",
            "._name.NameValidator",
            "._mode.ModeValidator",
            "._metasrc.MetasrcValidator",
            "._meta.MetaValidator",
            "._marker.MarkerValidator",
            "._line.LineValidator",
            "._legendrank.LegendrankValidator",
            "._legendgrouptitle.LegendgrouptitleValidator",
            "._legendgroup.LegendgroupValidator",
            "._imagsrc.ImagsrcValidator",
            "._imag.ImagValidator",
            "._idssrc.IdssrcValidator",
            "._ids.IdsValidator",
            "._hovertextsrc.HovertextsrcValidator",
            "._hovertext.HovertextValidator",
            "._hovertemplatesrc.HovertemplatesrcValidator",
            "._hovertemplate.HovertemplateValidator",
            "._hoveron.HoveronValidator",
            "._hoverlabel.HoverlabelValidator",
            "._hoverinfosrc.HoverinfosrcValidator",
            "._hoverinfo.HoverinfoValidator",
            "._fillcolor.FillcolorValidator",
            "._fill.FillValidator",
            "._customdatasrc.CustomdatasrcValidator",
            "._customdata.CustomdataValidator",
            "._connectgaps.ConnectgapsValidator",
            "._cliponaxis.CliponaxisValidator",
        ],
    )

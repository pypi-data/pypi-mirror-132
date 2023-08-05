import sys

if sys.version_info < (3, 7):
    from ._zsrc import ZsrcValidator
    from ._zmin import ZminValidator
    from ._zmid import ZmidValidator
    from ._zmax import ZmaxValidator
    from ._zauto import ZautoValidator
    from ._z import ZValidator
    from ._visible import VisibleValidator
    from ._unselected import UnselectedValidator
    from ._uirevision import UirevisionValidator
    from ._uid import UidValidator
    from ._textsrc import TextsrcValidator
    from ._text import TextValidator
    from ._subplot import SubplotValidator
    from ._stream import StreamValidator
    from ._showscale import ShowscaleValidator
    from ._showlegend import ShowlegendValidator
    from ._selectedpoints import SelectedpointsValidator
    from ._selected import SelectedValidator
    from ._reversescale import ReversescaleValidator
    from ._name import NameValidator
    from ._metasrc import MetasrcValidator
    from ._meta import MetaValidator
    from ._marker import MarkerValidator
    from ._locationssrc import LocationssrcValidator
    from ._locations import LocationsValidator
    from ._legendrank import LegendrankValidator
    from ._legendgrouptitle import LegendgrouptitleValidator
    from ._legendgroup import LegendgroupValidator
    from ._idssrc import IdssrcValidator
    from ._ids import IdsValidator
    from ._hovertextsrc import HovertextsrcValidator
    from ._hovertext import HovertextValidator
    from ._hovertemplatesrc import HovertemplatesrcValidator
    from ._hovertemplate import HovertemplateValidator
    from ._hoverlabel import HoverlabelValidator
    from ._hoverinfosrc import HoverinfosrcValidator
    from ._hoverinfo import HoverinfoValidator
    from ._geojson import GeojsonValidator
    from ._featureidkey import FeatureidkeyValidator
    from ._customdatasrc import CustomdatasrcValidator
    from ._customdata import CustomdataValidator
    from ._colorscale import ColorscaleValidator
    from ._colorbar import ColorbarValidator
    from ._coloraxis import ColoraxisValidator
    from ._below import BelowValidator
    from ._autocolorscale import AutocolorscaleValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._zsrc.ZsrcValidator",
            "._zmin.ZminValidator",
            "._zmid.ZmidValidator",
            "._zmax.ZmaxValidator",
            "._zauto.ZautoValidator",
            "._z.ZValidator",
            "._visible.VisibleValidator",
            "._unselected.UnselectedValidator",
            "._uirevision.UirevisionValidator",
            "._uid.UidValidator",
            "._textsrc.TextsrcValidator",
            "._text.TextValidator",
            "._subplot.SubplotValidator",
            "._stream.StreamValidator",
            "._showscale.ShowscaleValidator",
            "._showlegend.ShowlegendValidator",
            "._selectedpoints.SelectedpointsValidator",
            "._selected.SelectedValidator",
            "._reversescale.ReversescaleValidator",
            "._name.NameValidator",
            "._metasrc.MetasrcValidator",
            "._meta.MetaValidator",
            "._marker.MarkerValidator",
            "._locationssrc.LocationssrcValidator",
            "._locations.LocationsValidator",
            "._legendrank.LegendrankValidator",
            "._legendgrouptitle.LegendgrouptitleValidator",
            "._legendgroup.LegendgroupValidator",
            "._idssrc.IdssrcValidator",
            "._ids.IdsValidator",
            "._hovertextsrc.HovertextsrcValidator",
            "._hovertext.HovertextValidator",
            "._hovertemplatesrc.HovertemplatesrcValidator",
            "._hovertemplate.HovertemplateValidator",
            "._hoverlabel.HoverlabelValidator",
            "._hoverinfosrc.HoverinfosrcValidator",
            "._hoverinfo.HoverinfoValidator",
            "._geojson.GeojsonValidator",
            "._featureidkey.FeatureidkeyValidator",
            "._customdatasrc.CustomdatasrcValidator",
            "._customdata.CustomdataValidator",
            "._colorscale.ColorscaleValidator",
            "._colorbar.ColorbarValidator",
            "._coloraxis.ColoraxisValidator",
            "._below.BelowValidator",
            "._autocolorscale.AutocolorscaleValidator",
        ],
    )

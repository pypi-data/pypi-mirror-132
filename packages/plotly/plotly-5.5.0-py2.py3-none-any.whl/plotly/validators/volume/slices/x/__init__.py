import sys

if sys.version_info < (3, 7):
    from ._show import ShowValidator
    from ._locationssrc import LocationssrcValidator
    from ._locations import LocationsValidator
    from ._fill import FillValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._show.ShowValidator",
            "._locationssrc.LocationssrcValidator",
            "._locations.LocationsValidator",
            "._fill.FillValidator",
        ],
    )

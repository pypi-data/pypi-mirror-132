import _plotly_utils.basevalidators


class SizingValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="sizing", parent_name="layout.image", **kwargs):
        super(SizingValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            values=kwargs.pop("values", ["fill", "contain", "stretch"]),
            **kwargs
        )

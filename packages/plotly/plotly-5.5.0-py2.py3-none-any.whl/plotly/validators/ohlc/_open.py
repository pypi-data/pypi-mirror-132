import _plotly_utils.basevalidators


class OpenValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(self, plotly_name="open", parent_name="ohlc", **kwargs):
        super(OpenValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs
        )

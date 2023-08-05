import _plotly_utils.basevalidators


class YrefValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="yref", parent_name="layout.title", **kwargs):
        super(YrefValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "layoutstyle"),
            values=kwargs.pop("values", ["container", "paper"]),
            **kwargs
        )

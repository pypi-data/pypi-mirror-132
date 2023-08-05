import _plotly_utils.basevalidators


class LayerValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="layer", parent_name="layout.ternary.baxis", **kwargs
    ):
        super(LayerValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", ["above traces", "below traces"]),
            **kwargs
        )

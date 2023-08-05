import _plotly_utils.basevalidators


class ValueformatValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="valueformat", parent_name="indicator.delta", **kwargs
    ):
        super(ValueformatValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs
        )

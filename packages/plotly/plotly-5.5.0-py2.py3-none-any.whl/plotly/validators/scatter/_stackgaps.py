import _plotly_utils.basevalidators


class StackgapsValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="stackgaps", parent_name="scatter", **kwargs):
        super(StackgapsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["infer zero", "interpolate"]),
            **kwargs
        )

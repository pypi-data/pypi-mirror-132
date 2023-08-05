import _plotly_utils.basevalidators


class FillValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="fill", parent_name="volume.slices.y", **kwargs):
        super(FillValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            **kwargs
        )

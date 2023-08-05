import _plotly_utils.basevalidators


class ZminValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="zmin", parent_name="contourcarpet", **kwargs):
        super(ZminValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            implied_edits=kwargs.pop("implied_edits", {"zauto": False}),
            **kwargs
        )

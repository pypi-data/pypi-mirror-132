import _plotly_utils.basevalidators


class BordercolorsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(
        self,
        plotly_name="bordercolorsrc",
        parent_name="scattersmith.hoverlabel",
        **kwargs
    ):
        super(BordercolorsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs
        )

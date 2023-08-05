import _plotly_utils.basevalidators


class BsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="bsrc", parent_name="carpet", **kwargs):
        super(BsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs
        )

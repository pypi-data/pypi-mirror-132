import _plotly_utils.basevalidators


class SuffixsrcValidator(_plotly_utils.basevalidators.SrcValidator):
    def __init__(self, plotly_name="suffixsrc", parent_name="table.header", **kwargs):
        super(SuffixsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs
        )

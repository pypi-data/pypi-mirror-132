import _plotly_utils.basevalidators


class AlignmentgroupValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="alignmentgroup", parent_name="waterfall", **kwargs):
        super(AlignmentgroupValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs
        )

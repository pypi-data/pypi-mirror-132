import _plotly_utils.basevalidators


class SpanValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name="span", parent_name="violin", **kwargs):
        super(SpanValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            items=kwargs.pop(
                "items",
                [
                    {"editType": "calc", "valType": "any"},
                    {"editType": "calc", "valType": "any"},
                ],
            ),
            **kwargs
        )

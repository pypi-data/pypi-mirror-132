import _plotly_utils.basevalidators


class SplomValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(
        self, plotly_name="splom", parent_name="layout.template.data", **kwargs
    ):
        super(SplomValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Splom"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )

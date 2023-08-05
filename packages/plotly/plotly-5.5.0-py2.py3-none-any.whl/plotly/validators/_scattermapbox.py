import _plotly_utils.basevalidators


class ScattermapboxValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="scattermapbox", parent_name="", **kwargs):
        super(ScattermapboxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Scattermapbox"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            below
                Determines if this scattermapbox trace's layers
                are to be inserted before the layer with the
                specified ID. By default, scattermapbox layers
                are inserted above all the base layers. To
                place the scattermapbox layers above every
                other layer, set `below` to "''".
            connectgaps
                Determines whether or not gaps (i.e. {nan} or
                missing values) in the provided data arrays are
                connected.
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on Chart Studio Cloud
                for `customdata`.
            fill
                Sets the area to fill with a solid color. Use
                with `fillcolor` if not "none". "toself"
                connects the endpoints of the trace (or each
                segment of the trace if it has gaps) into a
                closed shape.
            fillcolor
                Sets the fill color. Defaults to a half-
                transparent variant of the line color, marker
                color, or marker line color, whichever is
                available.
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on Chart Studio Cloud
                for `hoverinfo`.
            hoverlabel
                :class:`plotly.graph_objects.scattermapbox.Hove
                rlabel` instance or dict with compatible
                properties
            hovertemplate
                Template string used for rendering the
                information that appear on hover box. Note that
                this will override `hoverinfo`. Variables are
                inserted using %{variable}, for example "y:
                %{y}" as well as %{xother}, {%_xother},
                {%_xother_}, {%xother_}. When showing info for
                several points, "xother" will be added to those
                with different x positions from the first
                point. An underscore before or after
                "(x|y)other" will add a space on that side,
                only when this field is shown. Numbers are
                formatted using d3-format's syntax
                %{variable:d3-format}, for example "Price:
                %{y:$.2f}". https://github.com/d3/d3-format/tre
                e/v1.4.5#d3-format for details on the
                formatting syntax. Dates are formatted using
                d3-time-format's syntax %{variable|d3-time-
                format}, for example "Day: %{2019-01-01|%A}".
                https://github.com/d3/d3-time-
                format/tree/v2.2.3#locale_format for details on
                the date formatting syntax. The variables
                available in `hovertemplate` are the ones
                emitted as event data described at this link
                https://plotly.com/javascript/plotlyjs-
                events/#event-data. Additionally, every
                attributes that can be specified per-point (the
                ones that are `arrayOk: true`) are available.
                Anything contained in tag `<extra>` is
                displayed in the secondary box, for example
                "<extra>{fullData.name}</extra>". To hide the
                secondary box completely, use an empty tag
                `<extra></extra>`.
            hovertemplatesrc
                Sets the source reference on Chart Studio Cloud
                for `hovertemplate`.
            hovertext
                Sets hover text elements associated with each
                (lon,lat) pair If a single string, the same
                string appears over all the data points. If an
                array of string, the items are mapped in order
                to the this trace's (lon,lat) coordinates. To
                be seen, trace `hoverinfo` must contain a
                "text" flag.
            hovertextsrc
                Sets the source reference on Chart Studio Cloud
                for `hovertext`.
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on Chart Studio Cloud
                for `ids`.
            lat
                Sets the latitude coordinates (in degrees
                North).
            latsrc
                Sets the source reference on Chart Studio Cloud
                for `lat`.
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            legendgrouptitle
                :class:`plotly.graph_objects.scattermapbox.Lege
                ndgrouptitle` instance or dict with compatible
                properties
            legendrank
                Sets the legend rank for this trace. Items and
                groups with smaller ranks are presented on
                top/left side while with `*reversed*
                `legend.traceorder` they are on bottom/right
                side. The default legendrank is 1000, so that
                you can use ranks less than 1000 to place
                certain items before all unranked items, and
                ranks greater than 1000 to go after all
                unranked items.
            line
                :class:`plotly.graph_objects.scattermapbox.Line
                ` instance or dict with compatible properties
            lon
                Sets the longitude coordinates (in degrees
                East).
            lonsrc
                Sets the source reference on Chart Studio Cloud
                for `lon`.
            marker
                :class:`plotly.graph_objects.scattermapbox.Mark
                er` instance or dict with compatible properties
            meta
                Assigns extra meta information associated with
                this trace that can be used in various text
                attributes. Attributes such as trace `name`,
                graph, axis and colorbar `title.text`,
                annotation `text` `rangeselector`,
                `updatemenues` and `sliders` `label` text all
                support `meta`. To access the trace `meta`
                values in an attribute in the same trace,
                simply use `%{meta[i]}` where `i` is the index
                or key of the `meta` item in question. To
                access trace `meta` in layout attributes, use
                `%{data[n[.meta[i]}` where `i` is the index or
                key of the `meta` and `n` is the trace index.
            metasrc
                Sets the source reference on Chart Studio Cloud
                for `meta`.
            mode
                Determines the drawing mode for this scatter
                trace. If the provided `mode` includes "text"
                then the `text` elements appear at the
                coordinates. Otherwise, the `text` elements
                appear on hover.
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            selected
                :class:`plotly.graph_objects.scattermapbox.Sele
                cted` instance or dict with compatible
                properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`plotly.graph_objects.scattermapbox.Stre
                am` instance or dict with compatible properties
            subplot
                Sets a reference between this trace's data
                coordinates and a mapbox subplot. If "mapbox"
                (the default value), the data refer to
                `layout.mapbox`. If "mapbox2", the data refer
                to `layout.mapbox2`, and so on.
            text
                Sets text elements associated with each
                (lon,lat) pair If a single string, the same
                string appears over all the data points. If an
                array of string, the items are mapped in order
                to the this trace's (lon,lat) coordinates. If
                trace `hoverinfo` contains a "text" flag and
                "hovertext" is not set, these elements will be
                seen in the hover labels.
            textfont
                Sets the icon text font
                (color=mapbox.layer.paint.text-color,
                size=mapbox.layer.layout.text-size). Has an
                effect only when `type` is set to "symbol".
            textposition
                Sets the positions of the `text` elements with
                respects to the (x,y) coordinates.
            textsrc
                Sets the source reference on Chart Studio Cloud
                for `text`.
            texttemplate
                Template string used for rendering the
                information text that appear on points. Note
                that this will override `textinfo`. Variables
                are inserted using %{variable}, for example "y:
                %{y}". Numbers are formatted using d3-format's
                syntax %{variable:d3-format}, for example
                "Price: %{y:$.2f}". https://github.com/d3/d3-fo
                rmat/tree/v1.4.5#d3-format for details on the
                formatting syntax. Dates are formatted using
                d3-time-format's syntax %{variable|d3-time-
                format}, for example "Day: %{2019-01-01|%A}".
                https://github.com/d3/d3-time-
                format/tree/v2.2.3#locale_format for details on
                the date formatting syntax. Every attributes
                that can be specified per-point (the ones that
                are `arrayOk: true`) are available. variables
                `lat`, `lon` and `text`.
            texttemplatesrc
                Sets the source reference on Chart Studio Cloud
                for `texttemplate`.
            uid
                Assign an id to this trace, Use this to provide
                object constancy between traces during
                animations and transitions.
            uirevision
                Controls persistence of some user-driven
                changes to the trace: `constraintrange` in
                `parcoords` traces, as well as some `editable:
                true` modifications such as `name` and
                `colorbar.title`. Defaults to
                `layout.uirevision`. Note that other user-
                driven trace attribute changes are controlled
                by `layout` attributes: `trace.visible` is
                controlled by `layout.legend.uirevision`,
                `selectedpoints` is controlled by
                `layout.selectionrevision`, and
                `colorbar.(x|y)` (accessible with `config:
                {editable: true}`) is controlled by
                `layout.editrevision`. Trace changes are
                tracked by `uid`, which only falls back on
                trace index if no `uid` is provided. So if your
                app can add/remove traces before the end of the
                `data` array, such that the same trace has a
                different index, you can still preserve user-
                driven changes if you give each trace a `uid`
                that stays with it as it moves.
            unselected
                :class:`plotly.graph_objects.scattermapbox.Unse
                lected` instance or dict with compatible
                properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
""",
            ),
            **kwargs
        )
